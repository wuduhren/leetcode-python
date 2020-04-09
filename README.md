# Overview
1. This is my Python (2.7) Leetcode solution.
As time grows, this also become a guide to prepare for software engineer interview.

2. I really take time tried to make the best solution and collect the best resource that I found.  
Because I wanted to help others like me. 
If you like my answer, a star on GitHub means a lot to me. 
https://github.com/wuduhren/leetcode-python  

3. The solution is at `problems/the-file-name/`.
For example, `merge-sorted-array.py`'s solution is at `https://leetcode.com/problems/merge-sorted-array/`.


# Leetcode Similar Problems
I found it makes sense to solve similar problems together, so that we can recognize the problem faster when we encounter a new one. My suggestion is to skip the HARD problems when you first go through these list.

### Two Pointers
|  Id | Name | Difficulty | Comments |
| ---: | --- | :---: | --- |
|  11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/ "Container With Most Water") | ★★ |  |
|  167 | [Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted "Two Sum II - Input array is sorted") | ★★ |  |
|  977 | [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array "Squares of a Sorted Array") | ★★ | merge sort |

### Recursion
|  Id | Name | Difficulty |  |  |
| ---: | --- | :---: | :---: | --- |
|  726 | [Number of Atoms](https://leetcode.com/problems/number-of-atoms "Number of Atoms") | ★★★ | [736](https://leetcode.com/problems/parse-lisp-expression/ "736") | [394](https://leetcode.com/problems/decode-string/ "394") |
|  856 | [Score of Parentheses](https://leetcode.com/problems/score-of-parentheses/ "Score of Parentheses") | ★★★ |  |  |

### Divide and Conquer
|  Id | Name | Difficulty | Comments |
| ---: | --- | :---: | --- |
|  169 | [Majority Element](https://leetcode.com/problems/majority-element "Majority Element") | ★★ |  |
|  315 | [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/ "Count of Smaller Numbers After Self") | ★★★★ | merge sort / BIT |

### Search
|  Id | Name | Difficulty |  |  |  |  |  |  | Comments |
| ---: | --- | :---: | :---: | --- | --- | --- | --- | --- | --- |
|  17 | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number "Letter Combinations of a Phone Number") | ★★ | [39](https://leetcode.com/problems/combination-sum/ "39") | [40](https://leetcode.com/problems/combination-sum-ii/ "40") | [77](https://leetcode.com/problems/combinations/ "77") | [78](https://leetcode.com/problems/subsets/ "78") | [90](https://leetcode.com/problems/subsets-ii/ "90") | [216](https://leetcode.com/problems/combination-sum-iii/ "216") | Combination |
|  46 | [Permutations](https://leetcode.com/problems/permutations/ "Permutations") | ★★ | [47](https://leetcode.com/problems/permutations-ii/ "47") | [784](https://leetcode.com/problems/letter-case-permutation/ "784") | [943](https://leetcode.com/problems/find-the-shortest-superstring "943") | [996](https://leetcode.com/problems/number-of-squareful-arrays/ "996") |  |  | Permutation |
|  22 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/ "Generate Parentheses") | ★★★ | [301](https://leetcode.com/problems/remove-invalid-parentheses/ "301") |  |  |  |  |  | DFS |
|  37 | [Sudoku Solver](https://leetcode.com/problems/sudoku-solver "Sudoku Solver") | ★★★ | [51](https://leetcode.com/problems/n-queens "51") | [52](https://leetcode.com/problems/n-queens-ii "52") |  |  |  |  | DFS |
|  79 | [Word Search](https://leetcode.com/problems/word-search/ "Word Search") | ★★★ | [212](https://leetcode.com/problems/word-search-ii/ "212") |  |  |  |  |  | DFS |
|  127 | [Word Ladder](https://leetcode.com/problems/word-ladder/ "Word Ladder") | ★★★★ | [126](https://leetcode.com/problems/word-ladder-ii/ "126") | [752](https://leetcode.com/problems/open-the-lock/ "752") |  |  |  |  | BFS |
|  542 | [01 Matrix](https://leetcode.com/problems/01-matrix/ "01 Matrix") | ★★★ | [675](https://leetcode.com/problems/cut-off-trees-for-golf-event/ "675") | [934](https://leetcode.com/problems/shortest-bridge/ "934") |  |  |  |  | BFS |
|  698 | [Partition to K Equal Sum Subsets](https://leetcode.com/problems/partition-to-k-equal-sum-subsets "Partition to K Equal Sum Subsets") | ★★★ | [93](https://leetcode.com/problems/restore-ip-addresses/ "93") | [131](https://leetcode.com/problems/palindrome-partitioning/ "131") | [241](https://leetcode.com/problems/different-ways-to-add-parentheses/ "241") | [282](https://leetcode.com/problems/expression-add-operators/ "282") | [842](https://leetcode.com/problems/split-array-into-fibonacci-sequence/ "842") |  | Partition |

### Hash Table
|  Id | Name | Difficulty |  |
| ---: | --- | :---: | :---: |
|  1 | [Two Sum](https://leetcode.com/problems/two-sum/ "Two Sum") | ★★ | [560](https://leetcode.com/problems/subarray-sum-equals-k/ "560") |

### List
|  Id | Name | Difficulty |  | Comments |
| ---: | --- | :---: | :---: | --- |
|  2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/ "Add Two Numbers") | ★★ | [445](https://leetcode.com/problems/add-two-numbers-ii/ "445") |  |
|  24 | [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/ "Swap Nodes in Pairs") | ★★ |  |  |
|  206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/ "Reverse Linked List") | ★★ |  |  |
|  141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/ "Linked List Cycle") | ★★ | [142](https://leetcode.com/problems/linked-list-cycle-ii "142") | fast/slow |
|  23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/ "Merge k Sorted Lists") | ★★★ | [21](https://leetcode.com/problems/merge-two-sorted-lists/ "21") | priority_queue |
|  147 | [Insertion Sort List](https://leetcode.com/problems/insertion-sort-list/ "Insertion Sort List") | ★★★ |  | insertion sort |
|  148 | [Sort List](https://leetcode.com/problems/sort-list/ "Sort List") | ★★★★ |  | merge sort O(1) space |
|  707 | [Design Linked List](https://leetcode.com/problems/design-linked-list "Design Linked List") | ★★★★ |  |  |

### Tree
|  Id | Name | Difficulty |  |  |  |  |  |  | Comments |
| ---: | --- | :---: | :---: | --- | --- | --- | --- | --- | --- |
|  94 | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/ "Binary Tree Inorder Traversal") | ★ | [589](https://leetcode.com/problems/n-ary-tree-preorder-traversal "589") | [590](https://leetcode.com/problems/n-ary-tree-postorder-traversal "590") |  |  |  |  | traversal |
|  100 | [Same Tree](https://leetcode.com/problems/same-tree/ "Same Tree") | ★★ | [101](https://leetcode.com/problems/symmetric-tree/ "101") | [104](https://leetcode.com/problems/maximum-depth-of-binary-tree/ "104") | [110](https://leetcode.com/problems/balanced-binary-tree/ "110") | [111](https://leetcode.com/problems/minimum-depth-of-binary-tree "111") | [572](https://leetcode.com/problems/subtree-of-another-tree "572") | [965](https://leetcode.com/problems/univalued-binary-tree/ "965") |  |
|  102 | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/ "Binary Tree Level Order Traversal") | ★★ | [107](https://leetcode.com/problems/binary-tree-level-order-traversal-ii "107") | [429](https://leetcode.com/problems/n-ary-tree-level-order-traversal "429") | [872](https://leetcode.com/problems/leaf-similar-trees/ "872") | [987](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree "987") |  |  | collecting nodes |
|  814 | [Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/ "Binary Tree Pruning") | ★★ | [669](https://leetcode.com/problems/trim-a-binary-search-tree/ "669") |  |  |  |  |  |  |
|  112 | [Path Sum](https://leetcode.com/problems/path-sum/ "Path Sum") | ★★★ | [113](https://leetcode.com/problems/path-sum-ii "113") | [437](https://leetcode.com/problems/path-sum-iii "437") |  |  |  |  |  |
|  124 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/ "Binary Tree Maximum Path Sum") | ★★★ | [543](https://leetcode.com/problems/diameter-of-binary-tree/ "543") | [687](https://leetcode.com/problems/longest-univalue-path/ "687") |  |  |  |  | Use both children, return one |
|  129 | [Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/ "Sum Root to Leaf Numbers") | ★★★ | [257](https://leetcode.com/problems/binary-tree-paths/ "257") |  |  |  |  |  |  |
|  236 | [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/ "Lowest Common Ancestor of a Binary Tree") | ★★★ | [235](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree "235") |  |  |  |  |  |  |
|  297 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/ "Serialize and Deserialize Binary Tree") | ★★★ | [449](https://leetcode.com/problems/serialize-and-deserialize-bst "449") |  |  |  |  |  |  |
|  508 | [Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum/ "Most Frequent Subtree Sum") | ★★★ |  |  |  |  |  |  |  |
|  968 | [Binary Tree Cameras](https://leetcode.com/problems/binary-tree-cameras/ "Binary Tree Cameras") | ★★★★ | [337](https://leetcode.com/problems/house-robber-iii/ "337") | [979](https://leetcode.com/problems/distribute-coins-in-binary-tree "979") |  |  |  |  |  |

### Binary Search
|  Id | Name | Difficulty |  |  |  |  |  | Comments |
| ---: | --- | :---: | :---: | --- | --- | --- | --- | --- |
|  35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/ "Search Insert Position") | ★★ | [34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/ "34") | [704](https://leetcode.com/problems/binary-search/ "704") | [981](https://leetcode.com/problems/time-based-key-value-store "981") |  |  | upper_bound |
|  33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array "Search in Rotated Sorted Array") | ★★★ | [81](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/ "81") | [153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/ "153") | [154](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii "154") | [162](https://leetcode.com/problems/find-peak-element "162") | [852](https://leetcode.com/problems/peak-index-in-a-mountain-array/ "852") | rotated / peak |
|  69 | [Sqrt(x)](https://leetcode.com/problems/sqrtx "Sqrt(x)") | ★★★ |  |  |  |  |  | upper_bound |
|  74 | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/ "Search a 2D Matrix") | ★★★ |  |  |  |  |  | treat 2d as 1d |
|  875 | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/ "Koko Eating Bananas") | ★★★ | [1011](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/ "1011") |  |  |  |  | guess ans and check |
|  378 | [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/ "Kth Smallest Element in a Sorted Matrix") | ★★★ | [668](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/ "668") |  |  |  |  | kth + matrix |
|  778 | [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water/ "Swim in Rising Water") | ★★★ | [174](https://leetcode.com/problems/dungeon-game/ "174") | [875](https://leetcode.com/problems/koko-eating-bananas/ "875") |  |  |  | guess ans and check |
|  4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/ "Median of Two Sorted Arrays") | ★★★★ |  |  |  |  |  |  |
|  719 | [Find K-th Smallest Pair Distance](https://leetcode.com/problems/find-k-th-smallest-pair-distance/ "Find K-th Smallest Pair Distance") | ★★★★ | [786](https://leetcode.com/problems/k-th-smallest-prime-fraction/ "786") |  |  |  |  | kth + two pointers |

### Binary Search Tree
|  Id | Name | Difficulty |  | Comments |
| ---: | --- | :---: | :---: | --- |
|  98 | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/ "Validate Binary Search Tree") | ★★ | [530](https://leetcode.com/problems/minimum-absolute-difference-in-bst "530") | inorder |
|  700 | [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/ "Search in a Binary Search Tree") | ★★ | [701](https://leetcode.com/problems/insert-into-a-binary-search-tree/ "701") | binary search |
|  230 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst "Kth Smallest Element in a BST") | ★★★ |  | inorder |
|  99 | [Recover Binary Search Tree](https://leetcode.com/problems/recover-binary-search-tree/ "Recover Binary Search Tree") | ★★★ |  | inorder |
|  108 | [Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/ "Convert Sorted Array to Binary Search Tree") | ★★★ |  |  |
|  501 | [Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/ "Find Mode in Binary Search Tree") | ★★★ |  | inorder |
|  450 | [Delete Node in a BST](https://leetcode.com/problems/delete-node-in-a-bst/ "Delete Node in a BST") | ★★★★ |  | binary search |

### Graph
|  Id | Name | Difficulty |  |  |  |  | Comments |
| ---: | --- | :---: | :---: | --- | --- | --- | --- |
|  133 | [Clone Graph](https://leetcode.com/problems/clone-graph/ "Clone Graph") | ★★ | [138](https://leetcode.com/problems/copy-list-with-random-pointer/ "138") |  |  |  | queue + hashtable |
|  200 | [Number of Islands](https://leetcode.com/problems/number-of-islands/ "Number of Islands") | ★★ | [547](https://leetcode.com/problems/friend-circles/ "547") | [695](https://leetcode.com/problems/max-area-of-island "695") | [733](https://leetcode.com/problems/flood-fill/ "733") | [827](https://leetcode.com/problems/making-a-large-island/ "827") | grid + connected components |
|  841 | [Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/ "Keys and Rooms") | ★★ |  |  |  |  | connected components |
|  207 | [Course Schedule](https://leetcode.com/problems/course-schedule/ "Course Schedule") | ★★★ | [210](https://leetcode.com/problems/course-schedule-ii/ "210") | [802](https://leetcode.com/problems/find-eventual-safe-states "802") |  |  | topology sorting |
|  399 | [Evaluate Division](https://leetcode.com/problems/evaluate-division "Evaluate Division") | ★★★ | [839](https://leetcode.com/problems/similar-string-groups "839") | [952](https://leetcode.com/problems/largest-component-size-by-common-factor/ "952") | [990](https://leetcode.com/problems/satisfiability-of-equality-equations "990") | [721](https://leetcode.com/problems/accounts-merge/ "721") | union find |
|  785 | [Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite "Is Graph Bipartite?") | ★★★ |  |  |  |  | bipartition |
|  684 | [Redundant Connection](https://leetcode.com/problems/redundant-connection "Redundant Connection") | ★★★★ | [685](https://leetcode.com/problems/redundant-connection-ii "685") | [787](https://leetcode.com/problems/cheapest-flights-within-k-stops/ "787") |  |  | cycle, union find |
|  743 | [Network Delay Time](https://leetcode.com/problems/network-delay-time "Network Delay Time") | ★★★★ | [882](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/ "882") |  |  |  | shortest path |
|  847 | [Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/ "Shortest Path Visiting All Nodes") | ★★★★ | [815](https://leetcode.com/problems/bus-routes/ "815") | [864](https://leetcode.com/problems/shortest-path-to-get-all-keys/ "864") | [924](https://leetcode.com/problems/minimize-malware-spread/ "924") |  | BFS |
|  943 | [Find the Shortest Superstring](https://leetcode.com/problems/find-the-shortest-superstring/ "Find the Shortest Superstring") | ★★★★ | [980](https://leetcode.com/problems/unique-paths-iii/ "980") | [996](https://leetcode.com/problems/number-of-squareful-arrays/ "996") |  |  | Hamiltonian path (DFS / DP) |
|  959 | [Regions Cut By Slashes](https://leetcode.com/problems/regions-cut-by-slashes/ "Regions Cut By Slashes") | ★★★★ |  |  |  |  | union find / grid + connected component |
|  332 | [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/ "Reconstruct Itinerary") | ★★★★ |  |  |  |  | Eulerian path |
|  1192 | [Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/ "Critical Connections in a Network") | ★★★★ |  |  |  |  | Tarjan |


### Dynamic Programming
|  Id | Name | Difficulty |  |  |  |  |  |  | Comments |
| ---: | --- | :---: | :---: | --- | --- | --- | --- | --- | --- |
|  70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs "Climbing Stairs") | ★ | [746](https://leetcode.com/problems/min-cost-climbing-stairs "746") |  |  |  |  |  | I: O(n), S = O(n), T = O(n) |
|  303 | [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable "Range Sum Query - Immutable") | ★ |  |  |  |  |  |  |  |
|  53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray "Maximum Subarray") | ★★ | [121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ "121") |  |  |  |  |  |  |
|  198 | [House Robber](https://leetcode.com/problems/house-robber/ "House Robber") | ★★★ | [213](https://leetcode.com/problems/house-robber-ii/ "213") | [309](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/ "309") | [740](https://leetcode.com/problems/delete-and-earn/ "740") | [790](https://leetcode.com/problems/domino-and-tromino-tiling/ "790") | [801](https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/ "801") |  | I: O(n), S = O(3n), T = O(3n) |
|  139 | [Word Break](https://leetcode.com/problems/word-break "Word Break") | ★★★ | [140](https://leetcode.com/problems/word-break-ii "140") | [818](https://leetcode.com/problems/race-car/ "818") |  |  |  |  | I: O(n), S = O(n), T = O(n^2) |
|  300 | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/ "Longest Increasing Subsequence") | ★★★ | [673](https://leetcode.com/problems/number-of-longest-increasing-subsequence "673") |  |  |  |  |  |  |
|  72 | [Edit Distance](https://leetcode.com/problems/edit-distance "Edit Distance") | ★★★ | [10](https://leetcode.com/problems/regular-expression-matching "10") | [44](https://leetcode.com/problems/wildcard-matching/ "44") | [97](https://leetcode.com/problems/interleaving-string "97") | [115](https://leetcode.com/problems/distinct-subsequences/ "115") | [583](https://leetcode.com/problems/delete-operation-for-two-strings/ "583") | [712](https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings "712") | I: O(m+n), S = O(mn), T = O(mn) |
|  322 | [Coin Change](https://leetcode.com/problems/coin-change "Coin Change") | ★★★ | [377](https://leetcode.com/problems/combination-sum-iv/ "377") | [416](https://leetcode.com/problems/partition-equal-subset-sum/ "416") | [494](https://leetcode.com/problems/target-sum "494") |  |  |  | I: O(n) + k, S = O(n), T = O(kn) |
|  813 | [Largest Sum of Averages](https://leetcode.com/problems/largest-sum-of-averages/ "Largest Sum of Averages") | ★★★ |  |  |  |  |  |  | I: O(n) + k, S = O(n), T = O(kn^2) |
|  312 | [Burst Balloons](https://leetcode.com/problems/burst-balloons/ "Burst Balloons") | ★★★★ | [664](https://leetcode.com/problems/strange-printer/ "664") | [1024](https://leetcode.com/problems/video-stitching/ "1024") | [1039](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/ "1039") |  |  |  | I: O(n), S = O(n^2), T = O(n^3) |
|  741 | [Cherry Pickup](https://leetcode.com/problems/cherry-pickup/ "Cherry Pickup") | ★★★★ |  |  |  |  |  |  | I: O(n^2), S = O(n^3), T = O(n^3) |
|  546 | [Remove Boxes](https://leetcode.com/problems/remove-boxes "Remove Boxes") | ★★★★★ |  |  |  |  |  |  | I: O(n), S = O(n^3), T = O(n^4) |
|  943 | [Find the Shortest Superstring](https://leetcode.com/problems/find-the-shortest-superstring/ "Find the Shortest Superstring") | ★★★★ | [980](https://leetcode.com/problems/unique-paths-iii/ "980") | [996](https://leetcode.com/problems/number-of-squareful-arrays/ "996") |  |  |  |  | I: O(n), S = O(n*2^n), T = (n^2*2^n) |
|  62 | [Unique Paths](https://leetcode.com/problems/unique-paths "Unique Paths") | ★★ | [63](https://leetcode.com/problems/unique-paths-ii "63") | [64](https://leetcode.com/problems/minimum-path-sum "64") | [120](https://leetcode.com/problems/triangle "120") | [174](https://leetcode.com/problems/dungeon-game "174") | [931](https://leetcode.com/problems/minimum-falling-path-sum/ "931") |  | I: O(mn), S = O(mn), T = O(mn) |
|  85 | [Maximal Rectangle](https://leetcode.com/problems/delete-operation-for-two-strings/ "Maximal Rectangle") | ★★★ | [221](https://leetcode.com/problems/maximal-square/ "221") | [304](https://leetcode.com/problems/range-sum-query-2d-immutable "304") |  |  |  |  |  |
|  688 | [Knight Probability in Chessboard](https://leetcode.com/problems/knight-probability-in-chessboard/ "Knight Probability in Chessboard") | ★★★ | [576](https://leetcode.com/problems/out-of-boundary-paths/ "576") | [935](https://leetcode.com/problems/knight-dialer/ "935") |  |  |  |  | I: O(mn) + k, S = O(kmn) T = O(kmn) |
|  322 | [Coin Change](https://leetcode.com/problems/reconstruct-itinerary/ "Coin Change") | ★★★ | [377](https://leetcode.com/problems/combination-sum-iv/ "377") | [416](https://leetcode.com/problems/partition-equal-subset-sum/ "416") | [494](https://leetcode.com/problems/target-sum/ "494") | [1043](https://leetcode.com/problems/partition-array-for-maximum-sum/ "1043") | [1049](https://leetcode.com/problems/last-stone-weight-ii/ "1049") |  | I: O(n) + k, S = O(n), T = O(kn) |
|   |  |  | [1220](https://leetcode.com/problems/count-vowels-permutation/ "1220") | [1230](https://leetcode.com/problems/toss-strange-coins/ "1230") | [1262](https://leetcode.com/problems/greatest-sum-divisible-by-three/ "1262") | [1269](https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/ "1269") |  |  |
|  813 | [Largest Sum of Averages](https://leetcode.com/problems/largest-sum-of-averages/ "Largest Sum of Averages") | ★★★★ | [1278](https://leetcode.com/problems/palindrome-partitioning-iii/ "1278") | [1335](https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/ "1335") | [410](https://leetcode.com/problems/split-array-largest-sum/ "410") |  |  |  | I: O(n) + k<br/>S = O(n*k), T = O(kn^2) |
|  1223 | [Dice Roll Simulation](https://leetcode.com/problems/dice-roll-simulation/ "Dice Roll Simulation") | ★★★★ |  |  |  |  |  |  | I: O(n) + k + p<br/>S = O(k*p), T = O(n^2kp) |
|  312 | [Burst Balloons](https://leetcode.com/problems/burst-balloons/ "Burst Balloons") | ★★★★ | [664](https://leetcode.com/problems/strange-printer/ "664") | [1024](https://leetcode.com/problems/video-stitching/ "1024") | [1039](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/ "1039") | [1140](https://leetcode.com/problems/stone-game-ii/ "1140") | [1130](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/ "1130") |  | I: O(n), S = O(n^2), T = O(n^3) |
|  741 | [Cherry Pickup](https://leetcode.com/problems/cherry-pickup/ "Cherry Pickup") | ★★★★ |  |  |  |  |  |  | I: O(n^2), S = O(n^3), T = O(n^3) |
|  546 | [Remove Boxes](https://leetcode.com/problems/remove-boxes/ "Remove Boxes") | ★★★★★ |  |  |  |  |  |  | I: O(n), S = O(n^3), T = O(n^4) |
|  943 | [Find the Shortest Superstring](https://leetcode.com/problems/find-the-shortest-superstring/ "Find the Shortest Superstring") | ★★★★★ | [980](https://leetcode.com/problems/unique-paths-iii/ "980") | [996](https://leetcode.com/problems/number-of-squareful-arrays/ "996") | [1125](https://leetcode.com/problems/smallest-sufficient-team/ "1125") |  |  |  | I: O(n)<br/>S = O(n*2^n), T = (n^2*2^n) |

### Advanced
|  Id | Name | Difficulty |  |  |  |  |  | Comments |
| ---: | --- | :---: | :---: | --- | --- | --- | --- | --- |
|  208 | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree "Implement Trie (Prefix Tree)") | ★★★ | [648](https://leetcode.com/problems/replace-words/ "648") | [676](https://leetcode.com/problems/implement-magic-dictionary "676") | [677](https://leetcode.com/problems/map-sum-pairs "677") | [720](https://leetcode.com/problems/longest-word-in-dictionary "720") | [745](https://leetcode.com/problems/prefix-and-suffix-search "745") | Trie |
|  307 | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable "Range Sum Query - Mutable") | ★★★ |  |  |  |  |  | BIT/Segment Tree |
|  901 | [Online Stock Span](https://leetcode.com/problems/online-stock-span "Online Stock Span") | ★★★ | [907](https://leetcode.com/problems/sum-of-subarray-minimums "907") | [1019](https://leetcode.com/problems/next-greater-node-in-linked-list/ "1019") |  |  |  | Monotonic Stack |
|  239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/ "Sliding Window Maximum") | ★★★ |  |  |  |  |  | Monotonic Queue |

This [list](https://docs.google.com/spreadsheets/d/1SbpY-04Cz8EWw3A_LBUmDEXKUMO31DBjfeMoA0dlfIA/edit#gid=126913158) is made by **huahua**, I found this on his [youtube](https://www.youtube.com/user/xxfflower/videos). Please visit his [website](https://zxi.mytechroad.com/blog/leetcode-problem-categories/) for more.


# Software Engineer Interview
## Overall Mindset
1. Having a right mindset is the most important one. It keeps you going when you are tired after work. Studying when everyone else are out having fun. Reminding you that your goals are not going to come easy, it takes time, self-discipline, mental and physical toughness...

2. [How to Get a Job at the Big 4](https://youtu.be/YJZCUhxNCv8).

3. [How I Got a Job at Google as a Software Engineer](https://www.youtube.com/watch?v=UPO-9iMjBpc).

4. [The #1 Daily Habit of Those Who Dominate](https://podcasts.apple.com/tw/podcast/the-mfceo-project/id1012570406?i=1000412624447) with Andy Frisella. It is also avaliable on Spotify or Youtube, just google it.

## Prepare in a Structural Way
1. [How should I prepare for my Google interview if I have 1 month left and I’m applying for a software engineer role?](https://www.quora.com/How-should-I-prepare-for-my-Google-interview-if-I-have-1-month-left-and-I%E2%80%99m-applying-for-a-software-engineer-role/answer/Anthony-D-Mays?ch=10&share=5c488000&srid=W0jqp)

2. [How can I get a job at Facebook or Google in 6 months?](https://www.quora.com/How-can-I-get-a-job-at-Facebook-or-Google-in-6-months-I-need-a-concise-work-plan-to-build-a-good-enough-skill-set-Should-I-join-some-other-start-up-or-build-my-own-projects-start-up-Should-I-just-focus-on-practicing-data-structures-and-algorithms/answer/Jimmy-Saade)

3. [What should I know from the CLRS 3rd edition book if my aim is to get into Google?](https://www.quora.com/What-should-I-know-from-the-CLRS-3rd-edition-book-if-my-aim-is-to-get-into-Google/answer/Jimmy-Saade)

## Data Structures and Algorithms for beginners
If you are new or know nothing about data structures and algorithms, I recommend [this course](<https://classroom.udacity.com/courses/ud513>). This course is taught in Python and design to help you find job and do well in the interview.


# System Design
1. [More resource](https://github.com/shashank88/system_design)

2. [Architecture 101](https://engineering.videoblocks.com/web-architecture-101-a3224e126947)

3. [Systems Design Interview Concepts](https://www.youtube.com/watch?v=REB_eGHK_P4). There are also lots of tech interview related topic in his channel.

4. [Narendra's Youtube Channel](https://www.youtube.com/channel/UCn1XnDWhsLS5URXTi5wtFTA/playlists)


# Knowledge Base Question
1. [Session vs Cookie](https://medium.com/@chriswrite/session-vs-cookie-software-engineer-top-asked-question-1-9bdbc0766739)
2. [Token Authentication](https://medium.com/@chriswrite/token-authentication-software-engineer-top-asked-question-2-76dd2ed7c2d5)
3. [TCP/UDP](https://www.youtube.com/watch?v=Vdc8TCESIg8)
    * Transport Layer
        * Application Layer (HTTP, FTP)
        * Transport Layer (UDP/TCP, Slice data to small packages)
        * Network Layer (IP)
        * Link Layer (Wifi)
        * Physical Layer (Coaxial Ethernet Cable)
    * UDP has smaller package size (8 bytes), while TCP needs 20 bytes due to it has larger header.
    * UDP are not order guaranteed. TCP are in order.
    * They both have error messages, but TCP will resent it again, UDP does not.
    * TCP needs a three-way handshake to initiate a connection between ports. It’s like a phone call. While UDP is like a mail.
    * In short, UDP is smaller and faster while TCP is reliable and ordered.
    * UDP example, video streaming, DNS lookups.
4. [HTTPS, CA, PKI](https://www.youtube.com/watch?v=i-rtxrEz_E8)
5. HTTP, HTTP Code, [Socket](https://www.youtube.com/watch?v=Y0g3M4VG6Ns), [WebSocket](https://www.youtube.com/watch?v=i5OVcTdt_OU), [HTTP KeepAlive](https://www.youtube.com/watch?v=j8lgFaIajko), HTTP2
6. DNS, CNAME, NS, A, AAAA, IPv4, IPv6
7. Code, Process, Thread
8. [Stack memory vs Heap memory](https://www.gribblelab.org/CBootCamp/7_Memory_Stack_vs_Heap.html)
    * Stack memory
        * Stores temporary variable created by functions.
        * Memory is managed by CPU for you. No need to allocate and free it by hand.
        * L.I.F.O.
        * Stacks has limit (That is why we seldom use recursion real life)
        * Stacks variable are local variable in nature.

    * Heap memory
        * Larger.
        * Slightly slower. Because we has to use "pointers" to access.
        * We are responsible to free() the memory.
        * Heap variable is global variable in nature.
9. GET vs POST
10. [CORS](https://www.youtube.com/watch?v=eWEgUcHPle0)  
...


# Others
## Resume
<https://drive.google.com/file/d/10b9NZDhPbUOW_C7108IKe9ev6Ed2UG7F/view>

## Interview Question Survey
<https://www.glassdoor.com/index.htm>  
<https://www.careercup.com/>

## Offer Negotiation
<https://haseebq.com/my-ten-rules-for-negotiating-a-job-offer/>

