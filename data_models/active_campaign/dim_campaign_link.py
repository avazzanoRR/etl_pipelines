from sqlalchemy import Column, Integer, UnicodeText, Identity, Unicode
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DimCampaignLink(Base):
    __tablename__ = "DimCampaignLink"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    link_id = Column(Integer, nullable=False)
    campaign_id = Column(Integer, nullable=False)
    message_id = Column(Integer, nullable=False)
    link_created_datetime = Column(DATETIME2, nullable=False)
    link_url_path = Column(UnicodeText, nullable=False)
    link_name = Column(UnicodeText, nullable=True)
    link_type = Column(Unicode(100), nullable = True)
    link_sub_type = Column(Unicode(100), nullable = True)
    link_clicks_report_url = Column(UnicodeText, nullable=True)
    mpp_link_clicks_report_url = Column(UnicodeText, nullable=True)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageDimCampaignLink(Base):
    __tablename__ = "StageDimCampaignLink"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, primary_key=True)
    link_id = Column(Integer, nullable=False)
    campaign_id = Column(Integer, nullable=False)
    message_id = Column(Integer, nullable=False)
    link_created_datetime = Column(DATETIME2, nullable=False)
    link_url_path = Column(UnicodeText, nullable=False)
    link_name = Column(UnicodeText, nullable=True)
    link_type = Column(Unicode(100), nullable = True)
    link_sub_type = Column(Unicode(100), nullable = True)
    link_clicks_report_url = Column(UnicodeText, nullable=True)
    mpp_link_clicks_report_url = Column(UnicodeText, nullable=True)
    source_data_datetime = Column(DATETIME2, nullable=False)
