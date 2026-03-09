from sqlalchemy import Column, Integer, Numeric, Unicode, Identity
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RptVideos(Base):
    __tablename__ = 'RptVideos'
    __table_args__ = {"schema":"VideoStats.dbo"}

    id = Column(Integer, Identity(start=1,increment=1), primary_key=True)
    video_uri = Column(Unicode(100), nullable=False)
    video_title = Column(Unicode(100), nullable=False)
    video_program = Column(Unicode(50), nullable=False)
    video_published_date = Column(DATE, nullable=False)
    reporting_start_date = Column(DATE, nullable=False)
    reporting_end_date = Column(DATE, nullable=False)
    video_views = Column(Integer, nullable=False)
    video_impressions = Column(Integer, nullable=False)
    total_seconds_viewed = Column(Integer, nullable=False)
    total_hours_viewed = Column(Numeric(18, 4), nullable=False)
    average_video_complete_percent = Column(Numeric(18, 4), nullable=False)
    average_seconds_viewed = Column(Integer, nullable=False)
    video_finishes = Column(Integer, nullable=False)
    video_downloads = Column(Integer, nullable=False)
    number_likes = Column(Integer, nullable=False)
    number_comments = Column(Integer, nullable=False)
    unique_video_viewers = Column(Integer, nullable=False)
    unique_video_loads = Column(Integer, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)


class StageRptVideos(Base):
    __tablename__ = 'StageRptVideos'
    __table_args__ = {"schema":"VideoStats.dbo"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    video_uri = Column(Unicode(100), nullable=False)
    video_title = Column(Unicode(100), nullable=False)
    video_program = Column(Unicode(50), nullable=False)
    video_published_date = Column(DATE, nullable=False)
    reporting_start_date = Column(DATE, nullable=False)
    reporting_end_date = Column(DATE, nullable=False)
    video_views = Column(Integer, nullable=False)
    video_impressions = Column(Integer, nullable=False)
    total_seconds_viewed = Column(Integer, nullable=False)
    total_hours_viewed = Column(Numeric(18, 4), nullable=False)
    average_video_complete_percent = Column(Numeric(18, 4), nullable=False)
    average_seconds_viewed = Column(Integer, nullable=False)
    video_finishes = Column(Integer, nullable=False)
    video_downloads = Column(Integer, nullable=False)
    number_likes = Column(Integer, nullable=False)
    number_comments = Column(Integer, nullable=False)
    unique_video_viewers = Column(Integer, nullable=False)
    unique_video_loads = Column(Integer, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)