class Table:
    def __init__(self):
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        self.time_slots = [
            '9:00-10:00', '10:00-11:00', '11:00-12:00',
            '12:00-1:00 (Recess)', '1:00-2:00', '2:00-3:00',
            '3:00-4:00', '4:00-5:00'
        ]
        self.timetable = {day: [''] * len(self.time_slots) for day in self.days}

    def add_course(self, day, time_slot, course):
        if day not in self.days:
            return -1  # Invalid day
        if time_slot not in self.time_slots:
            return -1  # Invalid time slot

        day_index = self.days.index(day)
        time_slot_index = self.time_slots.index(time_slot)
        if self.timetable[day][time_slot_index] == '' and 'Recess' not in time_slot:
            self.timetable[day][time_slot_index] = course
            return 0  # Course added successfully
        return -1  # Failed to add course

    def remove_course(self, day, time_slot):
        if day not in self.days or time_slot not in self.time_slots:
            return -1  # Invalid day or time slot

        day_index = self.days.index(day)
        time_slot_index = self.time_slots.index(time_slot)
        self.timetable[day][time_slot_index] = ''  # Remove course
        return 0  # Course removed successfully

    def clear_timetable(self):
        self.timetable = {day: [''] * len(self.time_slots) for day in self.days}

    def print_timetable(self):
        import pandas as pd
        df = pd.DataFrame(self.timetable, index=self.time_slots)
        print(df.T)