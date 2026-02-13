"""
Steganography Tool (LSB)

Hide secret text messages inside images using Least Significant Bit (LSB) encoding.
Requires: Pillow

Usage:
    python stegano_tool.py encode input.png "Secret Message" output.png
    python stegano_tool.py decode output.png

Author: Peter
"""

import sys
import argparse
from PIL import Image

def encode_image(img_path, message, output_path):
    """Encodes a message into an image using LSB."""
    try:
        img = Image.open(img_path)
        width, height = img.size
        pixels = list(img.getdata())

        # Convert message to binary
        binary_msg = ''.join(format(ord(char), '08b') for char in message) + '1111111111111110' # Delimiter
        data_len = len(binary_msg)
        
        if data_len > width * height * 3:
            raise ValueError("Message too long for this image.")

        new_pixels = []
        data_index = 0

        for pixel in pixels:
            r, g, b = pixel[:3] # Handle RGBA

            if data_index < data_len:
                r = (r & ~1) | int(binary_msg[data_index])
                data_index += 1
            if data_index < data_len:
                g = (g & ~1) | int(binary_msg[data_index])
                data_index += 1
            if data_index < data_len:
                b = (b & ~1) | int(binary_msg[data_index])
                data_index += 1

            new_pixels.append((r, g, b) + pixel[3:] if len(pixel) > 3 else (r, g, b))

        img.putdata(new_pixels)
        img.save(output_path, "PNG")
        print(f"[SUCCESS] Message hidden in {output_path}")

    except Exception as e:
        print(f"[ERROR] Encoding failed: {e}")

def decode_image(img_path):
    """Decodes a message from an LSB encoded image."""
    try:
        img = Image.open(img_path)
        pixels = list(img.getdata())
        
        binary_msg = ""
        for pixel in pixels:
            r, g, b = pixel[:3]
            binary_msg += str(r & 1)
            binary_msg += str(g & 1)
            binary_msg += str(b & 1)

        # Split by delimiter
        delimiter = '1111111111111110'
        if delimiter in binary_msg:
            binary_msg = binary_msg.split(delimiter)[0]
        else:
            print("[WARNING] No delimiter found. Message might be corrupted or image not encoded.")
            return

        # Convert binary to string
        message = ""
        for i in range(0, len(binary_msg), 8):
            byte = binary_msg[i:i+8]
            if len(byte) == 8:
                message += chr(int(byte, 2))
        
        print(f"[SUCCESS] Decoded Message: {message}")

    except Exception as e:
        print(f"[ERROR] Decoding failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LSB Steganography Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Encode
    enc_parser = subparsers.add_parser("encode", help="Hide a message in an image")
    enc_parser.add_argument("image", help="Input image path (PNG recommended)")
    enc_parser.add_argument("message", help="Secret message to hide")
    enc_parser.add_argument("output", help="Output image path")

    # Decode
    dec_parser = subparsers.add_parser("decode", help="Reveal a hidden message")
    dec_parser.add_argument("image", help="Encoded image path")

    args = parser.parse_args()

    if args.command == "encode":
        encode_image(args.image, args.message, args.output)
    elif args.command == "decode":
        decode_image(args.image)
