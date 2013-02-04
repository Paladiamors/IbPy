#!/usr/bin/env python
""" generated source for module AnyWrapperMsgGenerator """
# package: com.ib.client

from ib.lib import classmethod_ as classmethod
from ib.lib.overloading import overloaded

class AnyWrapperMsgGenerator(object):
    """ generated source for class AnyWrapperMsgGenerator """
    @classmethod
    @overloaded
    def error(cls, ex):
        """ generated source for method error """
        return "Error - " + ex.message

    @classmethod
    @error.register(object, str)
    def error_0(cls, str_):
        """ generated source for method error_0 """
        return str_

    @classmethod
    @error.register(object, int, int, str)
    def error_1(cls, id, errorCode, errorMsg):
        """ generated source for method error_1 """
        err = str(id)
        err += " | "
        err += str(id)
        err += " | "
        err += errorMsg
        return err

    @classmethod
    def connectionClosed(cls):
        """ generated source for method connectionClosed """
        return "Connection Closed"

