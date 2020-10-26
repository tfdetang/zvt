# -*- coding: utf-8 -*-
# this file is generated by gen_kdata_schema function, dont't change it
from sqlalchemy.ext.declarative import declarative_base

from zvt.contract.register import register_schema
from zvt.domain.quotes import StockKdataCommon

KdataBase = declarative_base()


class Stock15mHfqKdata(KdataBase, StockKdataCommon):
    __tablename__ = 'stock_15m_hfq_kdata'


register_schema(providers=['joinquant'], db_name='stock_15m_hfq_kdata', schema_base=KdataBase)

__all__ = ['Stock15mHfqKdata']
# the __all__ is generated
__all__ = ['Stock15mHfqKdata']