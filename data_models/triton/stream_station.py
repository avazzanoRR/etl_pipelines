from sqlalchemy import Column, Integer, Unicode, Identity, Numeric
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RptStreamStation(Base):
    __tablename__ = "RptStreamStation"
    __table_args__ = {"schema":"Triton.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    reporting_date_start = Column(DATE, nullable=False)
    reporting_date_end = Column(DATE, nullable=False)
    station = Column(Unicode(50), nullable=False)
    period_type = Column(Unicode(50), nullable=False)
    daypart = Column(Unicode(50), nullable=False)
    tlh = Column(Numeric(18,2), nullable=False)
    cume = Column(Integer, nullable=False)
    ss = Column(Integer, nullable=False)
    aas = Column(Numeric(18,2), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageRptStreamStation(Base):
    __tablename__ = "StageRptStreamStation"
    __table_args__ = {"schema":"Triton.dbo"}

    id = Column(Integer, primary_key=True)
    reporting_date_start = Column(DATE, nullable=False)
    reporting_date_end = Column(DATE, nullable=False)
    station = Column(Unicode(50), nullable=False)
    period_type = Column(Unicode(50), nullable=False)
    daypart = Column(Unicode(50), nullable=False)
    tlh = Column(Numeric(18,2), nullable=False)
    cume = Column(Integer, nullable=False)
    ss = Column(Integer, nullable=False)
    aas = Column(Numeric(18,2), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
