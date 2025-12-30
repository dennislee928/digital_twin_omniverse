#!/usr/bin/env python3
"""
USD to USDA Converter via USD Explorer Application

This script provides an automated way to convert USD files to USDA format
using the USD Explorer application, which is the easiest method when
USD Python API is not available.

Usage:
    python convert_via_explorer.py <input.usd> [output.usda]
    
Note: This script requires USD Explorer application to be installed.
"""

import sys
import os
import subprocess
import platform
from pathlib import Path


def find_usd_explorer_app():
    """
    Find USD Explorer application on the system.
    
    Returns:
        str: Path to USD Explorer application, or None if not found
    """
    system = platform.system().lower()
    
    # Common installation paths
    if system == "darwin":  # macOS
        possible_paths = [
            "/Applications/NVIDIA Omniverse/omni.usd.explorer.app",
            os.path.expanduser("~/Library/Application Support/Omniverse/omni.usd.explorer.app"),
            "/Applications/Omniverse/omni.usd.explorer.app",
        ]
    elif system == "windows":
        possible_paths = [
            os.path.expanduser("~/AppData/Local/Programs/Omniverse/omni.usd.explorer.exe"),
            "C:/Program Files/NVIDIA Omniverse/omni.usd.explorer.exe",
            "C:/Program Files/Omniverse/omni.usd.explorer.exe",
        ]
    else:  # Linux
        possible_paths = [
            os.path.expanduser("~/omniverse/omni.usd.explorer"),
            "/opt/nvidia/omniverse/omni.usd.explorer",
        ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return path
    
    return None


def convert_via_explorer_manual(input_path, output_path=None):
    """
    Provide manual instructions for converting via USD Explorer.
    
    Args:
        input_path: Input USD file path
        output_path: Output USDA file path (optional)
    """
    if output_path is None:
        base_name = os.path.splitext(input_path)[0]
        output_path = f"{base_name}.usda"
    
    print("=" * 70)
    print("USD to USDA Conversion via USD Explorer Application")
    print("=" * 70)
    print()
    print("Since USD Python API is not available, please use USD Explorer:")
    print()
    print("Steps:")
    print("1. Launch USD Explorer application")
    print("   - From Omniverse Launcher, find and launch 'USD Explorer'")
    print("   - Or launch your custom USD Explorer application")
    print()
    print("2. Open the USD file")
    print(f"   - File > Open")
    print(f"   - Navigate to: {os.path.abspath(input_path)}")
    print(f"   - Select the file and click Open")
    print()
    print("3. Save as USDA format")
    print("   - File > Save As")
    print("   - Choose format: USDA (ASCII)")
    print(f"   - Save to: {os.path.abspath(output_path)}")
    print("   - Click Save")
    print()
    print("=" * 70)
    print()
    print("Alternative: Use the automated script in Omniverse Kit environment")
    print("See: convert_in_kit_environment.py")
    print()


def create_kit_script(input_path, output_path=None):
    """
    Create a Python script that can be run in Omniverse Kit environment.
    
    Args:
        input_path: Input USD file path
        output_path: Output USDA file path (optional)
    """
    if output_path is None:
        base_name = os.path.splitext(input_path)[0]
        output_path = f"{base_name}.usda"
    
    abs_input = os.path.abspath(input_path)
    abs_output = os.path.abspath(output_path)
    
    script_content = f'''#!/usr/bin/env python3
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
        print(f"Opening USD file: {{input_path}}")
        stage = Usd.Stage.Open(input_path)
        if not stage:
            print(f"Error: Cannot open USD file {{input_path}}")
            return False
        
        print(f"Exporting to USDA: {{output_path}}")
        stage.Export(output_path)
        print(f"✓ Successfully converted: {{input_path}} -> {{output_path}}")
        return True
    
    # Convert the file
    input_file = r"{abs_input}"
    output_file = r"{abs_output}"
    
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
    print(f"Import error: {{e}}")
except Exception as e:
    print("=" * 70)
    print(f"Error during conversion: {{e}}")
    print("=" * 70)
    import traceback
    traceback.print_exc()
'''
    
    script_path = "convert_in_kit.py"
    with open(script_path, 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    # Make executable on Unix systems
    if platform.system() != "windows":
        os.chmod(script_path, 0o755)
    
    print(f"✓ Created Kit environment script: {script_path}")
    print()
    print("To use this script in Kit Console:")
    print("1. Launch your USD Explorer application")
    print("2. Open Window > Console (to access Python console)")
    print(f"3. Run: exec(open('{script_path}').read())")
    print()
    print("Or copy and paste the code from the script directly into the console.")
    print()
    
    return script_path


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nExamples:")
        print("  python convert_via_explorer.py Factory_Lite/Factory_Lite.usd")
        print("  python convert_via_explorer.py Factory_Lite/Factory_Lite.usd output.usda")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    if not os.path.exists(input_path):
        print(f"Error: File not found: {input_path}")
        sys.exit(1)
    
    # Check if USD Explorer is available
    explorer_path = find_usd_explorer_app()
    
    if explorer_path:
        print(f"Found USD Explorer at: {explorer_path}")
        print("However, automated conversion requires Kit SDK integration.")
        print("Please use manual method or Kit environment script.")
        print()
    
    # Provide manual instructions
    convert_via_explorer_manual(input_path, output_path)
    
    # Create Kit environment script
    create_kit_script(input_path, output_path)
    
    print("=" * 70)
    print("Summary:")
    print("=" * 70)
    print("1. Manual method: Follow the steps above in USD Explorer")
    print("2. Kit environment: Use convert_in_kit.py in Kit's Python console")
    print("=" * 70)


if __name__ == "__main__":
    main()
