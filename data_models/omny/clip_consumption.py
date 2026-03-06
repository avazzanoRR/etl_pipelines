from sqlalchemy import Column, Integer, Unicode, Numeric, String, Identity, Date, BigInteger
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RptClipConsumption(Base):
    __tablename__ = "RptClipConsumption"
    __table_args__ = {"schema":"Omny.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    clip_id = Column(String(255), nullable=False)
    listens = Column(Integer, nullable=False)
    time_spent_listening = Column(BigInteger, nullable=False)
    listened_to_25_percent = Column(Numeric(18, 4), nullable=False)
    listened_to_50_percent = Column(Numeric(18, 4), nullable=False)
    listened_to_75_percent = Column(Numeric(18, 4), nullable=False)
    listened_to_100_percent = Column(Numeric(18, 4), nullable=False)
    average_completion = Column(Numeric(18, 4), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageRptClipConsumption(Base):
    __tablename__ = "StageRptClipConsumption"
    __table_args__ = {"schema":"Omny.dbo"}

    id = Column(Integer, primary_key=True)
    clip_id = Column(String(255), nullable=False)
    listens = Column(Integer, nullable=False)
    time_spent_listening = Column(BigInteger, nullable=False)
    listened_to_25_percent = Column(Numeric(18, 4), nullable=False)
    listened_to_50_percent = Column(Numeric(18, 4), nullable=False)
    listened_to_75_percent = Column(Numeric(18, 4), nullable=False)
    listened_to_100_percent = Column(Numeric(18, 4), nullable=False)
    average_completion = Column(Numeric(18, 4), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
