import pandas as pd

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
            if time_slot == '12:00-1:00 (Recess)':
                print("Cannot add course during recess time")
                return -1
            else:
                time_index = self.time_slots.index(time_slot)
                self.timetable[day][time_index] = course
        else:
            print("Invalid day or time slot")
            return -1
    
    def print_timetable(self):
        df = pd.DataFrame(self.timetable, index=self.time_slots)
        print(df.T)
