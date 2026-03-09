from sqlalchemy import Column, Integer, Unicode, Numeric, Identity
from sqlalchemy.dialects.mssql import DATE, DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class FactGift(Base):
    __tablename__ = "FactGift"
    __table_args__ = {"schema": "RaisersEdge.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    match_hash = Column(Unicode(64), nullable=False, unique=True)
    gift_id = Column(Unicode(100), nullable=False)
    constituent_id = Column(Unicode(100), nullable=False)
    gift_date = Column(DATE, nullable=False)
    gift_date_added = Column(DATE, nullable=False)
    gift_constituency = Column(Unicode(100), nullable=False)
    campaign_list = Column(Unicode(300), nullable=False)
    appeal_list = Column(Unicode(300), nullable=False)
    package_list = Column(Unicode(300), nullable=False)
    fund_list = Column(Unicode(300), nullable=False)
    gift_type = Column(Unicode(100), nullable=False)
    gift_subtype = Column(Unicode(100), nullable=False)
    gift_installment_frequency = Column(Unicode(100), nullable=False)
    gift_amount = Column(Numeric(18, 2), nullable=False)
    gift_status = Column(Unicode(100), nullable=False)
    gift_status_date = Column(DATE, nullable=True)
    recurring_frequency = Column(Integer, nullable=False)
    total_projected_gift_amount = Column(Numeric(18, 2), nullable=False)
    market = Column(Unicode(100), nullable=False)
    ppm_ind = Column(Integer, nullable=False)
    gift_gl_post_status = Column(Unicode(100), nullable=False)
    gift_gl_post_date = Column(DATE, nullable=True)
    gift_payment_type = Column(Unicode(100), nullable=False)
    qrecid = Column(Integer, nullable=False)
    record_active_ind = Column(Integer, nullable=False)
    record_insert_datetime = Column(DATETIME2, nullable=False)
    record_update_datetime = Column(DATETIME2, nullable=False)
    record_deleted_datetime = Column(DATETIME2, nullable=True)


class StageFactGift(Base):
    __tablename__ = "StageFactGift"
    __table_args__ = {"schema": "RaisersEdge.dbo"}

    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    match_hash = Column(Unicode(64), nullable=False, unique=True)
    gift_id = Column(Unicode(100), nullable=False)
    constituent_id = Column(Unicode(100), nullable=False)
    gift_date = Column(DATE, nullable=False)
    gift_date_added = Column(DATE, nullable=False)
    gift_constituency = Column(Unicode(100), nullable=False)
    campaign_list = Column(Unicode(300), nullable=False)
    appeal_list = Column(Unicode(300), nullable=False)
    package_list = Column(Unicode(300), nullable=False)
    fund_list = Column(Unicode(300), nullable=False)
    gift_type = Column(Unicode(100), nullable=False)
    gift_subtype = Column(Unicode(100), nullable=False)
    gift_installment_frequency = Column(Unicode(100), nullable=False)
    gift_amount = Column(Numeric(18, 2), nullable=False)
    gift_status = Column(Unicode(100), nullable=False)
    gift_status_date = Column(DATE, nullable=True)
    recurring_frequency = Column(Integer, nullable=False)
    total_projected_gift_amount = Column(Numeric(18, 2), nullable=False)
    market = Column(Unicode(100), nullable=False)
    ppm_ind = Column(Integer, nullable=False)
    gift_gl_post_status = Column(Unicode(100), nullable=False)
    gift_gl_post_date = Column(DATE, nullable=True)
    gift_payment_type = Column(Unicode(100), nullable=False)
    qrecid = Column(Integer, nullable=False)
    record_active_ind = Column(Integer, nullable=False)
