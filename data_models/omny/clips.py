from sqlalchemy import Column, Integer, Unicode, Numeric, String, Identity
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RptClips(Base):
    __tablename__ = "RptClips"
    __table_args__ = {"schema":"Omny.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    clip_id = Column(Unicode(100), nullable=False)  # called "id" in the original extract
    published_utc = Column(DATETIME2, default=None)
    clip_title = Column(Unicode(500), default=None)
    clip_description = Column(Unicode(None), default=None)
    clip_duration_seconds = Column(Numeric(18,2), default=None)
    clip_episode_type = Column(Unicode(100), default=None)
    clip_tags = Column(Unicode(100), default=None)
    program_id = Column(Unicode(100), nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageRptClips(Base):
    __tablename__ = "StageRptClips"
    __table_args__ = {"schema":"Omny.dbo"}

    id = Column(Integer, primary_key=True)
    clip_id = Column(Unicode(100), nullable=False)  # called "id" in the original extract
    published_utc = Column(DATETIME2, default=None)
    clip_title = Column(Unicode(500), default=None)
    clip_description = Column(Unicode(None), default=None)
    clip_duration_seconds = Column(Numeric(18,2), default=None)
    clip_episode_type = Column(Unicode(100), default=None)
    clip_tags = Column(Unicode(100), default=None)
    program_id = Column(Unicode(100), nullable=False)
    source_data_datetime = Column(DATETIME2, default=None)
