#!/bin/bash
# 創建新擴展的腳本
# Script to create a new extension

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TEMPLATES_DIR="$PROJECT_ROOT/templates/extensions"

echo "=========================================="
echo "創建新擴展 / Create New Extension"
echo "=========================================="
echo ""

# 檢查模板是否存在
if [ ! -d "$TEMPLATES_DIR/basic_python" ]; then
    echo "錯誤: 找不到擴展模板"
    echo "Error: Extension template not found"
    exit 1
fi

# 獲取擴展名稱
read -p "輸入擴展名稱 (Extension name): " EXTENSION_NAME
if [ -z "$EXTENSION_NAME" ]; then
    echo "錯誤: 擴展名稱不能為空"
    exit 1
fi

# 轉換為小寫並替換空格為下劃線
EXTENSION_NAME=$(echo "$EXTENSION_NAME" | tr '[:upper:]' '[:lower:]' | tr ' ' '_')

# 獲取 Python 模組路徑
read -p "輸入 Python 模組路徑 (Python module path, 預設: $EXTENSION_NAME): " MODULE_PATH
MODULE_PATH=${MODULE_PATH:-$EXTENSION_NAME}

# 目標目錄
TARGET_DIR="$PROJECT_ROOT/extensions/$EXTENSION_NAME"

# 檢查目錄是否已存在
if [ -d "$TARGET_DIR" ]; then
    echo "警告: 目錄已存在: $TARGET_DIR"
    read -p "是否覆蓋? (y/N): " OVERWRITE
    if [ "$OVERWRITE" != "y" ] && [ "$OVERWRITE" != "Y" ]; then
        echo "取消創建"
        exit 0
    fi
    rm -rf "$TARGET_DIR"
fi

echo ""
echo "正在創建擴展..."
echo "Creating extension..."

# 複製模板
cp -r "$TEMPLATES_DIR/basic_python/template" "$TARGET_DIR"

# 替換模板變數
find "$TARGET_DIR" -type f -name "*.py" -o -name "*.toml" -o -name "*.md" | while read file; do
    if [ -f "$file" ]; then
        # 替換 {{extension_name}}
        sed -i.bak "s/{{extension_name}}/$EXTENSION_NAME/g" "$file"
        # 替換 {{python_module_path}}
        sed -i.bak "s/{{python_module_path}}/$MODULE_PATH/g" "$file"
        # 替換 {{ExtensionName}} (首字母大寫)
        EXTENSION_NAME_CAPITALIZED=$(echo "$EXTENSION_NAME" | sed 's/_\([a-z]\)/\U\1/g' | sed 's/^\([a-z]\)/\U\1/')
        sed -i.bak "s/{{ExtensionName}}/$EXTENSION_NAME_CAPITALIZED/g" "$file"
        # 刪除備份文件
        rm -f "$file.bak"
    fi
done

# 重命名目錄
if [ -d "$TARGET_DIR/{{python_module_path}}" ]; then
    mv "$TARGET_DIR/{{python_module_path}}" "$TARGET_DIR/$MODULE_PATH"
fi

echo ""
echo "=========================================="
echo "擴展創建完成！"
echo "Extension created successfully!"
echo "=========================================="
echo ""
echo "擴展位置 / Extension location:"
echo "  $TARGET_DIR"
echo ""
echo "下一步 / Next steps:"
echo "  1. 編輯擴展代碼: $TARGET_DIR/$MODULE_PATH/extension.py"
echo "     Edit extension code: $TARGET_DIR/$MODULE_PATH/extension.py"
echo ""
echo "  2. 配置擴展: $TARGET_DIR/config/extension.toml"
echo "     Configure extension: $TARGET_DIR/config/extension.toml"
echo ""
echo "  3. 在 .kit 文件中添加擴展依賴"
echo "     Add extension dependency in .kit file"
echo "     \"$EXTENSION_NAME\" = {}"
echo ""
