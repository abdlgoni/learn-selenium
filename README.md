# Wikipedia Automation Testing

Selenium Python automation framework untuk testing Wikipedia website.

## Setup

### 1. Clone Repository

```bash
git clone https://github.com/abdlgoni/wikipedia-automation.git
cd wikipedia-automation
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run with HTML report
pytest tests/ -v --html=reports/report.html --self-contained-html

# Run specific test
pytest tests/test_homepage.py -v
```

## Project Structure

```
wikipedia_automation/
├── pages/              # Page Object Models
├── tests/              # Test cases
├── utils/              # Utilities & helpers
├── reports/            # Test reports (ignored)
├── logs/               # Log files (ignored)
├── screenshots/        # Screenshots (ignored)
├── requirements.txt    # Dependencies
├── pytest.ini          # Pytest config
└── README.md          # Documentation
```

## Notes

- Screenshots are automatically taken on test failures
- Reports are generated in `reports/` directory
- Logs are saved in `logs/` directory
