class Event:
    def __init__(self, event_type, bus_id, stop=None, time=None, details=None):
        self.event_type = event_type    # e.g., "departure", "arrival", "delay", "maintenance"
        self.bus_id = bus_id            # e.g., "Bus 101"
        self.stop = stop                # e.g., "Stop A"
        self.time = time                # e.g., "09:00 AM"
        self.details = details          # e.g., "10 min late" or "sent to maintenance yard"

    def __str__(self):
        return f"[{self.time}] Bus {self.bus_id} {self.event_type} at {self.stop} ({self.details})"


class BusNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class BusStack:
    def __init__(self):
        self.top = None

    def push(self, event):
        node = BusNode(event)
        node.next = self.top  # jo pehle top tha, uske upar naya node
        self.top = node
        print(f"✅ Event pushed: {event}")

    def pop(self):
        if self.top is None:
            print("⚠️ Stack is empty")
            return None
        removed = self.top
        self.top = self.top.next
        print(f"🗑️ Event popped: {removed.data}")

    def peek(self):
        if self.top is None:
            print("⚠️ Stack is empty")
            return None
        print(self.top.data)

    def display(self):
        if self.top is None:
            print("⚠️ Stack is empty")
            return
        curr = self.top
        print("📜 Event History (Most recent first):")
        while curr:
            print(f"   {curr.data}")
            curr = curr.next
