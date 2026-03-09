from sqlalchemy import Column, Integer, Unicode, Identity
from sqlalchemy.dialects.mssql import DATE, DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DimConstituentEmail(Base):
    __tablename__ = "DimConstituentEmail"
    __table_args__ = {"schema": "RaisersEdge.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    constituent_id = Column(Unicode(100), nullable=False)
    email_address = Column(Unicode(254), nullable=False)
    qrecid = Column(Integer, nullable=False)
    record_active_ind = Column(Integer, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)
    record_deleted_datetime = Column(DATETIME2, nullable=True)


class StageDimConstituentEmail(Base):
    __tablename__ = "StageDimConstituentEmail"
    __table_args__ = {"schema": "RaisersEdge.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    constituent_id = Column(Unicode(100), nullable=False)
    email_address = Column(Unicode(254), nullable=False)
    qrecid = Column(Integer, nullable=False)
    record_active_ind = Column(Integer, nullable=False)
