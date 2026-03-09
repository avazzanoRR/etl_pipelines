from sqlalchemy import Column, Integer, UnicodeText, Identity
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class FactListSubscribe(Base):
    __tablename__ = "FactListSubscribe"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    contact_id = Column(Integer, nullable=False)
    list_id = Column(Integer, nullable=False)
    form_id = Column(Integer, nullable=True)
    list_subscribed_timestamp = Column(DATETIME2, nullable=True)
    subscriber_ip4_number = Column(UnicodeText, nullable=True)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)



class StageFactListSubscribe(Base):
    __tablename__ = "StageFactListSubscribe"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, nullable=False)
    list_id = Column(Integer, nullable=False)
    form_id = Column(Integer, nullable=True)
    list_subscribed_timestamp = Column(DATETIME2, nullable=True)
    subscriber_ip4_number = Column(UnicodeText, nullable=True)
    source_data_datetime = Column(DATETIME2, nullable=False)
