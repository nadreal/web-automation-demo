# QA Web Automation Demo

This project demonstrates **UI and API test automation** using **Playwright + pytest**.

### Features
- UI tests for [SauceDemo](https://www.saucedemo.com)
- API tests for [Reqres](https://reqres.in)
- Fixtures for browser management
- Reporting with `pytest-html` / Allure
- GitHub Actions CI pipeline

### CI/CD Using GitHub Actions pipeline
This project is fully automated using **GitHub Actions**.  
Whenever code is pushed to `main` or a pull request is created, the workflow runs **all UI and API tests automatically**.  

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/nadreal/web-automation-demo/python-test.yml?branch=main&style=flat-square)


The HTML test report is uploaded as an artifact for review.  
This ensures that every change is **tested before merging**, maintaining the quality of the project.

### How to Run
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -r requirements.txt
pytest --html=reports/report.html --self-contained-html #Run test and generate reports


