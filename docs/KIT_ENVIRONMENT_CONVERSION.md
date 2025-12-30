# Converting USD Files in Omniverse Kit Environment

This guide explains how to convert USD files to USDA format when USD Python API is not available in your system Python environment.

## Method 1: Using USD Explorer Application (Easiest)

This is the simplest method and requires no programming.

### Steps

1. **Launch USD Explorer Application**
   - Open Omniverse Launcher
   - Find and launch "USD Explorer" or your custom USD Explorer application

2. **Open the USD File**
   - Select **File > Open**
   - Navigate to your USD file (e.g., `Factory_Lite.usd`)
   - Click **Open**

3. **Save as USDA Format**
   - Select **File > Save As**
   - In the file dialog, choose format: **USDA (ASCII)**
   - Choose save location
   - Click **Save**

### Advantages

- ✅ No programming required
- ✅ Works immediately
- ✅ Visual feedback
- ✅ Can preview file before saving

## Method 2: Using Kit's Python Console

If you need to automate the conversion or convert multiple files, you can use Omniverse Kit's built-in Python console.

### Step 1: Launch Application

1. Launch your USD Explorer application
2. Open **Window > Console** to access the Python console

### Step 2: Run Conversion Script

#### Option A: Use Generated Script

1. **Generate the script**:
   ```bash
   python convert_via_explorer.py Factory_Lite/Factory_Lite.usd
   ```
   This creates `convert_in_kit.py`

2. **In Kit Console**, run:
   ```python
   exec(open('convert_in_kit.py').read())
   ```

#### Option B: Direct Code

In Kit Console, paste and run:

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

# Convert the file
input_file = r"/full/path/to/Factory_Lite.usd"
output_file = r"/full/path/to/Factory_Lite.usda"

if convert_usd_to_usda(input_file, output_file):
    print("Conversion completed successfully!")
```

**Important**: Use full absolute paths in the script.

### Step 3: Verify Conversion

1. Check that the `.usda` file was created
2. Open it in a text editor to verify it's in ASCII format
3. You should see readable USD syntax

## Method 3: Using Kit Command Line

If your application supports command-line execution, you can run scripts directly.

### Using Kit's Python

```bash
# Find Kit's Python executable
# Usually in: <app_install_dir>/kit/python/bin/python

# Run conversion script
<kit_python> convert_usd_to_usda.py Factory_Lite/Factory_Lite.usd
```

### Finding Kit Python

Kit Python is typically located at:
- **Windows**: `<app_dir>/kit/python/bin/python.exe`
- **Linux/macOS**: `<app_dir>/kit/python/bin/python`

## Automated Script

The `convert_via_explorer.py` script can help automate the process:

```bash
python convert_via_explorer.py Factory_Lite/Factory_Lite.usd
```

This script will:
1. Check if USD Explorer is available
2. Provide manual conversion instructions
3. Generate a Kit environment script (`convert_in_kit.py`)

## Troubleshooting

### Issue: Console Not Available

**Solution**:
- Ensure Console extension is enabled
- Check Window menu for Console option
- Try restarting the application

### Issue: Script Fails in Console

**Solution**:
- Use absolute paths (not relative)
- Check file permissions
- Ensure USD file is not locked by another process

### Issue: pxr Module Not Found in Console

**Solution**:
- This should not happen in Kit environment
- Try restarting the application
- Check that you're using Kit's console, not system Python

## Best Practices

### 1. Use Absolute Paths

Always use full absolute paths in scripts:
```python
# Good
input_file = r"/Users/username/project/Factory_Lite.usd"

# Avoid
input_file = "Factory_Lite.usd"  # May not work
```

### 2. Verify Before Converting

Check file exists and is readable:
```python
import os
if not os.path.exists(input_file):
    print(f"Error: File not found: {input_file}")
```

### 3. Handle Errors

Wrap conversion in try-except:
```python
try:
    stage = Usd.Stage.Open(input_path)
    stage.Export(output_path)
except Exception as e:
    print(f"Error: {e}")
```

## Related Resources

- [USD Conversion Guide](USD_CONVERSION_GUIDE.md)
- [USD Exploration Guide](USD_EXPLORATION_GUIDE.md)
- [Omniverse Documentation](https://docs.omniverse.nvidia.com/)
