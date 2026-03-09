from sqlalchemy import Column, Integer, Identity
from sqlalchemy.dialects.mssql import DATETIME2, DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class FactContactTag(Base):
    __tablename__ = "FactContactTag"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    contact_id = Column(Integer, nullable=False)
    tag_id = Column(Integer, nullable=False)
    tag_applied_timestamp = Column(DATETIME2, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageFactContactTag(Base):
    __tablename__ = "StageFactContactTag"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, nullable=False)
    tag_id = Column(Integer, nullable=False)
    tag_applied_timestamp = Column(DATETIME2, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
