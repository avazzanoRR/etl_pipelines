from sqlalchemy import Column, Integer, Unicode, Identity
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DimVideoTitles(Base):
    __tablename__ = 'DimVideoTitles'
    __table_args__ = {'schema': 'VideoStats.dbo'}
                                   
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    ig_post_id = Column(Unicode(100), nullable=False)
    ig_account_id = Column(Unicode(100), nullable=False)
    ig_account_username = Column(Unicode(50), nullable=False)
    ig_account_name = Column(Unicode(50), nullable=False)
    post_description = Column(Unicode(4000), nullable=False)
    reel_program = Column(Unicode(50), nullable=False)
    reel_duration_seconds = Column(Integer, nullable=False)
    published_datetime = Column(DATETIME2, nullable=False)
    post_permalink_url = Column(Unicode(100), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=True)


class StageDimVideoTitles(Base):
    __tablename__ = 'StageDimVideoTitles'
    __table_args__ = {'schema': 'VideoStats.dbo'}
                                   
    id = Column(Integer, primary_key=True, autoincrement=True)
    ig_post_id = Column(Unicode(100), nullable=False)
    ig_account_id = Column(Unicode(100), nullable=False)
    ig_account_username = Column(Unicode(50), nullable=False)
    ig_account_name = Column(Unicode(50), nullable=False)
    post_description = Column(Unicode(4000), nullable=False)
    reel_program = Column(Unicode(50), nullable=False)
    reel_duration_seconds = Column(Integer, nullable=False)
    published_datetime = Column(DATETIME2, nullable=False)
    post_permalink_url = Column(Unicode(100), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)

