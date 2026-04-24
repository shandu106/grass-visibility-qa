# Grass Visibility QA Project

## 📌 Overview
This project simulates a simple game visibility system written in Python.  
It is designed as a QA automation practice project to demonstrate test design, execution, and basic bug reporting.

The core idea is to test how a player's visibility changes based on:
- Grass density
- Player movement speed
- Crouching state
- Time of day

---

## 🎮 Core Logic

The system determines player visibility using predefined rules inside `logic.py`.

Possible outputs:
- VISIBLE
- SEMI_VISIBLE
- HIDDEN

---

## 🧪 Test Coverage

This project includes two types of test suites:

### ✔ Positive Tests (`tests_positive.py`)
These tests validate that the system behaves as expected under normal conditions.

### ❌ Negative Tests (`tests_negative.py`)
These tests check edge cases and ensure the system does NOT produce incorrect or unintended behavior.

---

## 🐞 Bug Reporting

A simple built-in bug reporting mechanism is included.

If a test case fails, the system automatically prints a structured bug report containing:
- Test name
- Expected result
- Actual result
- Severity level

---

## ▶️ How to Run

Run tests using Python:

```bash
python tests_positive.py
python tests_negative.py
