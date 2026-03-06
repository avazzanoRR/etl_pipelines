from sqlalchemy import Column, Integer, BigInteger, Unicode, Identity, Numeric
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RptStandardReport(Base):
    __tablename__ = "RptStandardReport"
    __table_args__ = {"schema":"GoogleAnalytics.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    week_start_date = Column(DATE, nullable=False)
    week_end_date = Column(DATE, nullable=False)
    page_title = Column(Unicode(None), nullable=False)
    page_path = Column(Unicode(None), nullable=False)
    page_path_level_1 = Column(Unicode(500), default=None)
    page_path_level_2 = Column(Unicode(500), default=None)
    page_path_level_3 = Column(Unicode(500), default=None)
    page_views_count = Column(Integer, default=None)
    active_users_count = Column(Integer, default=None)
    page_views_per_user = Column(Numeric(18,2), default=None)
    user_engagement_duration = Column(BigInteger, default=None)
    avg_engagement_time = Column(Numeric(18,2), default=None)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)



class StageRptStandardReport(Base):
    __tablename__ = "StageRptStandardReport"
    __table_args__ = {"schema":"GoogleAnalytics.dbo"}

    id = Column(Integer, primary_key=True)
    week_start_date = Column(DATE, default=None)
    week_end_date = Column(DATE, default=None)
    page_title = Column(Unicode(None), default=None)
    page_path = Column(Unicode(None), default=None)
    page_path_level_1 = Column(Unicode(500), default=None)
    page_path_level_2 = Column(Unicode(500), default=None)
    page_path_level_3 = Column(Unicode(500), default=None)
    page_views_count = Column(Integer, default=None)
    active_users_count = Column(Integer, default=None)
    page_views_per_user = Column(Numeric(18,2), default=None)
    user_engagement_duration = Column(BigInteger, default=None)
    avg_engagement_time = Column(Numeric(18,2), default=None)
    source_data_datetime = Column(DATETIME2, default=None)

