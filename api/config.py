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
        return os.getenv('MONGODB_NAME', 'gymManagement')

    @property
    def MONGODB_HOST(self):
        """ Specify the host of the database """
        return os.getenv('MONGODB_HOST', 'localhost')

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

    ############# [ SWAGGER CONFIGURATION ] #########################

    @property
    def SWAGGER_UI_DOC_EXPANSION(self):
        """ """
        return os.getenv('SWAGGER_UI_DOC_EXPANSION', 'list')

    @property
    def RESTPLUS_MASK_SWAGGER(self):
        """ """ 
        return os.getenv('RESTPLUS_MASK_SWAGGER', False)

    @property
    def RESTPLUS_VALIDATE(self):
        """ """
        return os.getenv('RESTPLUS_VALIDATE', True)

    @property
    def RESTPLUS_ERROR_404_HELP(self):
        """ """
        return os.getenv('RESTPLUS_ERROR_404_HELP', False)