class Solution(object):

    #I like this better and it's faster
    #Runtime: O(N)
    #Space: O(N)
    def addTwoNumbers(self, l1, l2):

        #get number from the whole linked list
        def getTotal(l):
            total = 0
            x = 0
            while l:
                total+=l.val*(10**x)
                x+=1
                l = l.next
            return total
        
        total = getTotal(l1)+getTotal(l2)

        #put the number back into linked list
        num_string = str(total)[::-1]
        pre = ListNode(None)
        curr = pre
        
        for n in num_string:
            curr.next = ListNode(int(n))
            curr = curr.next
            
        return pre.next


    #This solution is like adding two numbers in paper
    #Runtime: O(N)
    #Space: O(N)
    def addTwoNumbers(self, l1, l2):
        pre = ListNode(None)
        curr = pre

        #carry is either 0 or 1
        #because the max value of l1 and l2 is 18, for example
        #3+4=7, 7 has only one digit, so carry is 0, we put 7 in the node
        #8+7=15, 15 has two digits, so carry is 1, we put 5 in the node
        #we take carry into the next round calculation
        carry = 0

        while l1 or l2:
            total = carry
            
            if l1:
                total+=l1.val
                l1 = l1.next
            if l2:
                total+=l2.val
                l2 = l2.next
                
            if total>=10:
                carry=1
                curr.next = ListNode(total%10)
            else:
                carry = 0
                curr.next = ListNode(total)
            
            curr = curr.next
        
        #check if there is carry left behind, for example
        #[5]+[5]=[0,1]
        #both linked list are done iterate, but still haven't finish adding
        if carry!=0:
            curr.next = ListNode(carry)
            
        return pre.next