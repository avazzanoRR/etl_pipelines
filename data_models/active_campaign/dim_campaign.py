from sqlalchemy import cast, Column, Integer, UnicodeText, Identity, Unicode
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DimCampaign(Base):
    __tablename__ = "DimCampaign"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    campaign_id = Column(Integer, nullable=False)
    campaign_name = Column(Unicode(100), nullable = True)
    campaign_type = Column(Unicode(100), nullable=True)
    campaign_created_datetime = Column(DATETIME2, nullable=False)
    first_sent_datetime = Column(DATETIME2, nullable=False)
    last_sent_datetime = Column(DATETIME2, nullable=True)
    scheduled_ind = Column(Integer, nullable=True)
    scheduled_datetime = Column(DATETIME2, nullable=True)
    segment_id = Column(Integer, nullable=True)
    send_segment_name = Column(UnicodeText, nullable=True)
    split_type = Column(Unicode(100), nullable=True)
    split_content_ind = Column(Integer, nullable=True)
    split_offset_type = Column(Unicode(100), nullable=True)
    split_winner_messageid = Column(Integer, nullable=True)
    send_id = Column(Integer, nullable=True)
    thread_id = Column(Integer, nullable=True)
    series_id = Column(Integer, nullable=True)
    form_id = Column(Integer, nullable=True)
    marketing_program_name = Column(Unicode(100), nullable = True)
    marketing_program_type = Column(Unicode(100), nullable = True)
    marketing_program_sub_type = Column(Unicode(100), nullable = True)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)



class StageDimCampaign(Base):
    __tablename__ = "StageDimCampaign"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, nullable=False)
    campaign_name = Column(Unicode(100), nullable=True)
    campaign_type = Column(Unicode(100), nullable=True)
    campaign_created_datetime = Column(DATETIME2, nullable=False)
    first_sent_datetime = Column(DATETIME2, nullable=False)
    last_sent_datetime = Column(DATETIME2, nullable=True)
    scheduled_ind = Column(Integer, nullable=True)
    scheduled_datetime = Column(DATETIME2, nullable=True)
    segment_id = Column(Integer, nullable=True)
    send_segment_name = Column(UnicodeText, nullable=True)
    split_type = Column(Unicode(100), nullable=True)
    split_content_ind = Column(Integer, nullable=True)
    split_offset_type = Column(Unicode(100), nullable=True)
    split_winner_messageid = Column(Integer, nullable=True)
    send_id = Column(Integer, nullable=True)
    thread_id = Column(Integer, nullable=True)
    series_id = Column(Integer, nullable=True)
    form_id = Column(Integer, nullable=True)
    marketing_program_name = Column(Unicode(100), nullable = True)
    marketing_program_type = Column(Unicode(100), nullable = True)
    marketing_program_sub_type = Column(Unicode(100), nullable = True)
    source_data_datetime = Column(DATETIME2, nullable=False)
