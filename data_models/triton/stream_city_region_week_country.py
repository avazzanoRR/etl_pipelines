from sqlalchemy import Column, Integer, Unicode, Identity, Numeric
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RptStreamCityRegionWeekCountry(Base):
    __tablename__ = "RptStreamCityRegionWeekCountry"
    __table_args__ = {"schema":"Triton.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    country = Column(Unicode(100), nullable=False)
    city = Column(Unicode(100), nullable=False)
    region = Column(Unicode(100), nullable=False)
    week = Column(DATE, nullable=False)
    daypart = Column(Unicode(100), nullable=False)
    tlh = Column(Numeric(18,2), nullable=False)
    cume = Column(Integer, nullable=False)
    ss = Column(Integer, nullable=False)
    aas = Column(Numeric(18,2), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)


class StageRptStreamCityRegionWeekCountry(Base):
    __tablename__ = "StageRptStreamCityRegionWeekCountry"
    __table_args__ = {"schema":"Triton.dbo"}

    id = Column(Integer, primary_key=True)
    country = Column(Unicode(100), nullable=False)
    city = Column(Unicode(100), nullable=False)
    region = Column(Unicode(100), nullable=False)
    week = Column(DATE, nullable=False)
    daypart = Column(Unicode(100), nullable=False)
    tlh = Column(Numeric(18,2), nullable=False)
    cume = Column(Integer, nullable=False)
    ss = Column(Integer, nullable=False)
    aas = Column(Numeric(18,2), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
