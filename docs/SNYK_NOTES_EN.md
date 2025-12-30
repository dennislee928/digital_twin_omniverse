# Snyk Configuration Notes

## Why Snyk Shows Errors

This project is an **OpenUSD/Omniverse digital twin project** that does not contain standard package manager files that Snyk can scan:

- No `package.json` (Node.js/npm)
- No `requirements.txt` or `Pipfile` (Python)
- No `go.mod` (Go)
- No `pom.xml` or `build.gradle` (Java/Maven)
- No `Cargo.toml` (Rust)

## Project Structure

This project uses:
- **USD files** (`.usd`, `.usda`) - OpenUSD scene description files
- **Omniverse Kit templates** - Application templates for Omniverse
- **Packman** - Omniverse's dependency management system (see `tools/packman/`)

## Dependency Management

Dependencies for this project are managed through:
- Omniverse's **packman** system (see `repo.toml`, `repo_tools.toml`)
- Template dependencies defined in `templates/templates.toml`

## Security Scanning

### Omniverse-Specific Scanning Tools

For security scanning of this project, use the following Omniverse-specific tools and methods:

#### 1. NVIDIA Omniverse Built-in Security Features

- **Omniverse Launcher Security Checks**
  - Launch Omniverse Launcher
  - Check installed package versions and updates
  - Verify package signatures and integrity

- **USD File Validation**
  - Use USD tools to verify file integrity
  - Check external references and paths in USD files
  - Validate material and texture file security

#### 2. Packman Dependency Management Scanning

```bash
# Check packman dependencies
./repo.sh status

# Verify dependency integrity
./repo.sh verify

# Update dependencies and check for security updates
./repo.sh update
```

#### 3. Python Extension Security Scanning

**Important Note: `templates/extensions/` Directory Contains Template Files**

The `templates/extensions/` directory contains **template files** (using template variables like `{{extension_name}}`), not actual Python projects. These templates:
- Use Omniverse Kit API (`omni.ext`, `omni.kit`, etc.)
- Dependencies are managed through the **packman** system, not `requirements.txt`
- Primarily use standard library and Omniverse-provided modules

**Why Snyk Cannot Scan:**
- These are template files, not actual projects
- No `requirements.txt` or dependency definitions in `setup.py`
- Dependencies are managed by Omniverse's packman system

**Correct Scanning Methods:**

##### A. Use Bandit for Code Security Scanning (Recommended)

Bandit doesn't require requirements.txt and can directly scan Python code:

**Quick Scan (Using Provided Script):**

```bash
# Run from project root directory
./scan_extensions.sh
```

**Manual Scan:**

```bash
# Navigate to extensions directory
cd templates/extensions

# Install bandit
pip install bandit

# Scan all Python files
bandit -r . -f json -o bandit-report.json

# Or use HTML format report
bandit -r . -f html -o bandit-report.html

# Scan specific extension template only
bandit -r basic_python/template/ -f json -o basic_python-report.json
```

##### B. Scan Actual Generated Extension Projects

When you use these templates to generate actual extension projects, scan in the **generated project directory**:

```bash
# Assuming your generated extension is in my_extension/ directory
cd my_extension

# If requirements.txt exists, use pip-audit
pip install pip-audit
pip-audit -r requirements.txt

# Or use safety
pip install safety
safety check

# Use bandit to scan code
bandit -r . -f json -o bandit-report.json
```

##### C. Check Omniverse Dependency Updates

```bash
# Check packman dependencies in project root
cd /Users/lipeichen/Documents/Untitled/digital_twin_omniverse
./repo.sh status
./repo.sh verify
./repo.sh update
```

#### 4. USD File Content Review

Manually review USD file contents:

```bash
# Convert to readable format
python convert_usd_to_usda.py Factory_Lite/Factory_Lite.usd

# Check USDA files for:
# - External file reference paths
# - Material and texture file sources
# - Script and code embeddings
# - Network resource references
```

#### 5. NVIDIA Security Resources

- **NVIDIA Product Security Portal**: https://www.nvidia.com/en-us/security
- **Report Security Vulnerabilities**: https://www.nvidia.com/object/submit-security-vulnerability.html
- **Omniverse Documentation**: https://docs.omniverse.nvidia.com/
- **Omniverse Community Forum**: https://forums.developer.nvidia.com/c/omniverse/

#### 6. General Security Best Practices

1. **Regularly Update Omniverse and Dependencies**
   ```bash
   ./repo.sh update
   ```

2. **Check External References in USD Files**
   - Ensure all referenced file paths are secure
   - Avoid referencing untrusted external resources

3. **Review Python Extension Code**
   - Check for unsafe function calls
   - Verify input validation and error handling
   - Check file system and network access permissions

4. **Use Version Control**
   - Track all changes
   - Regularly review committed code
   - Use branch protection and code review processes

## Snyk Configuration

A `.snyk` file has been created to exclude this project from Snyk scanning, as it's not a standard software project with package manager dependencies.

**Note:** Files in the `templates/extensions/` directory are templates and don't contain `requirements.txt`, so Snyk cannot scan them. This is **expected behavior**.

### Alternatives

For the `templates/extensions/` directory, please use:

1. **Bandit** - Code security scanning (doesn't require requirements.txt)
2. **Packman** - Check Omniverse dependency updates
3. **Manual Review** - Check security best practices in template files

See the "Python Extension Security Scanning" section above for details.
