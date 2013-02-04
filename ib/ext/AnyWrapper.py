#!/usr/bin/env python
""" generated source for module AnyWrapper """
# 
#  * AnyWrapper.java
#  *
#  
# package: com.ib.client

from ib.lib.overloading import overloaded

class AnyWrapper(object):
    """ generated source for AnyWrapper

    """

    @overloaded
    def error(self, e):
        raise NotImplementedError()

    @error.register(object, str)
    def error_0(self, strval):
        raise NotImplementedError()

    @error.register(object, int, int, str)
    def error_1(self, id, errorCode, errorMsg):
        raise NotImplementedError()

    def connectionClosed(self):
        raise NotImplementedError()
