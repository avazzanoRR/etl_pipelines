from sqlalchemy import Column, Integer, Identity, Unicode
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RptAppReportWeekCountry(Base):
    __tablename__ = "RptAppReportWeekCountry"
    __table_args__ = {"schema":"GoogleAnalytics.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    reporting_date_start = Column(DATE, nullable=False)
    reporting_date_end = Column(DATE, nullable=False)
    total_users_count = Column(Integer, nullable=False)
    active_users_count = Column(Integer, nullable=False)
    new_users_count = Column(Integer, nullable=False)
    total_sessions = Column(Integer, nullable=False)
    total_engaged_sessions = Column(Integer, nullable=False)
    mobile_os_type = Column(Unicode(50), nullable=False)
    country = Column(Unicode(100), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)


class StageRptAppReportWeekCountry(Base):
    __tablename__ = "StageRptAppReportWeekCountry"
    __table_args__ = {"schema":"GoogleAnalytics.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    reporting_date_start = Column(DATE, nullable=False)
    reporting_date_end = Column(DATE, nullable=False)
    total_users_count = Column(Integer, nullable=False)
    active_users_count = Column(Integer, nullable=False)
    new_users_count = Column(Integer, nullable=False)
    total_sessions = Column(Integer, nullable=False)
    total_engaged_sessions = Column(Integer, nullable=False)
    mobile_os_type = Column(Unicode(50), nullable=False)
    country = Column(Unicode(100), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
