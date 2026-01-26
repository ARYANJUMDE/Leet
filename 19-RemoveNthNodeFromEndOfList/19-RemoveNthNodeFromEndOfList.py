# Last updated: 1/26/2026, 11:28:44 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        count=0
        curr=head
        while curr!=None:
            count=count+1
            curr=curr.next
        if head==None:
            return None
        if n==count:
            return head.next  
        
        else:
            
            pos=count-n+1
            i=1
            curr2=head
            while(i!=pos-1 and curr2.next!=None):
                curr2=curr2.next
                i=i+1
            curr2.next=curr2.next.next
            return head


        