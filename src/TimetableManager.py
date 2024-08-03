import logging
from Generate import GenerateTimetable
from Validate import ValidateTimetables
from FacultyList import FacultyList
from Timetable import Timetable

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TimeTableManager:
    def __init__(self, faculty_data):
        self.faculty_data = faculty_data
        self.generate_timetable = GenerateTimetable(faculty_data)
        self.departments_years = ['Y1D1', 'Y1D2', 'Y1D3', 'Y2D1', 'Y2D2', 'Y2D3', 'Y3D1', 'Y3D2', 'Y3D3', 'Y4D1', 'Y4D2', 'Y4D3']
        self.timetables = {}
        self.generated_permutations = {dep_year: [] for dep_year in self.departments_years}

    def create_timetables(self):
        return self._backtrack(0)

    def _backtrack(self, index):
        if index == len(self.departments_years):
            return True

        dep_year = self.departments_years[index]
        attempt = 0
        max_attempts = 10000  # Limit the number of attempts to avoid infinite loop

        while attempt < max_attempts:
            logger.info(f"Attempting to generate timetable for {dep_year}, attempt {attempt+1}")
            timetable = self.generate_timetable.next_permutation()

            if timetable is None:
                logger.error(f"No valid permutation found for {dep_year} after {max_attempts} attempts")
                return False

            if timetable in self.generated_permutations[dep_year]:
                logger.info(f"Skipping previously generated timetable for {dep_year}")
                continue

            self.generated_permutations[dep_year].append(timetable)
            self.timetables[dep_year] = timetable

            # Validate the entire set of timetables
            validator = ValidateTimetables(list(self.timetables.values()))
            valid, conflicts = validator.validate()

            if valid:
                logger.info(f"Valid timetable found for {dep_year}")
                if self._backtrack(index + 1):
                    return True
                else:
                    # If further timetables are invalid, backtrack and try next permutation
                    del self.timetables[dep_year]
            else:
                logger.info(f"Conflict found for {dep_year}: {conflicts}")
                # Remove the invalid timetable and try the next permutation
                del self.timetables[dep_year]
                attempt += 1

        logger.error(f"Backtracking failed for {dep_year}")
        return False

    def print_timetables(self):
        for dep_year, timetable in self.timetables.items():
            print(f"Timetable for {dep_year}:")
            timetable.print_timetable()
            print("\n")


# Sample faculty data
faculty_data = [
    ('Dr. Smith', 5, 'Differential Equations', 'Y1D1, Y2D1, Y3D1, Y4D1, Y1D2'),
    ('Prof. Johnson', 3, 'Algebra', 'Y1D2, Y2D2, Y3D2'),
    ('Dr. Brown', 4, 'Calculus', 'Y1D3, Y2D3, Y3D3, Y4D3'),
    ('Dr. White', 2, 'Geometry', 'Y1D1, Y2D1'),
    ('Ms. Black', 6, 'Statistics', 'Y1D2, Y2D2, Y3D2, Y4D2, Y1D3, Y2D3')
]

# Create and manage timetables
manager = TimeTableManager(faculty_data)
if manager.create_timetables():
    manager.print_timetables()
else:
    logger.error("Failed to generate valid timetables for all departments and years")
