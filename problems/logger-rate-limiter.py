class Logger(object):
    def __init__(self):
        self.log = collections.Counter() #store the latest timestamp

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.log or self.log[message]+10<=timestamp:
            self.log[message] = timestamp
            return True
        else:
            return False