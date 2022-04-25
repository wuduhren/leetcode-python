#2019/11/17 Update
"""
Add numbers, units to units digit, tens to tens digit...
If the added number is greater than 9
We will add 1 to next digit (`temp`) and only take the units digit of the added value.

For example, if we are adding units digits, 3 and 9, the sum is 12.
12 is greater than the 9, so we set `temp` to 1, so when we are calculating tens digits it will `+1`.
And we only take the units digit of 12, which is `12 - 10 = 2`.

The time complexity is O(N), N is the length of two linked list.
Space complexity is O(N), since we need to store a new linked list.
"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        temp = 0
        pre_head = ListNode(-1)
        curr = pre_head
        while l1 or l2 or temp:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + temp

            if val>=10:
                temp = 1
                val = val-10
            else:
                temp = 0

            curr.next = ListNode(val)

            if l1: l1 = l1.next
            if l2: l2 = l2.next
            curr = curr.next
        return pre_head.next


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
