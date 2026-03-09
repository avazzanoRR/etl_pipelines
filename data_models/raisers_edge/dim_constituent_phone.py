from sqlalchemy import Column, Integer, Unicode, Identity
from sqlalchemy.dialects.mssql import DATE, DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DimConstituentPhone(Base):
    __tablename__ = "DimConstituentPhone"
    __table_args__ = {"schema": "RaisersEdge.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    constituent_id = Column(Unicode(100), nullable=False)
    phone_number = Column(Unicode(50), nullable=False)
    qrecid = Column(Integer, nullable=False)
    record_active_ind = Column(Integer, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)
    record_deleted_datetime = Column(DATETIME2, nullable=True)


class StageDimConstituentPhone(Base):
    __tablename__ = "StageDimConstituentPhone"
    __table_args__ = {"schema": "RaisersEdge.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    constituent_id = Column(Unicode(100), nullable=False)
    phone_number = Column(Unicode(50), nullable=True)
    qrecid = Column(Integer, nullable=True)
    record_active_ind = Column(Integer, nullable=False)
