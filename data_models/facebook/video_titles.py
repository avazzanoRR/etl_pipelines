from sqlalchemy import Column, Integer, Numeric, Unicode, Identity
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DimFacebookVideoTitles(Base):
    __tablename__ = 'DimFacebookVideoTitles'
    __table_args__ = {'schema': 'VideoStats.dbo'}
                                   
    id = Column(Integer,Identity(start=1, increment=1), primary_key=True)
    universal_video_id = Column(Unicode(100), nullable=False)
    page_id = Column(Unicode(100), nullable=False)
    page_name = Column(Unicode(100), nullable=False)
    video_title = Column(Unicode(1000), nullable=False)
    video_program = Column(Unicode(100), nullable=False)
    published_datetime = Column(DATETIME2, nullable=False)
    published_week_date = Column(DATE, nullable=False)
    video_duration_seconds = Column(Numeric(18,4), nullable=False)
    video_duration_hours = Column(Numeric(18,4), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=True)



class StageDimFacebookVideoTitles(Base):
    __tablename__ = 'StageDimFacebookVideoTitles'
    __table_args__ = {'schema': 'VideoStats.dbo'}
                                   
    id = Column(Integer, primary_key=True)
    universal_video_id = Column(Unicode(100), nullable=False)
    page_id = Column(Unicode(100), nullable=False)
    page_name = Column(Unicode(100), nullable=False)
    video_title = Column(Unicode(1000), nullable=False)
    video_program = Column(Unicode(100), nullable=False)
    published_datetime = Column(DATETIME2, nullable=False)
    published_week_date = Column(DATE, nullable=False)
    video_duration_seconds = Column(Numeric(18, 4), nullable=False)
    video_duration_hours = Column(Numeric(18, 4), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)