import json
from datetime import date

def load_sessions():
    try:
        with open("sessions.json", "r") as file:
            loaded = json.load(file)
        return loaded
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_sessions(sessions):
    with open("sessions.json", "w") as file:
        json.dump(sessions, file)

def add_session(sessions, input_subject, input_date, input_minutes):
    new_session = {"subject": input_subject, "date": input_date, "duration_minutes": input_minutes}
    sessions.append(new_session)
    save_sessions(sessions)

def view_sessions(sessions):
    if len(sessions) == 0:
        print("No Sessions Recorded")
    else:
        for index in range(len(sessions)):
            session = sessions[index]
            display_number = index + 1
            print(f"{display_number}: {session['subject']} - {session['date']} - {session['duration_minutes']} minutes")

sessions_original = load_sessions()

running = True
while running:
    choice = input("What do you want to do? (Add / View / Quit) ")
    if choice.lower() == "add":
        session_subject = str(input("Enter the session's Subject: "))

        while True:
            date_category = input("Custom date or today's date? (Custom / Today) ")

            if date_category.lower() == "custom":
                session_date = input("Enter a date: ")
                break
            elif date_category.lower() == "today":
                session_date = date.today().isoformat()
                break
            else:
                print("Invalid input, try again")

        while True:
            try:
                session_duration = int(input("Enter the session duration in minutes: "))
                if session_duration <= 0:
                    print("Invalid input, try inputting a Positive number")
                else:
                    break
            except ValueError:
                print("Invalid input, try inputting a number")

        add_session(sessions_original, session_subject, session_date, session_duration)

    elif choice.lower() == "view":
        view_sessions(sessions_original)

    elif choice.lower() == "quit":
        save_sessions(sessions_original)
        running = False

    else:
        print("Invalid choice")