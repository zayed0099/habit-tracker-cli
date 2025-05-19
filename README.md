# 🧠 CLI Habit Tracker

A simple command-line interface (CLI) habit tracker built with Python. It helps you track your habits, manage streaks, and maintain consistency—all from your terminal!

---

## ✨ Features

- 📌 Add new habits  
- ✅ Mark habits as done or undone  
- 📊 View progress and streaks  
- 🗑️ Delete habits  
- 💾 Stores data locally in `data.json`  
- 🧠 Encourages consistency with visual streak tracking  

---

## 📦 Requirements

- Python 3.6+
- No external libraries needed (uses only built-in Python modules)

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/habit-tracker.git
   cd habit-tracker
   ```

2. **Run the habit tracker**
   ```bash
   python habit_tracker.py
   ```
   > Replace `habit_tracker.py` with your actual Python filename if it's different.

---

## 📂 File Structure

```
habit-tracker/
├── data.json           # Stores all habit data (auto-created)
└── habit_tracker.py    # Main CLI app script
```

---

## 🧑‍💻 How It Works

When you run the script, you’ll see a menu like this:

```
What would you like to do?
--------------------------------------------
| [1] Add Habit         | [4] Check Menu   |  
| [2] Edit Habit status | [5] Delete Habit |
| [3] Show Progress     | [6] Exit         |
--------------------------------------------
```

### [1] Add Habit
- Input a new habit name and start tracking from today.

### [2] Edit Habit Status
- Mark a habit as done ✅ or undone ❌ for the current day.
- Automatically updates the streak and last updated date.

### [3] Show Progress
- View detailed progress of a habit: start date, current streak, and last updated.

### [4] Check Menu
- Re-displays the menu at any time.

### [5] Delete Habit
- Permanently removes a habit from tracking after confirmation.

### [6] Exit
- Safely exits the tracker.

---

## 📘 Data Format (Example)

```json
[
  {
    "habit": "Exercise",
    "Start Date": "2025-05-19",
    "streak": "✔✔❌✔",
    "Last Updated": "2025-05-19"
  }
]
```

---

## 🛡️ License

This project is licensed under the MIT License. Feel free to use, modify, and share it.

---

## 💡 Future Ideas

- Add visualization with charts  
- Set habit reminders  
- Export streak history to CSV or PDF  
