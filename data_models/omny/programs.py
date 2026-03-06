from sqlalchemy import Column, Integer, Unicode, String, Identity
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RptPrograms(Base):
    __tablename__ = "RptPrograms"
    __table_args__ = {"schema":"Omny.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    program_id = Column(Unicode(100), nullable=False)
    program_name = Column(Unicode(500), nullable=False)
    program_description = Column(Unicode(1000), nullable=False)
    network_id = Column(Unicode(100), default=None)
    network_name = Column(Unicode(100), default=None)
    source_data_datetime = Column(DATETIME2, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)


class StageRptPrograms(Base):
    __tablename__ = "StageRptPrograms"
    __table_args__ = {"schema":"Omny.dbo"}

    id = Column(Integer, primary_key=True)
    program_id = Column(Unicode(100), nullable=False)
    program_name = Column(Unicode(500), nullable=False)
    program_description = Column(Unicode(1000), nullable=False)
    network_id = Column(Unicode(100), default=None)
    network_name = Column(Unicode(100), default=None)
    source_data_datetime = Column(DATETIME2, nullable=False)
