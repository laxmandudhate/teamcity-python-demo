# TeamCity Python Demo - Beginner's Guide to CI/CD

## Project Overview

This project is a **complete beginner-friendly Python demonstration** designed to teach the fundamentals of **Continuous Integration (CI)** using **TeamCity**. 

The project includes:
- A simple calculator application with basic arithmetic operations
- Comprehensive unit tests using pytest
- Full automation-ready setup for TeamCity CI/CD pipeline
- Clean, well-commented code for learning purposes

### What You'll Learn

- How to structure a Python project
- Writing unit tests with pytest
- Automating code testing with CI/CD
- Using TeamCity to build, test, and validate code automatically

---

## Folder Structure

```
teamcity-python-demo/
│
├── app.py                    # Main application file - entry point
├── calculator.py             # Calculator module with arithmetic functions
├── test_calculator.py        # Unit tests for calculator module
├── requirements.txt          # Project dependencies
├── .gitignore               # Git ignore file
└── README.md                # This file
```

### File Descriptions

| File | Purpose |
|------|----------|
| `app.py` | Main application that demonstrates all calculator functions |
| `calculator.py` | Core calculator module with add, subtract, multiply, divide functions |
| `test_calculator.py` | Pytest unit tests for all calculator functions |
| `requirements.txt` | Lists all Python dependencies (pytest) |
| `.gitignore` | Specifies which files/folders to ignore in Git |

---

## Prerequisites

Before you start, ensure you have the following installed on your system:

