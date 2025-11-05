from sqlalchemy import Column, ForeignKey, Integer, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, mapper
import model


metadata = MetaData()

Base = declarative_base()

# classical mapper
order_lines = Table(
    'order_lines', metadata, 
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sku', String(255)),
    Column('qty', Integer, nullable=False),
    Column('orderid', String(255)),
)

# depends on orm
class Order(Base):
    id = Column(Integer, primary_key=True)

class OrderLine(Base):
    id = Column(Integer, primary_key=True)
    sku = Column(String(250))
    qty = Integer(String(250))
    order_id = Column(Integer, ForeignKey('order.id'))
    order = relationship(Order)

class Allocation(Base):
    ...


def start_mappers():
    lines_mapper = mapper(model.OrderLine, order_lines)