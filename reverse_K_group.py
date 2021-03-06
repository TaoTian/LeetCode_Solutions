"""
这是我最近写的代码，作为目前的demo使用，之后会把可以放上来的project代码放上来demo。
"""

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/Data_Structure')

from LinkedList import *
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        len_l, tmp = 0, head
        while tmp:
            len_l += 1
            tmp = tmp.next

        dummy_head, dummy_head.next = ListNode(0), head
        prev_tail, prev_n, cur =dummy_head, dummy_head, head
        while len_l >= k:
            for i in xrange(k):
                cur.next, prev_n, cur = prev_n, cur, cur.next
            prev_tail.next.next, prev_tail.next, prev_tail = cur, prev_n, prev_tail.next
            len_l -= k
        return dummy_head.next

if __name__ == '__main__':
    print_list(Solution().reverseKGroup(build_list([1, 2, 3, 4]), 2))