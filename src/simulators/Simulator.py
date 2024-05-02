

class simulator:
    def __init__(self, shifts, workers):
        self.shifts = shifts
        self.workers = workers
        self.schedule = []
        self.schedule = self.generate_schedule()
    
    def generate_schedule(self):
        schedule = []
        for shift in self.shifts:
            for worker in self.workers:
                schedule.append((shift, worker))
        return schedule