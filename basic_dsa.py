"""Basic DSA Problems: Units I - III (20 problems, Python).
Each solution lists time (T) and space (S) complexity.
Run `python basic_dsa.py` to execute all tests.
"""

# ---------------- RECURSION ----------------

# 1. Print 1 to N.  T: O(n)  S: O(n) call stack
def print_1_to_n(n):
    if n == 0:                 # base case
        return
    print_1_to_n(n - 1)        # print smaller numbers first
    print(n, end=" ")          # then print n (on the way back)


# 2. Factorial.  T: O(n)  S: O(n)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# 3. Fibonacci (memoized).  T: O(n)  S: O(n)
def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


# 4. Sum of digits.  T: O(d)  S: O(d), d = number of digits
def sum_of_digits(n):
    n = abs(n)
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)


# 5. Power x^n (fast exponentiation).  T: O(log n)  S: O(log n)
def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    half = power(x, n // 2)
    return half * half if n % 2 == 0 else half * half * x


# 6. Is array sorted (recursion).  T: O(n)  S: O(n)
def is_sorted(arr, i=0):
    if i >= len(arr) - 1:
        return True
    if arr[i] > arr[i + 1]:
        return False
    return is_sorted(arr, i + 1)


# 7. All subsequences (include / exclude).  T: O(n * 2^n)  S: O(n)
def subsequences(s, idx=0, cur="", out=None):
    if out is None:
        out = []
    if idx == len(s):
        out.append(cur)
        return out
    subsequences(s, idx + 1, cur + s[idx], out)   # include
    subsequences(s, idx + 1, cur, out)            # exclude
    return out


# 8. Tower of Hanoi.  T: O(2^n)  S: O(n)
def hanoi(n, src="A", aux="B", dst="C", moves=None):
    if moves is None:
        moves = []
    if n == 0:
        return moves
    hanoi(n - 1, src, dst, aux, moves)            # move n-1 to aux
    moves.append((src, dst))                      # move disk n
    hanoi(n - 1, aux, src, dst, moves)            # move n-1 to dst
    return moves


# 9. All permutations (backtracking).  T: O(n * n!)  S: O(n)
def permutations(s):
    out, used, cur = [], [False] * len(s), []

    def backtrack():
        if len(cur) == len(s):
            out.append("".join(cur))
            return
        for i in range(len(s)):
            if not used[i]:
                used[i] = True; cur.append(s[i])  # choose
                backtrack()                       # explore
                cur.pop(); used[i] = False        # un-choose

    backtrack()
    return out


# 10. Subset sum.  T: O(2^n)  S: O(n)
def subset_sum(arr, target, i=0):
    if target == 0:
        return True
    if i == len(arr) or target < 0:
        return False
    return subset_sum(arr, target - arr[i], i + 1) or subset_sum(arr, target, i + 1)


# ---------------- SEARCHING (sorted arrays) ----------------

def _first(arr, x):
    lo, hi, res = 0, len(arr) - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            res = mid; hi = mid - 1               # keep looking left
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return res


def _last(arr, x):
    lo, hi, res = 0, len(arr) - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            res = mid; lo = mid + 1               # keep looking right
        elif arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return res


# 11. First and last occurrence.  T: O(log n)  S: O(1)
def first_last(arr, x):
    return _first(arr, x), _last(arr, x)


# 12. Count occurrences.  T: O(log n)  S: O(1)
def count_occurrences(arr, x):
    f, l = first_last(arr, x)
    return 0 if f == -1 else l - f + 1


# 13. Floor and ceil.  T: O(log n)  S: O(1)
def floor_ceil(arr, x):
    lo, hi, floor, ceil = 0, len(arr) - 1, None, None
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            return x, x
        if arr[mid] < x:
            floor = arr[mid]; lo = mid + 1
        else:
            ceil = arr[mid]; hi = mid - 1
    return floor, ceil


# 14. Search insert position.  T: O(log n)  S: O(1)
def search_insert(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


# ---------------- SORTING ----------------

# 15. Merge two sorted arrays (two pointers).  T: O(n+m)  S: O(n+m)
def merge_sorted(a, b):
    i = j = 0
    res = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i]); i += 1
        else:
            res.append(b[j]); j += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res


