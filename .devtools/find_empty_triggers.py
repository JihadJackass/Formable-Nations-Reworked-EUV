#!/usr/bin/env python3
"""
Find empty or suspicious trigger blocks in EU5 mod files.
Enhanced with auto-fix capability.
"""

import os
import re
import shutil
from pathlib import Path

def find_empty_triggers(filepath):
    """Find empty trigger blocks in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            lines = content.split('\n')
    except:
        return []
    
    issues = []
    
    # Pattern for common trigger blocks that might be empty
    trigger_keywords = [
        'potential', 'allow', 'trigger', 'AND', 'OR', 'NOT',
        'limit', 'visible', 'enabled', 'available', 'can_select'
    ]
    
    for keyword in trigger_keywords:
        # Pattern to match keyword = { with optional whitespace/newlines and then }
        pattern = rf'\b{keyword}\s*=\s*\{{\s*\}}'
        
        for match in re.finditer(pattern, content, re.IGNORECASE):
            line_num = content[:match.start()].count('\n') + 1
            
            start_line = max(0, line_num - 2)
            end_line = min(len(lines), line_num + 2)
            context = '\n'.join(f"    {i+1}: {lines[i]}" for i in range(start_line, end_line))
            
            issues.append({
                'type': f'Empty {keyword} block',
                'line': line_num,
                'context': context,
                'match': match.group(0),
                'start_pos': match.start(),
                'end_pos': match.end()
            })
    
    # Check for blocks with only whitespace/comments
    for keyword in trigger_keywords:
        pattern = rf'\b{keyword}\s*=\s*\{{([^{{}}]*)\}}'
        
        for match in re.finditer(pattern, content, re.IGNORECASE):
            block_content = match.group(1)
            cleaned = re.sub(r'#[^\n]*', '', block_content)
            if not cleaned.strip():
                line_num = content[:match.start()].count('\n') + 1
                
                # Skip if already reported
                if any(issue['line'] == line_num for issue in issues):
                    continue
                
                start_line = max(0, line_num - 2)
                end_line = min(len(lines), line_num + 3)
                context = '\n'.join(f"    {i+1}: {lines[i]}" for i in range(start_line, end_line))
                
                issues.append({
                    'type': f'Empty {keyword} block (whitespace only)',
                    'line': line_num,
                    'context': context,
                    'match': match.group(0)[:60] + '...' if len(match.group(0)) > 60 else match.group(0),
                    'start_pos': match.start(),
                    'end_pos': match.end()
                })
    
    return issues

def fix_empty_triggers(filepath, issues):
    """Remove empty trigger blocks from a file"""
    # Create backup
    backup_path = filepath + '.backup'
    shutil.copy2(filepath, backup_path)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Sort issues by position (descending) so we can remove from end to start
        sorted_issues = sorted(issues, key=lambda x: x['start_pos'], reverse=True)
        
        # Remove each empty block
        for issue in sorted_issues:
            # Remove the empty block including surrounding whitespace on same line
            content = content[:issue['start_pos']] + content[issue['end_pos']:]
        
        # Write fixed content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, backup_path
    except Exception as e:
        # Restore from backup if something goes wrong
        shutil.copy2(backup_path, filepath)
        return False, str(e)

def scan_project(root_path, auto_fix=False):
    """Scan entire project for empty triggers"""
    print("=" * 80)
    print("SCANNING PROJECT FOR EMPTY TRIGGER BLOCKS")
    print("=" * 80)
    print()
    
    # File extensions to check
    extensions = ['.txt', '.gui']
    
    all_issues = {}
    total_files = 0
    
    for root, dirs, files in os.walk(root_path):
        # Skip certain directories
        skip_dirs = ['.git', '__pycache__', 'node_modules']
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        
        for filename in files:
            # Skip readme files
            if filename.lower() == 'readme.txt' or filename.lower() == 'readme.md':
                continue
                
            if any(filename.endswith(ext) for ext in extensions):
                filepath = os.path.join(root, filename)
                relative_path = os.path.relpath(filepath, root_path)
                
                total_files += 1
                issues = find_empty_triggers(filepath)
                
                if issues:
                    all_issues[filepath] = {
                        'relative_path': relative_path,
                        'issues': issues
                    }
    
    # Report results
    print(f"Scanned {total_files} files")
    print()
    
    if not all_issues:
        print("[OK] No empty trigger blocks found!")
        return
    
    total_issue_count = sum(len(data['issues']) for data in all_issues.values())
    print(f"[WARNING] Found {total_issue_count} empty trigger blocks in {len(all_issues)} files")
    print()
    
    # Display issues
    for filepath, data in sorted(all_issues.items(), key=lambda x: x[1]['relative_path']):
        # Sort issues by line number DESCENDING (bottom to top)
        sorted_issues = sorted(data['issues'], key=lambda x: x['line'], reverse=True)
        
        print("=" * 80)
        print(f"FILE: {data['relative_path']}")
        if not auto_fix:
            print("NOTE: Fix these from TOP to BOTTOM of this list (bottom-to-top in file)")
        print("=" * 80)
        
        for issue in sorted_issues:
            print(f"\n  [!] {issue['type']} at line {issue['line']}")
            print(f"  File: {data['relative_path']}")
            print(f"  Match: {issue['match'][:80]}")
            print(f"\n  Context:")
            print(issue['context'])
            print()
    
    print("=" * 80)
    print(f"SUMMARY: {len(all_issues)} files, {total_issue_count} total issues")
    print("=" * 80)
    
    # Auto-fix mode
    if auto_fix:
        print()
        print("=" * 80)
        print("AUTO-FIX MODE")
        print("=" * 80)
        print()
        print(f"This will remove {total_issue_count} empty trigger blocks from {len(all_issues)} files.")
        print("Backup files (.backup) will be created for each modified file.")
        print()
        print("Files to be modified:")
        for filepath, data in sorted(all_issues.items(), key=lambda x: x[1]['relative_path']):
            print(f"  - {data['relative_path']} ({len(data['issues'])} issues)")
        print()
        
        confirmation = input("Do you want to proceed? (yes/no): ").strip().lower()
        
        if confirmation not in ['yes', 'y']:
            print("\n[CANCELLED] No changes made.")
            return
        
        print()
        print("Fixing files...")
        print()
        
        fixed_count = 0
        failed_count = 0
        
        for filepath, data in all_issues.items():
            success, result = fix_empty_triggers(filepath, data['issues'])
            if success:
                print(f"  [OK] Fixed {data['relative_path']}")
                print(f"       Backup: {result}")
                fixed_count += 1
            else:
                print(f"  [ERROR] Failed to fix {data['relative_path']}: {result}")
                failed_count += 1
        
        print()
        print("=" * 80)
        print(f"COMPLETE: {fixed_count} files fixed, {failed_count} failed")
        print("=" * 80)
        print()
        print("IMPORTANT: Review the changes before testing your mod!")
        print("Backups are saved as .backup files - delete them once you're satisfied.")

if __name__ == "__main__":
    import sys
    
    auto_fix = False
    project_path = None
    
    # Parse arguments
    for arg in sys.argv[1:]:
        if arg.lower() in ['--fix', '-f']:
            auto_fix = True
        elif not project_path:
            project_path = arg
    
    if not project_path:
        print("Empty Trigger Block Scanner")
        print("=" * 80)
        print()
        print("Usage:")
        print("  Scan only:  python find_empty_triggers.py <project_path>")
        print("  Auto-fix:   python find_empty_triggers.py <project_path> --fix")
        print()
        print("Or drag your mod folder onto this script.")
        print()
        project_path = input("Enter your mod's root directory path: ").strip()
    
    if not os.path.exists(project_path):
        print(f"[ERROR] Path '{project_path}' does not exist")
        input("\nPress Enter to exit...")
        sys.exit(1)
    
    scan_project(project_path, auto_fix=auto_fix)
    
    print("\n")
    input("Press Enter to exit...")
