# Last updated: 1/13/2026, 2:57:10 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        x=[]
        curr=head
        while curr!=None:
            x.append(curr.val)
            curr=curr.next
        
        s=''
        for num in x:
            s=s+str(num)
        
        t=int(s,2)
        return(t)
             
        