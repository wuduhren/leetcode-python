class Solution(object):
    def swapPairs(self, head):
        pre_head = ListNode(-1)
        curr = head
        prev = pre_head

        if not curr or not curr.next: return head

        while curr and curr.next:
            temp_next = curr.next.next

            prev.next = curr.next
            curr.next.next = curr
            curr.next = temp_next

            prev = curr
            curr = temp_next

        return pre_head.next


from collections import deque
class Solution(object):
    def swapPairs(self, head):
        curr = head
        q1 = deque([])
        q2 = deque([])
        seq = 0
        while curr:
            if seq%2==0:
                q2.append(curr)
            else:
                q1.append(curr)

            temp = curr.next
            curr.next = None #clear old link
            curr = temp
            seq+=1

        if seq==1:
            return head

        use_q1 = True
        pre_head = ListNode(-1)
        curr = pre_head
        while q1 or q2:
            if use_q1:
                if not q1: break
                curr.next = q1.popleft()
            else:
                curr.next = q2.popleft()
            curr = curr.next
            use_q1 = not use_q1

        if q2: curr.next = q2.popleft() #odd length of linked list

        return pre_head.next
