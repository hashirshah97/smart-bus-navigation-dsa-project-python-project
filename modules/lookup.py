class BusLookup:
    def __init__(self):
        self.bus_table = {}  # bus_id → [departure_time, route]

    def add_bus(self, bus_id, departure_time, route):
        """Add bus info to dictionary"""
        self.bus_table[bus_id] = [departure_time, route]
        print(f"✅ Bus {bus_id} added: Departure {departure_time}, Route {route}")

    def find_bus(self, bus_id):
        """Return bus info by bus_id"""
        if bus_id in self.bus_table:
            info = self.bus_table[bus_id]
            print(f"Bus {bus_id} → Departure: {info[0]}, Route: {info[1]}")
            return info
        else:
            print(f"❌ Bus {bus_id} not found")
            return None

    def display_all_buses(self):
        """Display all buses in the lookup table"""
        if not self.bus_table:
            print("⚠️ No buses available")
            return

        print("🚌 All Buses:")
        for bus_id, info in self.bus_table.items():
            print(f"Bus {bus_id} → Departure: {info[0]}, Route: {info[1]}")
