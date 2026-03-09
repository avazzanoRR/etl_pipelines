from sqlalchemy import Column, Integer, Unicode, Identity, UnicodeText
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DimContact(Base):
    __tablename__ = "DimContact"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    contact_id = Column(Integer, nullable=False)
    email_address = Column(UnicodeText, nullable=False)
    first_name = Column(UnicodeText, nullable=True)
    last_name = Column(UnicodeText, nullable =True)
    created_timestamp = Column(DATETIME2, nullable=False)
    updated_timestamp = Column(DATETIME2, nullable=False)
    email_domain = Column(Unicode(100), nullable=True)
    mpp_tracking_ind = Column(Integer, nullable=True)
    email_hash_id = Column(Unicode(100), nullable=True)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageDimContact(Base):
    __tablename__ = "StageDimContact"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, primary_key=True)
    contact_id = Column(Integer, nullable=False)
    email_address = Column(UnicodeText, nullable=False)
    first_name = Column(UnicodeText, nullable=True)
    last_name = Column(UnicodeText, nullable = True)
    created_timestamp = Column(DATETIME2, nullable=False)
    updated_timestamp = Column(DATETIME2, nullable=True)
    email_domain = Column(Unicode(100), nullable=True)
    mpp_tracking_ind = Column(Integer, nullable=True)
    email_hash_id = Column(Unicode(100), nullable=True)
    source_data_datetime = Column(DATETIME2, nullable=False)

