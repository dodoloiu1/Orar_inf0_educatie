from generator import get_timetable
from sample_data import classes, days, periods_per_day
from tabulate import tabulate

# Get the timetable once
timetable = get_timetable()

# Build a printable timetable for each class
for school_class in classes:
    class_name = school_class.name
    print(f"\nTimetable for class {class_name}:")
    table = []
    headers = ["Period"] + days
    for slot in range(1, periods_per_day+1):
        row = [f"{slot}"]
        for day in days:
            entry = timetable.get((school_class, day, slot))
            if entry:
                subject, teacher, room = entry
                row.append(f"{subject.name}\n{teacher.name}\nRoom {room.name}")
            else:
                row.append("")
        table.append(row)
    print(tabulate(table, headers=headers, tablefmt="grid"))

    # Check for gaps in the middle of the day for each day
    for day in days:
        scheduled_periods = [slot for slot in range(1, periods_per_day+1) if timetable.get((school_class, day, slot))]
        if scheduled_periods:
            # Find gaps between first and last scheduled period
            first = min(scheduled_periods)
            last = max(scheduled_periods)
            gaps = [slot for slot in range(first, last+1) if slot not in scheduled_periods]
            if len(gaps) > 1:
                print(f"WARNING: More than one gap in the schedule for {class_name} on {day}: gaps at periods {gaps}") 