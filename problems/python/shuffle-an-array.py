class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):

    def __init__(self, nums):
        self.nums = nums
        self.curr = self.getLinkList(self.nums)
    
    def reset(self):
        return self.nums
    
	#O(N^2) in time.
    def shuffle(self):
        ans = []
        
        #new LinkList
        head = None
        curr = head
                
        while len(ans)<len(self.nums):
            #each time remove a random node
            #add the val to ans
            #and add the node to the newLinkList
            
            #select a random node, self.curr
            rand = randrange(len(self.nums)-len(ans))
            while rand>0:
                self.curr = self.curr.next
                rand -= 1
            
            #add self.curr.next's value to ans
            ans.append(self.curr.next.val)
            
            #add self.curr.next to a new LinkList
            if not curr:
                head = self.curr.next
                curr = head
            else:
                curr.next = self.curr.next
                curr = curr.next
            
            #remove self.curr.next from the LinkList
            self.curr.next = self.curr.next.next
            
        curr.next = head
        self.curr = head
        return ans

    def getLinkList(self, nums):
        head = ListNode(nums[0])
        curr = head
        for i in xrange(1, len(self.nums)):
            curr.next = ListNode(nums[i])
            curr = curr.next
        curr.next = head
        return head