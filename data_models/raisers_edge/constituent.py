from sqlalchemy import Column, Integer, Unicode, Identity
from sqlalchemy.dialects.mssql import DATE, DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DimConstituent(Base):
    __tablename__ = "DimConstituent"
    __table_args__ = {"schema": "RaisersEdge.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    constituent_id = Column(Unicode(100), nullable=False)
    first_name = Column(Unicode(100), nullable=False)
    last_name = Column(Unicode(100), nullable=False)
    primary_addressee = Column(Unicode(200), nullable=False)
    primary_salutation = Column(Unicode(200), nullable=False)
    marital_status = Column(Unicode(50), nullable=False)
    sex = Column(Unicode(50), nullable=False)
    age = Column(Integer, nullable=True)
    birth_date = Column(Unicode(50), nullable=False)
    solicit_code_description = Column(Unicode(200), nullable=False)
    constituent_date_added = Column(DATE, nullable=False)
    constituent_date_last_changed = Column(DATE, nullable=False)
    spouse_first_name = Column(Unicode(100), nullable=False)
    spouse_last_name = Column(Unicode(100), nullable=False)
    spouse_birth_date = Column(Unicode(50), nullable=False)
    spouse_deceased_date = Column(Unicode(50), nullable=True)
    record_active_ind = Column(Integer, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)
    record_deleted_datetime = Column(DATETIME2, nullable=True)


class StageDimConstituent(Base):
    __tablename__ = "StageDimConstituent"
    __table_args__ = {"schema": "RaisersEdge.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    constituent_id = Column(Unicode(100), nullable=False)
    first_name = Column(Unicode(100), nullable=False)
    last_name = Column(Unicode(100), nullable=False)
    primary_addressee = Column(Unicode(200), nullable=False)
    primary_salutation = Column(Unicode(200), nullable=False)
    marital_status = Column(Unicode(50), nullable=False)
    sex = Column(Unicode(50), nullable=False)
    age = Column(Integer, nullable=True)
    birth_date = Column(Unicode(50), nullable=False)
    solicit_code_description = Column(Unicode(200), nullable=False)
    constituent_date_added = Column(DATE, nullable=False)
    constituent_date_last_changed = Column(DATE, nullable=False)
    spouse_first_name = Column(Unicode(100), nullable=False)
    spouse_last_name = Column(Unicode(100), nullable=False)
    spouse_birth_date = Column(Unicode(50), nullable=False)
    spouse_deceased_date = Column(Unicode(50), nullable=True)
    record_active_ind = Column(Integer, nullable=False)
