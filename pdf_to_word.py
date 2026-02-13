"""
PDF to Word Converter

Convert PDF documents to editable Microsoft Word files (.docx)
using the powerful `pdf2docx` library.

Author: Peter
"""

import os
import argparse
from pdf2docx import Converter

def convert_pdf_to_docx(pdf_file, docx_file):
    """
    Convert a single PDF file to Word DOCX format.
    """
    try:
        if not os.path.exists(pdf_file):
            print(f"Error: The file {pdf_file} does not exist.")
            return

        print(f"Converting {pdf_file} to {docx_file}...")

        # Create Converter
        cv = Converter(pdf_file)
        
        # Convert (default: start=0, end=None)
        cv.convert(docx_file)
        
        # Close PDF
        cv.close()
        
        print(f"Conversion complete: {docx_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF to Word DOCX.")
    parser.add_argument("pdf_file", help="Path to the input PDF file")
    parser.add_argument("--output", "-o", help="Path to the output DOCX file (optional)")
    
    args = parser.parse_args()
    
    output_file = args.output
    if not output_file:
        output_file = os.path.splitext(args.pdf_file)[0] + ".docx"
        
    convert_pdf_to_docx(args.pdf_file, output_file)