# ---------------- STACKS ----------------

# 16. Valid parentheses.  T: O(n)  S: O(n)
def is_valid_parentheses(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


# 17. Next greater element (monotonic stack).  T: O(n)  S: O(n)
def next_greater(arr):
    res, stack = [-1] * len(arr), []
    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(arr[i])
    return res


# 18. Min stack: every op O(1), S: O(n)
class MinStack:
    def __init__(self):
        self.stack = []                            # (value, min so far)

    def push(self, val):
        m = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, m))

    def pop(self):
        return self.stack.pop()[0]

    def top(self):
        return self.stack[-1][0]

    def get_min(self):
        return self.stack[-1][1]


# 19. Reverse a stack using recursion.  T: O(n^2)  S: O(n)
def _insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    top = stack.pop()
    _insert_at_bottom(stack, item)
    stack.append(top)


def reverse_stack(stack):
    if not stack:
        return
    top = stack.pop()
    reverse_stack(stack)
    _insert_at_bottom(stack, top)


# ---------------- LINKED LIST ----------------

class Node:
    def __init__(self, val, next=None):
        self.val, self.next = val, next


# 20. Remove duplicates from sorted linked list.  T: O(n)  S: O(1)
def remove_duplicates(head):
    cur = head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next               # skip duplicate
        else:
            cur = cur.next
    return head


def build_list(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.val); head = head.next
    return out


# ---------------- TESTS ----------------
if __name__ == "__main__":
    print_1_to_n(5); print()
    assert factorial(5) == 120 and factorial(0) == 1
    assert [fibonacci(i) for i in range(8)] == [0, 1, 1, 2, 3, 5, 8, 13]
    assert sum_of_digits(1234) == 10
    assert power(2, 10) == 1024 and power(2, -2) == 0.25
    assert is_sorted([1, 2, 3]) and not is_sorted([1, 3, 2])
    assert sorted(subsequences("abc")) == sorted(["abc", "ab", "ac", "a", "bc", "b", "c", ""])
    assert len(hanoi(3)) == 7
    assert sorted(permutations("abc")) == ["abc", "acb", "bac", "bca", "cab", "cba"]
    assert subset_sum([3, 34, 4, 12, 5, 2], 9) and not subset_sum([3, 34, 4], 100)
    a = [1, 2, 2, 2, 3, 5]
    assert first_last(a, 2) == (1, 3) and first_last(a, 4) == (-1, -1)
    assert count_occurrences(a, 2) == 3 and count_occurrences(a, 9) == 0
    assert floor_ceil([1, 2, 8, 10], 5) == (2, 8) and floor_ceil([1, 2], 0) == (None, 1)
    assert [search_insert([1, 3, 5, 6], x) for x in (5, 2, 7, 0)] == [2, 1, 4, 0]
    assert merge_sorted([1, 4, 7], [2, 3, 9, 10]) == [1, 2, 3, 4, 7, 9, 10]
    assert is_valid_parentheses("{[()]}") and not is_valid_parentheses("([)]")
    assert next_greater([4, 5, 2, 25]) == [5, 25, 25, -1]
    ms = MinStack()
    for v in (5, 3, 7, 2):
        ms.push(v)
    assert ms.get_min() == 2
    ms.pop(); ms.pop()
    assert ms.get_min() == 3 and ms.top() == 3
    st = [1, 2, 3, 4]; reverse_stack(st)
    assert st == [4, 3, 2, 1]
    assert to_list(remove_duplicates(build_list([1, 1, 2, 3, 3, 3]))) == [1, 2, 3]
    print("All 20 problems passed.")
