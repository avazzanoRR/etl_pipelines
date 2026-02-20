from etl_pipelines.source_1 import connector as source_1_connector
from etl_pipelines.source_2 import connector as source_2_connector
from etl_pipelines.source_3 import connector as source_3_connector

SOURCES = [
    {"name": "source_1", "connector": source_1_connector},
    {"name": "source_2", "connector": source_2_connector},
    {"name": "source_3", "connector": source_3_connector},
]