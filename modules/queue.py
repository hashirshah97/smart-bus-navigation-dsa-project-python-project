class PassengerQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, passenger):
        self.queue.append(passenger)
        print(f"✅ {passenger} added successfully to the queue")

    def dequeue(self):
        if not self.queue:
            print("❌ Queue is empty, no passenger to remove")
            return None
        removed = self.queue.pop(0)
        print(f"🚌 {removed} removed from the queue")
        return removed

    def peek(self):
        if self.queue:
            return self.queue[0]
        return "❌ Queue is empty"

    def size(self):
        return len(self.queue)

    def display(self):
        if not self.queue:
            print("❌ Queue is empty")
        else:
            print("🎟️ Current Queue:")
            for passenger in self.queue:
                print(passenger)
