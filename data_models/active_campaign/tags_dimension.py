from sqlalchemy import Column, Integer, UnicodeText, Identity, Unicode
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DimTag(Base):
    __tablename__ = "DimTag"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    tag_id = Column(Integer, nullable=False)
    tag_name = Column(Unicode(100), nullable=False)
    tag_description = Column(UnicodeText, nullable=True)
    tag_type = Column(Unicode(100), nullable = True)
    tag_sub_type = Column(Unicode(100), nullable = True)
    tag_created_datetime = Column(DATETIME2, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageDimTag(Base):
    __tablename__ = "StageDimTag"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, primary_key=True)
    tag_id = Column(Integer, nullable=False)
    tag_name = Column(Unicode(100), nullable=False)
    tag_description = Column(UnicodeText, nullable=True)
    tag_type = Column(Unicode(100), nullable = True)
    tag_sub_type = Column(Unicode(100), nullable = True)
    tag_created_datetime = Column(DATETIME2, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
