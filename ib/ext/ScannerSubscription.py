#!/usr/bin/env python
<<<<<<< HEAD
""" generated source for module ScannerSubscription """
# package: com.ib.client

from ib.lib import Double, Integer
from ib.lib.overloading import overloaded
class ScannerSubscription(object):
    """ generated source for class ScannerSubscription """
    NO_ROW_NUMBER_SPECIFIED = -1
    m_numberOfRows = NO_ROW_NUMBER_SPECIFIED
    m_instrument = str()
    m_locationCode = str()
    m_scanCode = str()
=======
# -*- coding: utf-8 -*-

##
# Translated source for ScannerSubscription.
##

# Source file: ScannerSubscription.java
# Target file: ScannerSubscription.py
#
# Original file copyright original author(s).
# This file copyright Troy Melhase, troy@gci.net.
#
# WARNING: all changes to this file will be lost.

from ib.lib import Double, Integer
from ib.lib.overloading import overloaded

class ScannerSubscription(object):
    """ generated source for ScannerSubscription

    """
    NO_ROW_NUMBER_SPECIFIED = -1
    m_numberOfRows = NO_ROW_NUMBER_SPECIFIED
    m_instrument = ""
    m_locationCode = ""
    m_scanCode = ""
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
    m_abovePrice = Double.MAX_VALUE
    m_belowPrice = Double.MAX_VALUE
    m_aboveVolume = Integer.MAX_VALUE
    m_averageOptionVolumeAbove = Integer.MAX_VALUE
    m_marketCapAbove = Double.MAX_VALUE
    m_marketCapBelow = Double.MAX_VALUE
<<<<<<< HEAD
    m_moodyRatingAbove = str()
    m_moodyRatingBelow = str()
    m_spRatingAbove = str()
    m_spRatingBelow = str()
    m_maturityDateAbove = str()
    m_maturityDateBelow = str()
    m_couponRateAbove = Double.MAX_VALUE
    m_couponRateBelow = Double.MAX_VALUE
    m_excludeConvertible = str()
    m_scannerSettingPairs = str()
    m_stockTypeFilter = str()

    #  Get
    @overloaded
    def numberOfRows(self):
        """ generated source for method numberOfRows """
=======
    m_moodyRatingAbove = ""
    m_moodyRatingBelow = ""
    m_spRatingAbove = ""
    m_spRatingBelow = ""
    m_maturityDateAbove = ""
    m_maturityDateBelow = ""
    m_couponRateAbove = Double.MAX_VALUE
    m_couponRateBelow = Double.MAX_VALUE
    m_excludeConvertible = ""
    m_scannerSettingPairs = ""
    m_stockTypeFilter = ""

    @overloaded
    def numberOfRows(self):
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_numberOfRows

    @overloaded
    def instrument(self):
<<<<<<< HEAD
        """ generated source for method instrument """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_instrument

    @overloaded
    def locationCode(self):
<<<<<<< HEAD
        """ generated source for method locationCode """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_locationCode

    @overloaded
    def scanCode(self):
<<<<<<< HEAD
        """ generated source for method scanCode """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_scanCode

    @overloaded
    def abovePrice(self):
<<<<<<< HEAD
        """ generated source for method abovePrice """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_abovePrice

    @overloaded
    def belowPrice(self):
<<<<<<< HEAD
        """ generated source for method belowPrice """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_belowPrice

    @overloaded
    def aboveVolume(self):
<<<<<<< HEAD
        """ generated source for method aboveVolume """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_aboveVolume

    @overloaded
    def averageOptionVolumeAbove(self):
<<<<<<< HEAD
        """ generated source for method averageOptionVolumeAbove """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_averageOptionVolumeAbove

    @overloaded
    def marketCapAbove(self):
<<<<<<< HEAD
        """ generated source for method marketCapAbove """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_marketCapAbove

    @overloaded
    def marketCapBelow(self):
<<<<<<< HEAD
        """ generated source for method marketCapBelow """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_marketCapBelow

    @overloaded
    def moodyRatingAbove(self):
<<<<<<< HEAD
        """ generated source for method moodyRatingAbove """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_moodyRatingAbove

    @overloaded
    def moodyRatingBelow(self):
<<<<<<< HEAD
        """ generated source for method moodyRatingBelow """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_moodyRatingBelow

    @overloaded
    def spRatingAbove(self):
<<<<<<< HEAD
        """ generated source for method spRatingAbove """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_spRatingAbove

    @overloaded
    def spRatingBelow(self):
<<<<<<< HEAD
        """ generated source for method spRatingBelow """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_spRatingBelow

    @overloaded
    def maturityDateAbove(self):
<<<<<<< HEAD
        """ generated source for method maturityDateAbove """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_maturityDateAbove

    @overloaded
    def maturityDateBelow(self):
<<<<<<< HEAD
        """ generated source for method maturityDateBelow """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_maturityDateBelow

    @overloaded
    def couponRateAbove(self):
