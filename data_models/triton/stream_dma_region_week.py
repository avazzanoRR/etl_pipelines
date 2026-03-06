from sqlalchemy import Column, Integer, Unicode, Identity, Numeric
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RptStreamDMARegionWeek(Base):
    __tablename__ = "RptStreamDMARegionWeek"
    __table_args__ = {"schema":"Triton.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    dma = Column(Unicode(100), nullable=False)
    region = Column(Unicode(100), nullable=False)
    week = Column(DATE, nullable=False)
    daypart = Column(Unicode(100), nullable=False)
    tlh = Column(Numeric(18,2), nullable=False)
    cume = Column(Integer, nullable=False)
    ss = Column(Integer, nullable=False)
    aas = Column(Numeric(18,2), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageRptStreamDMARegionWeek(Base):
    __tablename__ = "StageRptStreamDMARegionWeek"
    __table_args__ = {"schema":"Triton.dbo"}

    id = Column(Integer, primary_key=True)
    dma = Column(Unicode(100), nullable=False)
    region = Column(Unicode(100), nullable=False)
    week = Column(DATE, nullable=False)
    daypart = Column(Unicode(100), nullable=False)
    tlh = Column(Numeric(18,2), nullable=False)
    cume = Column(Integer, nullable=False)
    ss = Column(Integer, nullable=False)
    aas = Column(Numeric(18,2), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
