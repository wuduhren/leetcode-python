# Overview
1. This is my Python (2.7) Leetcode solution.
As time grows, this also become a guide to prepare for software engineer interview.

2. The solution is at `problems/the-file-name/`.
For example, `merge-sorted-array.py`'s solution is at `https://leetcode.com/problems/merge-sorted-array/`.

2. I really take time tried to make the best solution and collect the best resource that I found.  
Because I wanted to help others like me.  
Please [BUY ME A COFFEE](https://www.buymeacoffee.com/chriswu) if you want to show support.


# Leetcode Problem Lists
I found it makes sense to solve similar problems together, so that we can recognize the problem faster when we encounter a new one. My suggestion is to skip the HARD problems when you first go through these list.

* https://www.programcreek.com/2013/08/leetcode-problem-classification/
* https://github.com/wisdompeak/LeetCode
* https://docs.google.com/spreadsheets/d/1SbpY-04Cz8EWw3A_LBUmDEXKUMO31DBjfeMoA0dlfIA/edit#gid=126913158 ([huahua](https://www.youtube.com/user/xxfflower/videos)).
* https://leetcode.com/list/?selectedList=535ukjh5 (Only 74 problems)


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

5. [System Design Primer](https://github.com/donnemartin/system-design-primer)


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

