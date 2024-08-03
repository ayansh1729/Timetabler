class ValidateTimetables:
    def __init__(self, timetables):
        self.timetables = timetables

    def check_conflicts(self):
        faculty_schedule = {}
        for timetable in self.timetables:
            for day, time_slots in timetable.timetable.items():
                for time_index, faculty_id in enumerate(time_slots):
                    if faculty_id and faculty_id != '12:00-1:00 (Recess)':
                        time_slot = timetable.time_slots[time_index]
                        if faculty_id not in faculty_schedule:
                            faculty_schedule[faculty_id] = {}
                        if time_slot not in faculty_schedule[faculty_id]:
                            faculty_schedule[faculty_id][time_slot] = []
                        faculty_schedule[faculty_id][time_slot].append(day)
        
        conflicts = []
        for faculty_id, schedule in faculty_schedule.items():
            for time_slot, days in schedule.items():
                if len(days) > 1:
                    conflicts.append({
                        'faculty_id': faculty_id,
                        'time_slot': time_slot,
                        'days': days
                    })
        
        return conflicts

    def validate(self):
        conflicts = self.check_conflicts()
        if conflicts:
            return False, conflicts
        else:
            return True, None
