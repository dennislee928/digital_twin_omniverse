#!/bin/bash
# Physics Setup Script
#
# This script helps configure physics simulation in your USD Explorer application
# by updating the .kit file with necessary settings.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "=========================================="
echo "Physics Simulation Setup"
echo "=========================================="
echo ""

# Find .kit files
KIT_FILES=$(find "$PROJECT_ROOT" -name "*.kit" -type f | grep -v node_modules | head -5)

if [ -z "$KIT_FILES" ]; then
    echo "No .kit files found in project"
    echo "Please specify the path to your .kit file:"
    read -p "Kit file path: " KIT_FILE
    if [ ! -f "$KIT_FILE" ]; then
        echo "Error: File not found: $KIT_FILE"
        exit 1
    fi
    KIT_FILES="$KIT_FILE"
fi

echo "Found .kit file(s):"
echo "$KIT_FILES" | nl
echo ""

if [ $(echo "$KIT_FILES" | wc -l) -gt 1 ]; then
    echo "Multiple .kit files found. Please select one:"
    read -p "Enter number: " SELECTION
    KIT_FILE=$(echo "$KIT_FILES" | sed -n "${SELECTION}p")
else
    KIT_FILE=$(echo "$KIT_FILES" | head -1)
fi

echo "Using: $KIT_FILE"
echo ""

# Backup original file
BACKUP_FILE="${KIT_FILE}.backup.$(date +%Y%m%d_%H%M%S)"
cp "$KIT_FILE" "$BACKUP_FILE"
echo "Backup created: $BACKUP_FILE"
echo ""

# Check if PhysX extension is already added
if grep -q '"omni.physx.bundle"' "$KIT_FILE"; then
    echo "✓ PhysX extension already configured"
else
    echo "Adding PhysX extension..."
    
    # Find [dependencies] section
    if grep -q "^\[dependencies\]" "$KIT_FILE"; then
        # Add after [dependencies] line
        sed -i.bak '/^\[dependencies\]/a\
"omni.physx.bundle" = {}
' "$KIT_FILE"
        rm -f "${KIT_FILE}.bak"
        echo "✓ PhysX extension added"
    else
        echo "Warning: [dependencies] section not found"
        echo "Please manually add: \"omni.physx.bundle\" = {}"
    fi
fi

# Check and update Fabric Scene Delegate setting
if grep -q "useFabricSceneDelegate" "$KIT_FILE"; then
    # Check current value
    CURRENT_VALUE=$(grep "useFabricSceneDelegate" "$KIT_FILE" | head -1 | sed 's/.*= *//' | tr -d ' ')
    
    if [ "$CURRENT_VALUE" = "true" ]; then
        echo "Updating useFabricSceneDelegate from true to false..."
        sed -i.bak 's/useFabricSceneDelegate = true/useFabricSceneDelegate = false/g' "$KIT_FILE"
        rm -f "${KIT_FILE}.bak"
        echo "✓ Fabric Scene Delegate disabled"
    else
        echo "✓ Fabric Scene Delegate already disabled"
    fi
else
    echo "Adding useFabricSceneDelegate setting..."
    
    # Try to find [settings.app.usdrt] section
    if grep -q "^\[settings.app.usdrt\]" "$KIT_FILE"; then
        sed -i.bak '/^\[settings.app.usdrt\]/a\
useFabricSceneDelegate = false
' "$KIT_FILE"
        rm -f "${KIT_FILE}.bak"
    else
        # Add new section
        echo "" >> "$KIT_FILE"
        echo "[settings.app.usdrt]" >> "$KIT_FILE"
        echo "useFabricSceneDelegate = false" >> "$KIT_FILE"
    fi
    echo "✓ Fabric Scene Delegate setting added"
fi

echo ""
echo "=========================================="
echo "Setup Complete!"
echo "=========================================="
echo ""
echo "Changes made to: $KIT_FILE"
echo ""
echo "Next steps:"
echo "1. Review the changes in the .kit file"
echo "2. Build and launch your application"
echo "3. Follow the Physics Simulation Guide to set up your scene"
echo ""
echo "Backup file: $BACKUP_FILE"
echo ""
