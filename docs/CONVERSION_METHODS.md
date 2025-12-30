# USD to USDA Conversion Methods

Complete guide to converting USD files to USDA format when USD Python API is not available in your system Python environment.

## Overview

When `check_usd_environment.py` shows that USD Python API is not available, you have three methods to convert USD files:

1. **USD Explorer Application** (Easiest - Recommended)
2. **Omniverse Kit Python Console** (For automation)
3. **Install USD Python Bindings** (Advanced)

## Method 1: USD Explorer Application (Easiest)

### Quick Start

Run the helper script:
```bash
python convert_via_explorer.py Factory_Lite/Factory_Lite.usd
```

This will provide step-by-step instructions.

### Manual Steps

1. **Launch USD Explorer**
   - Open Omniverse Launcher
   - Find and launch "USD Explorer" or your custom application

2. **Open USD File**
   - Select **File > Open**
   - Navigate to your USD file
   - Click **Open**

3. **Save as USDA**
   - Select **File > Save As**
   - Choose format: **USDA (ASCII)**
   - Choose save location
   - Click **Save**

### Advantages

- ✅ No programming required
- ✅ Works immediately
- ✅ Visual feedback
- ✅ Can preview before saving

## Method 2: Omniverse Kit Python Console

For automation or batch conversion, use Kit's built-in Python console.

### Step 1: Generate Kit Script

```bash
python convert_via_explorer.py Factory_Lite/Factory_Lite.usd
```

This creates `convert_in_kit.py` with your file paths.

### Step 2: Run in Kit Console

1. **Launch USD Explorer application**

2. **Open Python Console**
   - Select **Window > Console**

3. **Run the script**
   ```python
   exec(open('convert_in_kit.py').read())
   ```

### Alternative: Direct Code

Copy and paste this into Kit Console:

```python
from pxr import Usd
import os

def convert_usd_to_usda(input_path, output_path):
    """Convert USD to USDA format."""
    stage = Usd.Stage.Open(input_path)
    if not stage:
        print(f"Error: Cannot open USD file {input_path}")
        return False
    
    stage.Export(output_path)
    print(f"Successfully converted: {input_path} -> {output_path}")
    return True

# Use absolute paths
input_file = r"/full/path/to/Factory_Lite.usd"
output_file = r"/full/path/to/Factory_Lite.usda"

convert_usd_to_usda(input_file, output_file)
```

### Batch Conversion

To convert multiple files:

```python
from pxr import Usd
import os
import glob

def convert_usd_to_usda(input_path, output_path):
    stage = Usd.Stage.Open(input_path)
    if not stage:
        return False
    stage.Export(output_path)
    return True

# Convert all USD files in a directory
usd_files = glob.glob("/path/to/directory/*.usd")
for usd_file in usd_files:
    usda_file = usd_file.replace('.usd', '.usda')
    if convert_usd_to_usda(usd_file, usda_file):
        print(f"Converted: {usd_file}")
```

## Method 3: Install USD Python Bindings

For advanced users who want to use USD Python API in their system Python.

### Option A: Build from Source

1. **Clone USD repository**
   ```bash
   git clone https://github.com/PixarAnimationStudios/USD.git
   cd USD
   ```

2. **Build and install**
   ```bash
   python build_scripts/build_usd.py /usr/local/usd
   ```

3. **Set environment variables**
   ```bash
   export PYTHONPATH=/usr/local/usd/lib/python:$PYTHONPATH
   ```

### Option B: Use Pre-compiled Releases

Check USD releases for pre-compiled binaries for your platform.

## Comparison of Methods

| Method | Difficulty | Automation | Best For |
|--------|-----------|------------|----------|
| USD Explorer UI | ⭐ Easy | ❌ Manual | Single files, beginners |
| Kit Console | ⭐⭐ Medium | ✅ Yes | Batch conversion, automation |
| Install Bindings | ⭐⭐⭐ Advanced | ✅ Yes | Development, scripting |

## Troubleshooting

### Issue: Can't find USD Explorer

**Solution**:
- Check Omniverse Launcher for installed applications
- Verify application is properly installed
- Try launching from command line if available

### Issue: Console not available

**Solution**:
- Ensure Console extension is enabled
- Check Window menu
- Restart application

### Issue: Script fails in Console

**Solution**:
- Use absolute paths (not relative)
- Check file permissions
- Ensure USD file is not locked

## Related Tools

- `check_usd_environment.py` - Check if USD API is available
- `convert_via_explorer.py` - Helper script for conversion
- `convert_in_kit.py` - Generated script for Kit console

## Related Documentation

- [Kit Environment Conversion Guide](KIT_ENVIRONMENT_CONVERSION.md)
- [USD Conversion Guide](USD_CONVERSION_GUIDE.md)
- [USD Exploration Guide](USD_EXPLORATION_GUIDE.md)
