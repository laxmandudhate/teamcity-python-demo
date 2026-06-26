# TeamCity Python Demo

A sample Python application with Flask API and calculator module for TeamCity CI/CD pipeline demonstration.

## Features

- **Flask REST API** - Simple web service with calculator endpoints
- **Calculator Module** - Basic mathematical operations (add, subtract, multiply, divide)
- **Unit Tests** - Comprehensive test coverage using pytest
- **Docker Support** - Containerized application ready for deployment
- **TeamCity Integration** - Ready for CI/CD pipeline configuration

## Project Structure

```
teamcity-python-demo/
├── app.py              # Flask application
├── calculator.py       # Calculator module
├── test_calculator.py  # Unit tests
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Docker (optional, for containerized deployment)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/laxmandudhate/teamcity-python-demo.git
cd teamcity-python-demo
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Local Development

```bash
python app.py
```

The API will be available at `http://localhost:5000`

### Docker

```bash
docker build -t teamcity-python-demo .
docker run -p 5000:5000 teamcity-python-demo
```

## API Endpoints

### Health Check
- **GET** `/` - Returns API status

### Calculator Operations
- **POST** `/api/calculate` - Perform calculation
  ```json
  {
    "operation": "add",
    "a": 10,
    "b": 5
  }
  ```

- **GET** `/api/add/<a>/<b>` - Add two numbers
- **GET** `/api/subtract/<a>/<b>` - Subtract two numbers
- **GET** `/api/multiply/<a>/<b>` - Multiply two numbers
- **GET** `/api/divide/<a>/<b>` - Divide two numbers

## Running Tests

```bash
# Run all tests
python -m pytest

# Run with coverage report
python -m pytest --cov=.

# Run specific test file
python -m pytest test_calculator.py -v
```

## TeamCity Integration

This project is configured for TeamCity CI/CD. Add the following build configuration:

1. **Build Step 1: Install Dependencies**
   ```
   Command: pip install -r requirements.txt
   ```

2. **Build Step 2: Run Tests**
   ```
   Command: pytest --cov=. --cov-report=xml
   ```

3. **Build Step 3: Build Docker Image** (Optional)
   ```
   Command: docker build -t teamcity-python-demo .
   ```

## License

MIT License

## Author

Laxman Dudhate
