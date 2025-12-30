#!/usr/bin/env python3
"""
USD 環境檢查腳本

此腳本檢查系統是否具備運行 USD 相關工具所需的環境。

This script checks if the system has the required environment for running USD tools.
"""

import sys
import os

def check_python_version():
    """檢查 Python 版本"""
    version = sys.version_info
    print(f"Python 版本 / Python version: {version.major}.{version.minor}.{version.micro}")
    if version.major < 3 or (version.major == 3 and version.minor < 6):
        print("  ⚠️  需要 Python 3.6 或更高版本")
        print("  ⚠️  Requires Python 3.6 or higher")
        return False
    print("  ✓ Python 版本符合要求")
    print("  ✓ Python version is acceptable")
    return True

def check_usd_api():
    """檢查 USD Python API"""
    print("\n檢查 USD Python API / Checking USD Python API...")
    try:
        from pxr import Usd
        print("  ✓ USD Python API (pxr) 已安裝")
        print("  ✓ USD Python API (pxr) is installed")
        
        # 嘗試獲取版本資訊
        try:
            import pxr
            print(f"  ✓ pxr 模組路徑: {pxr.__file__}")
            print(f"  ✓ pxr module path: {pxr.__file__}")
        except:
            pass
        return True
    except ImportError:
        print("  ✗ USD Python API (pxr) 未安裝")
        print("  ✗ USD Python API (pxr) is not installed")
        return False

def check_omniverse_environment():
    """檢查 Omniverse 環境變數"""
    print("\n檢查 Omniverse 環境 / Checking Omniverse environment...")
    
    env_vars = {
        "OMNIVERSE_PATH": os.environ.get("OMNIVERSE_PATH"),
        "KIT_PATH": os.environ.get("KIT_PATH"),
        "OMNIVERSE_APP_PATH": os.environ.get("OMNIVERSE_APP_PATH"),
    }
    
    found = False
    for var_name, var_value in env_vars.items():
        if var_value:
            print(f"  ✓ {var_name} = {var_value}")
            found = True
    
    if not found:
        print("  ✗ 未檢測到 Omniverse 環境變數")
        print("  ✗ No Omniverse environment variables detected")
        print("  ℹ️  這表示可能不在 Omniverse 應用程式環境中")
        print("  ℹ️  This indicates you may not be in an Omniverse application environment")
    
    return found

def main():
    separator = "=" * 70
    
    print(separator)
    print("USD 環境檢查 / USD Environment Check")
    print(separator)
    print()
    
    results = {
        "python": check_python_version(),
        "usd_api": check_usd_api(),
        "omniverse": check_omniverse_environment(),
    }
    
    print()
    print(separator)
    print("檢查結果摘要 / Summary")
    print(separator)
    
    if results["usd_api"]:
        print()
        print("✅ 可以運行 USD 轉換腳本")
        print("✅ Can run USD conversion script")
        print()
        print("  執行方式 / Usage:")
        print("    python convert_usd_to_usda.py <input.usd> [output.usda]")
    else:
        print()
        print("❌ 無法運行 USD 轉換腳本（缺少 USD Python API）")
        print("❌ Cannot run USD conversion script (missing USD Python API)")
        print()
        print("💡 建議 / Recommendations:")
        print()
        print("  1. 使用 USD Explorer 應用程式轉換檔案（最簡單）")
        print("     Use USD Explorer application to convert files (easiest)")
        print()
        print("     步驟 / Steps:")
        print("     - 啟動 USD Explorer 應用程式")
        print("       Launch USD Explorer application")
        print("     - 開啟 USD 檔案 (File > Open)")
        print("       Open USD file (File > Open)")
        print("     - 選擇 File > Save As > USDA (ASCII) 格式")
        print("       Select File > Save As > USDA (ASCII) format")
        print()
        print("  2. 在 Omniverse Kit 應用程式的 Python 環境中運行腳本")
        print("     Run script in Omniverse Kit application's Python environment")
        print()
        print("  3. 安裝 USD Python 綁定")
        print("     Install USD Python bindings")
        print("     - 從 https://github.com/PixarAnimationStudios/USD 編譯安裝")
        print("       Build from https://github.com/PixarAnimationStudios/USD")
    
    print()
    print(separator)
    
    return 0 if results["usd_api"] else 1

if __name__ == "__main__":
    sys.exit(main())
