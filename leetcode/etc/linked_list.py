class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head

        while cur.next != None:
            cur = cur.next

        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0

        while cur.next != None:
            total += 1
            cur = cur.next

        return total

    def display(self):
        elems = []
        cur_node = self.head

        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)

        print(elems)

    def get(self, idx):
        if idx >= self.length():
            print("ERROR: 'GET' Index out of range!")
            return None

        cur_idx = 0
        cur_node = self.head

        while True:
            cur_node = cur_node.next

            if cur_idx == idx:
                return cur_node.data

            cur_idx += 1

    def erase(self, idx):
        if idx >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return
        cur_idx = 0
        cur_node = self.head

        while True:
            last_node = cur_node
            cur_node = cur_node.next

            if cur_idx == idx:
                last_node.next = cur_node.next
                return

            cur_idx += 1


my_list = LinkedList()


my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()
my_list.erase(1)
my_list.display()


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         init = Node("init")
#         self.head = init
#         self.tail = init

#         self.cur = None
#         self.length = 0

#     def __len__(self):
#         return self.length

#     def __str__(self):
#         cur = self.head
#         cur = cur.next
#         s = ""
#         for i in range(self.length):
#             s += f"{cur.data}, "
#             cur = cur.next

#         return f"[{s[:-2]}]"

#     def append(self, data):
#         new_node = Node(data)
#         self.tail.next = new_node
#         self.tail = new_node
#         self.length += 1


# l = LinkedList()
# l.append(10)
# l.append(20)
# l.append(30)
# l.append(40)
# l.append(50)
# l.append(15)
