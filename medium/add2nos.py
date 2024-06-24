# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit1 = []
        digit2 = []

        while l1 is not None:
            digit1.append(l1.val)
            l1 = l1.next

        while l2 is not None:
            digit2.append(l2.val)
            l2 = l2.next

        digit1_int = int(''.join([str(i) for i in digit1[::-1]]))
        digit2_int = int(''.join([str(i) for i in digit2[::-1]]))
        sum_digit = digit1_int + digit2_int

        if sum_digit == 0:
            return ListNode(0, None)

        link_sum = None
        while sum_digit != 0:
            remainder = sum_digit % 10
            sum_digit = sum_digit//10
            if link_sum:
                last_element = link_sum
                while last_element.next is not None:
                    last_element = last_element.next
                last_element.next = ListNode(remainder, None)
            else:
                link_sum = ListNode(remainder, None)

        return link_sum


l1 = ListNode(3)
l2 = ListNode(4, l1)
l3 = ListNode(2, l2)


l7 = ListNode(4)
l8 = ListNode(6, l7)
l9 = ListNode(5, l8)

s = Solution()
link_sum = s.addTwoNumbers(l3, l9)
# link_sum = s.addTwoNumbers(ListNode(0), ListNode(0))

sum = []
while link_sum is not None:
    sum.append(link_sum.val)
    link_sum = link_sum.next
print(sum)
