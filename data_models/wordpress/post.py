from sqlalchemy import Column, Integer, Unicode, Identity
from sqlalchemy.dialects.mssql import DATETIME2
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DimPost(Base):
    __tablename__ = "DimPost"
    __table_args__ = {"schema":"WordPress.dbo"}
    
    id = Column(Integer, Identity(start=1, increment=1), primary_key=True)
    post_id = Column(Integer, nullable=False)
    published_datetime = Column(DATETIME2(7), nullable=False)
    modified_datetime = Column(DATETIME2(7), nullable=False)
    status_desc = Column(Unicode(50), nullable=False)
    author_name = Column(Unicode(100), nullable=False)
    post_title = Column(Unicode(100), nullable=False)
    word_count = Column(Integer, nullable=False)
    categories_desc = Column(Unicode(100), nullable=False)
    tags_desc = Column(Unicode(100), nullable=False)
    url_path = Column(Unicode(100), nullable=False)
    ga_path_level_1 = Column(Unicode(100), nullable=False)
    ga_path_level_2 = Column(Unicode(100), nullable=False)
    ga_path_level_3 = Column(Unicode(100), nullable=False)
    source_data_datetime = Column(DATETIME2(7), nullable=False)
    record_insert_datetime = Column(DATETIME2(7), nullable=False)


class StageDimPost(Base):
    __tablename__ = "StageDimPost"
    __table_args__ = {"schema":"WordPress.dbo"}
    
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, nullable=False)
    published_datetime = Column(DATETIME2(7), nullable=False)
    modified_datetime = Column(DATETIME2(7), nullable=False)
    status_desc = Column(Unicode(50), nullable=False)
    author_name = Column(Unicode(100), nullable=False)
    post_title = Column(Unicode(100), nullable=False)
    word_count = Column(Integer, nullable=False)
    categories_desc = Column(Unicode(100), nullable=False)
    tags_desc = Column(Unicode(100), nullable=False)
    url_path = Column(Unicode(100), nullable=False)
    ga_path_level_1 = Column(Unicode(100), nullable=False)
    ga_path_level_2 = Column(Unicode(100), nullable=False)
    ga_path_level_3 = Column(Unicode(100), nullable=False)
    source_data_datetime = Column(DATETIME2(7), nullable=False)
