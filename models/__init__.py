#!/usr/bin/python3
"""Module used for package initialization
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
