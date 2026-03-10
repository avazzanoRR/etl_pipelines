from sqlalchemy import Column, Integer, Unicode, Identity
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RptPosts(Base):
    __tablename__ = 'RptPosts'
    __table_args__ = {'schema': 'VideoStats.dbo'}
                                   
    id = Column(Integer, Identity(start=1,increment=1), primary_key=True)
    tweet_id = Column(Unicode(50), nullable=False)
    tweet_permalink = Column(Unicode(100), nullable=False)
    tweet_text = Column(Unicode(4000), nullable=False)
    video_program = Column(Unicode(50), nullable=False)
    published_datetime = Column(DATETIME2, nullable=False)
    tweet_lifetime_impressions = Column(Integer, nullable=False)
    tweet_lifetime_engagements = Column(Integer, nullable=False)
    tweet_lifetime_media_views = Column(Integer, nullable=False)
    post_lifespan = Column(Integer, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageRptPosts(Base):
    __tablename__ = 'StageRptPosts'
    __table_args__ = {'schema': 'VideoStats.dbo'}
                                   
    id = Column(Integer, primary_key=True)
    tweet_id = Column(Unicode(50), nullable=False)
    tweet_permalink = Column(Unicode(100), nullable=False)
    tweet_text = Column(Unicode(4000), nullable=False)
    video_program = Column(Unicode(50), nullable=False)
    published_datetime = Column(DATETIME2, nullable=False)
    tweet_lifetime_impressions = Column(Integer, nullable=False)
    tweet_lifetime_engagements = Column(Integer, nullable=False)
    tweet_lifetime_media_views = Column(Integer, nullable=False)
    post_lifespan = Column(Integer, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)