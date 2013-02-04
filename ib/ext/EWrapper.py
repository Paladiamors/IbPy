#!/usr/bin/env python
<<<<<<< HEAD
""" generated source for module EWrapper """
# 
#  * EWrapper.java
#  *
#  
# package: com.ib.client

from ib.ext.AnyWrapper import AnyWrapper
class EWrapper(AnyWrapper):
    """ generated source for interface EWrapper """

    # /////////////////////////////////////////////////////////////////////
    #  Interface methods
    # /////////////////////////////////////////////////////////////////////
    
    def tickPrice(self, tickerId, field, price, canAutoExecute):
        """ generated source for method tickPrice """
        raise NotImplementedError()
    
    def tickSize(self, tickerId, field, size):
        """ generated source for method tickSize """
        raise NotImplementedError()
    
    def tickOptionComputation(self, tickerId, field, impliedVol, delta, optPrice, pvDividend, gamma, vega, theta, undPrice):
        """ generated source for method tickOptionComputation """
        raise NotImplementedError()
    
    def tickGeneric(self, tickerId, tickType, value):
        """ generated source for method tickGeneric """
        raise NotImplementedError()
    
    def tickString(self, tickerId, tickType, value):
        """ generated source for method tickString """
        raise NotImplementedError()
    
    def tickEFP(self, tickerId, tickType, basisPoints, formattedBasisPoints, impliedFuture, holdDays, futureExpiry, dividendImpact, dividendsToExpiry):
        """ generated source for method tickEFP """
        raise NotImplementedError()
    
    def orderStatus(self, orderId, status, filled, remaining, avgFillPrice, permId, parentId, lastFillPrice, clientId, whyHeld):
        """ generated source for method orderStatus """
        raise NotImplementedError()
    
    def openOrder(self, orderId, contract, order, orderState):
        """ generated source for method openOrder """
        raise NotImplementedError()
    
    def openOrderEnd(self):
        """ generated source for method openOrderEnd """
        raise NotImplementedError()
    
    def updateAccountValue(self, key, value, currency, accountName):
        """ generated source for method updateAccountValue """
        raise NotImplementedError()
    
    def updatePortfolio(self, contract, position, marketPrice, marketValue, averageCost, unrealizedPNL, realizedPNL, accountName):
        """ generated source for method updatePortfolio """
        raise NotImplementedError()
    
    def updateAccountTime(self, timeStamp):
        """ generated source for method updateAccountTime """
        raise NotImplementedError()
    
    def accountDownloadEnd(self, accountName):
        """ generated source for method accountDownloadEnd """
        raise NotImplementedError()
    
    def nextValidId(self, orderId):
        """ generated source for method nextValidId """
        raise NotImplementedError()
    
    def contractDetails(self, reqId, contractDetails):
        """ generated source for method contractDetails """
        raise NotImplementedError()
    
    def bondContractDetails(self, reqId, contractDetails):
        """ generated source for method bondContractDetails """
        raise NotImplementedError()
    
    def contractDetailsEnd(self, reqId):
        """ generated source for method contractDetailsEnd """
        raise NotImplementedError()
    
    def execDetails(self, reqId, contract, execution):
        """ generated source for method execDetails """
        raise NotImplementedError()
    
    def execDetailsEnd(self, reqId):
        """ generated source for method execDetailsEnd """
        raise NotImplementedError()
    
    def updateMktDepth(self, tickerId, position, operation, side, price, size):
        """ generated source for method updateMktDepth """
        raise NotImplementedError()
    
    def updateMktDepthL2(self, tickerId, position, marketMaker, operation, side, price, size):
        """ generated source for method updateMktDepthL2 """
        raise NotImplementedError()
    
    def updateNewsBulletin(self, msgId, msgType, message, origExchange):
        """ generated source for method updateNewsBulletin """
        raise NotImplementedError()
    
    def managedAccounts(self, accountsList):
        """ generated source for method managedAccounts """
        raise NotImplementedError()
    
    def receiveFA(self, faDataType, xml):
        """ generated source for method receiveFA """
        raise NotImplementedError()
    
    def historicalData(self, reqId, date, open, high, low, close, volume, count, WAP, hasGaps):
        """ generated source for method historicalData """
        raise NotImplementedError()
    
    def scannerParameters(self, xml):
        """ generated source for method scannerParameters """
        raise NotImplementedError()
    
    def scannerData(self, reqId, rank, contractDetails, distance, benchmark, projection, legsStr):
        """ generated source for method scannerData """
        raise NotImplementedError()
    
    def scannerDataEnd(self, reqId):
        """ generated source for method scannerDataEnd """
        raise NotImplementedError()
    
    def realtimeBar(self, reqId, time, open, high, low, close, volume, wap, count):
        """ generated source for method realtimeBar """
        raise NotImplementedError()
    
    def currentTime(self, time):
        """ generated source for method currentTime """
        raise NotImplementedError()
    
    def fundamentalData(self, reqId, data):
        """ generated source for method fundamentalData """
        raise NotImplementedError()
    
    def deltaNeutralValidation(self, reqId, underComp):
        """ generated source for method deltaNeutralValidation """
        raise NotImplementedError()
    
    def tickSnapshotEnd(self, reqId):
        """ generated source for method tickSnapshotEnd """
        raise NotImplementedError()
    
    def marketDataType(self, reqId, marketDataType):
        """ generated source for method marketDataType """
        raise NotImplementedError()
    
    def commissionReport(self, commissionReport):
        """ generated source for method commissionReport """
        raise NotImplementedError()
