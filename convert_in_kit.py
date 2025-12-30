#!/usr/bin/env python3
"""
USD to USDA Converter Script for Omniverse Kit Environment

This script should be run from within Omniverse Kit application's Python console
or using Kit's command-line tools.

Usage in Kit Console:
    exec(open('convert_via_explorer.py').read())
"""

import sys
import os

# Add the script directory to path if needed
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)

try:
    from pxr import Usd
    
    def convert_usd_to_usda(input_path, output_path):
        """Convert USD to USDA format."""
        stage = Usd.Stage.Open(input_path)
        if not stage:
            print(f"Error: Cannot open USD file {input_path}")
            return False
        
        stage.Export(output_path)
        print(f"Successfully converted: {input_path} -> {output_path}")
        return True
    
    # Convert the file
    input_file = r"/Users/lipeichen/Documents/Untitled/digital_twin_omniverse/Factory_Lite/Factory_Lite.usd"
    output_file = r"/Users/lipeichen/Documents/Untitled/digital_twin_omniverse/Factory_Lite/Factory_Lite.usda"
    
    if convert_usd_to_usda(input_file, output_file):
        print("Conversion completed successfully!")
    else:
        print("Conversion failed!")
        
except ImportError:
    print("Error: USD Python API (pxr) is not available in this environment")
    print("Please ensure you are running this in Omniverse Kit application's Python console")
