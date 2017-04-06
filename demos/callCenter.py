'''
Call():
Create your call class with an init method. Each instance of Call() should have a few attributes:
unique id
caller name
caller phone number
time of call
reason for call
The call class should have a display method that prints all call attributes.
'''



from string import ascii_uppercase, digits, ascii_lowercase
from random import choice
from datetime import datetime

# print datetime.now()
#
# print ''.join(choice(ascii_uppercase + digits + ascii_lowercase) for _ in range(12))

class Call(object):
    def __init__(self, name, phone_number, reason_for_call):
        self.id = ''.join(choice(ascii_uppercase + digits) for _ in range(12))
        self.name = name
        self.phone_number = phone_number
        self.time_of_call = datetime.now()
        self.reason_for_call = reason_for_call

    def displayInfo(self):
        print 'Call id is: {}'.format(self.id)
        print 'Call name is: {}'.format(self.name)
        print 'Call phone_number is: {}'.format(self.phone_number)
        print 'Call time_of_call is: {}'.format(self.time_of_call)
        print 'Call reason_for_call is: {}'.format(self.reason_for_call)


# call1 = Call('Phil', '111-111-1111', 'make call')
# call1.displayInfo()


'''
CallCenter():
Create you call center class with an init method. Each instance of CallCenter() should have the following attributes:

calls: should be a list of call objects
queue size: should be the length of the call list

The call center class should have an add method that adds a new call to the end of the call list

The call center class should have a remove method that removes the call from the beginning of the list (index 0).

The call center class should have a method called info that shows the name and phone number for each call in the queue as well as the length of the queue.

You should be able to test your code to prove that it works. Remember to build one piece at a time and test as you go for easier debugging!
'''

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queueSize = len(self.calls)

    def add_call(self, name, phone_number, reason_for_call):
        newCall = Call(name, phone_number, reason_for_call)
        self.calls.append(newCall)
        self.queueSize = len(self.calls)

    def remove_call(self):
        del self.calls[0]
        self.queueSize = len(self.calls)

    def show_calls(self):
        print 'the length of the call is: {}'.format(self.queueSize)
        for call in self.calls:
            print 'name of caller is: {}, phone_number is: {}'.format(call.name, call.phone_number)

customerSupport = CallCenter()
customerSupport.add_call('Phil', '111-111-1111', 'make call')
customerSupport.add_call('Phil', '222-111-1111', 'make call')
customerSupport.add_call('Phil', '333-111-1111', 'make call')
customerSupport.show_calls()
customerSupport.remove_call()
customerSupport.show_calls()
