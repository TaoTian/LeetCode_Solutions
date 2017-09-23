# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow.next, slow = None, slow.next

        prev, cur = None, slow
        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        tmp_f, tmp_s = head, prev
        while tmp_f and tmp_s:
            nex_f, nex_s = tmp_f.next, tmp_s.next
            tmp_f.next, tmp_s.next = tmp_s, nex_f
            tmp_f, tmp_s = nex_f, nex_s
        
if __name__ == '__main__':
    print_list(Solution().reorderList(build_list([1,2,3,4])))
