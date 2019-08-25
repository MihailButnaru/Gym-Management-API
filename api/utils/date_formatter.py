# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
"""
Converter
    Datetime str to date.isoformat
"""
import json
import datetime

def date_formatter(date):
    """
        Args:
            date (str): datetime 
    """
    if isinstance(date, datetime.datetime):
        return date.isoformat()
    return date