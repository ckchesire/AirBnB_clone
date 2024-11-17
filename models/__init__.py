#!/usr/bin/python3
"""Module used for package initialization
"""
from models.engine.file_storage import FileStorage

''' Create instance of file storage '''
storage = FileStorage()
storage.reload()
