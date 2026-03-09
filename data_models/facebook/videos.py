from sqlalchemy import Column, Integer, Numeric, Unicode, Identity
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RptVideos(Base):
    __tablename__ = 'RptVideos'
    __table_args__ = {'schema': 'VideoStats.dbo'}
                                   
    id = Column(Integer,Identity(start=1, increment=1), primary_key=True)
    universal_video_id = Column(Unicode(100), nullable=False)
    page_id = Column(Unicode(100), nullable=False)
    page_name = Column(Unicode(100), nullable=False)
    video_title = Column(Unicode(1000), nullable=False)
    video_program = Column(Unicode(50), nullable=False)
    published_datetime = Column(DATETIME2, nullable=False)
    published_week_date = Column(DATE, nullable=False)
    video_duration_seconds = Column(Numeric(18,4), nullable=False)
    video_duration_hours = Column(Numeric(18,4), nullable=False)
    video_view_date = Column(DATETIME2, nullable=False)
    reporting_week_date = Column(DATETIME2, nullable=False)
    video_impressions = Column(Integer, nullable=False)
    video_reach = Column(Integer, nullable=False)
    video_views_3_seconds_total = Column(Integer, nullable=False)
    video_views_3_seconds_boosted = Column(Integer, nullable=False)
    video_views_3_seconds_organic = Column(Integer, nullable=False)
    video_views_60_seconds = Column(Integer, nullable=False)
    video_viewers_3_seconds = Column(Integer, nullable=False)
    video_viewers_60_seconds = Column(Integer, nullable=False)
    total_seconds_viewed = Column(Numeric(18,4), nullable=False)
    total_hours_viewed = Column(Numeric(18,4), nullable=False)
    total_reactions = Column(Integer, nullable=False)
    total_comments = Column(Integer, nullable=False)
    total_shares = Column(Integer, nullable=False)
    total_reactions_comments_shares = Column(Integer, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=True)



class StageRptVideos(Base):
    __tablename__ = 'StageRptVideos'
    __table_args__ = {'schema': 'VideoStats.dbo'}
                                   
    id = Column(Integer, primary_key=True)
    universal_video_id = Column(Unicode(100), nullable=False)
    page_id = Column(Unicode(100), nullable=False)
    page_name = Column(Unicode(100), nullable=False)
    video_title = Column(Unicode(1000), nullable=False)
    video_program = Column(Unicode(50), nullable=False)
    published_datetime = Column(DATETIME2, nullable=False)
    published_week_date = Column(DATE, nullable=False)
    video_duration_seconds = Column(Numeric(18, 4), nullable=False)
    video_duration_hours = Column(Numeric(18, 4), nullable=False)
    video_view_date = Column(DATETIME2, nullable=False)
    reporting_week_date = Column(DATETIME2, nullable=False)
    video_impressions = Column(Integer, nullable=False)
    video_reach = Column(Integer, nullable=False)
    video_views_3_seconds_total = Column(Integer, nullable=False)
    video_views_3_seconds_boosted = Column(Integer, nullable=False)
    video_views_3_seconds_organic = Column(Integer, nullable=False)
    video_views_60_seconds = Column(Integer, nullable=False)
    video_viewers_3_seconds = Column(Integer, nullable=False)
    video_viewers_60_seconds = Column(Integer, nullable=False)
    total_seconds_viewed = Column(Numeric(18, 4), nullable=False)
    total_hours_viewed = Column(Numeric(18, 4), nullable=False)
    total_reactions = Column(Integer, nullable=False)
    total_comments = Column(Integer, nullable=False)
    total_shares = Column(Integer, nullable=False)
    total_reactions_comments_shares = Column(Integer, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)