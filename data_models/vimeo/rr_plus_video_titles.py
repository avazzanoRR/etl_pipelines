from sqlalchemy import Column, Integer, Numeric, Unicode, Identity
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DimRRPlusVideoTitles(Base):
    __tablename__ = 'DimRRPlusVideoTitles'
    __table_args__ = {"schema":"VideoStats.dbo"}

    id = Column(Integer, Identity(start=1,increment=1), primary_key=True)
    video_uri = Column(Unicode(50))
    video_title = Column(Unicode(100))
    video_published_date = Column(DATETIME2)
    video_program = Column(Unicode(50))
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)


class StageDimRRPlusVideoTitles(Base):
    __tablename__ = 'StageDimRRPlusVideoTitles'
    __table_args__ = {"schema":"VideoStats.dbo"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    video_uri = Column(Unicode(50))
    video_title = Column(Unicode(100))
    video_published_date = Column(DATETIME2)
    video_program = Column(Unicode(50))
    source_data_datetime = Column(DATETIME2, nullable=False)
