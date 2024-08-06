import random

NUM_DAYS = 5
NUM_SLOTS = 8
NUM_FACULTIES = 5


class Timetable:
    def __init__(self):
        self.schedule = [[None for _ in range(NUM_SLOTS)] for _ in range(NUM_DAYS)]

    def copy(self):
        new_timetable = Timetable()
        new_timetable.schedule = [row[:] for row in self.schedule]
        return new_timetable

    def is_valid(self):
        for day in range(NUM_DAYS):
            faculty_count = set()
            for slot in range(NUM_SLOTS):
                faculty = self.schedule[day][slot]
                if faculty and faculty in faculty_count:
                    return False
                faculty_count.add(faculty)
        return True

def create_random_timetable():
    timetable = Timetable()
    # Fill timetable with random valid assignments
    for day in range(NUM_DAYS):
        faculties = list(range(NUM_FACULTIES))
        random.shuffle(faculties)
        for slot in range(NUM_SLOTS):
            if slot < NUM_FACULTIES:
                timetable.schedule[day][slot] = faculties[slot]
    return timetable

def fitness(timetable):
    # Define fitness function based on your constraints
    if not timetable.is_valid():
        return 0
    return sum(sum(1 for slot in day if slot is not None) for day in timetable.schedule)

def crossover(parent1, parent2):
    # Implement crossover logic to combine two parents
    child = parent1.copy()
    for day in range(NUM_DAYS):
        if random.random() < 0.5:
            child.schedule[day] = parent2.schedule[day][:]
    return child

def mutate(timetable):
    # Implement mutation logic to introduce changes
    day = random.randint(0, NUM_DAYS - 1)
    slot = random.randint(0, NUM_SLOTS - 1)
    timetable.schedule[day][slot] = random.randint(0, NUM_FACULTIES - 1)

def genetic_algorithm():
    population = [create_random_timetable() for _ in range(10)]
    best_timetable = None
    best_fitness = 0

    for generation in range(100):
        population = sorted(population, key=fitness, reverse=True)

        # Update best timetable
        if fitness(population[0]) > best_fitness:
            best_fitness = fitness(population[0])
            best_timetable = population[0].copy()

        next_generation = population[:2]  # Elitism, keep the best two

        while len(next_generation) < 10:
            parent1, parent2 = random.sample(population[:5], 2)  # Select parents
            child = crossover(parent1, parent2)
            mutate(child)
            if child.is_valid():
                next_generation.append(child)

        population = next_generation
        print(f"Generation {generation}: Best fitness = {best_fitness}")

    # Print the best timetable found
    print("Best timetable found:")
    if best_timetable:
        for day_idx, day in enumerate(best_timetable.schedule):
            print(f"Day {day_idx + 1}: {day}")

genetic_algorithm()