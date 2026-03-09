from sqlalchemy import Column, Integer, Identity, UnicodeText
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class FactListUpdate(Base):
    __tablename__ = "FactListUpdate"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    contact_id = Column(Integer, nullable=False)
    list_id = Column(Integer, nullable=False)
    list_status_updated_timestamp = Column(DATETIME2, nullable=True)
    list_status_id = Column(Integer, nullable=False)
    unsubscribe_campaign_id  = Column(Integer, nullable=True)
    unsubscribe_message_id = Column(Integer, nullable=True)
    unsubscribe_reason = Column(UnicodeText, nullable=True)
    unsubscriber_ip4_number = Column(UnicodeText, nullable=True)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageFactListUpdate(Base):
    __tablename__ = "StageFactListUpdate"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, nullable=False)
    list_id = Column(Integer, nullable=False)
    list_status_updated_timestamp = Column(DATETIME2, nullable=True)
    list_status_id = Column(Integer, nullable=False)
    unsubscribe_campaign_id = Column(Integer, nullable=True)
    unsubscribe_message_id = Column(Integer, nullable=True)
    unsubscribe_reason = Column(UnicodeText, nullable=True)
    unsubscriber_ip4_number = Column(UnicodeText, nullable=True)
    source_data_datetime = Column(DATETIME2, nullable=False)
