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
import platform

def check_environment():
    """檢查是否在 Omniverse 環境中"""
    omniverse_indicators = [
        os.environ.get("OMNIVERSE_PATH"),
        os.environ.get("KIT_PATH"),
        os.environ.get("OMNIVERSE_APP_PATH"),
    ]
    return any(indicators for indicators in omniverse_indicators if indicators)

def print_helpful_message():
    """顯示有用的錯誤訊息和解決方案"""
    print("=" * 70)
    print("錯誤: 無法匯入 USD Python API (pxr)")
    print("Error: Cannot import USD Python API (pxr)")
    print("=" * 70)
    print()
    
    # 檢查環境
    in_omniverse = check_environment()
    if in_omniverse:
        print("⚠️  檢測到 Omniverse 環境變數，但無法匯入 pxr 模組")
        print("⚠️  Omniverse environment detected, but cannot import pxr module")
        print()
        print("可能的原因 / Possible reasons:")
        print("  1. 需要在 Omniverse Kit 應用程式的 Python 環境中運行")
        print("     Need to run in Omniverse Kit application's Python environment")
        print("  2. USD 擴展未正確安裝")
        print("     USD extension not properly installed")
        print()
    else:
        print("此腳本需要 USD Python API，可在以下環境中使用：")
        print("This script requires USD Python API, available in:")
        print()
        print("方法 1: 在 Omniverse Kit 應用程式中運行")
        print("Method 1: Run in Omniverse Kit application")
        print("  - 啟動您的 USD Explorer 應用程式")
        print("    Launch your USD Explorer application")
        print("  - 使用應用程式內建的 Python 控制台")
        print("    Use the built-in Python console in the application")
        print("  - 或使用 Kit 的命令列工具")
        print("    Or use Kit's command-line tools")
        print()
        print("方法 2: 安裝 USD Python 綁定")
        print("Method 2: Install USD Python bindings")
        print("  - 從 https://github.com/PixarAnimationStudios/USD 編譯安裝")
        print("    Build and install from https://github.com/PixarAnimationStudios/USD")
        print("  - 或使用預編譯的 USD 發行版")
        print("    Or use pre-compiled USD releases")
        print()
    
    print("✅ 推薦方案 / Recommended Solution:")
    print("  使用 USD Explorer 應用程式轉換檔案（最簡單的方法）")
    print("  Use USD Explorer application to convert files (easiest method)")
    print()
    print("  步驟 / Steps:")
    print("  1. 啟動 USD Explorer 應用程式")
    print("     Launch USD Explorer application")
    print("  2. 開啟 USD 檔案 (File > Open)")
    print("     Open USD file (File > Open)")
    print("  3. 選擇 File > Save As")
    print("     Select File > Save As")
    print("  4. 選擇 USDA (ASCII) 格式並儲存")
    print("     Choose USDA (ASCII) format and save")
    print()
    print("📖 詳細說明請參閱：VARIANT_PRESENTER_GUIDE.md")
    print("📖 For details, see: VARIANT_PRESENTER_GUIDE.md")
    print("=" * 70)

# Try to import USD Python API
try:
    from pxr import Usd
except ImportError:
    print_helpful_message()
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
