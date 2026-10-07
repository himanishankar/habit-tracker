#step A: Data persistence function 
import json
import os
from datetime import datetime, timedelta

DATA_FILE = "habits.json"

def load_habits():
    """Loads habits from the JSON file or returns an empty dict if the file doesn't exist."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_habits(habits):
    """Saves the current habits dictionary back to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(habits, f, indent=4)

#step B: Core business logic
def add_habit(habits, name):
    key = name.lower().replace(" ", "_")
    if key in habits:
        print("⚠️ That habit already exists!")
        return
    habits[key] = {
        "name": name,
        "last_completed": None,
        "streak": 0
    }
    save_habits(habits)
    print(f"✅ Habit '{name}' successfully created!")

def complete_habit(habits, key):
    if key not in habits:
        print("⚠️ Habit not found.")
        return
    
    habit = habits[key]
    today_str = datetime.now().strftime("%Y-%m-%d")
    yesterday_str = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    
    if habit["last_completed"] == today_str:
        print(f"💪 You already logged '{habit['name']}' today! Keep up the great work.")
        return
        
    if habit["last_completed"] == yesterday_str:
        habit["streak"] += 1
    else:
        # Streak broken or first time tracking
        habit["streak"] = 1
        
    habit["last_completed"] = today_str
    save_habits(habits)
    print(f"🔥 Awesome! '{habit['name']}' logged. Current Streak: {habit['streak']} days!")

#step C: Interactive CLI menu loop
def list_habits(habits):
    if not habits:
        print("\n📭 No habits tracked yet. Add one to get started!")
        return
    print("\n--- 🎯 YOUR HABITS ---")
    for key, data in habits.items():
        last = data["last_completed"] if data["last_completed"] else "Never"
        print(f"• ID: [{key}] | {data['name']} | 🔥 Streak: {data['streak']} days | 📅 Last: {last}")

def main():
    while True:
        habits = load_habits()
        print("\n=== HABIT TRAKER CLI ===")
        print("1. View Current Habits")
        print("2. Add a New Habit")
        print("3. Check-off a Habit")
        print("4. Exit Application")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == "1":
            list_habits(habits)
        elif choice == "2":
            name = input("Enter the name of the habit: ").strip()
            if name: add_habit(habits, name)
        elif choice == "3":
            list_habits(habits)
            if habits:
                key = input("\nEnter the ID of the habit to complete: ").strip()
                complete_habit(habits, key)
        elif choice == "4":
            print("Goodbye! Stay consistent! 👋")
            break
        else:
            print("❌ Invalid input choice. Please select 1-4.")

if __name__ == "__main__":
    main()
