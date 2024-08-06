import pandas as pd

class FacultyList:
    def __init__(self, faculty_data):
        self.faculty_data = faculty_data
        self.faculty_dict = self._create_faculty_dict()

    def _generate_unique_key(self, name):
        parts = name.split()
        initials = ''.join([part[0] for part in parts if part[0].isalpha()])
        base_key = initials.upper()
        
        suffix = 1
        unique_key = base_key
        while unique_key in self.existing_keys:
            unique_key = f"{base_key}{suffix}"
            suffix += 1
        self.existing_keys.add(unique_key)
        return unique_key

    def _create_faculty_dict(self):
        self.existing_keys = set()
        faculty_dict = {}
        for name, num_classes, course_name, courses in self.faculty_data:
            unique_key = self._generate_unique_key(name)
            course_list = courses.split(', ')
            for course in course_list:
                if course not in faculty_dict:
                    faculty_dict[course] = []
                faculty_dict[course].append({
                    'unique_key': unique_key,
                    'faculty_name': name,
                    'course_name': course_name,
                    'num_classes': num_classes
                })
        return faculty_dict

    def get_faculty_dict(self):
        return self.faculty_dict

    def print_faculty_dict(self):
        print("Faculty Dictionary:")
        for course, faculty_list in self.faculty_dict.items():
            print(f"\nCourse: {course}")
            for faculty in faculty_list:
                print(f"  - Unique Key: {faculty['unique_key']}")
                print(f"    Faculty Name: {faculty['faculty_name']}")
                print(f"    Course Name: {faculty['course_name']}")
                print(f"    Number of Classes: {faculty['num_classes']}")
                print()

# Faculty data
faculty_data = [
    ('Dr. Smith', 5, 'Differential Equations', 'Y1D1, Y2D1, Y3D1, Y4D1, Y1D2'),
    ('Prof. Johnson', 3, 'Algebra', 'Y1D2, Y2D2, Y3D2'),
    ('Dr. Brown', 4, 'Calculus', 'Y1D3, Y2D3, Y3D3, Y4D3'),
    ('Dr. White', 2, 'Geometry', 'Y1D1, Y2D1'),
    ('Ms. Black', 6, 'Statistics', 'Y1D2, Y2D2, Y3D2, Y4D2, Y1D3, Y2D3')
]

# Initialize FacultyList and print the dictionary using the class method
data = FacultyList(faculty_data)
data.print_faculty_dict()
