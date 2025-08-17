class Customer:
    def __init__(self, customer_id, name, email, phone, from_, to, bus_no, departure_time):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.from_ = from_
        self.to = to
        self.departure_time = departure_time
        self.bus_no = bus_no

    def __str__(self):
        return (f"🆔 ID: {self.customer_id} | 👤 Name: {self.name} | "
                f"📧 Email: {self.email} | 📱 Phone: {self.phone} | "
                f"📍 From: {self.from_} | 📍 To: {self.to}| "
                f"🚌 Bus NO: {self.bus_no} | 🕒 Departure Time {self.departure_time} "
                )


class CustomerNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class CustomerLinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = CustomerNode(value)
        if self.head == None:
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node

    def view(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next

    def search(self, id):
        curr = self.head
        while curr is not None:
            if curr.data.customer_id == id:
                print(curr.data)
                return
            curr = curr.next
        else:
            return "Not Found "

    def delete(self, id):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data.customer_id == id:
            self.head = self.head.next
            print(f"Deleted customer with ID {id}")
            return

        curr = self.head
        prev = None
        while curr is not None:
            if curr.data.customer_id == id:
                prev.next = curr.next
                print(f"Deleted customer with ID {id}")
                return
            prev = curr
            curr = curr.next

        print("Not Found")

    def update(self, id, data):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data.customer_id == id:
            self.head.data = data
            print("✅ Customer updated (Head Node)")
            return

        curr = self.head
        while curr is not None:
            if curr.data.customer_id == id:
                curr.data = data
                print("✅ Customer updated")
                return
            curr = curr.next

        print("❌ Not Found")

    def count(self):
        if self.head is None:
            print("List is empty")
            return 0

        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.next

        print(f"📦 Total Customers: {count}")
        return count



