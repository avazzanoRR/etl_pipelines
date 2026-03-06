from sqlalchemy import Column, Integer, Identity, Numeric
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RptPodcastWeek(Base):
    __tablename__ = "RptPodcastWeek"
    __table_args__ = {"schema":"Triton.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    week = Column(DATE, nullable=False)
    downloads = Column(Integer, nullable=False)
    downloaders = Column(Integer, nullable=False)
    downloaded_hours = Column(Numeric(18,2), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageRptPodcastWeek(Base):
    __tablename__ = "StageRptPodcastWeek"
    __table_args__ = {"schema":"Triton.dbo"}

    id = Column(Integer, primary_key=True)
    week = Column(DATE, nullable=False)
    downloads = Column(Integer, nullable=False)
    downloaders = Column(Integer, nullable=False)
    downloaded_hours = Column(Numeric(18,2), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
