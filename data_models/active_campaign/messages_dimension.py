from sqlalchemy import Column, Integer, UnicodeText, Identity
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DimMessage(Base):
    __tablename__ = "DimMessage"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    message_id = Column(Integer, nullable=False)
    message_created_datetime = Column(DATETIME2, nullable=False)
    message_name = Column(UnicodeText, nullable=True)
    subject_line_text = Column(UnicodeText, nullable=True)
    subject_preheader_text = Column(UnicodeText, nullable = True)
    from_name = Column(UnicodeText, nullable=True)
    from_email_address = Column(UnicodeText, nullable=True)
    reply_to_email_address = Column(UnicodeText, nullable=True)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageDimMessage(Base):
    __tablename__ = "StageDimMessage"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, primary_key=True)
    message_id = Column(Integer, nullable=False)
    message_created_datetime = Column(DATETIME2, nullable=False)
    message_name = Column(UnicodeText, nullable=True)
    subject_line_text = Column(UnicodeText, nullable=True)
    subject_preheader_text = Column(UnicodeText, nullable = True)
    from_name = Column(UnicodeText, nullable=True)
    from_email_address = Column(UnicodeText, nullable=True)
    reply_to_email_address = Column(UnicodeText, nullable=True)
    source_data_datetime = Column(DATETIME2, nullable=False)
