"""
This problem is better using BFS. Because we need to find the shortest step.
Using DFS, we may eventually find the `endWord` but not the shortest path.

First, build a memo so that we can find the related word without going through a~z every time we pop out a new word from queue.
So for example
```
wordList = ["hot","dot","dog","lot","log","cog"]

memo = {
    'lo#': ['lot', 'log'],
    'l#t': ['lot'],
    '#ot': ['hot', 'dot', 'lot'],
    'h#t': ['hot'],
    'do#': ['dot', 'dog'],
    'l#g': ['log'],
    'co#': ['cog'],
    '#og': ['dog', 'log', 'cog'],
    'd#g': ['dog'],
    'd#t': ['dot'],
    'c#g': ['cog'],
    'ho#': ['hot']
}
```

Second build a queue to BFS from `beginWord` to `endWord`.
Everytime we pop a word we first check if it is visited.
Then check if it is `endWord`, if true, return the steps.
If not, put all the neighbor to the queue.

If the queue ended and we did not find the `endWord`, return 0.

The time complexity is O(W*C), W is the word count, C is the character count in each word.
The space complexity is also O(W*C).
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        memo = collections.defaultdict(list)
        for word in wordList:
            for i in xrange(len(word)):
                memo[word[:i]+'#'+word[i+1:]].append(word)

        seen = set()
        q = collections.deque([(beginWord, 1)])
        while q:
            word, steps = q.popleft()
            if word==endWord: return steps
            seen.add(word)

            for i in xrange(len(word)):
                for next_word in memo[word[:i]+'#'+word[i+1:]]:
                    if next_word not in seen:
                        q.append((next_word, steps+1))
        return 0

"""
When comparing to other solution, I made some changes.
Which is the timing of adding the word to the `visited` hash-set.
I think by adding the word to the hash-set in the for loop, makes the queue smaller, so it would be slightly faster.
But the time complexity is totally the same.
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        memo = collections.defaultdict(list)
        for word in wordList:
            for i in xrange(len(word)):
                memo[word[:i]+'#'+word[i+1:]].append(word)

        seen = set()
        q = collections.deque([(beginWord, 1)])
        while q:
            word, steps = q.popleft()
            if word==endWord: return steps

            for i in xrange(len(word)):
                for next_word in memo[word[:i]+'#'+word[i+1:]]:
                    if next_word not in seen:
                        q.append((next_word, steps+1))
                        seen.add(next_word)
        return 0

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList = set(wordList)
        seen = set()
        q = collections.deque([(beginWord, 1)])
        while q:
            word, steps = q.popleft()
            if word==endWord: return steps

            for i in xrange(len(word)):
                for alphabet in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i]+alphabet+word[i+1:]
                    if next_word not in seen and next_word in wordList:
                        q.append((next_word, steps+1))
                        seen.add(next_word)
        return 0