=======
# -*- coding: utf-8 -*-

##
# Translated source for EWrapper.
##

# Source file: EWrapper.java
# Target file: EWrapper.py
#
# Original file copyright original author(s).
# This file copyright Troy Melhase, troy@gci.net.
#
# WARNING: all changes to this file will be lost.

from ib.ext.AnyWrapper import AnyWrapper

class EWrapper(AnyWrapper):
    """ generated source for EWrapper

    """

    def tickPrice(self, tickerId, field, price, canAutoExecute):
        raise NotImplementedError()

    def tickSize(self, tickerId, field, size):
        raise NotImplementedError()

    def tickOptionComputation(self, tickerId,
                                    field,
                                    impliedVol,
                                    delta,
                                    optPrice,
                                    pvDividend,
                                    gamma,
                                    vega,
                                    theta,
                                    undPrice):
        raise NotImplementedError()

    def tickGeneric(self, tickerId, tickType, value):
        raise NotImplementedError()

    def tickString(self, tickerId, tickType, value):
        raise NotImplementedError()

    def tickEFP(self, tickerId,
                      tickType,
                      basisPoints,
                      formattedBasisPoints,
                      impliedFuture,
                      holdDays,
                      futureExpiry,
                      dividendImpact,
                      dividendsToExpiry):
        raise NotImplementedError()

    def orderStatus(self, orderId,
                          status,
                          filled,
                          remaining,
                          avgFillPrice,
                          permId,
                          parentId,
                          lastFillPrice,
                          clientId,
                          whyHeld):
        raise NotImplementedError()

    def openOrder(self, orderId, contract, order, orderState):
        raise NotImplementedError()

    def openOrderEnd(self):
        raise NotImplementedError()

    def updateAccountValue(self, key, value, currency, accountName):
        raise NotImplementedError()

    def updatePortfolio(self, contract,
                              position,
                              marketPrice,
                              marketValue,
                              averageCost,
                              unrealizedPNL,
                              realizedPNL,
                              accountName):
        raise NotImplementedError()

    def updateAccountTime(self, timeStamp):
        raise NotImplementedError()

    def accountDownloadEnd(self, accountName):
        raise NotImplementedError()

    def nextValidId(self, orderId):
        raise NotImplementedError()

    def contractDetails(self, reqId, contractDetails):
        raise NotImplementedError()

    def bondContractDetails(self, reqId, contractDetails):
        raise NotImplementedError()

    def contractDetailsEnd(self, reqId):
        raise NotImplementedError()

    def execDetails(self, reqId, contract, execution):
        raise NotImplementedError()

    def execDetailsEnd(self, reqId):
        raise NotImplementedError()

    def updateMktDepth(self, tickerId,
                             position,
                             operation,
                             side,
                             price,
                             size):
        raise NotImplementedError()

    def updateMktDepthL2(self, tickerId,
                               position,
                               marketMaker,
                               operation,
                               side,
                               price,
                               size):
        raise NotImplementedError()

    def updateNewsBulletin(self, msgId, msgType, message, origExchange):
        raise NotImplementedError()

    def managedAccounts(self, accountsList):
        raise NotImplementedError()

    def receiveFA(self, faDataType, xml):
        raise NotImplementedError()

    def historicalData(self, reqId,
                             date,
                             open,
                             high,
                             low,
                             close,
                             volume,
                             count,
                             WAP,
                             hasGaps):
        raise NotImplementedError()

    def scannerParameters(self, xml):
        raise NotImplementedError()

    def scannerData(self, reqId,
                          rank,
                          contractDetails,
                          distance,
                          benchmark,
                          projection,
                          legsStr):
        raise NotImplementedError()

    def scannerDataEnd(self, reqId):
        raise NotImplementedError()

    def realtimeBar(self, reqId,
                          time,
                          open,
                          high,
                          low,
                          close,
                          volume,
                          wap,
                          count):
        raise NotImplementedError()

    def currentTime(self, time):
        raise NotImplementedError()

    def fundamentalData(self, reqId, data):
        raise NotImplementedError()

    def deltaNeutralValidation(self, reqId, underComp):
        raise NotImplementedError()

    def tickSnapshotEnd(self, reqId):
        raise NotImplementedError()


>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
