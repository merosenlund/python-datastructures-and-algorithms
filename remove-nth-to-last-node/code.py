# Given a linked list and a value n, remove the nth to last node and return the resulting list.

# Ex: Given the following linked lists...

# 1->2->3->null, n = 1, return 1->2->null
# 1->2->3->null, n = 2, return 1->3->null
# 1->2->3->null, n = 3, return 2->3->null

# I only have 11 minutes left for this problem so let's see how far I can get!

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third
