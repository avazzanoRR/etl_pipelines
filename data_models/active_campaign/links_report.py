from sqlalchemy import Column, Integer, Identity
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class RptLinkClicks(Base):
    __tablename__ = "RptLinkClicks"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    link_id = Column(Integer, nullable=False)
    message_id = Column(Integer, nullable=False)
    campaign_id = Column(Integer, nullable=False)
    total_link_clicks = Column(Integer, nullable=False)
    unique_link_clicks = Column(Integer, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageRptLinkClicks(Base):
    __tablename__ = "StageRptLinkClicks"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, primary_key=True)
    link_id = Column(Integer, nullable=False)
    message_id = Column(Integer, nullable=False)
    campaign_id = Column(Integer, nullable=False)
    total_link_clicks = Column(Integer, nullable=False)
    unique_link_clicks = Column(Integer, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
