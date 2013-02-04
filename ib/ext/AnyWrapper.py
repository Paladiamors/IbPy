#!/usr/bin/env python
<<<<<<< HEAD
""" generated source for module AnyWrapper """
# 
#  * AnyWrapper.java
#  *
#  
# package: com.ib.client
=======
# -*- coding: utf-8 -*-

##
# Translated source for AnyWrapper.
##

# Source file: AnyWrapper.java
# Target file: AnyWrapper.py
#
# Original file copyright original author(s).
# This file copyright Troy Melhase, troy@gci.net.
#
# WARNING: all changes to this file will be lost.
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465

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
<<<<<<< HEAD
=======


>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
