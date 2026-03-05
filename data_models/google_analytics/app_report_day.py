from sqlalchemy import Column, Integer, Identity, Unicode
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RptAppReportDay(Base):
    __tablename__ = "RptAppReportDay"
    __table_args__ = {"schema":"GoogleAnalytics.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    reporting_date = Column(DATE, nullable=False)
    total_users_count = Column(Integer, nullable=False)
    active_users_count = Column(Integer, nullable=False)
    new_users_count = Column(Integer, nullable=False)
    total_sessions = Column(Integer, nullable=False)
    total_engaged_sessions = Column(Integer, nullable=False)
    mobile_os_type = Column(Unicode(50), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageRptAppReportDay(Base):
    __tablename__ = "StageRptAppReportDay"
    __table_args__ = {"schema":"GoogleAnalytics.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    reporting_date = Column(DATE, nullable=False)
    total_users_count = Column(Integer, nullable=False)
    active_users_count = Column(Integer, nullable=False)
    new_users_count = Column(Integer, nullable=False)
    total_sessions = Column(Integer, nullable=False)
    total_engaged_sessions = Column(Integer, nullable=False)
    mobile_os_type = Column(Unicode(50), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    