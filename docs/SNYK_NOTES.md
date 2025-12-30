# Snyk Configuration Notes

## Why Snyk Shows Errors

This project is an **OpenUSD/Omniverse digital twin project** that does not contain standard package manager files that Snyk can scan:

-   No `package.json` (Node.js/npm)
-   No `requirements.txt` or `Pipfile` (Python)
-   No `go.mod` (Go)
-   No `pom.xml` or `build.gradle` (Java/Maven)
-   No `Cargo.toml` (Rust)

## Project Structure

This project uses:

-   **USD files** (`.usd`, `.usda`) - OpenUSD scene description files
-   **Omniverse Kit templates** - Application templates for Omniverse
-   **Packman** - Omniverse's dependency management system (see `tools/packman/`)

## Dependency Management

Dependencies for this project are managed through:

-   Omniverse's **packman** system (see `repo.toml`, `repo_tools.toml`)
-   Template dependencies defined in `templates/templates.toml`

## Security Scanning

### Omniverse 專用掃描工具

對於此專案的安全掃描，建議使用以下 Omniverse 專用工具和方法：

#### 1. NVIDIA Omniverse 內建安全功能

-   **Omniverse Launcher 安全檢查**

    -   啟動 Omniverse Launcher
    -   檢查已安裝套件的版本和更新
    -   檢視套件簽章和完整性驗證

-   **USD 檔案驗證**
    -   使用 USD 工具驗證檔案完整性
    -   檢查 USD 檔案中的外部引用和路徑
    -   驗證材質和紋理檔案的安全性

#### 2. Packman 依賴管理掃描

```bash
# 檢查 packman 依賴
./repo.sh status

# 驗證依賴完整性
./repo.sh verify

# 更新依賴並檢查安全更新
./repo.sh update
```

#### 3. Python 擴展安全掃描

**重要說明：`templates/extensions/` 目錄包含模板檔案**

`templates/extensions/` 目錄包含的是**模板檔案**（使用 `{{extension_name}}` 等模板變數），不是實際的 Python 專案。這些模板：

-   使用 Omniverse Kit API（`omni.ext`, `omni.kit` 等）
-   依賴通過 **packman** 系統管理，不使用 `requirements.txt`
-   主要使用標準庫和 Omniverse 提供的模組

**為什麼 Snyk 無法掃描：**

-   這些是模板檔案，不是實際專案
-   沒有 `requirements.txt` 或 `setup.py` 中的依賴定義
-   依賴由 Omniverse 的 packman 系統管理

**正確的掃描方法：**

##### A. 使用 Bandit 進行程式碼安全掃描（推薦）

Bandit 不依賴 requirements.txt，可以直接掃描 Python 程式碼：

**快速掃描（使用提供的腳本）：**

```bash
# 在專案根目錄執行
./scan_extensions.sh
```

**手動掃描：**

```bash
# 進入擴展目錄
cd templates/extensions

# 安裝 bandit
pip install bandit

# 掃描所有 Python 檔案
bandit -r . -f json -o bandit-report.json

# 或使用 HTML 格式報告
bandit -r . -f html -o bandit-report.html

# 只掃描特定擴展模板
bandit -r basic_python/template/ -f json -o basic_python-report.json
```

##### B. 掃描實際生成的擴展專案

當您使用這些模板生成實際的擴展專案後，在**生成的專案目錄**中進行掃描：

```bash
# 假設您生成的擴展在 my_extension/ 目錄
cd my_extension

# 如果有 requirements.txt，可以使用 pip-audit
pip install pip-audit
pip-audit -r requirements.txt

# 或使用 safety
pip install safety
safety check

# 使用 bandit 掃描程式碼
bandit -r . -f json -o bandit-report.json
```

##### C. 檢查 Omniverse 依賴更新

```bash
# 在專案根目錄檢查 packman 依賴
cd /Users/lipeichen/Documents/Untitled/digital_twin_omniverse
./repo.sh status
./repo.sh verify
./repo.sh update
```

#### 4. USD 檔案內容審查

手動檢查 USD 檔案內容：

```bash
# 轉換為可讀格式
python convert_usd_to_usda.py Factory_Lite/Factory_Lite.usd

# 檢查 USDA 檔案中的：
# - 外部檔案引用路徑
# - 材質和紋理檔案來源
# - 腳本和程式碼嵌入
# - 網路資源引用
```

#### 5. NVIDIA 安全資源

-   **NVIDIA Product Security Portal**: https://www.nvidia.com/en-us/security
-   **報告安全漏洞**: https://www.nvidia.com/object/submit-security-vulnerability.html
-   **Omniverse 文件**: https://docs.omniverse.nvidia.com/
-   **Omniverse 社群論壇**: https://forums.developer.nvidia.com/c/omniverse/

#### 6. 一般安全最佳實踐

1. **定期更新 Omniverse 和依賴**

    ```bash
    ./repo.sh update
    ```

2. **檢查 USD 檔案中的外部引用**

    - 確保所有引用的檔案路徑安全
    - 避免引用不受信任的外部資源

3. **審查 Python 擴展程式碼**

    - 檢查是否有不安全的函數呼叫
    - 驗證輸入驗證和錯誤處理
    - 檢查檔案系統和網路存取權限

4. **使用版本控制**
    - 追蹤所有變更
    - 定期審查提交的程式碼
    - 使用分支保護和程式碼審查流程

## Snyk Configuration

A `.snyk` file has been created to exclude this project from Snyk scanning, as it's not a standard software project with package manager dependencies.

**注意：** `templates/extensions/` 目錄中的檔案是模板，不包含 `requirements.txt`，因此 Snyk 無法掃描。這是**預期的行為**。

### 替代方案

對於 `templates/extensions/` 目錄，請使用：

1. **Bandit** - 程式碼安全掃描（不依賴 requirements.txt）
2. **Packman** - 檢查 Omniverse 依賴更新
3. **手動審查** - 檢查模板檔案中的安全最佳實踐

詳見上方「Python 擴展安全掃描」章節。
