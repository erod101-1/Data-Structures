# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution_Brute_Force:
    def get_ll_size(self,head: Optional[ListNode])-> int:
        cnt = 0
        while head != None:
            head = head.next
            cnt += 1
        return cnt
    def find_twin_node(self,i,n):
        return n - 1 - i
    def get_twin_sum(self,head: Optional[ListNode],i,n):
        twin_node_pos = self.find_twin_node(i,n)
        curr_val = head.val
        cnt = 0
        while head != None and cnt < twin_node_pos - i:
            head = head.next
            cnt += 1
        return curr_val + head.val
            
    def pairSum(self, head: Optional[ListNode]) -> int:
        ll_size = self.get_ll_size(head)
        curr_node_pos = 0
        sum = 0
        while head != None and curr_node_pos < ll_size // 2:
            csum = self.get_twin_sum(head,curr_node_pos,ll_size)
            sum = csum if csum > sum else sum
            curr_node_pos += 1
            head = head.next
        return sum
    
class Solution:
    def get_ll_size(self,head: Optional[ListNode])-> int:
        cnt = 0
        while head != None:
            head = head.next
            cnt += 1
        return cnt
    def split_ll_at_mid(self,head: Optional[ListNode],size)-> Optional[ListNode]:
        cnt = 0
        while head != None and cnt < size // 2:
            head = head.next
            cnt += 1
        return head
    def reverse_ll(self,head: Optional[ListNode])-> Optional[ListNode]:
        prev = None
        curr = head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr 
            curr = next
        return prev
    def pairSum(self, head: Optional[ListNode]) -> int:
        size = self.get_ll_size(head)
        split_ll = self.split_ll_at_mid(head,size)
        split_rev_ll = self.reverse_ll(split_ll)
        sum = 0
        while head != None and split_rev_ll != None:
            sum = head.val + split_rev_ll.val if head.val + split_rev_ll.val > sum else sum
            head = head.next
            split_rev_ll = split_rev_ll.next
        return sum

print(Solution().pairSum(ListNode(4,ListNode(2,ListNode(2,ListNode(3))))))