- **Python 3.7 or higher** - [Download here](https://www.python.org/downloads/)
- **Git** - [Download here](https://git-scm.com/)
- **pip** - Usually comes with Python (package installer)

### Check Your Installation

```bash
# Check Python version
python --version

# Check pip version
pip --version

# Check Git version
git --version
```

---

## Step 1: Install Python

### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **IMPORTANT**: Check the box "Add Python to PATH"
4. Click "Install Now"
5. Verify installation: `python --version`

### macOS
```bash
# Using Homebrew (recommended)
brew install python3

# Verify
python3 --version
```

### Linux (Ubuntu/Debian)
```bash
# Update package manager
sudo apt update

# Install Python
sudo apt install python3 python3-pip

# Verify
python3 --version
```

---

## Step 2: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/laxmandudhate/teamcity-python-demo.git

# Navigate to the project directory
cd teamcity-python-demo
```

---

## Step 3: Create Virtual Environment

A virtual environment isolates your project dependencies from system Python. This is **best practice**.

### Windows
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# You should see (venv) in your terminal
```

### Linux/macOS
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# You should see (venv) in your terminal
```

---

## Step 4: Install Dependencies

Once your virtual environment is activated:

```bash
# Install all dependencies from requirements.txt
pip install -r requirements.txt

# Verify installation
pip list
```

This installs:
- **pytest** - Testing framework for writing and running unit tests

---

## Step 5: Run the Application

```bash
# Run the main application
python app.py
```

**Expected Output:**
```
==================================================
Welcome to the TeamCity Python Demo Calculator!
==================================================

Using sample values: num1 = 20, num2 = 5

--- Addition Operation ---
add(20, 5) = 25

--- Subtraction Operation ---
subtract(20, 5) = 15

--- Multiplication Operation ---
multiply(20, 5) = 100

--- Division Operation ---
divide(20, 5) = 4.0

==================================================
Summary of Results:
==================================================
Addition:       20 + 5 = 25
Subtraction:    20 - 5 = 15
Multiplication: 20 × 5 = 100
Division:       20 ÷ 5 = 4.0
==================================================
```

---

## Step 6: Run Tests

```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run tests with coverage report
pytest -v --tb=short
```

**Expected Output:**
```
test_calculator.py::TestAddition::test_add_positive_numbers PASSED
test_calculator.py::TestAddition::test_add_negative_numbers PASSED
test_calculator.py::TestAddition::test_add_mixed_numbers PASSED
test_calculator.py::TestAddition::test_add_with_zero PASSED
test_calculator.py::TestAddition::test_add_floats PASSED
test_calculator.py::TestSubtraction::test_subtract_positive_numbers PASSED
...
[Success: All tests should PASS]
```

---

## Step 7: Git Workflow

### Initial Setup (First Time Only)

```bash
# Initialize git repository
git init

# Add all files to staging area
git add .

# Commit the initial code
git commit -m "Initial Commit"

# Rename branch to 'main' (modern standard)
git branch -M main

# Add remote repository
git remote add origin https://github.com/laxmandudhate/teamcity-python-demo.git

# Push to GitHub
git push -u origin main
```

### Making Changes

```bash
# Check status of files
git status

# Add modified files
git add .

# Create a commit with a meaningful message
git commit -m "Your descriptive message here"

# Push changes to GitHub
git push origin main
```

### Creating a New Branch (for features)

```bash
# Create and switch to new branch
git checkout -b feature/new-feature

# Make your changes and commit
git add .
git commit -m "Add new feature"

# Push the new branch
git push -u origin feature/new-feature
```

---

## TeamCity CI/CD Workflow

### What is TeamCity?

**TeamCity** is a continuous integration server that automatically:
- Detects code changes
- Runs tests
- Builds your application
- Reports results

### How This Project Works with TeamCity

#### **Step 1: Repository Clone**
When you push code to GitHub, TeamCity automatically detects the change and:
```bash
git clone https://github.com/laxmandudhate/teamcity-python-demo.git
```

#### **Step 2: Install Dependencies**
TeamCity installs all required packages:
```bash
pip install -r requirements.txt
```

#### **Step 3: Run Tests**
TeamCity runs pytest to validate code:
```bash
pytest
```

#### **Step 4: Build Status Report**
- ✅ **SUCCESS**: All tests pass → Build succeeds
- ❌ **FAILED**: Any test fails → Build fails

### TeamCity Build Configuration Example

In TeamCity, you would configure a build step like this:

```yaml
Build Step 1: Install Dependencies
Command: pip install -r requirements.txt

Build Step 2: Run Tests
Command: pytest -v

Build Step 3: (Optional) Code Coverage
Command: pytest --cov
```

### Why This is Important

| Benefit | Description |
|---------|-------------|
| **Automation** | Tests run automatically - no manual testing needed |
| **Early Bug Detection** | Bugs caught immediately when code is pushed |
| **Continuous Quality** | Ensures code quality is maintained |
| **Documentation** | Build history shows what changed and when |
| **Team Confidence** | Team knows code is tested before deployment |

---

## Troubleshooting Guide

### Issue: "python: command not found"
**Solution:** Python is not installed or not in PATH
```bash
# Check if Python is installed
python --version

# If not, install Python first (see Prerequisites section)
```

### Issue: Virtual environment not activating
**Windows:** Use `venv\Scripts\activate` (with backslashes)
**Linux/Mac:** Use `source venv/bin/activate` (with forward slashes)

### Issue: "ModuleNotFoundError: No module named 'pytest'"
**Solution:** Activate virtual environment and install dependencies
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue: Git says "fatal: not a git repository"
**Solution:** Initialize git first
```bash
git init
git remote add origin https://github.com/laxmandudhate/teamcity-python-demo.git
```

### Issue: Tests fail locally but should pass
**Solution:** Check Python version compatibility
```bash
python --version  # Should be 3.7 or higher
pytest --version  # Should be latest version
```

---

## Code Quality Standards

This project follows these standards:

- ✅ **PEP 8 Compliance** - Python style guide
- ✅ **Descriptive Comments** - Explain what and why
- ✅ **Docstrings** - Document functions and modules
- ✅ **Type Hints** - Make code intentions clear
- ✅ **Error Handling** - Proper exception handling
- ✅ **Unit Tests** - Comprehensive test coverage

---

## Learning Resources

### Python
- [Python Official Documentation](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Real Python Tutorials](https://realpython.com/)

### Testing
- [Pytest Documentation](https://docs.pytest.org/)
- [Unit Testing Best Practices](https://wiki.python.org/moin/PythonSpeed/PythonSpeed)

### CI/CD & TeamCity
- [TeamCity Documentation](https://www.jetbrains.com/help/teamcity/)
- [Continuous Integration Explained](https://martinfowler.com/articles/continuousIntegration.html)
- [GitHub & CI/CD Integration](https://github.blog/category/ci-cd/)

### Git & Version Control
- [Git Official Guide](https://git-scm.com/doc)
- [GitHub Learning Lab](https://lab.github.com/)

---

## Next Steps

1. ✅ Clone this repository
2. ✅ Set up your virtual environment
3. ✅ Run the application locally
4. ✅ Run the tests to ensure everything works
5. ✅ Study the code comments to understand implementation
6. ✅ Integrate with TeamCity for automated testing
7. ✅ Experiment by modifying the calculator functions

---

## Contributing

Feel free to fork this project and submit pull requests with improvements!

### How to Contribute

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes
4. Ensure all tests pass: `pytest -v`
5. Commit changes: `git commit -m "Add my feature"`
6. Push to branch: `git push origin feature/my-feature`
7. Submit a Pull Request

---

## License

This project is open source and available under the MIT License.

---

## Contact & Support

- **Author**: Laxman Dudhate
- **GitHub**: [@laxmandudhate](https://github.com/laxmandudhate)
- **Repository**: [teamcity-python-demo](https://github.com/laxmandudhate/teamcity-python-demo)

---

## Summary Checklist

- [ ] Cloned repository
- [ ] Created virtual environment
- [ ] Installed dependencies
- [ ] Ran application successfully
- [ ] All tests passed
- [ ] Understood the project structure
- [ ] Ready to integrate with TeamCity

---

**Happy Learning! 🚀**

This project is designed to help beginners understand how CI/CD works in practice. Use it as a foundation for your learning journey!