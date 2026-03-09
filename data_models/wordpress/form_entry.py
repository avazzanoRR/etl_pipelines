from sqlalchemy import Column, Integer, Unicode, Identity, UnicodeText
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class FactFormEntry(Base):
    __tablename__ = "FactFormEntry"
    __table_args__ = {"schema":"WordPress.dbo"}
    
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    form_entry_id = Column(Integer, nullable=False)
    form_id = Column(Integer, nullable=False)
    form_entry_datetime = Column(DATETIME2(7), nullable=False)
    email_address = Column(UnicodeText, nullable=True)
    first_name = Column(UnicodeText, nullable=True)
    last_name = Column(UnicodeText, nullable=True)
    entry_ip_address = Column(Unicode(100), nullable=False)
    entry_user_agent = Column(Unicode(100), nullable=False)
    browser_family = Column(Unicode(100), nullable=False)
    browser_version = Column(Unicode(100), nullable=False)
    os_family = Column(Unicode(100), nullable=False)
    os_version = Column(Unicode(100), nullable=False)
    device_family = Column(Unicode(100), nullable=False)
    device_type = Column(Unicode(100), nullable=False)
    is_touch_capable = Column(Integer, nullable=False)
    is_bot = Column(Integer, nullable=False)
    utm_source = Column(Unicode(100), nullable=False)
    utm_medium = Column(Unicode(100), nullable=False)
    utm_campaign = Column(Unicode(100), nullable=False)
    utm_content = Column(Unicode(100), nullable=False)
    utm_term = Column(Unicode(100), nullable=False)
    source_data_datetime = Column(DATETIME2(7), nullable=False)
    record_insert_datetime = Column(DATETIME2(7), nullable=False)


class StageFactFormEntry(Base):
    __tablename__ = "StageFactFormEntry"
    __table_args__ = {"schema":"WordPress.dbo"}
    
    id = Column(Integer, primary_key=True)
    form_entry_id = Column(Integer, nullable=False)
    form_id = Column(Integer, nullable=False)
    form_entry_datetime = Column(DATETIME2(7), nullable=False)
    email_address = Column(UnicodeText, nullable=True)
    first_name = Column(UnicodeText, nullable=True)
    last_name = Column(UnicodeText, nullable=True)
    entry_ip_address = Column(Unicode(100), nullable=False)
    entry_user_agent = Column(Unicode(100), nullable=False)
    browser_family = Column(Unicode(100), nullable=False)
    browser_version = Column(Unicode(100), nullable=False)
    os_family = Column(Unicode(100), nullable=False)
    os_version = Column(Unicode(100), nullable=False)
    device_family = Column(Unicode(100), nullable=False)
    device_type = Column(Unicode(100), nullable=False)
    is_touch_capable = Column(Integer, nullable=False)
    is_bot = Column(Integer, nullable=False)
    utm_source = Column(Unicode(100), nullable=False)
    utm_medium = Column(Unicode(100), nullable=False)
    utm_campaign = Column(Unicode(100), nullable=False)
    utm_content = Column(Unicode(100), nullable=False)
    utm_term = Column(Unicode(100), nullable=False)
    source_data_datetime = Column(DATETIME2(7), nullable=False)