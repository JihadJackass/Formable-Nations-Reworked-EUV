# DEVTOOLS INFORMATION

## find_empty_triggers.py

### Purpose
This diagnostic tool identifies and optionally removes empty trigger blocks that cause the EU5 error:
```
[jomini_trigger.cpp:1111]: Invalid size of trigger container input evaluation weights
```

### What It Does
Scans your entire mod for problematic empty trigger blocks including:
- `potential = { }`
- `allow = { }`
- `trigger = { }`
- `AND = { }`, `OR = { }`, `NOT = { }`
- `limit = { }`
- `visible = { }`, `enabled = { }`, `available = { }`
- Blocks with only whitespace or comments

### Two Modes of Operation

#### 1. Scan Mode (Default)
Reports empty trigger blocks without making changes.

**Usage:**
- **Drag and drop** your mod's root folder onto `find_empty_triggers.py`
- **Or run from command line:**
  ```bash
  python find_empty_triggers.py "C:\path\to\your\mod"
  ```

#### 2. Auto-Fix Mode
Automatically removes empty trigger blocks with confirmation prompt.

**Usage:**
```bash
python find_empty_triggers.py "C:\path\to\your\mod" --fix
```

**Safety Features:**
- Shows preview of all files that will be modified
- Requires explicit confirmation (type "yes" or "y")
- Creates `.backup` files before making any changes
- Allows easy rollback if needed

### What It Reports

#### Scan Mode Output
Issues are sorted **bottom-to-top** within each file for easier manual fixing:

```
================================================================================
FILE: common/government_reforms/my_reforms.txt
NOTE: Fix these from TOP to BOTTOM of this list (bottom-to-top in file)
================================================================================

  [!] Empty potential block at line 145
  File: common/government_reforms/my_reforms.txt
  Match: potential = { }

  Context:
    143:     fnr_another_reform = {
    144:         unique = yes
    145:         potential = { }
    146:         allow = {

  [!] Empty allow block at line 67
  File: common/government_reforms/my_reforms.txt
  Match: allow = { }

  Context:
    65:     fnr_my_reform = {
    66:         unique = yes
    67:         allow = { }
    68:         country_modifier = {
```

**Why Bottom-to-Top?**
When you fix issues from the top of the list downward, earlier line numbers remain valid. This prevents the need to re-scan after each fix.

#### Auto-Fix Mode Output
```
AUTO-FIX MODE
================================================================================

This will remove 8 empty trigger blocks from 3 files.
Backup files (.backup) will be created for each modified file.

Files to be modified:
  - common/government_reforms/my_reforms.txt (5 issues)
  - events/flavor_events.txt (2 issues)
  - decisions/my_decisions.txt (1 issues)

Do you want to proceed? (yes/no):
```

After confirmation:
```
Fixing files...

  [OK] Fixed common/government_reforms/my_reforms.txt
       Backup: C:\mod\common\government_reforms\my_reforms.txt.backup
  [OK] Fixed events/flavor_events.txt
       Backup: C:\mod\events\flavor_events.txt.backup

COMPLETE: 2 files fixed, 0 failed

IMPORTANT: Review the changes before testing your mod!
Backups are saved as .backup files - delete them once you're satisfied.
```

### Files Scanned
- All `.txt` files (script files, configs, events, decisions, etc.)
- All `.gui` files (graphical interface definitions)

### Files Excluded
- `readme.txt` and `readme.md` (documentation files)
- Directories: `.git`, `__pycache__`, `node_modules`

### Requirements
- Python 3.6 or higher
- No additional dependencies required
- Works on Windows, macOS, and Linux

### Best Practices

#### Manual Fixing (Scan Mode)
1. Run scan mode first to see all issues
2. Fix issues from **top to bottom** of each file section
3. This order keeps line numbers accurate as you work

#### Auto-Fix Mode
1. **Always review the preview** before confirming
2. Test your mod after auto-fixing
3. Keep `.backup` files until you're certain everything works
4. Delete `.backup` files once satisfied with changes

#### Restoring from Backup
If auto-fix causes problems:
```bash
# Windows
copy "my_file.txt.backup" "my_file.txt"

# Linux/Mac
cp my_file.txt.backup my_file.txt
```

### When to Use

**Use This Tool When:**
- Encountering trigger container evaluation weight errors
- After adding new government reforms, decisions, or events
- During mod debugging or code cleanup
- Before publishing mod updates
- After merging code from multiple sources

**Common Causes of Empty Blocks:**
- Copy-paste errors
- Incomplete implementations
- Commented-out code removal
- Template generation mistakes
- Merge conflicts

### Troubleshooting

**Script closes immediately:**
- Updated version pauses with "Press Enter to exit..."
- If issues persist, run from command prompt/terminal

**Unicode/emoji errors:**
- Script uses ASCII characters only `[OK]`, `[WARNING]`, `[!]`
- Should work in all terminals and command prompts

**Auto-fix not working:**
- Ensure you typed "yes" or "y" exactly
- Check file permissions (files must be writable)
- Review console output for error messages

**Want to undo auto-fix:**
- Restore from `.backup` files (see "Restoring from Backup" above)
- Backup files are created in the same directory as originals

### Command Line Options

```bash
# Scan only (default)
python find_empty_triggers.py "C:\path\to\mod"

# Auto-fix with confirmation
python find_empty_triggers.py "C:\path\to\mod" --fix

# Short flag version
python find_empty_triggers.py "C:\path\to\mod" -f
```

### Example Workflow

1. **Initial Scan:**
   ```bash
   python find_empty_triggers.py "C:\my_mod"
   ```
   Result: Found 15 issues in 4 files

2. **Review Output:**
   - Note which files have issues
   - Decide if manual or auto-fix is better

3. **Option A - Manual Fix:**
   - Open each file
   - Fix from top to bottom of the report
   - Re-scan to verify

4. **Option B - Auto-Fix:**
   ```bash
   python find_empty_triggers.py "C:\my_mod" --fix
   ```
   - Review the preview
   - Type "yes" to confirm
   - Test your mod
   - Delete `.backup` files if satisfied

### Notes

- **Line numbers are approximate** after manual edits - always use context
- **Auto-fix is reversible** - backup files let you undo changes
- **Always test after fixing** - empty blocks may have been placeholders
- **Not all empty blocks are errors** - but they trigger this specific bug
