from sqlalchemy import Column, Integer, Unicode, Identity
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DimForm(Base):
    __tablename__ = "DimForm"
    __table_args__ = {"schema":"WordPress.dbo"}
    
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    form_id = Column(Integer, nullable=False)
    form_name = Column(Unicode(100), nullable=False)
    ac_campaign_name = Column(Unicode(100), nullable=True)
    active_status = Column(Integer, nullable=False)
    special_status = Column(Integer, nullable=True)
    digital_campaign_ind = Column(Integer, nullable=True)
    address_ind = Column(Integer, nullable=True)
    source_data_datetime = Column(DATETIME2(7), nullable=False)
    record_insert_datetime = Column(DATETIME2(7), nullable=False)
    record_deleted_datetime = Column(DATETIME2(7), nullable=True)


class StageDimForm(Base):
    __tablename__ = "StageDimForm"
    __table_args__ = {"schema":"WordPress.dbo"}
    
    id = Column(Integer, primary_key=True)
    form_id = Column(Integer, nullable=False)
    form_name = Column(Unicode(100), nullable=False)
    ac_campaign_name = Column(Unicode(100), nullable=True)
    active_status = Column(Integer, nullable=False)
    special_status = Column(Integer, nullable=True)
    digital_campaign_ind = Column(Integer, nullable=True)
    address_ind = Column(Integer, nullable=True)
    source_data_datetime = Column(DATETIME2(7), nullable=False)