from sqlalchemy import Column, Integer, Unicode, Numeric, Identity
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RptVideos(Base):
    __tablename__ = 'RptVideos'
    __table_args__ = {'schema': 'VideoStats.dbo'}
                                   
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    ig_post_id = Column(Unicode(100), nullable=False)
    ig_account_id = Column(Unicode(100), nullable=False)
    ig_account_username = Column(Unicode(50), nullable=False)
    ig_account_name = Column(Unicode(50), nullable=False)
    post_permalink_url = Column(Unicode(100), nullable=False)
    post_description = Column(Unicode(4000), nullable=False)
    post_type = Column(Unicode(50), nullable=False)
    reel_program = Column(Unicode(50), nullable=False)
    reel_duration_seconds = Column(Integer, nullable=False)
    reel_duration_hours = Column(Numeric(18,2), nullable=False)
    published_datetime = Column(DATETIME2, nullable=False)
    reel_lifetime_views = Column(Integer, nullable=False)
    post_lifetime_impressions = Column(Integer, nullable=False)
    post_lifetime_reach = Column(Integer, nullable=False)
    post_lifetime_shares = Column(Integer, nullable=False)
    lifetime_follows_from_post = Column(Integer, nullable=False)
    post_lifetime_likes = Column(Integer, nullable=False)
    post_lifetime_comments = Column(Integer, nullable=False)
    post_lifetime_saves = Column(Integer, nullable=False)
    post_lifespan = Column(Integer, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageRptVideos(Base):
    __tablename__ = 'StageRptVideos'
    __table_args__ = {'schema': 'VideoStats.dbo'}
                                   
    id = Column(Integer, primary_key=True, autoincrement=True)
    ig_post_id = Column(Unicode(100), nullable=False)
    ig_account_id = Column(Unicode(100), nullable=False)
    ig_account_username = Column(Unicode(50), nullable=False)
    ig_account_name = Column(Unicode(50), nullable=False)
    post_permalink_url = Column(Unicode(100), nullable=False)
    post_description = Column(Unicode(4000), nullable=False)
    post_type = Column(Unicode(50), nullable=False)
    reel_program = Column(Unicode(50), nullable=False)
    reel_duration_seconds = Column(Integer, nullable=False)
    reel_duration_hours = Column(Numeric(18,2), nullable=False)
    published_datetime = Column(DATETIME2, nullable=False)
    reel_lifetime_views = Column(Integer, nullable=False)
    post_lifetime_impressions = Column(Integer, nullable=False)
    post_lifetime_reach = Column(Integer, nullable=False)
    post_lifetime_shares = Column(Integer, nullable=False)
    lifetime_follows_from_post = Column(Integer, nullable=False)
    post_lifetime_likes = Column(Integer, nullable=False)
    post_lifetime_comments = Column(Integer, nullable=False)
    post_lifetime_saves = Column(Integer, nullable=False)
    post_lifespan = Column(Integer, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)