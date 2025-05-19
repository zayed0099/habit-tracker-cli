HabitTrack CLI
A simple command-line habit tracker that helps you build and maintain streaks for your daily habits.
Features

📝 Add new habits to track
✅ Mark habits as completed or missed
📊 View your progress and streaks
🗑️ Delete habits you no longer want to track
📆 Track habit completion with visual streak indicators

Installation

Clone this repository:
git clone https://github.com/yourusername/habit-track-cli.git
cd habit-track-cli

No additional dependencies required! HabitTrack uses only Python standard libraries.

Usage
Run the application:
python habit_tracker.py
Commands
The app provides a simple menu-driven interface:
What would you like to do?
--------------------------------------------
| [1] Add Habit         | [4] Check Menu   |  
| [2] Edit Habit status | [5] Delete Habit |
| [3] Show Progress     | [6] Exit         |
--------------------------------------------

Add Habit (1): Create a new habit to track
Edit Habit status (2): Mark a habit as completed (✅) or missed (❌) for today
Show Progress (3): View detailed information about a specific habit including streak
Check Menu (4): Display the menu again
Delete Habit (5): Remove a habit from tracking
Exit (6): Close the application

Data Storage
Your habits are stored locally in a JSON file (data.json) in the same directory as the script.
Example
--------------------------------------------
-> 1
Enter the name of the habit : Morning Meditation
New habit has been added!
--------------------------------------------
-> 3
* Morning Meditation
What habit would you like to learn more about? => Morning Meditation
--------------------------------------------
Habit Name :  Morning Meditation
Start Date :  2025-05-19
Streak     :  ✔
Last Updated 2025-05-19
Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.