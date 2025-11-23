#!/usr/bin/env python3
"""
Batch Flag Color Converter
Process multiple flag images at once
"""

from PIL import Image
import numpy as np
import os
import glob

def batch_convert_flags(input_folder, output_folder, dark_threshold=128):
    """
    Convert all images in a folder to red and white flags.
    
    Args:
        input_folder: Folder containing flag images
        output_folder: Folder to save converted flags
        dark_threshold: Brightness threshold (default: 128)
    """
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Supported image formats
    formats = ['*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif']
    image_files = []
    
    for fmt in formats:
        image_files.extend(glob.glob(os.path.join(input_folder, fmt)))
    
    if not image_files:
        print(f"No images found in {input_folder}")
        return
    
    print(f"Found {len(image_files)} image(s) to process\n")
    
    for i, input_path in enumerate(image_files, 1):
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)
        output_path = os.path.join(output_folder, f"{name}_converted.png")
        
        try:
            # Load and convert
            img = Image.open(input_path).convert('RGB')
            img_array = np.array(img)
            
            # Calculate brightness
            brightness = np.mean(img_array, axis=2)
            
            # Create output
            output = np.zeros_like(img_array)
            dark_mask = brightness < dark_threshold
            
            output[dark_mask] = [255, 0, 0]      # Red
            output[~dark_mask] = [255, 255, 255]  # White
            
            # Save
            result_img = Image.fromarray(output.astype('uint8'))
            result_img.save(output_path)
            
            print(f"✓ [{i}/{len(image_files)}] {filename} -> {os.path.basename(output_path)}")
            
        except Exception as e:
            print(f"✗ [{i}/{len(image_files)}] {filename} - Error: {e}")
    
    print(f"\n✓ Done! Converted flags saved to: {output_folder}")


if __name__ == "__main__":
    # Usage: Process all images in a folder
    input_folder = "C:\Users\UA-CEO\Documents\Paradox Interactive\Europa Universalis V\mod\Formable Nations Reworked\main_menu\gfx\coat_of_arms\colored_emblems\flag_color_conversion"
    output_folder = "C:\Users\UA-CEO\Documents\Paradox Interactive\Europa Universalis V\mod\Formable Nations Reworked\main_menu\gfx\coat_of_arms\colored_emblems\flag_color_conversion"
    
    print("=" * 60)
    print("BATCH FLAG COLOR CONVERTER")
    print("=" * 60)
    print(f"Input:  {input_folder}")
    print(f"Output: {output_folder}")
    print("=" * 60 + "\n")
    
    batch_convert_flags(input_folder, output_folder)
