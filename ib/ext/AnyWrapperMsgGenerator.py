#!/usr/bin/env python
<<<<<<< HEAD
""" generated source for module AnyWrapperMsgGenerator """
# package: com.ib.client
=======
# -*- coding: utf-8 -*-

##
# Translated source for AnyWrapperMsgGenerator.
##

# Source file: AnyWrapperMsgGenerator.java
# Target file: AnyWrapperMsgGenerator.py
#
# Original file copyright original author(s).
# This file copyright Troy Melhase, troy@gci.net.
#
# WARNING: all changes to this file will be lost.
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465

from ib.lib import classmethod_ as classmethod
from ib.lib.overloading import overloaded

class AnyWrapperMsgGenerator(object):
<<<<<<< HEAD
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
=======
    """ generated source for AnyWrapperMsgGenerator

    """

    @classmethod
    @overloaded
    def error(cls, ex):
        return "Error - " + ex.message

    @classmethod
    @error.register(type, str)
    def error_0(cls, strval):
        return strval

    @classmethod
    @error.register(type, int, int, str)
    def error_1(cls, id, errorCode, errorMsg):
        err = str(id)
        err += " | "
        err += str(errorCode)
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        err += " | "
        err += errorMsg
        return err

    @classmethod
    def connectionClosed(cls):
<<<<<<< HEAD
        """ generated source for method connectionClosed """
        return "Connection Closed"

=======
        return "Connection Closed"


>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
