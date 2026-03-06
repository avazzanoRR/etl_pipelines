from sqlalchemy import Column, Integer, Unicode, Numeric, String, Identity, Date, BigInteger
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RptConsumption(Base):
    __tablename__ = "RptConsumption"
    __table_args__ = {"schema":"Omny.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    week = Column(Date, nullable=False)
    network_name = Column(Unicode(100), nullable=False)
    total_clips = Column(Integer, nullable=False)
    total_listen_count = Column(Integer, nullable=False)
    total_listen_duration_milliseconds = Column(BigInteger, nullable=False)
    consumed_quarter = Column(Numeric(18, 4), nullable=False)
    consumed_half = Column(Numeric(18, 4), nullable=False)
    consumed_three_quarters = Column(Numeric(18, 4), nullable=False)
    consumed_full = Column(Numeric(18, 4), nullable=False)
    min_consumption = Column(Numeric(18, 4), nullable=False)
    average_consumption = Column(Numeric(18, 4), nullable=False)
    max_consumption = Column(Numeric(18, 4), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageRptConsumption(Base):
    __tablename__ = "StageRptConsumption"
    __table_args__ = {"schema":"Omny.dbo"}

    id = Column(Integer, primary_key=True)
    week = Column(Date, nullable=False)
    network_name = Column(Unicode(100), nullable=False)
    total_clips = Column(Integer, nullable=False)
    total_listen_count = Column(Integer, nullable=False)
    total_listen_duration_milliseconds = Column(BigInteger, nullable=False)
    consumed_quarter = Column(Numeric(18, 4), nullable=False)
    consumed_half = Column(Numeric(18, 4), nullable=False)
    consumed_three_quarters = Column(Numeric(18, 4), nullable=False)
    consumed_full = Column(Numeric(18, 4), nullable=False)
    min_consumption = Column(Numeric(18, 4), nullable=False)
    average_consumption = Column(Numeric(18, 4), nullable=False)
    max_consumption = Column(Numeric(18, 4), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
