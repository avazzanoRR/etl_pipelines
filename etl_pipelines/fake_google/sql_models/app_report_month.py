from sqlalchemy import Column, Integer, Identity, Numeric
from sqlalchemy.dialects.mssql import DATE
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class RptAppReportMonth(Base):
    __tablename__ = "RptAppReportMonth"
    __table_args__ = {"schema": "GoogleAnalytics.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    date = Column(DATE, nullable=False)
    total_sessions = Column(Integer, nullable=False)
    new_users = Column(Integer, nullable=False)
    sessions_per_new_user = Column(Numeric(18, 2), nullable=False)


class StageRptAppReportMonth(Base):
    __tablename__ = "StageRptAppReportMonth"
    __table_args__ = {"schema": "GoogleAnalytics.dbo"}

    id = Column(Integer, primary_key=True)
    date = Column(DATE, default=None)
    total_sessions = Column(Integer, default=None)
    new_users = Column(Integer, default=None)
    sessions_per_new_user = Column(Numeric(18, 2), default=None)