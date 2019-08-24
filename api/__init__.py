# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
from api.config import Config
from api.app import create_app
from api.database.mongo_init import init_mongo_connection


_config = Config()
db_connector = init_mongo_connection(_config)
app = create_app(_config)