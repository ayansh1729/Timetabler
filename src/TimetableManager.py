from Table import Table
from FacultyList import FacultyList
from Generate import TimetableGenerator
from Validate import ValidateTimetables

# Example faculty data
faculty_data = [
        ('Dr. Smith', 5, 'Differential Equations', 'Y1D1, Y2D1'),
        ('Prof. Johnson', 3, 'Algebra', 'Y1D2, Y2D2, Y3D2'),
        ('Dr. Brown', 4, 'Calculus', 'Y1D3, Y2D3, Y3D3, Y4D3'),
        ('Dr. White', 2, 'Geometry', 'Y1D4, Y2D4'),
        ('Ms. Black', 6, 'Statistics', 'Y4D2, Y1D5, Y2D3')
    ]

departments = ['Y1D1', 'Y1D2', 'Y1D3', 'Y2D1', 'Y2D2', 'Y2D3', 'Y3D1', 'Y3D2', 'Y3D3', 'Y4D1', 'Y4D2', 'Y4D3']


time_tables = []
for department in departments:
    print(f"Generating timetables for {department}...")
    
    # Generate timetables for the current department
    generator = TimetableGenerator(department, faculty_data)
    
    # Validate the generated timetables
    generated = generator.next_permutation()
    generated.print_timetable()
    time_tables.append(generated)
    

valid,conflicts = ValidateTimetables(time_tables).validate()

if valid:
    print(f"All timetables for {department} are valid.")
else:
    print(f"Conflicts found in the timetables for {department}:")
    for conflict in conflicts:
        print(f"Faculty {conflict['faculty_id']} has conflicts at {conflict['time_slot']} on days: {', '.join(conflict['days'])}")
print("\n")

# from itertools import permutations

# class RecursiveTimetableSolver:
#     def __init__(self, faculty_data, departments):
#         self.faculty_data = faculty_data
#         self.departments = departments
#         self.current_permutations = {dept: None for dept in departments}
#         self.current_index = {dept: 0 for dept in departments}
#         self.solutions = {dept: None for dept in departments}
    
#     def generate_permutations(self, department):
#         # Generate all permutations of timetables for the given department
#         generator = TimetableGenerator(department, self.faculty_data)
#         return generator.timetables
    
#     def process_department(self, dept_index):
#         if dept_index >= len(self.departments):
#             return True  # All departments processed successfully

#         department = self.departments[dept_index]
#         permutations_list = self.generate_permutations(department)
        
#         if not permutations_list:
#             return False  # No permutations available for this department
        
#         while self.current_index[department] < len(permutations_list):
#             timetable = permutations_list[self.current_index[department]]
#             self.current_index[department] += 1
            
#             # Check if this timetable conflicts with previously set timetables
#             valid = True
#             for prev_dept in self.departments[:dept_index]:
#                 if self.solutions[prev_dept]:
#                     # Check for conflicts with previous department timetables
#                     if not self.check_no_conflicts(self.solutions[prev_dept], timetable):
#                         valid = False
#                         break
            
#             if valid:
#                 # Store valid timetable and proceed to next department
#                 self.solutions[department] = timetable
#                 if self.process_department(dept_index + 1):
#                     return True  # Proceed to next department if successful

#         # Backtrack if no valid timetable was found
#         self.solutions[department] = None
#         return False

#     def check_no_conflicts(self, previous_timetable, current_timetable):
#         # Combine validation for two timetables to check if they conflict
#         combined_timetables = [previous_timetable, current_timetable]
#         validator = ValidateTimetables(combined_timetables)
#         valid, _ = validator.validate()
#         print(valid)
#         return valid

#     def solve(self):
#         return self.process_department(0)

# # Example usage
# if __name__ == "__main__":
    # faculty_data = [
    #     ('Dr. Smith', 5, 'Differential Equations', 'Y1D1, Y2D1'),
    #     ('Prof. Johnson', 3, 'Algebra', 'Y1D2, Y2D2, Y3D2'),
    #     ('Dr. Brown', 4, 'Calculus', 'Y1D3, Y2D3, Y3D3, Y4D3'),
    #     ('Dr. White', 2, 'Geometry', 'Y1D4, Y2D3'),
    #     ('Ms. Black', 6, 'Statistics', 'Y4D2, Y1D3, Y2D3')
    # ]

#     departments = ['Y1D1', 'Y1D2', 'Y1D3', 'Y2D1', 'Y2D2', 'Y2D3', 'Y3D1', 'Y3D2', 'Y3D3', 'Y4D1', 'Y4D2', 'Y4D3']

#     solver = RecursiveTimetableSolver(faculty_data, departments)
#     if solver.solve():
#         print("Solution found!")
#         for dept in departments:
#             timetable = solver.solutions[dept]
#             if timetable:
#                 print(f"Timetable for {dept}:")
#                 timetable.print_timetable()
#     else:
#         print("No solution found.")

