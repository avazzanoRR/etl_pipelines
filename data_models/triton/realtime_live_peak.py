from sqlalchemy import Column, Integer, Identity
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RptRealtimeLivePeak(Base):
    __tablename__ = "RptRealtimeLivePeak"
    __table_args__ = {"schema":"Triton.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    livestream_datetime = Column(DATETIME2, nullable=False)
    livestream_date = Column(DATE, nullable=False)
    livestream_hour = Column(Integer, nullable=False)
    livestream_minute = Column(Integer, nullable=False)
    peak_concurrent_value = Column(Integer, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageRptRealtimeLivePeak(Base):
    __tablename__ = "StageRptRealtimeLivePeak"
    __table_args__ = {"schema":"Triton.dbo"}

    id = Column(Integer, primary_key=True)
    livestream_datetime = Column(DATETIME2, nullable=False)
    livestream_date = Column(DATE, nullable=False)
    livestream_hour = Column(Integer, nullable=False)
    livestream_minute = Column(Integer, nullable=False)
    peak_concurrent_value = Column(Integer, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
