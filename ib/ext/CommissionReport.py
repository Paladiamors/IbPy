#!/usr/bin/env python
""" generated source for module CommissionReport """
# 
#  * CommissionReport.java
#  *
#  
# package: com.ib.client
class CommissionReport(object):
    """ generated source for class CommissionReport """
    m_execId = ""
    m_commission = 0.0
    m_currency = ""
    m_realizedPNL = 0.0
    m_yield = 0.0
    m_yieldRedemptionDate = 0

    #  YYYYMMDD format
    def __init__(self):
        """ generated source for method __init__ """
        self.m_commission = 0
        self.m_realizedPNL = 0
        self.m_yield = 0
        self.m_yieldRedemptionDate = 0

    def __eq__(self, p_other):
        """ generated source for method equals """
        l_bRetVal = False
        if p_other == None:
            l_bRetVal = False
        elif self == p_other:
            l_bRetVal = True
        else:
            #manualy edited this
            l_bRetVal = self.m_execId == p_other.m_execId
        return l_bRetVal

