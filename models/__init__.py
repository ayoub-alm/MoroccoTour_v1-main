#!/usr/bin/python3
"""database storage initialisation"""

from models.engine.db_storage import DBStorage


storage = DBStorage()
storage.reload()
