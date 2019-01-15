#https://leetcode.com/problems/fruit-into-type_baskets/

class Solution(object):
    #Time Efficiency: O(N), where N is the fruit count in the trees.
    #Space Efficiency: O(K), where K is the total types of fruit in the trees.
    def totalFruit(self, tree):
        counter = 0 #max fruit count
        start = 0 #the point where from start to i has only two types of fruit
        mark = {} #we keep track of each type of fruit's index last seen
        type_basket = [] #types of fruit in the basket now

        for i in range(len(tree)):
            t = tree[i]
            if t not in type_basket:
                if len(type_basket)<2:
                    """
                    if this type of fruit not in type_basket
                    and the type_basket is not full yet
                    add the type to the type_basket
                    """
                    type_basket.append(t)

                elif len(type_basket)==2:
                    """
                    if this type of fruit not in type_basket
                    and the type_basket has two types already
                    we get rid of the type with smaller last seen index
                    by moving the start to its index+1
                    so now between start and i has only two types of fruit
                    """
                    t1 = type_basket[0]
                    t2 = type_basket[1]
                    if mark[t1]<mark[t2]:
                        start = mark[t1]+1
                        type_basket[0] = t
                    else:
                        start = mark[t2]+1
                        type_basket[1] = t
                else:
                    #basket should not have more than two types
                    print('ERROR')
                    return 0
            
            counter = max(counter, i-start+1)
            mark[t] = i
        return counter
