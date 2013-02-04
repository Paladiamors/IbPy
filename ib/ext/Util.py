#!/usr/bin/env python
<<<<<<< HEAD
""" generated source for module Util """
# 
#  * Util.java
#  
# package: com.ib.client
#import java.util.Vector
from ib.lib import Double, Integer
class Util(object):
    """ generated source for class Util """
    @classmethod
    def StringIsEmpty(cls, str_):
        """ generated source for method StringIsEmpty """
        return str_ == None or 0 == len(str_)

    @classmethod
    def NormalizeString(cls, str_):
        """ generated source for method NormalizeString """
        return str_ if str_ != None else ""

    @classmethod
    def StringCompare(cls, lhs, rhs):
        """ generated source for method StringCompare """
        return cls.NormalizeString(lhs).compareTo(cls.NormalizeString(rhs))

    @classmethod
    def StringCompareIgnCase(cls, lhs, rhs):
        """ generated source for method StringCompareIgnCase """
        return cls.NormalizeString(lhs).compareToIgnoreCase(cls.NormalizeString(rhs))

    @classmethod
    def VectorEqualsUnordered(cls, lhs, rhs):
        """ generated source for method VectorEqualsUnordered """
        if lhs == rhs:
            return True
        lhsCount = 0 if lhs == None else len(lhs)
        rhsCount = 0 if rhs == None else len(rhs)
        if lhsCount != rhsCount:
            return False
        if lhsCount == 0:
            return True
        matchedRhsElems = [None]*rhsCount
        lhsIdx = 0
        while lhsIdx < lhsCount:
            lhsElem = lhs.get(lhsIdx)
            rhsIdx = 0
            while rhsIdx < rhsCount:
                if matchedRhsElems[rhsIdx]:
                    continue 
                if lhsElem == rhs.get(rhsIdx):
=======
# -*- coding: utf-8 -*-

##
# Translated source for Util.
##

# Source file: Util.java
# Target file: Util.py
#
# Original file copyright original author(s).
# This file copyright Troy Melhase, troy@gci.net.
#
# WARNING: all changes to this file will be lost.

from ib.lib import Double, Integer

class Util(object):
    """ generated source for Util

    """

    @classmethod
    def StringIsEmpty(cls, strval):
        return strval is None or (len(strval) == 0)

    @classmethod
    def NormalizeString(cls, strval):
        return strval if strval is not None else ""

    @classmethod
    def StringCompare(cls, lhs, rhs):
        return cmp(str(lhs), str(rhs))

    @classmethod
    def StringCompareIgnCase(cls, lhs, rhs):
        return cmp(str(lhs).lower(), str(rhs).lower())

    @classmethod
    def VectorEqualsUnordered(cls, lhs, rhs):
        if (lhs == rhs):
            return True
        lhsCount = 0 if lhs is None else len(lhs)
        rhsCount = 0 if rhs is None else len(rhs)
        if (lhsCount != rhsCount):
            return False
        if (lhsCount == 0):
            return True
        matchedRhsElems = [bool() for __idx0 in range(rhsCount)]
        ## for-while
        lhsIdx = 0
        while lhsIdx < lhsCount:
            lhsElem = lhs[lhsIdx]
            rhsIdx = 0
            ## for-while
            while rhsIdx < rhsCount:
                if matchedRhsElems[rhsIdx]:
                    continue
                if lhsElem == rhs[rhsIdx]:
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
                    matchedRhsElems[rhsIdx] = True
                    break
                rhsIdx += 1
            if rhsIdx >= rhsCount:
<<<<<<< HEAD
                #  no matching elem found
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
                return False
            lhsIdx += 1
        return True

    @classmethod
    def IntMaxString(cls, value):
<<<<<<< HEAD
        """ generated source for method IntMaxString """
        return "" if (value == Integer.MAX_VALUE) else "" + value

    @classmethod
    def DoubleMaxString(cls, value):
        """ generated source for method DoubleMaxString """
        return "" if (value == Double.MAX_VALUE) else "" + value
=======
        return "" if (value == Integer.MAX_VALUE) else str(value)

    @classmethod
    def DoubleMaxString(cls, value):
        return "" if (value == Double.MAX_VALUE) else str(value)

>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465

