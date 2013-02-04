#!/usr/bin/env python
<<<<<<< HEAD
""" generated source for module UnderComp """
# 
#  * UnderComp.java
#  *
#  
# package: com.ib.client
class UnderComp(object):
    """ generated source for class UnderComp """
    m_conId = int()
=======
# -*- coding: utf-8 -*-

##
# Translated source for UnderComp.
##

# Source file: UnderComp.java
# Target file: UnderComp.py
#
# Original file copyright original author(s).
# This file copyright Troy Melhase, troy@gci.net.
#
# WARNING: all changes to this file will be lost.


class UnderComp(object):
    """ generated source for UnderComp

    """
    m_conId = 0
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
    m_delta = float()
    m_price = float()

    def __init__(self):
<<<<<<< HEAD
        """ generated source for method __init__ """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_conId = 0
        self.m_delta = 0
        self.m_price = 0

    def __eq__(self, p_other):
<<<<<<< HEAD
        """ generated source for method equals """
        if self == p_other:
            return True
        if p_other == None or not (isinstance(p_other, (UnderComp, ))):
            return False
        l_theOther = p_other
        if self.m_conId != l_theOther.m_conId:
            return False
        if self.m_delta != l_theOther.m_delta:
            return False
        if self.m_price != l_theOther.m_price:
            return False
        return True

=======
        if self is p_other:
            return True
        if p_other is None or not isinstance(p_other, (UnderComp)):
            return False
        l_theOther = p_other
        if (self.m_conId != l_theOther.m_conId):
            return False
        if (self.m_delta != l_theOther.m_delta):
            return False
        if (self.m_price != l_theOther.m_price):
            return False
        return True


>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
