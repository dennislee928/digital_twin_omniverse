# Import Assets Guide

This guide explains how to import 3D assets into your USD Explorer application from various sources, including CAD drawings, manufacturer models, or asset libraries.

## Overview

End users will import 3D data from various sources:
- CAD drawings
- Manufacturer models
- Asset libraries (such as NVIDIA Assets)

This guide demonstrates how to import assets from the NVIDIA Assets library.

## Step 1: Launch Application

### Launch from VS Code

1. **Open Project in VS Code**
   - Open the project folder containing your USD Explorer application

2. **Launch Application**
   - Use VS Code's terminal or command palette to launch the application
   - Or launch directly from Omniverse Launcher

### Launch from Omniverse Launcher

1. Open **Omniverse Launcher**
2. Find your custom application
3. Click **Launch** to start the application

## Step 2: Load Factory_Lite.usd

1. **Open File**
   - After the application starts, select **File > Open**
   - Or click the **Open** button on the welcome screen

2. **Select File**
   - Navigate to the `Factory_Lite.usd` file location
   - Select the file and click **Open**

3. **Confirm Loading**
   - After the file loads, you should see the factory scene in the viewport

## Step 3: Access NVIDIA Assets Library

1. **Find NVIDIA Assets Tab**
   - Locate the **NVIDIA Assets** tab at the **lower left** of the application window
   - If the tab is not visible, you may need to expand the left panel

2. **Click Warehouse Option**
   - In the NVIDIA Assets panel, click the **Warehouse** option
   - This will display the warehouse-related asset library

## Step 4: Browse and Select Asset

1. **Scroll Through Options**
   - Scroll through the available assets in the Warehouse library
   - Assets may include:
     - Shelving and storage equipment
     - Material handling equipment
     - Packaging materials
     - Other warehouse-related objects

2. **Select Asset to Add**
   - Find the asset you want to add to the scene
   - Consider the asset's purpose and placement

## Step 5: Drag and Drop Asset to Scene

1. **Drag Asset**
   - **Drag** the selected asset from the asset browser
   - Drag the asset toward the **viewport**

2. **View Placement Indicator**
   - As the asset is dragged into the viewport, **cross hairs** will appear
   - The cross hairs indicate where the asset will be placed on the **floor**
   - Move the mouse to adjust the placement position

3. **Release Asset**
   - When the position is suitable, **release the mouse button**
   - The asset will automatically sit on the **ground plane**
   - The asset will automatically align to the ground

## Asset Placement Features

### Auto-Alignment Features

- **Ground Plane Alignment**: Assets automatically sit on the scene's ground plane
- **Position Indicator**: Cross hairs provide real-time position feedback
- **Live Preview**: You can see a preview of the asset position while dragging

### Post-Placement Adjustments

After placing an asset, you can:
- **Move**: Use the move tool to adjust position
- **Rotate**: Use the rotate tool to adjust orientation
- **Scale**: Use the scale tool to adjust size
- **Delete**: Remove the asset if not needed

## Workflow Tips

### 1. Plan Asset Placement

Before adding assets:
- Consider the overall layout of the scene
- Plan asset positions and orientations
- Ensure assets don't overlap with existing objects

### 2. Using Multiple Assets

- You can add multiple assets from the library
- Each asset will automatically align to the ground plane
- Use the move tool to adjust relative positions

### 3. Organize Scene

- Use USD's layer functionality to organize assets
- Create different layers for different asset types
- Use naming conventions to keep the scene tidy

## Next Step: Duplicate Assets

In the next step, you'll learn methods for **duplicating assets** using OpenUSD.

### Methods for Duplicating Assets

OpenUSD provides several methods for duplicating assets:

1. **Direct Copy**
   - Select asset in scene
   - Use copy/paste functionality

2. **Instancing**
   - Create instances of assets
   - Saves memory and improves performance

3. **References**
   - Reference the original asset
   - Maintains link to the original asset

## Common Questions

### Q: Can't find NVIDIA Assets tab?

**A**: 
- Check if the left panel is expanded
- Confirm the application has loaded all extensions correctly
- Try restarting the application

### Q: Asset not placing correctly?

**A**:
- Ensure there's a ground plane in the scene
- Check if the asset's coordinate system is correct
- Use the move tool to manually adjust position

### Q: How to delete an added asset?

**A**:
- Select the asset
- Press `Delete` key or use the delete option in the edit menu

### Q: Can I import custom assets?

**A**: Yes!
- Use **File > Import** to import custom assets
- Supports multiple formats (USD, FBX, OBJ, etc.)
- Imported assets are automatically converted to USD format

## Related Resources

- [USD Exploration Guide](docs/USD_EXPLORATION_GUIDE.md)
- [Variant Presenter Setup Guide](VARIANT_PRESENTER_GUIDE.md)
- [Omniverse Documentation](https://docs.omniverse.nvidia.com/)
- [NVIDIA Assets Library](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/overview.html)

## Workflow Summary

```
1. Launch Application
   ↓
2. Load Factory_Lite.usd
   ↓
3. Open NVIDIA Assets > Warehouse
   ↓
4. Browse and Select Asset
   ↓
5. Drag and Drop Asset to Viewport
   ↓
6. Asset Automatically Sits on Ground Plane
   ↓
7. (Next) Learn Methods for Duplicating Assets
```
