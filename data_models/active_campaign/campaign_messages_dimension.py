from sqlalchemy import Column, Integer, UnicodeText, Identity
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DimCampaignMessage(Base):
    __tablename__ = "DimCampaignMessage"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    campaign_message_id = Column(Integer, nullable=False)
    campaign_id = Column(Integer, nullable=False)
    message_id = Column(Integer, nullable=False)
    subject_line_text = Column(UnicodeText, nullable=True)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageDimCampaignMessage(Base):
    __tablename__ = "StageDimCampaignMessage"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    campaign_message_id = Column(Integer, nullable=False)
    campaign_id = Column(Integer, nullable=False)
    message_id = Column(Integer, nullable=False)
    subject_line_text = Column(UnicodeText, nullable=True)
    source_data_datetime = Column(DATETIME2, nullable=False)
