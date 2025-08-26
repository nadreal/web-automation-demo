# QA Automation Demo

This project demonstrates **UI and API test automation** using **Playwright + pytest**.

### Features
- UI tests for [SauceDemo](https://www.saucedemo.com)
- API tests for [Reqres](https://reqres.in)
- Fixtures for browser management
- Reporting with `pytest-html` / Allure
- GitHub Actions CI pipeline

### How to Run
```bash
pip install -r requirements.txt
pytest --html=reports/report.html --self-contained-html