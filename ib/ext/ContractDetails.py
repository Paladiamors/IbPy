#!/usr/bin/env python
<<<<<<< HEAD
""" generated source for module ContractDetails """
# 
#  * ContractDetails.java
#  *
#  
# package: com.ib.client
=======
# -*- coding: utf-8 -*-

##
# Translated source for ContractDetails.
##

# Source file: ContractDetails.java
# Target file: ContractDetails.py
#
# Original file copyright original author(s).
# This file copyright Troy Melhase, troy@gci.net.
#
# WARNING: all changes to this file will be lost.

>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
from ib.lib.overloading import overloaded
from ib.ext.Contract import Contract

class ContractDetails(object):
<<<<<<< HEAD
    """ generated source for class ContractDetails """
    m_summary = None #Contract()
    m_marketName = ""
    m_tradingClass = ""
    m_minTick = 0.0
=======
    """ generated source for ContractDetails

    """
    m_summary = None
    m_marketName = ""
    m_tradingClass = ""
    m_minTick = float()
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
    m_priceMagnifier = 0
    m_orderTypes = ""
    m_validExchanges = ""
    m_underConId = 0
    m_longName = ""
    m_contractMonth = ""
    m_industry = ""
    m_category = ""
    m_subcategory = ""
    m_timeZoneId = ""
    m_tradingHours = ""
    m_liquidHours = ""
<<<<<<< HEAD
    m_evRule = ""
    m_evMultiplier = 0.0
    m_secIdList = None # Vector()

    #  CUSIP/ISIN/etc.
    #  BOND values
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
    m_cusip = ""
    m_ratings = ""
    m_descAppend = ""
    m_bondType = ""
    m_couponType = ""
    m_callable = False
    m_putable = False
    m_coupon = 0
    m_convertible = False
    m_maturity = ""
    m_issueDate = ""
    m_nextOptionDate = ""
    m_nextOptionType = ""
    m_nextOptionPartial = False
    m_notes = ""

    @overloaded
    def __init__(self):
<<<<<<< HEAD
        """ generated source for method __init__ """
        self.m_summary = Contract()
        self.m_minTick = 0
        self.m_underConId = 0
        self.m_evMultiplier = 0

    @__init__.register(object, Contract, str, str, float, str, str, int, str, str, str, str, str, str, str, str, str, float)
    def __init___0(self, p_summary, p_marketName, p_tradingClass, p_minTick, p_orderTypes, p_validExchanges, p_underConId, p_longName, p_contractMonth, p_industry, p_category, p_subcategory, p_timeZoneId, p_tradingHours, p_liquidHours, p_evRule, p_evMultiplier):
        """ generated source for method __init___0 """
=======
        self.m_summary = Contract()
        self.m_minTick = 0
        self.m_underConId = 0

    @__init__.register(object, Contract, str, str, float, str, str, int, str, str, str, str, str, str, str, str)
    def __init___0(self, p_summary,
                         p_marketName,
                         p_tradingClass,
                         p_minTick,
                         p_orderTypes,
                         p_validExchanges,
                         p_underConId,
                         p_longName,
                         p_contractMonth,
                         p_industry,
                         p_category,
                         p_subcategory,
                         p_timeZoneId,
                         p_tradingHours,
                         p_liquidHours):
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_summary = p_summary
        self.m_marketName = p_marketName
        self.m_tradingClass = p_tradingClass
        self.m_minTick = p_minTick
        self.m_orderTypes = p_orderTypes
        self.m_validExchanges = p_validExchanges
        self.m_underConId = p_underConId
        self.m_longName = p_longName
        self.m_contractMonth = p_contractMonth
        self.m_industry = p_industry
        self.m_category = p_category
        self.m_subcategory = p_subcategory
        self.m_timeZoneId = p_timeZoneId
        self.m_tradingHours = p_tradingHours
        self.m_liquidHours = p_liquidHours
<<<<<<< HEAD
        self.m_evRule = p_evRule
        self.m_evMultiplier = p_evMultiplier
=======

>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465

