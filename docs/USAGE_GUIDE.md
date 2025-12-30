# USD Conversion Tools - Usage Guide

Quick reference guide for using the USD conversion tools.

## Quick Start

### Method 1: Manual Conversion (Easiest)

```bash
# Step 1: Run the helper script
python convert_via_explorer.py Factory_Lite/Factory_Lite.usd
```

The script will output step-by-step instructions. Then:

1. **Launch USD Explorer** application
2. **File > Open** → Select your USD file
3. **File > Save As** → Choose **USDA (ASCII)** format
4. **Save** the file

### Method 2: Automated Conversion in Kit Console

```bash
# Step 1: Generate the Kit environment script
python convert_via_explorer.py Factory_Lite/Factory_Lite.usd
```

This creates `convert_in_kit.py`. Then:

1. **Launch USD Explorer** application
2. **Window > Console** (to open Python console)
3. In the console, type:
   ```python
   exec(open('convert_in_kit.py').read())
   ```

**Important**: The `exec(open('convert_in_kit.py').read())` command must be run **inside the Kit Console**, not in your terminal!

## Common Mistakes

### ❌ Wrong: Running Python code in terminal

```bash
# This will NOT work in terminal
exec(open('convert_in_kit.py').read())
```

**Error**: `zsh: parse error near ')'`

**Why**: This is Python code, not shell commands.

### ✅ Correct: Run in Kit Console

1. Launch USD Explorer
2. Open Window > Console
3. Paste the Python code there

### ❌ Wrong: Running comments in terminal

```bash
# This is a comment
python convert_via_explorer.py Factory_Lite/Factory_Lite.usd
```

**Error**: `zsh: command not found: #`

**Why**: Shell tries to execute `#` as a command.

### ✅ Correct: Comments are for documentation

Comments (lines starting with `#`) are for documentation only. Don't copy them into terminal.

## Step-by-Step Example

### Complete Workflow

```bash
# 1. Check your environment
python check_usd_environment.py

# 2. Generate conversion helper
python convert_via_explorer.py Factory_Lite/Factory_Lite.usd

# 3. Follow the output instructions
#    - Either use manual method in USD Explorer
#    - Or use convert_in_kit.py in Kit Console
```

## File Locations

After running `convert_via_explorer.py`:

- **Generated script**: `convert_in_kit.py` (in project root)
- **Input file**: `Factory_Lite/Factory_Lite.usd`
- **Output file**: `Factory_Lite/Factory_Lite.usda` (will be created)

## Troubleshooting

### Script not found

```bash
# Make sure you're in the project directory
cd /Users/lipeichen/Documents/Untitled/digital_twin_omniverse

# Check if script exists
ls convert_via_explorer.py
```

### Kit Console not available

- Ensure USD Explorer application is running
- Check Window menu for Console option
- Console extension may need to be enabled

### File paths in convert_in_kit.py

The generated script uses absolute paths. If you move files, regenerate:

```bash
python convert_via_explorer.py <new_path>/file.usd
```

## Related Documentation

- [Conversion Methods](docs/CONVERSION_METHODS.md) - Detailed comparison
- [Kit Environment Conversion](docs/KIT_ENVIRONMENT_CONVERSION.md) - Complete guide
- [Utilities README](UTILITIES_README.md) - All tools documentation
