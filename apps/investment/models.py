from apps import db
from enum import Enum, unique

@unique
class TransacationType(Enum):
    """
    交易类型，分为股票和期货
    """
    Stock = 0
    Commodity = 1


@unique
class OperationType(Enum):
    """
    操作类型
    """
    Buy_S = 0 #买入股票
    Sell_S = 1 #卖出股票


class Stock(db.Model):
    """
    股票
    """

    __tablename__ = "股票信息"

    id = db.Column(db.Integer, primary_key=True)
    stock_code = db.Column(db.String(64))
    stock_name = db.Column(db.String(64))
    market_time = db.Column(db.Date)
    market_address = db.Column(db.String(64))
    established_time = db.Column(db.Date)
    province = db.Column(db.String(64))
    city = db.Column(db.String(64))
    industry_1 = db.Column(db.String(64))
    industry_2 = db.Column(db.String(64))
    industry_3 = db.Column(db.String(64))


class TransactionRecord(db.Model):

    __tablename__ = "交易记录"

    id = db.Column(db.Integer, primary_key=True)
    transaction_type = db.Column(db.String(64)) #交易类型有股票，期货
    operation_type = db.Column(db.String(64)) #操作类型，买入，卖出...
    product_code = db.Column(db.String(64)) #交易产品的代码，股票为股票代码，期货为期货代码
    product_name = db.Column(db.String(64)) #交易产品的名称
    transaction_time = db.Column(db.Date) #交易时间
    organization = db.Column(db.String(64)) #交易机构
    price = db.Column(db.Float) #交易单价
    amount = db.Column(db.Integer) #交易份额
    total_price = db.Column(db.Float) #成交总价
    profit_loss = db.Column(db.Float) #盈亏记录
    reason = db.Column(db.String(128)) #操作理由
