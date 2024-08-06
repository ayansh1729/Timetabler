import pandas as pd
import copy
from Table import Table
from FacultyList import FacultyList

class TimetableGenerator:
    def __init__(self, department_name, faculty_data):
        self.department_name = department_name
        self.faculty_list = self.filter_faculty_data(faculty_data, department_name)
        self.timetables = []
        self.current_index = 0  # To keep track of the next permutation
        self.generate_timetables(0, 0, Table(), self.faculty_list.get_faculty_dict())

    def filter_faculty_data(self, faculty_data, department_name):
        filtered_data = []
        for name, num_classes, course_name, courses in faculty_data:
            if department_name in courses:
                filtered_data.append((name, num_classes, course_name, department_name))
        return FacultyList(filtered_data)

    def generate_timetables(self, i, j, table, faculty_dict):
        if len(self.timetables) >= 5000:
            return
        if i >= len(table.days):
            self.timetables.append(copy.deepcopy(table))
            return

        if j >= len(table.time_slots):
            self.generate_timetables(i + 1, 0, table, faculty_dict)  # Move to the next day
            return

        # Try each faculty for the current slot
        for course, faculty_list in faculty_dict.items():
            for idx, faculty in enumerate(faculty_list):
                if faculty['num_classes'] > 0:
                    # Check if this faculty already has a class scheduled for the current day
                    if any(faculty['faculty_name'] == entry for entry in table.timetable[table.days[i]]):
                        continue  # Skip this faculty if already scheduled for the current day

                    # Try adding this faculty's course to the timetable
                    if table.add_course(table.days[i], table.time_slots[j], faculty['faculty_name']) == 0:
                        # Decrease the number of classes for this faculty
                        faculty['num_classes'] -= 1

                        # Recursively generate timetables with this faculty's course added
                        self.generate_timetables(i, j + 1, table, faculty_dict)

                        # Remove the course and reset the faculty list
                        table.remove_course(table.days[i], table.time_slots[j])
                        faculty['num_classes'] += 1

        # Try the next slot without adding any course
        self.generate_timetables(i, j + 1, table, faculty_dict)

    def next_permutation(self):
        if self.current_index < len(self.timetables):
            timetable = self.timetables[self.current_index]
            self.current_index += 1
            return timetable
        else:
            return None  # No more permutations available

    def save_timetables(self, filename='timetables.pkl'):
        with open(filename, 'wb') as f:
            import pickle
            pickle.dump(self.timetables, f)

    def load_timetables(self, filename='timetables.pkl'):
        with open(filename, 'rb') as f:
            import pickle
            self.timetables = pickle.load(f)
            self.current_index = 0  # Reset the index after loading

# Example usage
if __name__ == "__main__":
    faculty_data = [
        ('Dr. Smith', 5, 'Differential Equations', 'Y1D1, Y2D1, Y3D1, Y4D1, Y1D2'),
        ('Prof. Johnson', 3, 'Algebra', 'Y1D2, Y2D2, Y3D2'),
        ('Dr. Brown', 4, 'Calculus', 'Y1D3, Y2D3, Y3D3, Y4D3'),
        ('Dr. White', 2, 'Geometry', 'Y1D1, Y2D1'),
        ('Ms. Black', 6, 'Statistics', 'Y1D2, Y2D2, Y3D2, Y4D2, Y1D3, Y2D3')
    ]

    generator = TimetableGenerator('Y1D2', faculty_data)
    next_timetable = generator.next_permutation()

    # if next_timetable:
    #     next_timetable.print_timetable()
    # else:
    #     print("No more timetables available.")
    for i in range(10):
        generator.next_permutation().print_timetable()
