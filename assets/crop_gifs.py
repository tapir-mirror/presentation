#!/usr/bin/env python3
"""
GIF Cropping Utility
Removes the top 10% of each GIF frame to improve alignment in presentations.
"""

import os
from PIL import Image, ImageSequence
import argparse

def crop_gif_top(input_path, output_path, crop_percentage=0.1):
    """
    Crop the top portion of a GIF file.
    
    Args:
        input_path (str): Path to input GIF file
        output_path (str): Path to output GIF file
        crop_percentage (float): Percentage of height to crop from top (0.1 = 10%)
    """
    try:
        # Open the GIF
        with Image.open(input_path) as img:
            frames = []
            durations = []
            
            # Get original dimensions
            width, height = img.size
            crop_height = int(height * crop_percentage)
            new_height = height - crop_height
            
            print(f"Processing {input_path}:")
            print(f"  Original size: {width}x{height}")
            print(f"  Cropping top {crop_height}px ({crop_percentage*100}%)")
            print(f"  New size: {width}x{new_height}")
            
            # Process each frame
            for frame_num, frame in enumerate(ImageSequence.Iterator(img)):
                # Convert frame to RGBA if needed
                if frame.mode != 'RGBA':
                    frame = frame.convert('RGBA')
                
                # Crop the frame (left, top, right, bottom)
                cropped_frame = frame.crop((0, crop_height, width, height))
                frames.append(cropped_frame)
                
                # Get frame duration
                try:
                    duration = frame.info.get('duration', 100)
                    durations.append(duration)
                except:
                    durations.append(100)  # Default duration
            
            # Save the cropped GIF
            if frames:
                frames[0].save(
                    output_path,
                    save_all=True,
                    append_images=frames[1:],
                    duration=durations,
                    loop=0,
                    optimize=True
                )
                print(f"  Saved to: {output_path}")
                print(f"  Processed {len(frames)} frames")
            else:
                print(f"  Error: No frames found in {input_path}")
                
    except Exception as e:
        print(f"Error processing {input_path}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Crop the top portion of GIF files')
    parser.add_argument('files', nargs='*', help='GIF files to process')
    parser.add_argument('--crop', type=float, default=0.1, 
                       help='Percentage to crop from top (default: 0.1 for 10%)')
    parser.add_argument('--suffix', default='_cropped', 
                       help='Suffix to add to output files (default: _cropped)')
    parser.add_argument('--output-dir', 
                       help='Output directory (default: same as input)')
    
    args = parser.parse_args()
    
    # If no files specified, process the specific GIFs mentioned
    if not args.files:
        gif_files = [
            'alexp.gif', 'alexv.gif', 'dianap.gif', 
            'dianav.gif', 'kalp.gif', 'kalv.gif'
        ]
        # Check if files exist in current directory
        existing_files = [f for f in gif_files if os.path.exists(f)]
        if existing_files:
            args.files = existing_files
        else:
            print("No GIF files specified and default files not found.")
            print("Usage: python crop_gifs.py [file1.gif file2.gif ...]")
            return
    
    # Process each file
    for input_file in args.files:
        if not os.path.exists(input_file):
            print(f"Warning: File not found: {input_file}")
            continue
        
        # Generate output filename
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}{args.suffix}.gif"
        
        # Use output directory if specified
        if args.output_dir:
            os.makedirs(args.output_dir, exist_ok=True)
            output_file = os.path.join(args.output_dir, os.path.basename(output_file))
        
        # Crop the GIF
        crop_gif_top(input_file, output_file, args.crop)
        print()

if __name__ == "__main__":
    main() 