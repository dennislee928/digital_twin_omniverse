# Variant Presenter Setup Guide

This guide explains how to add the Variant Presenter extension to your USD Explorer application and explore the Variants functionality in OpenUSD.

## What are Variants?

OpenUSD can store multiple variations of assets called **variants**. **VariantSets** are made up of two or more opinions. Variants make it possible for stakeholders to review different assets, materials, and asset placement within a single USD file.

## Step 1: Convert Factory_Lite.usd to USDA Format

First, we need to convert the USD file to readable ASCII format to view variant definitions in VS Code.

### Method A: Using USD Explorer Application

1. Launch your USD Explorer application
2. Open the `Factory_Lite.usd` file
3. Select **File > Save As**
4. Choose format as **USDA (ASCII)**
5. Save as `Factory_Lite.usda`

### Method B: Using Python Script

```bash
# Run from project root directory
python convert_usd_to_usda.py Factory_Lite/Factory_Lite.usd
```

## Step 2: View Variant Definitions in VS Code

1. Open the `Factory_Lite.usda` file in VS Code
2. Use the search function (`Cmd+F` or `Ctrl+F`) to search for **"variant"**
3. You'll see variant definitions like this:

```usda
def "SomePrim" (
    variants = {
        string variantSetName = "variantValue"
    }
    prepend variantSets = "variantSetName"
)
{
    variantSet "variantSetName" = {
        "variantValue" {
            # Variant-specific content
        }
        "anotherVariantValue" {
            # Another variant's content
        }
    }
}
```

## Step 3: Add Variant Presenter Extension to Application

Variant Presenter is a sample extension for presenting and selecting variants, which can be customized with application-specific UI and logic.

### 3.1 Locate Your Application's .kit File

Your custom application should have a `.kit` file. Depending on the template you used, it might be located at:

- If you used USD Explorer template: `<your_app_directory>/omni.usd_explorer.kit`
- Or similar location

**Note**: If you haven't created a custom application yet, please create one using the USD Explorer template first.

### 3.2 Edit the .kit File

1. **Exit your application** (if running)
2. Open your application's `.kit` file in VS Code
3. Find the `[dependencies]` section
4. Add the following line to the `[dependencies]` section:

```toml
[dependencies]
# ... other dependencies ...
"omni.kit.variant.presenter" = {}
```

### 3.3 Save the File

After saving the `.kit` file, restart your application.

## Step 4: Use Variant Presenter

1. **Launch your application**
2. **Open Factory_Lite.usd** file
3. In your application, choose **Tools > Variants > Variant Presenter** to access the Variant Presenter panel

## Step 5: Compare .usda Code with Application Display

In the Variant Presenter panel, you can:

1. **View all available VariantSets**
2. **View variant options in each VariantSet**
3. **Switch between different variants** and see scene changes in real-time
4. **Compare variant definitions** in the `.usda` file with what's displayed in the application

### Variant Definition Example

In the `.usda` file, you might see a structure like this:

```usda
def "Factory_Equipment" (
    prepend variantSets = "equipmentType"
)
{
    variantSet "equipmentType" = {
        "TypeA" {
            def "Equipment" (
                prepend payload = @./SubUSDs/Equipment_TypeA.usd@
            )
        }
        "TypeB" {
            def "Equipment" (
                prepend payload = @./SubUSDs/Equipment_TypeB.usd@
            )
        }
    }
}
```

This means:
- There's a VariantSet named `equipmentType`
- It contains two variants: `TypeA` and `TypeB`
- Each variant references a different USD file

## Advantages of Variants

1. **Single File for Multiple Versions**: No need to create separate files for each version
2. **Quick Switching**: Quickly switch between different variants for comparison
3. **Collaboration Friendly**: Team members can view and select different variants
4. **Reduced File Count**: All variants are in a single USD file

## Learn More

- **Create a Variant Set** topic: Learn how to code variant sets with OpenUSD
- [OpenUSD Official Documentation](https://openusd.org/)
- [Omniverse Documentation](https://docs.omniverse.nvidia.com/)

## Troubleshooting

### Issue: Cannot Find .kit File

**Solution**:
- Confirm you've created a custom application from a template
- Check the application installation directory
- Look at application settings in Omniverse Launcher

### Issue: Variant Presenter Menu Not Appearing

**Solution**:
- Confirm you've correctly added `"omni.kit.variant.presenter" = {}` to the `.kit` file
- Confirm you've restarted the application
- Check if the extension is properly loaded (Window > Extensions)

### Issue: Cannot See Variant Options

**Solution**:
- Confirm the `Factory_Lite.usd` file contains variant definitions
- Search for "variant" in VS Code to confirm variants exist in the file
- Try selecting different prims in the scene to view their variants
