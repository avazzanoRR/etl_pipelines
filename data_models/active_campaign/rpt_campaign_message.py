from sqlalchemy import Column, Integer, Identity
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RptCampaignMessage(Base):
    __tablename__ = "RptCampaignMessage"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    campaign_message_id = Column(Integer, nullable=False)
    campaign_id = Column(Integer, nullable=False)
    message_id = Column(Integer, nullable=False)
    total_sent = Column(Integer, nullable=False)
    total_opens = Column(Integer, nullable=False)
    total_verified_opens = Column(Integer, nullable=False)
    unique_opens = Column(Integer, nullable=False)
    unique_verified_opens = Column(Integer, nullable=False)
    total_link_clicks = Column(Integer, nullable=False)
    unique_link_clicks = Column(Integer, nullable=False)
    total_forwards = Column(Integer, nullable = False)
    unique_forwards = Column(Integer, nullable = False)
    total_hard_bounces= Column(Integer, nullable = False)
    total_soft_bounces= Column(Integer, nullable = False)
    total_unsubscribes = Column(Integer, nullable = False)
    total_updates = Column(Integer, nullable = False)
    total_social_shares = Column(Integer, nullable = False)
    total_replies = Column(Integer, nullable = False)
    unique_replies = Column(Integer, nullable = False)
    split_percentage = Column(Integer, nullable = False)
    initial_split_percentage = Column(Integer, nullable = False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageRptCampaignMessage(Base):
    __tablename__ = "StageRptCampaignMessage"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, primary_key=True)
    campaign_message_id = Column(Integer, nullable=False)
    campaign_id = Column(Integer, nullable=False)
    message_id = Column(Integer, nullable=False)
    total_sent = Column(Integer, nullable=False)
    total_opens = Column(Integer, nullable=False)
    total_verified_opens = Column(Integer, nullable=False)
    unique_opens = Column(Integer, nullable=False)
    unique_verified_opens = Column(Integer, nullable=False)
    total_link_clicks = Column(Integer, nullable=False)
    unique_link_clicks = Column(Integer, nullable=False)
    total_forwards = Column(Integer, nullable = False)
    unique_forwards = Column(Integer, nullable = False)
    total_hard_bounces= Column(Integer, nullable = False)
    total_soft_bounces= Column(Integer, nullable = False)
    total_unsubscribes = Column(Integer, nullable = False)
    total_updates = Column(Integer, nullable = False)
    total_social_shares = Column(Integer, nullable = False)
    total_replies = Column(Integer, nullable = False)
    unique_replies = Column(Integer, nullable = False)
    split_percentage = Column(Integer, nullable = False)
    initial_split_percentage = Column(Integer, nullable = False)
    source_data_datetime = Column(DATETIME2, nullable=False)
