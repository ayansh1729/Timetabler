class Timetable:
    def __init__(self):
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        self.time_slots = [
            '9:00-10:00', '10:00-11:00', '11:00-12:00',
            '12:00-1:00 (Recess)', '1:00-2:00', '2:00-3:00',
            '3:00-4:00', '4:00-5:00'
        ]
        self.timetable = {day: [''] * len(self.time_slots) for day in self.days}
    
    def add_course(self, day, time_slot, course):
        if day in self.days and time_slot in self.time_slots:
            time_index = self.time_slots.index(time_slot)
            self.timetable[day][time_index] = course
        else:
            print("Invalid day or time slot")

    def get_schedule(self):
        schedule = []
        for day in self.days:
            for time_index, time_slot in enumerate(self.time_slots):
                if self.timetable[day][time_index]:
                    schedule.append((day, time_slot, self.timetable[day][time_index]))
        return schedule

def load_timetables():
    timetables = []
    return timetables

def validate_timetables(timetables):
    faculty_schedule = {}

    for timetable in timetables:
        schedule = timetable.get_schedule()
        for day, time_slot, course in schedule:
            faculty_key = course.split()[0] 
            
            unique_identifier = (faculty_key, day, time_slot)
            
            if unique_identifier in faculty_schedule:
                print(f"Conflict detected: {unique_identifier} in {faculty_schedule[unique_identifier]} and {timetable}")
                return False
            
            faculty_schedule[unique_identifier] = timetable

    print("All timetables are valid.")
    return True

if __name__ == "__main__":
    timetables = load_timetables()

    validate_timetables(timetables)

