# Last updated: 1/26/2026, 11:28:35 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        x=[]
        curr=head
        while curr!=None:
            if curr.val not in x:
                x.append(curr.val)
                
            curr=curr.next
        dummy=ListNode(0)
        temp=dummy

        for num in x:
            temp.next=ListNode(num)
            temp=temp.next
        return dummy.next



        