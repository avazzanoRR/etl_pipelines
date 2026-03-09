from sqlalchemy import Column, Integer, Unicode, Identity
from sqlalchemy.dialects.mssql import DATE, DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DimConstituentPrimaryAddress(Base):
    __tablename__ = "DimConstituentPrimaryAddress"
    __table_args__ = {"schema": "RaisersEdge.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    constituent_id = Column(Unicode(100), nullable=False)
    preferred_address_line_1 = Column(Unicode(200), nullable=False)
    preferred_address_line_2 = Column(Unicode(200), nullable=False)
    preferred_city = Column(Unicode(100), nullable=False)
    preferred_state = Column(Unicode(50), nullable=False)
    preferred_zip = Column(Unicode(20), nullable=False)
    preferred_address_date_added = Column(DATE, nullable=False)
    preferred_address_date_last_changed = Column(DATE, nullable=False)
    preferred_send_mail_to_this_address = Column(Unicode(10), nullable=False)
    preferred_dpc = Column(Integer, nullable=True)
    qrecid = Column(Integer, nullable=False)
    record_active_ind = Column(Integer, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)
    record_deleted_datetime = Column(DATETIME2, nullable=True)


class StageDimConstituentPrimaryAddress(Base):
    __tablename__ = "StageDimConstituentPrimaryAddress"
    __table_args__ = {"schema": "RaisersEdge.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    constituent_id = Column(Unicode(100), nullable=False)
    preferred_address_line_1 = Column(Unicode(200), nullable=False)
    preferred_address_line_2 = Column(Unicode(200), nullable=False)
    preferred_city = Column(Unicode(100), nullable=False)
    preferred_state = Column(Unicode(50), nullable=False)
    preferred_zip = Column(Unicode(20), nullable=False)
    preferred_address_date_added = Column(DATE, nullable=False)
    preferred_address_date_last_changed = Column(DATE, nullable=False)
    preferred_send_mail_to_this_address = Column(Unicode(10), nullable=False)
    preferred_dpc = Column(Integer, nullable=True)
    qrecid = Column(Integer, nullable=False)
    record_active_ind = Column(Integer, nullable=False)
