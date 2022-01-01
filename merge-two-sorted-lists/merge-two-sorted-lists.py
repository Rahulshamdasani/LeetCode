# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, head1: ListNode, head2: ListNode) -> ListNode:
        if(head1 == None and head2 == None):
            return None
        elif(head1 == None):
            return head2
        elif(head2 == None):
            return head1
        
        if(head1.val <=head2.val):
            parent = head1
            head1 = head1.next
            parent.next = None
            
        else:
            parent = head2
            
            head2 = head2.next
            parent.next = None
            
        finalhead = parent

        while(head1!= None and head2!= None):
            # print("********")
            # print("1st ll",head1)
            # print("2nd ll",head2)
            # print("parent=",finalhead)
            if(head1.val<=head2.val):
                # print("appending 1st")
                parent.next = head1
                parent = head1
                head1 = head1.next
            
            else:
                # print("appending 2st")
                
                parent.next = head2
                parent = head2
                head2 = head2.next
            
        if(head1!=None):
            parent.next = head1
        elif(head2 != None):
            parent.next = head2
        
        return finalhead