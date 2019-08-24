# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
import os

class Config():
    """
    Configuration parameters
    """
    ############# [ MONGO CONFIGURATION ] #########################

    @property
    def MONGODB_NAME(self):
        """ Specify the name of the database """
        return os.getenv('MONGODB_NAME', None)

    @property
    def MONGODB_HOST(self):
        """ Specify the host of the database """
        return os.getenv('MONGODB_HOST', None)

    @property
    def MONGODB_PORT(self):
        """ Specify the port of the database """
        return os.getenv('MONGODB_PORT', 27017)

    @property
    def MONGODB_USERNAME(self):
        """ Specify the username of the database """
        return os.getenv('MONGODB_USERNAME', None)

    @property
    def MONGODB_PASSWORD(self):
        """ Specify the password of the database """
        return os.getenv('MONGODB_PASSWORD', None)