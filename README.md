# QA Testing Lab

A comprehensive Quality Assurance automation project that demonstrates real-world testing practices using Python.
This repository includes multiple test levels and test design techniques applied to web scraping and data validation projects.

---

## Project Overview

This project simulates a real QA automation environment and includes:

* Web scraping projects (Scrapy, Selenium, Playwright, BeautifulSoup)
* Unit tests for isolated components
* Integration tests for full workflows
* Smoke and sanity tests for system validation
* Regression tests for stability checks
* Test design techniques (Boundary Value, Equivalence Partitioning, Negative/Positive testing)

---

## Project Structure

```
QA_project/
│
├── kaldata_spider/              # Scrapy project
├── telegraph_beautifulsoup/     # BeautifulSoup scraper
├── inegi_playwright/            # Playwright automation
│
└── tests/
    ├── unit/
    ├── integration/
    ├── smoke/
    ├── sanity/
    ├── regression/
    ├── positive/
    ├── negative/
    ├── boundary_value/
    └── equivalence_partitioning/
```

---

## Test Types

### Unit Tests

Isolated testing of functions and parsers.

### Integration Tests

End-to-end validation of scraping workflows.

### Smoke Tests

Basic checks to ensure systems are running.

### Sanity Tests

Quick validation of core functionality.

### Regression Tests

Ensure existing functionality is not broken after updates.

### Test Design Techniques

* Boundary Value Analysis
* Equivalence Partitioning
* Positive / Negative Testing

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Running Tests

Run all tests:

```bash
pytest
```

Run specific category:

```bash
pytest tests/unit/
pytest tests/integration/
```

---

## Example Test Coverage

* Scrapy spider extraction validation
* Selenium UI navigation checks
* Playwright data extraction
* API and HTML parsing validation

---

## Technologies Used

* Python 3.12
* Pytest
* Scrapy
* Selenium
* Playwright
* BeautifulSoup
* Requests

---

## Purpose

This project was created to demonstrate:

* QA Engineering skills
* Test automation design
* Web scraping validation strategies
* Real-world testing architecture

---

