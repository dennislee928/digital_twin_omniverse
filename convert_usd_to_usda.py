#!/usr/bin/env python3
"""
USD to USDA Converter Script

This script converts binary USD files (.usd) to ASCII USDA format (.usda)
for easier inspection and learning purposes.

Usage:
    python convert_usd_to_usda.py <input.usd> [output.usda]
    
If output filename is not provided, it will use the input filename with .usda extension.
"""

import sys
import os

try:
    from pxr import Usd, UsdUtils
except ImportError:
    print("錯誤: 無法匯入 USD Python API (pxr)")
    print("請確保已安裝 NVIDIA Omniverse 或 USD 工具")
    print("Error: Cannot import USD Python API (pxr)")
    print("Please ensure NVIDIA Omniverse or USD tools are installed")
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
