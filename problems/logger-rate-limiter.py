class Logger(object):
    def __init__(self):
        self.log = collections.Counter() #store the latest timestamp

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.log or self.log[message]+10<=timestamp:
            self.log[message] = timestamp
            return True
        else:
            return False



class Logger(object):

    def __init__(self):
        #stores the messages within 10 seconds
        self.q = collections.deque()
        self.set = set()
        

    def shouldPrintMessage(self, timestamp, message):
        while self.q and timestamp-self.q[0][0]>=10:
            time, msg = self.q.popleft()
            self.set.remove(msg)
        
        if message not in self.set:
            self.q.append((timestamp, message))
            self.set.add(message)
            return True
        else:
            return False