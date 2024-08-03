from itertools import permutations
from FacultyList import FacultyList
from Timetable import Timetable

class TimetableManager:
    def __init__(self, name, faculty_keys):
        self.name = name
        self.timetable = Timetable()
        self.current_permutation = 0
        self.permutations = list(permutations(self.timetable.time_slots[:-1])) 
        self.faculty_keys = faculty_keys

    def generate_next_permutation(self):
        if self.current_permutation < len(self.permutations):
            perm = self.permutations[self.current_permutation]
            self.current_permutation += 1
            
            self.timetable = Timetable()
            for day_index, day in enumerate(self.timetable.days):
                for slot_index, time_slot in enumerate(perm):
                    faculty_key = list(self.faculty_keys.keys())[day_index % len(self.faculty_keys)]
                    self.timetable.add_course(day, time_slot, f'{faculty_key} Course {slot_index + 1}')
        else:
            print("No more permutations available.")

    def print_timetable(self):
        print(f"Timetable: {self.name}")
        self.timetable.print_timetable()
        print()

def generate_timetables(faculty_list):
    faculty_keys = faculty_list.get_faculty_keys()
    department_faculty = faculty_list.get_department_faculty()

    # Define years
    years = ['Year1', 'Year2', 'Year3', 'Year4']
    
    managers = []
    
    for year in years:
        for dept, faculty_info in department_faculty.items():
            name = f'{year} - {dept}'
            faculty_keys_for_dept = {name: key for name, _, key in faculty_info}
            manager = TimetableManager(name, faculty_keys_for_dept)
            managers.append(manager)

    for manager in managers:
        manager.generate_next_permutation()
        manager.print_timetable()

if __name__ == "__main__":
    faculty_data = [
        ('Dr. Smith', 5, 'Dept1'),
        ('Prof. Johnson', 3, 'Dept2'),
        ('Dr. Brown', 4, 'Dept3'),
        ('Dr. White', 2, 'Dept1'),
        ('Ms. Black', 6, 'Dept2')
    ]
    faculty_list = FacultyList(faculty_data)

    generate_timetables(faculty_list)
