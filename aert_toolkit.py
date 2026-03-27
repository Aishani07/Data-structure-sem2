# Algorithmic Efficiency & Recursion Toolkit (AERT)

# -----------------------------
# Part A: Stack ADT
# -----------------------------

class StackADT:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# -----------------------------
# Part B: Factorial
# -----------------------------

def factorial(n):
    if n < 0:
        return "Invalid input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


# -----------------------------
# Fibonacci (Naive)
# -----------------------------

naive_calls = 0

def fib_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)


# -----------------------------
# Fibonacci (Memoization)
# -----------------------------

memo_calls = 0

def fib_memo(n, memo={}):
    global memo_calls
    memo_calls += 1

    if n in memo:
        return memo[n]

    if n <= 1:
        memo[n] = n
        return n

    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


# -----------------------------
# Part C: Tower of Hanoi
# -----------------------------

def hanoi(n, source, auxiliary, destination, stack):
    if n == 1:
        move = f"Move disk 1 from {source} to {destination}"
        stack.push(move)
        print(move)
        return

    hanoi(n-1, source, destination, auxiliary, stack)

    move = f"Move disk {n} from {source} to {destination}"
    stack.push(move)
    print(move)

    hanoi(n-1, auxiliary, source, destination, stack)


# -----------------------------
# Part D: Recursive Binary Search
# -----------------------------

def binary_search(arr, key, low, high, stack):

    if low > high:
        return -1

    mid = (low + high) // 2
    stack.push(mid)

    if arr[mid] == key:
        return mid

    elif key < arr[mid]:
        return binary_search(arr, key, low, mid-1, stack)

    else:
        return binary_search(arr, key, mid+1, high, stack)


# -----------------------------
# MAIN FUNCTION
# -----------------------------

def main():

    print("\n----- FACTORIAL TESTS -----")
    fact_tests = [0,1,5,10]

    for n in fact_tests:
        print(f"factorial({n}) =", factorial(n))


    print("\n----- FIBONACCI TESTS -----")
    fib_tests = [5,10,20,30]

    for n in fib_tests:
        global naive_calls, memo_calls

        naive_calls = 0
        memo_calls = 0

        naive_result = fib_naive(n)
        memo_result = fib_memo(n)

        print(f"\nFibonacci n={n}")
        print("Naive Result:", naive_result)
        print("Naive Calls:", naive_calls)

        print("Memoized Result:", memo_result)
        print("Memoized Calls:", memo_calls)


    print("\n----- TOWER OF HANOI (N=3) -----")

    stack = StackADT()
    hanoi(3, 'A', 'B', 'C', stack)

    print("\nTotal Moves:", stack.size())


    print("\n----- BINARY SEARCH TESTS -----")

    arr = [1,3,5,7,9,11,13]
    searches = [7,1,13,2]

    for key in searches:
        stack = StackADT()
        index = binary_search(arr, key, 0, len(arr)-1, stack)

        print("\nSearching:", key)
        print("Index:", index)
        print("Mid indices visited:", stack.items)


    print("\nEmpty Array Test")

    arr = []
    stack = StackADT()
    result = binary_search(arr, 5, 0, len(arr)-1, stack)
    print("Result:", result)


if __name__ == "__main__":
    main()