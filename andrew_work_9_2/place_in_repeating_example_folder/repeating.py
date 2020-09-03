import time, os, sys, sched

# POLLING_INTERVAL = 1

class Repeat(object):
    def __init__(self, wait, funcName):
        self.schedule = sched.scheduler(time.time, time.sleep)
        self._running = False
        self.wait = wait
        self.funcName = funcName
        self.interval = self.wait
        # self.interval = POLLING_INTERVAL

    def periodic(self, action, actionargs=()):
        if self._running:
            self.event = self.schedule.enter(self.interval, 1, self.periodic, (action, actionargs))
            action(*actionargs)

    def start(self):
        self._running = True
        self.periodic(self.funcName)
        self.schedule.run( )

    def stop(self):
        self._running = False
        if self.schedule and self.event:
            self.schedule.cancel(self.event)

#to use this function
#r = repeating.Repeat(1, function_name)
#r.start()

#a Variable Argument version, that has the number of times the method should run built in.
class RepeatVA(object):
    def __init__(self, wait, funcName,limit, *args):
        # * tells python it is a variable argument
        self.schedule = sched.scheduler(time.time, time.sleep)
        self._running = False
        self.wait = wait
        self.funcName = funcName
        self.interval = self.wait
        self.arg = args
        self.limit = limit
        self.counter = 0

        # self.interval = POLLING_INTERVAL

    def periodic(self, action, actionargs=()):
        if self._running:
            self.counter += 1
            self.event = self.schedule.enter(self.interval, 1, self.periodic, (action, actionargs))
            action(*actionargs)
            if self.counter >= self.limit:
                self.stop()

    def start(self):
        self._running = True
        self.periodic(self.funcName, self.arg)
        self.schedule.run( )

    def stop(self):
        self._running = False
        if self.schedule and self.event:
            self.schedule.cancel(self.event)

#this class is for repeating with the stop provided in the calling function
#I don't think it is as useful as the one above
class RepeatVAnoMax(object):
    def __init__(self, wait, funcName, *args):
        # * tells python it is a variable argument
        self.schedule = sched.scheduler(time.time, time.sleep)
        self._running = False
        self.wait = wait
        self.funcName = funcName
        self.interval = self.wait
        self.arg = args
        # self.interval = POLLING_INTERVAL

    def periodic(self, action, actionargs=()):
        if self._running:
            self.event = self.schedule.enter(self.interval, 1, self.periodic, (action, actionargs))
            action(*actionargs)


    def start(self):
        self._running = True
        self.periodic(self.funcName, self.arg)
        self.schedule.run( )

    def stop(self):
        self._running = False
        if self.schedule and self.event:
            self.schedule.cancel(self.event)