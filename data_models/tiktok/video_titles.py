from sqlalchemy import Column, Integer, Unicode, Identity
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DimVideoTitles(Base):
    __tablename__ = 'DimVideoTitles'
    __table_args__ = {'schema': 'VideoStats.dbo'}
                                   
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    tiktok_video_id = Column(Unicode(100), nullable=False)
    video_link = Column(Unicode(100), nullable=False)
    video_title = Column(Unicode(4000), nullable=False)
    video_program = Column(Unicode(50), nullable=False)
    published_datetime = Column(DATETIME2, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=True)


class StageDimVideoTitles(Base):
    __tablename__ = 'StageDimVideoTitles'
    __table_args__ = {'schema': 'VideoStats.dbo'}
                                   
    id = Column(Integer, primary_key=True, autoincrement=True)
    tiktok_video_id = Column(Unicode(100), nullable=False)
    video_link = Column(Unicode(100), nullable=False)
    video_title = Column(Unicode(4000), nullable=False)
    video_program = Column(Unicode(50), nullable=False)
    published_datetime = Column(DATETIME2, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)

