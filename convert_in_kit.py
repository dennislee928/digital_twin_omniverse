#!/usr/bin/env python3
"""
USD to USDA Converter Script for Omniverse Kit Environment

This script should be run from within Omniverse Kit application's Python console.

Usage in Kit Console:
    exec(open('convert_in_kit.py').read())
    
Or copy and paste the code below directly into Kit Console.
"""

try:
    from pxr import Usd
    
    def convert_usd_to_usda(input_path, output_path):
        """Convert USD to USDA format."""
        print(f"Opening USD file: {input_path}")
        stage = Usd.Stage.Open(input_path)
        if not stage:
            print(f"Error: Cannot open USD file {input_path}")
            return False
        
        print(f"Exporting to USDA: {output_path}")
        stage.Export(output_path)
        print(f"✓ Successfully converted: {input_path} -> {output_path}")
        return True
    
    # Convert the file
    input_file = r"/Users/lipeichen/Documents/Untitled/digital_twin_omniverse/Factory_Lite/Factory_Lite.usd"
    output_file = r"/Users/lipeichen/Documents/Untitled/digital_twin_omniverse/Factory_Lite/Factory_Lite.usda"
    
    print("=" * 70)
    print("USD to USDA Conversion in Kit Environment")
    print("=" * 70)
    print()
    
    if convert_usd_to_usda(input_file, output_file):
        print()
        print("=" * 70)
        print("Conversion completed successfully!")
        print("=" * 70)
    else:
        print()
        print("=" * 70)
        print("Conversion failed!")
        print("=" * 70)
        
except ImportError as e:
    print("=" * 70)
    print("Error: USD Python API (pxr) is not available")
    print("=" * 70)
    print()
    print("Please ensure you are running this in Omniverse Kit application's Python console")
    print("(Window > Console in USD Explorer application)")
    print()
    print(f"Import error: {e}")
except Exception as e:
    print("=" * 70)
    print(f"Error during conversion: {e}")
    print("=" * 70)
    import traceback
    traceback.print_exc()
