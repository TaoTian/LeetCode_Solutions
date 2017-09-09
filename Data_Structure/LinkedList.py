# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list(head):
    if not head:
        return

    out = ''
    while head:
        out += `head.val` + '->'
        head = head.next
    print out[:len(out) - 2]

def build_list(arr):
    dummy = ListNode(0)
    prev = dummy
    for i in xrange(len(arr)):
        prev.next = prev = ListNode(arr[i])
    return dummy.next