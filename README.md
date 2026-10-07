# 🎯 Interactive Terminal-Based Habit Tracker

A minimal, light-weight Command Line Interface (CLI) application built using Python to track daily habits and calculate user consistency streaks without reliance on heavy graphical interfaces or external databases.

## 🛠️ Technical Highlights
- **Flat-File Architecture:** Implements local state persistence using unstructured file operations to read/write custom JSON objects (`habits.json`) natively.
- **Dynamic Streak Calculation:** Implements a time-delta evaluation algorithm analyzing string dates to increment, preserve, or break user progress counters accurately.
- **Zero Dependencies:** Employs standard library frameworks (`json`, `os`, `datetime`), ensuring extreme portability and immediate local deployment execution capabilities.

## 🚀 Execution Instructions
Ensure you have Python 3 installed on your environment. Clone this project repository and run the program file directly from your terminal:

```bash
# Clone the repository
git clone <your-repository-url>

# Enter the project directory
cd habit-tracker-cli

# Run the software utility script
python tracker.py
```

## 📊 JSON Database Schema Pattern Example
The persistence layers represent state management utilizing the following structured schema design:
```json
{
  "leetcode_problems": {
    "name": "LeetCode Problems",
    "last_completed": "2026-10-07",
    "streak": 5
  }
}
```
