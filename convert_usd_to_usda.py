#!/usr/bin/env python3
"""
USD to USDA Converter Script

This script converts binary USD files (.usd) to ASCII USDA format (.usda)
for easier inspection and learning purposes.

Usage:
    python convert_usd_to_usda.py <input.usd> [output.usda]
    
If output filename is not provided, it will use the input filename with .usda extension.

Note: This script requires the USD Python API (pxr module), which is available:
1. In NVIDIA Omniverse applications (run from within Omniverse Kit environment)
2. When USD is installed with Python bindings

Alternative: Use USD Explorer application to convert files:
  1. Open the USD file in USD Explorer
  2. Select File > Save As
  3. Choose USDA (ASCII) format
"""

import sys
import os

# Try to import USD Python API
try:
    from pxr import Usd
except ImportError:
    print("=" * 70)
    print("錯誤: 無法匯入 USD Python API (pxr)")
    print("Error: Cannot import USD Python API (pxr)")
    print("=" * 70)
    print()
    print("此腳本需要 USD Python API，可在以下環境中使用：")
    print("This script requires USD Python API, available in:")
    print()
    print("1. NVIDIA Omniverse 應用程式環境")
    print("   (在 Omniverse Kit 環境中運行此腳本)")
    print("   NVIDIA Omniverse application environment")
    print("   (Run this script from within Omniverse Kit environment)")
    print()
    print("2. 已安裝 USD Python 綁定的系統")
    print("   System with USD Python bindings installed")
    print()
    print("替代方案 / Alternative:")
    print("  使用 USD Explorer 應用程式轉換檔案：")
    print("  Use USD Explorer application to convert files:")
    print("  1. 在 USD Explorer 中開啟 USD 檔案")
    print("     Open the USD file in USD Explorer")
    print("  2. 選擇 File > Save As")
    print("     Select File > Save As")
    print("  3. 選擇 USDA (ASCII) 格式")
    print("     Choose USDA (ASCII) format")
    print()
    print("詳細說明請參閱：VARIANT_PRESENTER_GUIDE.md")
    print("For details, see: VARIANT_PRESENTER_GUIDE.md")
    print("=" * 70)
    sys.exit(1)


def convert_usd_to_usda(input_path, output_path=None):
    """
    將 USD 檔案轉換為 USDA (ASCII) 格式
    
    Args:
        input_path: 輸入的 .usd 檔案路徑
        output_path: 輸出的 .usda 檔案路徑（可選）
    """
    if not os.path.exists(input_path):
        print(f"錯誤: 找不到檔案 {input_path}")
        sys.exit(1)
    
    # 如果沒有指定輸出路徑，使用輸入檔名加上 .usda 副檔名
    if output_path is None:
        base_name = os.path.splitext(input_path)[0]
        output_path = f"{base_name}.usda"
    
    print(f"正在轉換: {input_path} -> {output_path}")
    
    try:
        # 開啟 USD 檔案
        stage = Usd.Stage.Open(input_path)
        if not stage:
            print(f"✗ 錯誤: 無法開啟 USD 檔案 {input_path}")
            sys.exit(1)
        
        # 匯出為 ASCII 格式 (.usda)
        stage.Export(output_path)
        print(f"✓ 轉換成功: {output_path}")
            
    except Exception as e:
        print(f"✗ 轉換時發生錯誤: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("\n範例:")
        print("  python convert_usd_to_usda.py Factory_Lite/Factory_Lite.usd")
        print("  python convert_usd_to_usda.py Factory_Lite/SubUSDs/Vehicle_Hanger_Adjust.usd")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    convert_usd_to_usda(input_path, output_path)


if __name__ == "__main__":
    main()
