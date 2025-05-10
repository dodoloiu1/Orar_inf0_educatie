from models import Teacher, Subject, Room, SchoolClass, Period

teachers = [Teacher('Alice'), Teacher('Bob'), Teacher('Carol'), Teacher('Dave'), Teacher('Eve')]
subjects = [Subject('Math'), Subject('English'), Subject('Physics'), Subject('Chemistry'), Subject('Biology')]
rooms = [Room('101'), Room('102'), Room('103'), Room('104'), Room('105')]
classes = [SchoolClass('9A'), SchoolClass('9B')]
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
periods_per_day = 5
periods = [Period(day, slot+1) for day in days for slot in range(periods_per_day)]

# Example: lessons to schedule (class, subject, teacher, lessons per week)
lessons = [
    {'class': classes[0], 'subject': subjects[0], 'teacher': teachers[0], 'count': 4},
    {'class': classes[0], 'subject': subjects[1], 'teacher': teachers[1], 'count': 4},
    {'class': classes[0], 'subject': subjects[2], 'teacher': teachers[2], 'count': 2},
    {'class': classes[0], 'subject': subjects[3], 'teacher': teachers[3], 'count': 1},
    {'class': classes[0], 'subject': subjects[4], 'teacher': teachers[4], 'count': 3},
    {'class': classes[1], 'subject': subjects[0], 'teacher': teachers[0], 'count': 3},
    {'class': classes[1], 'subject': subjects[1], 'teacher': teachers[1], 'count': 4},
    {'class': classes[1], 'subject': subjects[2], 'teacher': teachers[2], 'count': 2},
    {'class': classes[1], 'subject': subjects[3], 'teacher': teachers[3], 'count': 2},
    {'class': classes[1], 'subject': subjects[4], 'teacher': teachers[4], 'count': 2},

] 
