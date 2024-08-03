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
