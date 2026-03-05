from sqlalchemy import Column, Integer, Identity, Numeric, Unicode
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RptStandardReportSummaryCountry(Base):
    __tablename__ = "RptStandardReportSummaryCountry"
    __table_args__ = {"schema":"GoogleAnalytics.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    week_start_date = Column(DATE, nullable=False)
    week_end_date = Column(DATE, nullable=False)
    country = Column(Unicode(100), nullable=False)
    total_users_count = Column(Integer, nullable=False)
    active_users_count = Column(Integer, nullable=False)
    new_users_count = Column(Integer, nullable=False)
    total_sessions = Column(Integer, nullable=False)
    page_views_count = Column(Integer, nullable=False)
    page_views_per_user = Column(Numeric(18,2), nullable=False)
    avg_time_on_page = Column(Numeric(18,2), nullable=False)
    bounce_rate = Column(Numeric(18,2), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)


class StageRptStandardReportSummaryCountry(Base):
    __tablename__ = "StageRptStandardReportSummaryCountry"
    __table_args__ = {"schema":"GoogleAnalytics.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    week_start_date = Column(DATE, nullable=False)
    week_end_date = Column(DATE, nullable=False)
    country = Column(Unicode(100), nullable=False)
    total_users_count = Column(Integer, nullable=False)
    active_users_count = Column(Integer, nullable=False)
    new_users_count = Column(Integer, nullable=False)
    total_sessions = Column(Integer, nullable=False)
    page_views_count = Column(Integer, nullable=False)
    page_views_per_user = Column(Numeric(18,2), nullable=False)
    avg_time_on_page = Column(Numeric(18,2), nullable=False)
    bounce_rate = Column(Numeric(18,2), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)

