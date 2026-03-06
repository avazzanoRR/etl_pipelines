from sqlalchemy import Column, Integer, Unicode, Identity, Numeric
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RptPodcastDayEpisodeDMA(Base):
    __tablename__ = "RptPodcastDayEpisodeDMA"
    __table_args__ = {"schema":"Triton.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    reporting_week = Column(DATE, nullable=False)
    reporting_date = Column(DATE, nullable=False)
    published_date = Column(DATE, nullable=False)
    dma = Column(Unicode(100), nullable=False)
    program_name = Column(Unicode(500), nullable=False)
    episode_title = Column(Unicode(None), nullable=False)
    downloads = Column(Integer, nullable=False)
    downloaders = Column(Integer, nullable=False)
    downloaded_hours = Column(Numeric(18,2), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)



class StageRptPodcastDayEpisodeDMA(Base):
    __tablename__ = "StageRptPodcastDayEpisodeDMA"
    __table_args__ = {"schema":"Triton.dbo"}

    id = Column(Integer, primary_key=True)
    reporting_week = Column(DATE, nullable=False)
    reporting_date = Column(DATE, nullable=False)
    published_date = Column(DATE, nullable=False)
    dma = Column(Unicode(100), nullable=False)
    program_name = Column(Unicode(500), nullable=False)
    episode_title = Column(Unicode(None), nullable=False)
    downloads = Column(Integer, nullable=False)
    downloaders = Column(Integer, nullable=False)
    downloaded_hours = Column(Numeric(18,2), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
