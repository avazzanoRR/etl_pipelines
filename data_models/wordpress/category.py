from sqlalchemy import Column, Integer, Unicode, Identity
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DimCategory(Base):
    __tablename__ = "DimCategory"
    __table_args__ = {"schema":"WordPress.dbo"}
    
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    category_id = Column(Integer, nullable=False)
    category_name = Column(Unicode(100), nullable=False)
    source_data_datetime = Column(DATETIME2(7), nullable=False)
    record_insert_datetime = Column(DATETIME2(7), nullable=False)


class StageDimCategory(Base):
    __tablename__ = "StageDimCategory"
    __table_args__ = {"schema":"WordPress.dbo"}
    
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, nullable=False)
    category_name = Column(Unicode(100), nullable=False)
    source_data_datetime = Column(DATETIME2(7), nullable=False)