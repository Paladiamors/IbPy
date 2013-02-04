#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# Defines message types for the Receiver class.
#
# This module inspects the EWrapper class to build a set of Message
# types.  In creating the types, it also builds a registry of them
# that the Receiver class then uses to determine message types.
##

<<<<<<< HEAD
from functools import partial
from inspect import getargspec
from types import MethodType

from ib.ext.EWrapper import EWrapper
=======
from ast import NodeVisitor, parse
from inspect import getsourcefile
from re import match

from ib.ext.AnyWrapper import AnyWrapper
from ib.ext.EWrapper import EWrapper
from ib.ext.EClientSocket import  EClientSocket
from ib.lib import toTypeName


class SignatureAccumulator(NodeVisitor):
    """

    """
    def __init__(self, classes):
	NodeVisitor.__init__(self)
	self.signatures = []
	for filename in (getsourcefile(cls) for cls in classes):
            self.visit(parse(open(filename).read()))

    def visit_FunctionDef(self, node):
	args = [arg.id for arg in node.args.args]
	self.signatures.append((node.name, args[1:]))


class EClientSocketAccumulator(SignatureAccumulator):
    def getSignatures(self):
        for name, args in self.signatures:
	    if match('(?i)req|cancel|place', name):
	        yield (name, args)


class EWrapperAccumulator(SignatureAccumulator):
    def getSignatures(self):
        for name, args in self.signatures:
	    if match('(?!((?i)error.*))', name):
		yield (name, args)
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465


##
# Dictionary that associates wrapper method names to the message class
# that should be instantiated for delivery during that method call.
registry = {}


<<<<<<< HEAD
class MessageType(type):
    """ MessageType -> simple metaclass to track Message subclasses

    As new Message subclasses are defined (see below), they are saved
    to the registry mapping.
    """
    def __init__(cls, name, bases, namespace):
        """ Constructor.

        @param name name of newly created type
        @param bases tuple of base classes for new type
        @param namespace dictionary with namespace of new type
        """
        setattr(cls, 'typeName', name)
        try:
            registry[namespace['__assoc__']] = cls
        except (KeyError, ):
            pass


class Message(object):
    """ Base class of all Message types.

    """
    __metaclass__ = MessageType
    __slots__ = []
=======
def messageTypeNames():
    """ Builds set of message type names.

    @return set of all message type names as strings
    """
    def typeNames():
	for types in registry.values():
	    for typ in types:
		yield typ.typeName
    return set(typeNames())


class Message(object):
    """ Base class for Message types.

    """
    __slots__ = ()
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465

    def __init__(self, **kwds):
        """ Constructor.

        @param **kwds keywords and values for instance
        """
        for name in self.__slots__:
            setattr(self, name, kwds.pop(name, None))
        assert not kwds

    def __len__(self):
        """ x.__len__() <==> len(x)

        """
        return len(self.keys())

    def __str__(self):
        """ x.__str__() <==> str(x)

        """
        name = self.typeName
        items = str.join(', ', ['%s=%s' % item for item in self.items()])
<<<<<<< HEAD
        return '<%s %s>' % (name, items)
=======
        return '<%s%s>' % (name, (' ' + items) if items else '')
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465

    def items(self):
        """ List of message (slot, slot value) pairs, as 2-tuples.

        @return list of 2-tuples, each slot (name, value)
        """
        return zip(self.keys(), self.values())

    def values(self):
        """ List of instance slot values.

        @return list of each slot value
        """
        return [getattr(self, key, None) for key in self.keys()]

    def keys(self):
        """ List of instance slots.

        @return list of each slot.
        """
        return self.__slots__


class Error(Message):
    """ Specialized message type.

    The error family of method calls can't be built programmatically,
    so we define one here.
    """
<<<<<<< HEAD
    __assoc__ = 'error'
    __slots__ = ['id', 'errorCode', 'errorMsg']


def isWrapperMethod(name, value):
    """ Predicate for wrapper methods.

    @param name name of class attribute as string
    @param value value of class attribute; any object
    @return True if wrapper method
    """
    return (not name.startswith('_') and
            not name.startswith('error') and
            isinstance(value, MethodType))


def selectWrapperMethods(cls):
    """ Wrapper methods of a class.

    @param cls class object to inspect
    @return list of two-tuples, each (name, argnames)
    """
    clsitems = [(name, getattr(cls, name)) for name in dir(cls)]
    clsitems = [(name, method) for name, method in clsitems
                if isWrapperMethod(name, method)]
    def argns(meth):
        args, varargs, varkw, defaults = getargspec(meth)
        return args[1:] # without leading 'self'
    return [(name, argns(method)) for name, method in clsitems]


def buildMessageTypes(wrapper, mapping, *bases):
    """ Construct message types and add to given mapping.

    @param wrapper class object to inspect for methods
    @param mapping dictionary for adding new message types
    @param bases sequence of base classes for message types
    @return None
    """
    for name, args in selectWrapperMethods(wrapper):
        typename = name[0].upper() + name[1:]
        typens = {'__slots__':args, '__assoc__':name}
        mapping[typename] = type(typename, bases, typens)


# create message types in the module namespace from the EWrapper
# abstract class
buildMessageTypes(EWrapper, globals(), Message)

##
# A (partial) method so other modules can use the same mappings we
# have.
wrapperMethods = partial(selectWrapperMethods, EWrapper)


def messageTypeNames():
    """ Builds set of message type names.

    @return set of all message type names as strings
    """
    return set([t.typeName for t in registry.values()])
=======
    __slots__ = ('id', 'errorCode', 'errorMsg')


def buildMessageRegistry(seq, suffixes=[''], bases=(Message, )):
    """ Construct message types and add to given mapping.

    @param seq pairs of method (name, arguments)
    @param bases sequence of base classes for message types
    @return None
    """
    for name, args in sorted(seq):
	for suffix in suffixes:
	    typename = toTypeName(name) + suffix
	    typens = {'__slots__':args, '__assoc__':name, 'typeName':name}
            msgtype = type(typename, bases, typens)
	    if name in registry:
		registry[name] = registry[name] + (msgtype, )
	    else:
		registry[name] = (msgtype, )




eWrapperAccum = EWrapperAccumulator((AnyWrapper, EWrapper))
eClientAccum = EClientSocketAccumulator((EClientSocket, ))

wrapperMethods = list(eWrapperAccum.getSignatures())
clientSocketMethods = list(eClientAccum.getSignatures())
errorMethods = [('error', Error.__slots__), ]

buildMessageRegistry(wrapperMethods)
buildMessageRegistry(clientSocketMethods, suffixes=('Pre', 'Post'))
buildMessageRegistry(errorMethods)

def initModule():
    target = globals()
    for messageTypes in registry.values():
	for messageType in messageTypes:
	    target[messageType.typeName] = messageType

try:
    initModule()
except (NameError, ):
    pass
else:
    del(initModule)


del(AnyWrapper)
del(EWrapper)
del(EClientSocket)
del(eWrapperAccum)
del(eClientAccum)
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
