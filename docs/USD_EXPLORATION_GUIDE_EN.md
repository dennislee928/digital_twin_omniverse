# USD Exploration Guide

This guide helps you understand OpenUSD file structure and digital twin development concepts.

## Step 1: Open Files in USD Explorer

1. **Launch your custom application** (USD Explorer template)
2. At the opening screen, click **New**, which will open a new file in Layout mode
3. In **Layout mode**, open the `Factory_Lite.usd` file

### Mode Explanation

- **Review Mode**: For end users to navigate, review, and add comments
- **Layout Mode**: For power users to assemble large scenes and execute changes

## Step 2: Convert to USDA Format

### Method A: Using USD Explorer Application (Recommended)

1. Open `Factory_Lite.usd` in the application
2. Select **File > Save As** or **Export**
3. Choose format as **USDA (ASCII)**
4. Save as `Factory_Lite.usda`

### Method B: Using Python Script

```bash
python convert_usd_to_usda.py Factory_Lite/Factory_Lite.usd
```

## Step 3: Examine Factory_Lite.usda Structure

Open the `.usda` file in VS Code or a text editor, and search for the term `.usd`.

### Key Concept: Payload References

You'll see structures like this:

```usda
def "Vehicle_Hanger_Adjust" (
    prepend payload = @./SubUSDs/Vehicle_Hanger_Adjust.usd@
)
```

This means:

- `Factory_Lite.usd` is a **composition file**
- It uses **payload** mechanism to reference other USD files
- Each asset (like `Vehicle_Hanger_Adjust`) is stored in a separate USD file
- These files are located in the `SubUSDs/` folder

### Why This Design?

1. **Lightweight Main File**: `Factory_Lite.usd` itself is small, containing only references
2. **Modularity**: Each asset can be updated independently without dealing with the entire scene
3. **Team Collaboration**: Different teams can edit different assets simultaneously
4. **Performance**: Can lazy load assets that aren't needed

## Step 4: Examine Individual Assets

1. Navigate to the `SubUSDs/` folder in the application
2. Locate `Vehicle_Hanger_Adjust.usd`
3. Double-click to open the asset

### Convert Individual Asset to USDA

Similarly, save `Vehicle_Hanger_Adjust.usd` as `.usda` format.

### Examine Asset Content

In the `.usda` file, you'll see:

- **Vertex Positions**: Define the shape in 3D space
- **Faces**: Define geometric shapes
- **Materials and Attributes**: Data related to visual appearance

## OpenUSD Advantages

### 1. Data Aggregation

- Can combine different types of data from multiple sources
- Supports assembly of complex scenes

### 2. Reference Mechanisms (References & Payloads)

- **Reference**: Direct reference, loaded immediately
- **Payload**: Lazy loading, loaded only when needed (better performance)

### 3. Variants

- The same asset can have multiple versions
- Can dynamically switch between different variants

### 4. Layers

- Supports multi-layer editing
- Can override specific attributes without modifying the original file

## Next Steps: Exploring Variants

In the next phase, you'll learn:

- How **Variants** are represented in OpenUSD
- How to use variants to manage different versions of assets
- How to use the Variant Presenter extension to view and switch variants

**Detailed Guide**: See [Variant Presenter Setup Guide](VARIANT_PRESENTER_GUIDE_EN.md)

## Related Resources

- [Learn OpenUSD Learning Path](https://www.nvidia.com/en-us/omniverse/learn/openusd/)
- [Data Aggregation and Navigation Guide](https://docs.omniverse.nvidia.com/)
- [USD Official Documentation](https://openusd.org/)
- [Create a Variant Set](https://docs.omniverse.nvidia.com/) - Learn how to code variant sets
