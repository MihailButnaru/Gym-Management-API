# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
"""
Creates a MongoDB connection
"""
import logging
from mongoengine import connect

def init_mongo_connection(config):
    """
    MongoDB connection to get access to the database
        Args:
            config (param): config parameters
    """
    _log = logging.getLogger(__name__)
    return connect(
        db=config.MONGODB_NAME,
        host=config.MONGODB_HOST,
        port=config.MONGODB_PORT
    )
