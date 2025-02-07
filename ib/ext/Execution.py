#!/usr/bin/env python
""" generated source for module Execution """
# 
#  * Execution.java
#  *
#  
# package: com.ib.client

from ib.lib.overloading import overloaded

class Execution(object):
    """ generated source for class Execution """
    m_orderId = int()
    m_clientId = int()
    m_execId = str()
    m_time = str()
    m_acctNumber = str()
    m_exchange = str()
    m_side = str()
    m_shares = int()
    m_price = float()
    m_permId = int()
    m_liquidation = int()
    m_cumQty = int()
    m_avgPrice = float()
    m_orderRef = str()
    m_evRule = str()
    m_evMultiplier = float()

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        self.m_orderId = 0
        self.m_clientId = 0
        self.m_shares = 0
        self.m_price = 0
        self.m_permId = 0
        self.m_liquidation = 0
        self.m_cumQty = 0
        self.m_avgPrice = 0
        self.m_evMultiplier = 0

    @__init__.register(object, int, int, str, str, str, str, str, int, float, int, int, int, float, str, str, float)
    def __init___0(self, p_orderId, p_clientId, p_execId, p_time, p_acctNumber, p_exchange, p_side, p_shares, p_price, p_permId, p_liquidation, p_cumQty, p_avgPrice, p_orderRef, p_evRule, p_evMultiplier):
        """ generated source for method __init___0 """
        self.m_orderId = p_orderId
        self.m_clientId = p_clientId
        self.m_execId = p_execId
        self.m_time = p_time
        self.m_acctNumber = p_acctNumber
        self.m_exchange = p_exchange
        self.m_side = p_side
        self.m_shares = p_shares
        self.m_price = p_price
        self.m_permId = p_permId
        self.m_liquidation = p_liquidation
        self.m_cumQty = p_cumQty
        self.m_avgPrice = p_avgPrice
        self.m_orderRef = p_orderRef
        self.m_evRule = p_evRule
        self.m_evMultiplier = p_evMultiplier

    def __eq__(self, p_other):
        """ generated source for method equals """
        l_bRetVal = False
        if p_other == None:
            l_bRetVal = False
        elif self == p_other:
            l_bRetVal = True
        else:
            l_theOther = p_other
            l_bRetVal = self.m_execId == l_theOther.m_execId
        return l_bRetVal

