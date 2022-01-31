# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """ 
        p=l1;
        i=1
        # print("val1={}".format(p.val))
        q=l2;
        # print("val2={}".format(q.val))
        sum=l1.val+l2.val
        # print("sum={}".format(sum))
        carry=sum/10;
        # print("carry={}".format(carry))
        sum=sum%10
        # print("sum/10={}".format(sum))
        start=current=ListNode(sum)
        # print("outside Loop")
        # print("current.val={}".format(current.val))
        while(q!=None or p!=None):
           
            a=0 
            b=0
            if(p!=None):
                if(p.next!=None):
                    p=p.next
                else:
                    p=None
                
            if(p!=None):
                a=p.val;
                # print("val1={}".format(a))
                
            if(q!=None):
                if(q.next!=None):
                    q=q.next
                else:
                    q=None
            
            if(q!=None):
                b=q.val
                # print("val2={}".format(b))
                
            if(p==None and q==None):
                break
            s=a+b+carry
            # print("sum={}".format(sum))
            carry=s/10
            # print("carry={}".format(carry))
            s=s%10
            # print("sum/10={}".format(sum))
            i=i+1
            if(i>1):
                current.next=ListNode(floor(s))
                current=current.next
            # print("p={}".format(p.val))
            # print(q.val)
            
        if(floor(carry)>0):
            current.next=ListNode(floor(carry))             
            current=current.next
        return start