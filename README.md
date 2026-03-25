
# 🎭 Playwright Test Automation Suite

Recently, I learned Playwright by going through the documentation in the Automation Panda GitHub repository. Using this knowledge, I built a solution for automated browser testing that supports multiple browsers, along with features like screenshots, video recording, and parallel execution.

---

## 📋 Table of Contents
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Advanced Options](#advanced-options)
- [Project Structure](#project-structure)

---

## 🚀 Installation

### Quick Setup
Install all dependencies with a single command:

```bash
pip install -r requirements.txt
```

### Manual Installation
If you prefer to install packages individually, run:

```bash
pip install pytest
pip install playwright
pip install pytest-playwright
pip install pytest-xdist
```

### Install Playwright Browsers
After installing dependencies, install all Playwright browser binaries:

```bash
playwright install
```

---

## ▶️ Running Tests

### Basic Test Execution
Run all tests in headed mode (browser window visible) with Chromium:

```bash
python -m pytest tests --headed --browser chromium --slowmo 1000
```

**Parameters:**
- `--headed` — Run tests with visible browser window
- `--browser chromium` — Specify browser (chromium, firefox, webkit)
- `--slowmo 1000` — Slow down test execution by 1000ms

---

## 📸 Advanced Options

### Screenshots
Capture screenshots during test execution:

```bash
# Capture screenshots on every action
python -m pytest tests --screenshot on

# Capture screenshots only on test failure
python -m pytest tests --screenshot only-on-failure
```

### Video Recording
Record videos of your test runs:

```bash
# Record all test executions
python -m pytest tests --video on

# Keep videos only for failed tests
python -m pytest tests --video retain-on-failure
```

### Parallel Execution
Speed up test execution using pytest-xdist with multiple workers:

```bash
python -m pytest tests -n 2
```

Use `-n` flag to specify number of parallel workers (e.g., `-n 4` for 4 workers)

### Verbose Output
Get detailed test information and execution reports:

```bash
python -m pytest tests --verbose
```

**Combine with any command above:**
```bash
python -m pytest tests --headed --browser chromium --slowmo 1000 --verbose
```

---

## 📁 Project Structure

```
.
├── pages/                          # Page Object Models
│   ├── search.py                   # Search page interactions
│   ├── result.py                   # Results page interactions
│   └── __init__.py
├── tests/                          # Test files
│   ├── test_search.py              # Search functionality tests
│   ├── conftest.py                 # Pytest configuration & fixtures
│   └── __pycache__/
├── test-results/                   # Test execution reports
├── playwright_automation/          # Virtual environment
├── requirements.txt                # Project dependencies
└── README.md                        # This file
```

---

## 💡 Quick Tips

✨ **Pro Tips:**
- Use `--slowmo` during development to observe test behavior
- Combine `--screenshot only-on-failure` with `--verbose` for debugging
- Use parallel execution (`-n`) for faster CI/CD pipelines
- Check `test-results/` directory for artifact files after test runs

---

## 📦 Dependencies

- **Playwright** — Automated browser testing library
- **Pytest** — Testing framework
- **Pytest-Playwright** — Playwright plugin for Pytest
- **Pytest-Xdist** — Parallel test execution

---

*Happy Testing! 🎉*