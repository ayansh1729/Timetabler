import itertools
from FacultyList import FacultyList
from Timetable import Timetable

class GenerateTimetable:
    def __init__(self, faculty_list):
        self.faculty_list = FacultyList(faculty_list)
        self.timetables = self._generate_timetables()

    def _generate_timetables(self):
        faculty_dict = self.faculty_list.get_faculty_dict()
        timetables = []
        
        for course, faculty in faculty_dict.items():
            faculty_permutations = list(itertools.permutations(faculty))
            for perm in faculty_permutations:
                perm_list = list(perm)  # Convert tuple to list
                timetable = Timetable()
                for day, time_slot in zip(timetable.days, timetable.time_slots[:-1]):
                    if perm_list:
                        faculty_member = perm_list.pop(0)
                        timetable.add_course(day, time_slot, faculty_member['unique_key'])
                timetables.append(timetable)
        return timetables

    def next_permutation(self):
        if hasattr(self, 'timetables') and self.timetables:
            return self.timetables.pop(0)
        else:
            return None

    def get_all_permutations(self):
        return self.timetables

# Sample faculty data
faculty_data = [
    ('Dr. Smith', 5, 'Differential Equations', 'Y1D1, Y2D1, Y3D1, Y4D1, Y1D2'),
    ('Prof. Johnson', 3, 'Algebra', 'Y1D2, Y2D2, Y3D2'),
    ('Dr. Brown', 4, 'Calculus', 'Y1D3, Y2D3, Y3D3, Y4D3'),
    ('Dr. White', 2, 'Geometry', 'Y1D1, Y2D1'),
    ('Ms. Black', 6, 'Statistics', 'Y1D2, Y2D2, Y3D2, Y4D2, Y1D3, Y2D3')
]

# Create GenerateTimetable object
generate_timetable = GenerateTimetable(faculty_data)

# Get and print the next permutation
next_perm = generate_timetable.next_permutation()
if next_perm:
    next_perm.print_timetable()

# Print all remaining permutations
for perm in generate_timetable.get_all_permutations():
    perm.print_timetable()
