class Node:
    def __init__(self, device_type: str, mark: str, measurement_limit: float, release_year: int):
        self.device_type = device_type
        self.mark = mark
        self.measurement_limit = measurement_limit
        self.release_year = release_year
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = Node(None, None, 0, 0)
        self.next = Node(None, None, 0, 0)
        self.tail = Node(None, None, 0, 0)
        self.head.next = self.tail
        self.tail.next = self.head

    def sort_list_by_release_year(self):
        curr = self.head
        if self.head is None:
            print("The list is empty")
        else:
            while True:
                index_val = curr.next
                while index_val != self.head:
                    if curr.release_year > index_val.release_year:
                        temp = curr.release_year
                        curr.release_year = index_val.release_year
                        index_val.release_year = temp
                    index_val = index_val.next
                curr = curr.next
                if curr.next == self.head:
                    break

    def add_data_by_year_acs(self, device_type, mark, measurement_limit, release_year):
        self.sort_list_by_release_year()
        ptr_1 = Node(device_type, mark, measurement_limit, release_year)
        temp = self.head
        ptr_1.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                while True:
                    if temp.release_year < release_year:
                        self.push_back(device_type, mark, measurement_limit, release_year)
            temp.next = ptr_1
        else:
            ptr_1.next = ptr_1
        self.head = ptr_1

    def search_devices_with_specific_measurement_limit(self, specific_measurement_limit: float):
        curr = self.head
        i = 1
        flag_val = False
        if self.head is None:
            print("The list is empty")
        else:
            while True:
                if curr.measurement_limit == specific_measurement_limit:
                    flag_val = True
                    print(f"The element with measurement limit {specific_measurement_limit}"
                          f" is present in list at position : {str(i)}, "
                          f"element`s type : {curr.device_type}")

                curr = curr.next
                i += 1
                if curr == self.head:
                    break

            if not flag_val:
                print("The element is not present in list")

    def push_back(self, device_type: str, mark: str, measurement_limit: float, release_year: int):
        ptr_1 = Node(device_type, mark, measurement_limit, release_year)
        temp = self.head
        ptr_1.next = self.head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = ptr_1
        else:
            ptr_1.next = ptr_1
        self.head = ptr_1

    def pop_back(self):
        if self.head is None:
            return
        else:
            if self.head != self.tail:
                curr = self.head
                while curr.next != self.tail:
                    curr = curr.next
                popped = self.tail
                self.tail = curr
                self.tail.next = self.head
                return popped
            else:
                self.head = self.tail = None

    def print_ll(self):
        temp = self.head
        if self.head is not None:
            while True:
                print(f"Device type:{temp.device_type}, device relase year: {temp.release_year}, "
                      f"device mark: {temp.mark}, device measurement_limit {temp.measurement_limit}")
                temp = temp.next
                if temp == self.head:
                    break


my_ll = CircularLinkedList()

my_ll.push_back("First", "Voltage Gen", 1, 2020)
my_ll.push_back("First", "Current Gen", 0.5, 2022)
my_ll.push_back("Second", "Voltage-1", 1.3, 2017)
my_ll.push_back("Second", "Current-1", 0.5, 2021)
my_ll.search_devices_with_specific_measurement_limit(0.5)
print("==================================")
my_ll.print_ll()
print("==================================")
my_ll.sort_list_by_release_year()
my_ll.print_ll()


my_ll.add_data_by_year_acs("spec", "S2", 0.1, 2010)
