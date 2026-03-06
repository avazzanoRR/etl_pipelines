from sqlalchemy import Column, Integer, Unicode, Identity, Numeric
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RptStreamWeekStationDistributorPlayerPlatformCountry(Base):
    __tablename__ = "RptStreamWeekStationDistributorPlayerPlatformCountry"
    __table_args__ = {"schema":"Triton.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    week = Column(DATE, nullable=False)
    station = Column(Unicode(50), nullable=False)
    distributor = Column(Unicode, nullable=False)
    player = Column(Unicode(100), nullable=False)
    platform = Column(Unicode(100), nullable=False)
    country = Column(Unicode(100), nullable=False)
    daypart = Column(Unicode(50), nullable=False)
    tlh = Column(Numeric(18,2), nullable=False)
    cume = Column(Integer, nullable=False)
    ss = Column(Integer, nullable=False)
    aas = Column(Numeric(18,2), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=True)


class StageStreamWeekStationDistributorPlayerPlatformCountry(Base):
    __tablename__ = "StageStreamWeekStationDistributorPlayerPlatformCountry"
    __table_args__ = {"schema":"Triton.dbo"}

    id = Column(Integer, primary_key=True)
    week = Column(DATE, nullable=False)
    station = Column(Unicode(50), nullable=False)
    distributor = Column(Unicode, nullable=False)
    player = Column(Unicode(100), nullable=False)
    platform = Column(Unicode(100), nullable=False)
    country = Column(Unicode(100), nullable=False)
    daypart = Column(Unicode(50), nullable=False)
    tlh = Column(Numeric(18,2), nullable=False)
    cume = Column(Integer, nullable=False)
    ss = Column(Integer, nullable=False)
    aas = Column(Numeric(18,2), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
