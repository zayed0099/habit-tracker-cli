'''A basic cli habit tracker which will keep track, show me my streak'''
import os                       # Built-in Os module for file location handling
from datetime import date       # For working with date-time
from pathlib import Path        # For working with file location. Same as os
import json                     # For working with json

# Display menu options for user interaction
menu = '''What would you like to do?
--------------------------------------------
| [1] Add Habit         | [4] Check Menu   |  
| [2] Edit Habit status | [5] Delete Habit |
| [3] Show Progress     | [6] Exit         |
--------------------------------------------
'''
# File database Location
location = os.path.join(os.path.dirname(__file__), 'data.json')

print(menu)

# Main Logical Part
while True:
    print("--------------------------------------------")
    # Taking user input
    try: 
        user_input = int(input("-> "))

    except ValueError:
        print("Please enter a valid number.") # raisng error if invalid input
        user_input = None
        
    # Adding new habit to file
    if user_input == 1:
        try:
            # Initializing The variables and getting data from user to work with
            add_habit = input("Enter the name of the habit : ")
            today = str(date.today()) # Using the datetime module to get todays date.
            streak = "✔"

            # Saving the data as a dictionary
            saved_data = {'habit' : add_habit, 'Start Date' : today, 'streak' : streak, 'Last Updated' : today}

            try:
                if Path(location).exists():
                    # Importing data
                    with open(location, 'r') as f:
                        habit_database = json.load(f)
                    
                    # Cleaning the habit Name
                    add_habit_cleaned = add_habit.lower().strip()
                    # gathering all habit Name for verification.
                    all_habit_names = [habit['habit'].lower() for habit in habit_database]

                    # Check if the habit exists. If exists add it to the db.
                    if add_habit_cleaned not in all_habit_names:
                        habit_database.append(saved_data)
                        with open(location, 'w') as f:
                            json.dump(habit_database, f, indent=4)
                        print("New habit has been added!")

                        # Show error if the habit already exists.
                    else: 
                        print("The habit already exists!")
                            
                else:
                # Else make the file and add the data in there as list of dictionary(s)
                    listed = [saved_data]
                    with open(location, 'w') as f:
                        json.dump(listed, f, indent=4)


            except Exception as e:
                print("#func1 An error occured:", e)


        except Exception as e:
            print("#UI1 An error occurred:", e)

    # Marking habit done + Working with Streaks
    elif user_input == 2:
        try:
            # Importing data
            if Path(location).exists():
                with open(location, 'r') as f:
                    habit_database = json.load(f)
            
            # Showing all available habit.
            for habits_data in habit_database:
                print("*", habits_data['habit'])

            print('''What do you want to mark? 
[1] Done ✔️ 
[2] Undone ❌
''')        
            try:
                confirm = int(input("=>"))
            except ValueError:
                print("Enter a correct Number")

            # Managing streak data 
            if confirm == 1:
                # Querying user.
                habit_name = input("Enter the name of the habit : ")
                today = str(date.today()) # Using the datetime module to get todays date.

                # Looping through list to update dictionary key
                for habit in habit_database:
                    if habit['habit'].lower() == habit_name.strip().lower():
                        if habit['Last Updated'] == today:
                            print("Already marked for today.")
                        else:
                            habit['streak'] += "✔"
                            habit['Last Updated'] = today
                            print(f"Marked as done for {today} 👍")

                            # Writing updated data to the file
                            with open(location, "w") as f:
                                json.dump(habit_database, f, indent=4)

            elif confirm == 2:
                # Querying user.
                habit_name = input("Enter the name of the habit : ")
                # Looping through list to update dictionary key
                for habit in habit_database:
                    if habit['habit'].lower() == habit_name.strip().lower():
                        if habit['Last Updated'] == today:
                            print("Already marked for today.")
                        #Check if marked today, if not add the x to the streak
                        else:
                            habit['streak'] +=  "❌"
                            print("Updated! Please try to be more consistent next time.👎")

                        # Writing updated data to the file
                        with open(location, "w") as f:
                            json.dump(habit_database, f, indent=4)
   
        except Exception as e:
            print("#UI2 An error occured:", e)
    
    # Showing Progress
    elif user_input == 3:
        try:
            # Importing data
            if Path(location).exists():
                with open(location, 'r') as f:
                    habit_database = json.load(f)

            # Showing all available habit.
            for habits_data in habit_database:
                print("*", habits_data['habit'])

            try:
                # Taking user choice to show progress about specific habit. 
                query = input("What habit would you like to learn more about? => ")

                # Looping through list to show data from dictionary.
                for habit_data in habit_database:
                    if habit_data['habit'].lower() == query.strip().lower():
                        print("--------------------------------------------")
                        print("Habit Name : ", habit_data['habit'])
                        print("Start Date : ", habit_data['Start Date'])
                        print("Streak     : ", habit_data['streak'])
                        print("Last Updated", habit_data['Last Updated'])

            except ValueError:
                print("Please enter a valid Habit name") # raisng error if invalid input
                query = None


        except Exception as e:
            print("#UI3 An error occured:", e)
    
    # Printing Menu 
    elif user_input == 4:
        print(menu)
    # Delete Menu
    elif user_input == 5:
        try:
            # Importing data
            with open(location, 'r') as f:
                habit_database = json.load(f)

            # Showing all Habits
            for habit_data in habit_database:
                print("🔥", habit_data['habit'] )

            # Asking User which query to delete
            delete_query = input("Which habit do you want to Delete? -> ")

            # Cleaning the habit Name
            habit_name_cleaned = delete_query.lower().strip()
            # gathering all habit Name for verification.
            all_habit_names = [habit['habit'].lower() for habit in habit_database]            

            # Checking if the queried habit name matches any from the db
            if habit_name_cleaned in all_habit_names: # Confirmation of the request
                print("Are you sure you want to delete the habit?") 
                yon = input("(Y/n) ->")

                # If user confirms, a new list w/o the deleted habit will be created.
                if yon.strip().lower() == 'y':
                    for data in habit_database:
                        if data['habit'] == habit_name_cleaned:
                            new_list = [habit for habit in habit_database if habit['habit'] != habit_name_cleaned]

                            try:
                                # Writing back the data to the file
                                with open(location, 'w') as f:
                                    json.dump(new_list, f, indent=4)

                            except FileNotFoundError:
                                print("del An error occured:", FileNotFoundError)

                            print(f"Habit : {delete_query} ,has been deleted.")
                # If user says No.
                else:
                    print("The request has been canceled.")

        except Exception as e:
            print("#DLF An error occured: ", e)
    # Exit Menu
    elif user_input == 6:
        break



