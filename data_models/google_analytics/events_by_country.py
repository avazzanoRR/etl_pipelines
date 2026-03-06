from sqlalchemy import Column, Integer, Unicode, Identity, Numeric
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RptEventsByCountry(Base):
    __tablename__ = "RptEventsByCountry"
    __table_args__ = {"schema":"GoogleAnalytics.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    week_start_date = Column(DATE, nullable=False)
    week_end_date = Column(DATE, nullable=False)
    country = Column(Unicode(100), nullable=False)
    platform = Column(Unicode(100), nullable=False)
    event_name = Column(Unicode(500), nullable=False)
    event_count = Column(Integer, default=None)
    event_count_per_user = Column(Numeric(18,2), default=None)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)


class StageRptEventsByCountry(Base):
    __tablename__ = "StageRptEventsByCountry"
    __table_args__ = {"schema":"GoogleAnalytics.dbo"}

    id = Column(Integer, primary_key=True)
    week_start_date = Column(DATE, default=None)
    week_end_date = Column(DATE, default=None)
    country = Column(Unicode(100), default=None)
    platform = Column(Unicode(100), default=None)
    event_name = Column(Unicode(500), default=None)
    event_count = Column(Integer, default=None)
    event_count_per_user = Column(Numeric(18,2), default=None)
    source_data_datetime = Column(DATETIME2, default=None)
