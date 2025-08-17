class BusSchedule:
    def __init__(self):
        self.schedules = []

    def add_bus(self, bus_id, departure_time, route):
        self.schedules.append([bus_id, departure_time, route])

    def display_schedule(self):
        if not self.schedules:
            print("No buses scheduled")
            return

        print("🚌 Bus Schedules:")
        for bus in self.schedules:
            print(f"Bus Id: {bus[0]}, Departure Time: {bus[1]}, Route: {bus[2]} ")

    def bubble_sort(self):
        """Sort schedules by departure_time using Bubble Sort"""
        n = len(self.schedules)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.schedules[j][1] > self.schedules[j + 1][1]:
                    self.schedules[j], self.schedules[j + 1] = self.schedules[j + 1], self.schedules[j]

    def selection_sort(self):
        """Sort schedules by departure_time using Selection Sort"""
        n = len(self.schedules)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self.schedules[j][1] < self.schedules[min_idx][1]:
                    min_idx = j
            self.schedules[i], self.schedules[min_idx] = self.schedules[min_idx], self.schedules[i]
