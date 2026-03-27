# ==============================
# TASK 1: Dynamic Array
# ==============================

class DynamicArray:
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.size = 0
        self.arr = [None] * self.capacity

    def append(self, x):
        if self.size == self.capacity:
            self._resize()
        self.arr[self.size] = x
        self.size += 1

    def _resize(self):
        print(f"Resizing from {self.capacity} to {self.capacity * 2}")
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def pop(self):
        if self.size == 0:
            print("Array is empty")
            return None
        val = self.arr[self.size - 1]
        self.arr[self.size - 1] = None
        self.size -= 1
        return val

    def __str__(self):
        return str([self.arr[i] for i in range(self.size)])


# ==============================
# NODE CLASS
# ==============================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# ==============================
# TASK 2: Singly Linked List
# ==============================

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_value(self, x):
        temp = self.head
        prev = None

        while temp:
            if temp.data == x:
                if prev:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return
            prev = temp
            temp = temp.next

        print("Value not found")

    def traverse(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        print(result)


# ==============================
# Doubly Linked List
# ==============================

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def insert_after(self, target, x):
        temp = self.head
        while temp:
            if temp.data == target:
                new_node = Node(x)
                new_node.next = temp.next
                new_node.prev = temp

                if temp.next:
                    temp.next.prev = new_node

                temp.next = new_node
                return
            temp = temp.next
        print("Target not found")

    def delete_at_position(self, pos):  # 0-based
        if not self.head:
            print("List empty")
            return

        temp = self.head

        if pos == 0:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return

        for _ in range(pos):
            if not temp:
                print("Position out of range")
                return
            temp = temp.next

        if not temp:
            print("Position out of range")
            return

        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

    def traverse(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        print(result)


# ==============================
# TASK 3: Stack using SLL
# ==============================

class Stack:
    def __init__(self):
        self.head = None

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            print("Stack Underflow")
            return None
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        if not self.head:
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None


# ==============================
# Queue using SLL
# ==============================

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, x):
        new_node = Node(x)
        if not self.tail:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.head:
            print("Queue Underflow")
            return None
        val = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return val

    def front(self):
        if not self.head:
            return None
        return self.head.data


# ==============================
# TASK 4: Parentheses Checker
# ==============================

def is_balanced(expr):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.push(ch)
        elif ch in ")}]":
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False

    return stack.is_empty()


# ==============================
# MAIN TEST RUNNER
# ==============================

if __name__ == "__main__":

    print("\n===== TASK 1: Dynamic Array =====")
    da = DynamicArray(2)
    for i in range(10):
        da.append(i)
        print(da)

    print("Pop:", da.pop())
    print("Pop:", da.pop())
    print("Pop:", da.pop())
    print("After pops:", da)

    print("\n===== TASK 2: Singly Linked List =====")
    sll = SinglyLinkedList()
    sll.insert_beginning(1)
    sll.insert_beginning(2)
    sll.insert_beginning(3)
    sll.traverse()

    sll.insert_end(4)
    sll.insert_end(5)
    sll.insert_end(6)
    sll.traverse()

    sll.delete_value(4)
    sll.traverse()

    print("\n===== Doubly Linked List =====")
    dll = DoublyLinkedList()
    dll.insert_end(1)
    dll.insert_end(2)
    dll.insert_end(3)
    dll.insert_after(2, 99)
    dll.traverse()

    dll.delete_at_position(1)
    dll.traverse()

    dll.delete_at_position(2)
    dll.traverse()

    print("\n===== TASK 3: Stack =====")
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)
    print("Peek:", st.peek())
    print("Pop:", st.pop())
    print("Pop:", st.pop())

    print("\n===== Queue =====")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Front:", q.front())
    print("Dequeue:", q.dequeue())
    print("Dequeue:", q.dequeue())

    print("\n===== TASK 4: Parentheses Checker =====")
    tests = ["([])", "([)]", "(((", ""]
    for t in tests:
        print(f"{t} ->", is_balanced(t))