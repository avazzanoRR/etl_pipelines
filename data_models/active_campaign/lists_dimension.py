from sqlalchemy import Column, Integer, UnicodeText, Identity, Unicode
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DimList(Base):
    __tablename__ = "DimList"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    list_id = Column(Integer, nullable=False)
    list_name = Column(Unicode(100), nullable=False)
    list_description = Column(UnicodeText, nullable=False)
    list_created_datetime = Column(DATETIME2, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageDimList(Base):
    __tablename__ = "StageDimList"
    __table_args__ = {"schema":"ActiveCampaign.dbo"}

    id = Column(Integer, primary_key=True)
    list_id = Column(Integer, nullable=False)
    list_name = Column(Unicode(100), nullable=False)
    list_description = Column(UnicodeText, nullable=False)
    list_created_datetime = Column(DATETIME2, nullable=False)
    source_data_datetime = Column(DATETIME2, nullable=False)
