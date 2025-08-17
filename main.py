from modules.graph import CityGraph
from modules.queue import PassengerQueue
from modules.passenger import CustomerLinkedList, Customer
from modules.stack import BusStack, Event
from modules.schedule import BusSchedule
from modules.lookup import BusLookup


def main():
    city_graph = CityGraph()
    passengers = CustomerLinkedList()
    ticket_queue = PassengerQueue()
    event_stack = BusStack()
    bus_schedule = BusSchedule()
    bus_lookup = BusLookup()

    while True:
        print("\n=== Smart City Transport CLI ===")
        print("1. Add Route")
        print("2. Display Routes")
        print("3. Find Shortest Route")
        print("4. Add Passenger / Book Ticket")
        print("5. Remove Passenger / Cancel Ticket")
        print("6. Display All Passengers")
        print("7. Bus Arrival / Departure Event")
        print("8. Display Event History")
        print("9. Add Bus to Schedule")
        print("10. Display Bus Schedule")
        print("11. Sort Bus Schedule (Bubble)")
        print("12. Sort Bus Schedule (Selection)")
        print("13. Add Bus to Lookup")
        print("14. Find Bus by ID")
        print("15. Display All Lookup Buses")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            stop1 = input("Enter stop 1: ")
            stop2 = input("Enter stop 2: ")
            dist = float(input("Enter distance: "))
            city_graph.add_route(stop1, stop2, dist)
        elif choice == "2":
            city_graph.display_routes()
        elif choice == "3":
            start = input("Start stop: ")
            end = input("End stop: ")
            city_graph.find_shortest_route(start, end)
        elif choice == "4":
            cid = input("Customer ID: ")
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            from_ = input("From: ")
            to = input("To: ")
            bus_no = input("Bus Number")
            departure_time = input("Enter Departure Time : ")
            cust = Customer(cid, name, email, phone, from_, to,bus_no,departure_time)
            passengers.add(cust)
            ticket_queue.enqueue(cust)
        elif choice == "5":
            cid = input("Customer ID to remove: ")
            passengers.delete(cid)
        elif choice == "6":
            passengers.view()
        elif choice == "7":
            bus_id = input("Bus ID: ")
            event_type = input("Event type (arrival/departure/delay): ")
            stop = input("Stop: ")
            time = input("Time: ")
            details = input("Details: ")
            ev = Event(event_type, bus_id, stop, time, details)
            event_stack.push(ev)
        elif choice == "8":
            event_stack.display()
        elif choice == "9":
            bus_id = input("Bus ID: ")
            dep_time = input("Departure Time: ")
            route = input("Route: ")
            bus_schedule.add_bus(bus_id, dep_time, route)
        elif choice == "10":
            bus_schedule.display_schedule()
        elif choice == "11":
            bus_schedule.bubble_sort()
            print("✅ Bus schedule sorted using Bubble Sort")
        elif choice == "12":
            bus_schedule.selection_sort()
            print("✅ Bus schedule sorted using Selection Sort")
        elif choice == "13":
            bus_id = input("Bus ID: ")
            dep_time = input("Departure Time: ")
            route = input("Route: ")
            bus_lookup.add_bus(bus_id, dep_time, route)
        elif choice == "14":
            bus_id = input("Bus ID to find: ")
            bus_lookup.find_bus(bus_id)
        elif choice == "15":
            bus_lookup.display_all_buses()
        elif choice == "0":
            print("Exiting CLI. Bye!")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()