"""
Auto-Vlog Generator

Simple video concatenator using MoviePy.
Merges all .mp4 files in a directory into one final video.

Requires: moviepy

Author: Peter
"""

import os
import argparse
from moviepy.editor import VideoFileClip, concatenate_videoclips

def merge_videos(input_dir, output_file):
    """Merges all MP4 files in directory."""
    try:
        clips = []
        files = sorted([f for f in os.listdir(input_dir) if f.endswith(".mp4")])
        
        if not files:
            print("[ERROR] No MP4 files found in directory.")
            return

        print(f"Found {len(files)} videos. Processing...")
        
        for filename in files:
            path = os.path.join(input_dir, filename)
            print(f"Loading {filename}...")
            clip = VideoFileClip(path)
            clips.append(clip)

        print("Concatenating...")
        final_clip = concatenate_videoclips(clips)
        
        print(f"Writing to {output_file}...")
        final_clip.write_videofile(output_file)
        
        print("[SUCCESS] Video merged!")

    except Exception as e:
        print(f"[ERROR] Merge failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge MP4 videos in a folder.")
    parser.add_argument("input_dir", help="Directory containing .mp4 files")
    parser.add_argument("output_file", help="Output filename (e.g. final.mp4)")
    
    args = parser.parse_args()
    
    merge_videos(args.input_dir, args.output_file)
