from sqlalchemy import Column, Integer, Identity, Numeric, Unicode
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RptPodcastWeekCountryDMARegion(Base):
    __tablename__ = "RptPodcastWeekCountryDMARegion"
    __table_args__ = {"schema":"Triton.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    week = Column(DATE, nullable=False)
    country = Column(Unicode(100), nullable=False)
    dma = Column(Unicode(100), nullable=False)
    region = Column(Unicode(100), nullable=False)
    downloads = Column(Integer, nullable=False)
    downloaders = Column(Integer, nullable=False)
    downloaded_hours = Column(Numeric(18,2), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)


class StageRptPodcastWeekCountryDMARegion(Base):
    __tablename__ = "StageRptPodcastWeekCountryDMARegion"
    __table_args__ = {"schema":"Triton.dbo"}

    id = Column(Integer, primary_key=True)
    week = Column(DATE, nullable=False)
    country = Column(Unicode(100), nullable=False)
    dma = Column(Unicode(100), nullable=False)
    region = Column(Unicode(100), nullable=False)
    downloads = Column(Integer, nullable=False)
    downloaders = Column(Integer, nullable=False)
    downloaded_hours = Column(Numeric(18,2), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