<<<<<<< HEAD
        """ generated source for method couponRateAbove """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_couponRateAbove

    @overloaded
    def couponRateBelow(self):
<<<<<<< HEAD
        """ generated source for method couponRateBelow """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_couponRateBelow

    @overloaded
    def excludeConvertible(self):
<<<<<<< HEAD
        """ generated source for method excludeConvertible """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_excludeConvertible

    @overloaded
    def scannerSettingPairs(self):
<<<<<<< HEAD
        """ generated source for method scannerSettingPairs """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        return self.m_scannerSettingPairs

    @overloaded
    def stockTypeFilter(self):
<<<<<<< HEAD
        """ generated source for method stockTypeFilter """
        return self.m_stockTypeFilter

    #  Set
    @numberOfRows.register(object, int)
    def numberOfRows_0(self, num):
        """ generated source for method numberOfRows_0 """
=======
        return self.m_stockTypeFilter

    @numberOfRows.register(object, int)
    def numberOfRows_0(self, num):
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_numberOfRows = num

    @instrument.register(object, str)
    def instrument_0(self, txt):
<<<<<<< HEAD
        """ generated source for method instrument_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_instrument = txt

    @locationCode.register(object, str)
    def locationCode_0(self, txt):
<<<<<<< HEAD
        """ generated source for method locationCode_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_locationCode = txt

    @scanCode.register(object, str)
    def scanCode_0(self, txt):
<<<<<<< HEAD
        """ generated source for method scanCode_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_scanCode = txt

    @abovePrice.register(object, float)
    def abovePrice_0(self, price):
<<<<<<< HEAD
        """ generated source for method abovePrice_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_abovePrice = price

    @belowPrice.register(object, float)
    def belowPrice_0(self, price):
<<<<<<< HEAD
        """ generated source for method belowPrice_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_belowPrice = price

    @aboveVolume.register(object, int)
    def aboveVolume_0(self, volume):
<<<<<<< HEAD
        """ generated source for method aboveVolume_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_aboveVolume = volume

    @averageOptionVolumeAbove.register(object, int)
    def averageOptionVolumeAbove_0(self, volume):
<<<<<<< HEAD
        """ generated source for method averageOptionVolumeAbove_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_averageOptionVolumeAbove = volume

    @marketCapAbove.register(object, float)
    def marketCapAbove_0(self, cap):
<<<<<<< HEAD
        """ generated source for method marketCapAbove_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_marketCapAbove = cap

    @marketCapBelow.register(object, float)
    def marketCapBelow_0(self, cap):
<<<<<<< HEAD
        """ generated source for method marketCapBelow_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_marketCapBelow = cap

    @moodyRatingAbove.register(object, str)
    def moodyRatingAbove_0(self, r):
<<<<<<< HEAD
        """ generated source for method moodyRatingAbove_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_moodyRatingAbove = r

    @moodyRatingBelow.register(object, str)
    def moodyRatingBelow_0(self, r):
<<<<<<< HEAD
        """ generated source for method moodyRatingBelow_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_moodyRatingBelow = r

    @spRatingAbove.register(object, str)
    def spRatingAbove_0(self, r):
<<<<<<< HEAD
        """ generated source for method spRatingAbove_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_spRatingAbove = r

    @spRatingBelow.register(object, str)
    def spRatingBelow_0(self, r):
<<<<<<< HEAD
        """ generated source for method spRatingBelow_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_spRatingBelow = r

    @maturityDateAbove.register(object, str)
    def maturityDateAbove_0(self, d):
<<<<<<< HEAD
        """ generated source for method maturityDateAbove_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_maturityDateAbove = d

    @maturityDateBelow.register(object, str)
    def maturityDateBelow_0(self, d):
<<<<<<< HEAD
        """ generated source for method maturityDateBelow_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_maturityDateBelow = d

    @couponRateAbove.register(object, float)
    def couponRateAbove_0(self, r):
<<<<<<< HEAD
        """ generated source for method couponRateAbove_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_couponRateAbove = r

    @couponRateBelow.register(object, float)
    def couponRateBelow_0(self, r):
<<<<<<< HEAD
        """ generated source for method couponRateBelow_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_couponRateBelow = r

    @excludeConvertible.register(object, str)
    def excludeConvertible_0(self, c):
<<<<<<< HEAD
        """ generated source for method excludeConvertible_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_excludeConvertible = c

    @scannerSettingPairs.register(object, str)
    def scannerSettingPairs_0(self, val):
<<<<<<< HEAD
        """ generated source for method scannerSettingPairs_0 """
=======
>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
        self.m_scannerSettingPairs = val

    @stockTypeFilter.register(object, str)
    def stockTypeFilter_0(self, val):
<<<<<<< HEAD
        """ generated source for method stockTypeFilter_0 """
        self.m_stockTypeFilter = val

=======
        self.m_stockTypeFilter = val


>>>>>>> 20ffc5bc49675c47bd2ac3241f31212183085465
