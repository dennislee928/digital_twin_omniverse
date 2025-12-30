#!/bin/bash
# 掃描 templates/extensions 目錄的 Python 程式碼安全
# Scan Python code security in templates/extensions directory

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXTENSIONS_DIR="${SCRIPT_DIR}/templates/extensions"

echo "=========================================="
echo "Python Extension Security Scanner"
echo "=========================================="
echo ""
echo "掃描目錄: ${EXTENSIONS_DIR}"
echo "Scanning directory: ${EXTENSIONS_DIR}"
echo ""

# 檢查 bandit 是否已安裝
if ! command -v bandit &> /dev/null; then
    echo "⚠️  Bandit 未安裝，正在安裝..."
    echo "⚠️  Bandit not installed, installing..."
    pip install bandit
fi

# 建立輸出目錄
OUTPUT_DIR="${SCRIPT_DIR}/security-reports"
mkdir -p "${OUTPUT_DIR}"

echo "開始掃描..."
echo "Starting scan..."
echo ""

# 執行 bandit 掃描
bandit -r "${EXTENSIONS_DIR}" \
    -f json \
    -o "${OUTPUT_DIR}/bandit-report.json" \
    -f txt \
    -o "${OUTPUT_DIR}/bandit-report.txt" \
    || true

echo ""
echo "=========================================="
echo "掃描完成！"
echo "Scan complete!"
echo "=========================================="
echo ""
echo "報告位置 / Report location:"
echo "  JSON: ${OUTPUT_DIR}/bandit-report.json"
echo "  TXT:  ${OUTPUT_DIR}/bandit-report.txt"
echo ""
echo "查看報告 / View reports:"
echo "  cat ${OUTPUT_DIR}/bandit-report.txt"
echo ""
