from sqlalchemy import Column, Integer, Numeric, Unicode, Identity
from sqlalchemy.dialects.mssql import DATE, DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class FactRecurringDonorStatus(Base):
    __tablename__ = "FactRecurringDonorStatus"
    __table_args__ = {"schema": "RaisersEdge.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    gift_id = Column(Unicode(100), nullable=False)
    constituent_id = Column(Unicode(100), nullable=False)
    recurring_gift_start_date = Column(DATE, nullable=False)
    recurring_gift_status = Column(Unicode(100), nullable=False)
    recurring_gift_status_date = Column(DATE, nullable=True)
    qrecid = Column(Integer, nullable=False)
    record_active_ind = Column(Integer, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)
    record_deleted_datetime = Column(DATETIME2, nullable=True)


class StageFactRecurringDonorStatus(Base):
    __tablename__ = "StageFactRecurringDonorStatus"
    __table_args__ = {"schema": "RaisersEdge.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    gift_id = Column(Unicode(100), nullable=False)
    constituent_id = Column(Unicode(100), nullable=False)
    recurring_gift_start_date = Column(DATE, nullable=False)
    recurring_gift_status = Column(Unicode(100), nullable=False)
    recurring_gift_status_date = Column(DATE, nullable=True)
    qrecid = Column(Integer, nullable=False)
    record_active_ind = Column(Integer, nullable=False)
