from itertools import permutations
from Timetable import Timetable

class TimetableManager:
    def __init__(self, name):
        self.name = name
        self.timetable = Timetable()
        self.current_permutation = 0
        self.permutations = list(permutations(self.timetable.time_slots[:-1]))

    def generate_next_permutation(self):
        if self.current_permutation < len(self.permutations):
            perm = self.permutations[self.current_permutation]
            self.current_permutation += 1
            
            self.timetable = Timetable()
            for day_index, day in enumerate(self.timetable.days):
                for slot_index, time_slot in enumerate(perm):
                    self.timetable.add_course(day, time_slot, f'{self.name} Course {day_index * len(perm) + slot_index + 1}')
        else:
            print("No more permutations available.")

    def print_timetable(self):
        print(f"Timetable: {self.name}")
        self.timetable.print_timetable()
        print()

departments = ['Dept1', 'Dept2', 'Dept3', 'Dept4', 'Dept5']
years = ['Year1', 'Year2', 'Year3', 'Year4']

managers = [TimetableManager(f'{year} - {dept}') for year in years for dept in departments]

for manager in managers:
    manager.generate_next_permutation()
    manager.print_timetable()
