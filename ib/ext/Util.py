#!/usr/bin/env python
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
                    matchedRhsElems[rhsIdx] = True
                    break
                rhsIdx += 1
            if rhsIdx >= rhsCount:
                #  no matching elem found
                return False
            lhsIdx += 1
        return True

    @classmethod
    def IntMaxString(cls, value):
        """ generated source for method IntMaxString """
        return "" if (value == Integer.MAX_VALUE) else "" + value

    @classmethod
    def DoubleMaxString(cls, value):
        """ generated source for method DoubleMaxString """
        return "" if (value == Double.MAX_VALUE) else "" + value

