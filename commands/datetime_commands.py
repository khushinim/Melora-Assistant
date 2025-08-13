# commands/datetime_commands.py
from datetime import datetime
from utils import speak


def handle_datetime(command):
    now = datetime.now()
    handled = False

    # --- Handle day/month/year/date/time ---
    parts = []
    if "day" in command:
        parts.append(f"Today is {now.strftime('%A')}")  
        handled = True
    if "date" in command:
        parts.append(f"The date is {now.strftime("%d %B %Y")}")  
        handled = True
    if "month" in command:
        parts.append(f"This month is {now.strftime('%B')}")
        handled = True
    if "year" in command:
        parts.append(f"The year is {now.strftime('%Y')}")
        handled = True
    if "time" in command:
        parts.append(f"The time is {now.strftime('%I:%M %p')}")
        handled = True

    if parts:
        speak(" and ".join(parts))
        return True

    return handled
