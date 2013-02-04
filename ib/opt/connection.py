#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
<<<<<<< HEAD
# Defines Connection class to encapsulate a connection to IB TWS.
=======
# Defines the Connection class to encapsulate a connection to IB TWS.
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
#
# Connection instances defer failed attribute lookup to their receiver
# and sender member objects.  This makes it easy to access the
# receiver to register functions:
#
# >>> con = ibConnection()
# >>> con.register(my_callable)
#
# And it makes it easy to access the sender functions:
#
# >>> con.reqScannerParameters()
# >>> con.placeOrder(...)
#
##
<<<<<<< HEAD
from ib.lib.logger import logger
=======
from ib.opt.dispatcher import Dispatcher
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
from ib.opt.receiver import Receiver
from ib.opt.sender import Sender


class Connection(object):
    """ Encapsulates a connection to TWS.

    """
<<<<<<< HEAD
    def __init__(self, host, port, clientId, receiver, sender):
=======
    def __init__(self, host, port, clientId, receiver, sender, dispatcher):
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        """ Constructor.

        @param host name of host for connection; default is localhost
        @param port port number for connection; default is 7496
        @param clientId client identifier to send when connected
<<<<<<< HEAD
=======
	@param receiver instance for reading from the connected socket
	@param sender instance for writing to the connected socket
	@param dispatcher instance for dispatching socket messages
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        """
        self.host = host
        self.port = port
        self.clientId = clientId
        self.receiver = receiver
        self.sender = sender
<<<<<<< HEAD
=======
	self.dispatcher = dispatcher
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465

    def __getattr__(self, name):
        """ x.__getattr__('name') <==> x.name

<<<<<<< HEAD
        @return named attribute from instance receiver or sender
        """
        try:
            return getattr(self.receiver, name)
        except (AttributeError, ):
            try:
                return getattr(self.sender, name)
            except (AttributeError, ):
                pass
        raise AttributeError(name)
=======
        @return attribute of instance dispatcher, receiver, or sender
        """
	for obj in (self.dispatcher, self.receiver, self.sender):
	    try:
		return getattr(obj, name)
	    except (AttributeError, ):
		pass
	err = "'%s' object has no attribute '%s'"
	raise AttributeError(err % (self.__class__.__name__, name))
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465

    def connect(self):
        """ Establish a connection to TWS with instance attributes.

        @return True if connected, otherwise raises an exception
        """
        return self.sender.connect(self.host, self.port, self.clientId,
                                   self.receiver)

<<<<<<< HEAD
    def disconnect(self):
        """ Disconnect from TWS

        @return True if disconnected, False otherwise
        """
        return self.sender.disconnect()

    def enableLogging(self, enable=True):
        """ Enable or disable logging of all messages.

        @param enable if True (default), enables logging; otherwise disables
        @return True if enabled, False otherwise
        """
        if enable:
            self.logger = logger()
            self.receiver.registerAll(self.logMessage)
        else:
            self.receiver.unregisterAll(self.logMessage)
        return enable

    def logMessage(self, message):
        """ Format and send a message values to the logger.

        @param message instance of Message
        @return None
        """
        line = str.join(', ', ['%s=%s' % item for item in message.items()])
        self.logger.debug('%s(%s)', message.typeName, line)

    @classmethod
    def create(cls, host='localhost', port=7496, clientId=0, receiver=None,
               sender=None):
        """ Creates and returns Connection class (or subclass) instance.

        @param host name of host for connection; default is localhost
        @param port port number for connection; default is 7496
        @param clientId client identifier to send when connected
        @return Connection (or subclass) instance
        """
        receiver = Receiver() if receiver is None else receiver
        sender = Sender() if sender is None else sender
        return cls(host, port, clientId, receiver, sender)
=======
    @classmethod
    def create(cls, host='localhost', port=7496, clientId=0,
	       receiver=None, sender=None, dispatcher=None):
        """ Creates and returns Connection class (or subclass) instance.

        For the receiver, sender, and dispatcher parameters, pass in
        an object instance for those duties; leave as None to have new
        instances constructed.

        @param host name of host for connection; default is localhost
        @param port port number for connection; default is 7496
        @param clientId client identifier to send when connected

	@param receiver=None object for reading messages
        @param sender=None object for writing requests
        @param dispatcher=None object for dispatching messages

        @return Connection (or subclass) instance
        """
	dispatcher = Dispatcher() if dispatcher is None else dispatcher
        receiver = Receiver(dispatcher) if receiver is None else receiver
        sender = Sender(dispatcher) if sender is None else sender
        return cls(host, port, clientId, receiver, sender, dispatcher)
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
