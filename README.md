# High School Timetable Generator (MVP)

This project generates a simple timetable for high schools, assigning teachers, subjects, and rooms to classes while avoiding conflicts.

## Features
- Greedy algorithm for fast timetable generation
- Avoids teacher, class, and room conflicts
- Simple data model and sample data
- Prints timetable in a readable table format

## Setup
1. Install Python 3.8+
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the main script:
```
python main.py
```

## Customization
- Edit `sample_data.py` to change teachers, classes, subjects, rooms, and lessons.
- The algorithm can be improved in `generator.py` for more complex constraints.

## Output
The timetable for each class will be printed in the terminal in a table format. #   O r a r _ i n f 0 _ e d u c a t i e  
 