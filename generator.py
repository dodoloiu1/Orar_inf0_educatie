from models import Teacher, Subject, Room, SchoolClass, Period
from sample_data import teachers, subjects, rooms, classes, days, periods_per_day, periods, lessons
from typing import Dict, List, Tuple
from random import shuffle

def get_timetable() -> Dict[Tuple[SchoolClass, str, int], Tuple[Subject, Teacher, Room]]:
    timetable = {}
    teacher_busy: Dict[Tuple[Teacher, str, int], bool] = {}
    room_busy: Dict[Tuple[Room, str, int], bool] = {}

    # Organize lessons by class
    class_lessons: Dict[SchoolClass, List[Dict]] = {c: [] for c in classes}
    for lesson in lessons:
        class_lessons[lesson['class']].append(lesson.copy())

    for school_class in classes:
        print(f"\nProcessing class {school_class.name}")
        # Build a per-subject remaining count for this class
        remaining = []
        for lesson in class_lessons[school_class]:
            for _ in range(lesson['count']):
                remaining.append({'subject': lesson['subject'], 'teacher': lesson['teacher']})
        shuffle(remaining)
        # Distribute lessons across days
        lesson_idx = 0
        for day in days:
            print(f"\nTrying to schedule {school_class.name} for {day}")
            lessons_today = []
            # Fill up to periods_per_day or until no lessons left
            for _ in range(periods_per_day):
                if lesson_idx < len(remaining):
                    lessons_today.append(remaining[lesson_idx])
                    lesson_idx += 1
            print(f"Lessons to assign for {school_class.name} on {day}: {[l['subject'].name for l in lessons_today]}")
            # Try to schedule these lessons
            if not schedule_lessons_for_day(timetable, teacher_busy, room_busy, 
                                         school_class, day, lessons_today):
                print(f"WARNING: Could not schedule all lessons for {school_class.name} on {day}")
    return timetable

def schedule_lessons_for_day(timetable: Dict, teacher_busy: Dict, room_busy: Dict,
                           class_name: SchoolClass, day: str, 
                           lessons_to_schedule: List[Dict]) -> bool:
    # Don't shuffle periods - we want them contiguous
    # Find the earliest available contiguous block
    if not lessons_to_schedule:
        return True  # Nothing to schedule, so we succeeded
        
    num_lessons = len(lessons_to_schedule)
    
    # Find all possible starting periods that would allow contiguous scheduling
    for start_period in range(1, periods_per_day - num_lessons + 2):
        period_range = list(range(start_period, start_period + num_lessons))
        
        # Check if this contiguous block can fit all lessons
        can_schedule = True
        test_assignments = []  # Store potential assignments to commit if successful
        
        for i, period in enumerate(period_range):
            lesson = lessons_to_schedule[i]
            subject = lesson['subject']
            teacher = lesson['teacher']
            
            # Check if teacher is available
            if teacher_busy.get((teacher, day, period), False):
                print(f"Teacher {teacher.name} is busy for {class_name.name} on {day} period {period}")
                can_schedule = False
                break
                
            # Find an available room
            room_found = False
            for room in rooms:
                if not room_busy.get((room, day, period), False):
                    test_assignments.append((period, subject, teacher, room))
                    room_found = True
                    break
                    
            if not room_found:
                print(f"No available rooms for {class_name.name} on {day} period {period}")
                can_schedule = False
                break
                
        if can_schedule:
            # Commit all assignments - we found a contiguous block
            for period, subject, teacher, room in test_assignments:
                timetable[(class_name, day, period)] = (subject, teacher, room)
                teacher_busy[(teacher, day, period)] = True
                room_busy[(room, day, period)] = True
                print(f"Assigned {subject.name} ({teacher.name}) to {class_name.name} on {day} period {period} in room {room.name}")
            return True
            
    # If we reach here, we couldn't find a contiguous block for all lessons
    # Schedule as many as possible in any available slots
    available_slots = list(range(1, periods_per_day + 1))
    available_slots.sort()  # Ensure we try earlier periods first
    
    assigned_any = False
    for lesson in lessons_to_schedule:
        subject = lesson['subject']
        teacher = lesson['teacher']
        assigned = False
        
        for slot in available_slots:
            if teacher_busy.get((teacher, day, slot), False):
                continue
                
            for room in rooms:
                if not room_busy.get((room, day, slot), False):
                    timetable[(class_name, day, slot)] = (subject, teacher, room)
                    teacher_busy[(teacher, day, slot)] = True
                    room_busy[(room, day, slot)] = True
                    available_slots.remove(slot)
                    print(f"Assigned {subject.name} ({teacher.name}) to {class_name.name} on {day} period {slot} in room {room.name}")
                    assigned = True
                    assigned_any = True
                    break
                    
            if assigned:
                break
                
        if not assigned:
            print(f"Could not assign {subject.name} ({teacher.name}) to {class_name.name} on {day} (skipping this lesson)")
            
    return assigned_any 