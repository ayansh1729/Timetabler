class FacultyList:
    def __init__(self, faculty_data):
        """
        Initialize the FacultyList with a list of faculty data.
        
        :param faculty_data: List of tuples (Faculty Name, Number of Courses, Department)
        """
        self.faculty_data = faculty_data
        self.faculty_keys = {}
        self.department_faculty = {}
        self._generate_faculty_keys()
        self._organize_by_department()

    def _generate_faculty_keys(self):
        """
        Generate a dictionary mapping faculty names to unique keys.
        """
        self.faculty_keys = {faculty[0]: f'F{index + 1}' for index, faculty in enumerate(self.faculty_data)}
    
    def _organize_by_department(self):
        """
        Organize faculty data by department.
        """
        self.department_faculty = {}
        for faculty in self.faculty_data:
            name, num_courses, department = faculty
            if department not in self.department_faculty:
                self.department_faculty[department] = []
            self.department_faculty[department].append((name, num_courses, self.faculty_keys[name]))

    def get_faculty_keys(self):
        """
        Return the dictionary of faculty keys.
        """
        return self.faculty_keys

    def get_department_faculty(self):
        """
        Return the dictionary of faculty organized by department.
        """
        return self.department_faculty

# Example usage
if __name__ == "__main__":
    # Define the faculty list
    faculty_data = [
        ('Dr. Smith', 5, 'Dept1'),
        ('Prof. Johnson', 3, 'Dept2'),
        ('Dr. Brown', 4, 'Dept3'),
        ('Dr. White', 2, 'Dept1'),
        ('Ms. Black', 6, 'Dept2')
    ]
    
    # Create a FacultyList instance
    faculty_list = FacultyList(faculty_data)
    
    # Print the results
    print("Faculty Keys:")
    print(faculty_list.get_faculty_keys())
    print("\nDepartment Faculty List:")
    for dept, faculty in faculty_list.get_department_faculty().items():
        print(f"{dept}: {faculty}")
