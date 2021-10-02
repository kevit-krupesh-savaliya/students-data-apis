"""Logging Module"""
import logging
import os
from logging.handlers import RotatingFileHandler

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Create a custom logger

# Create handlers
c_handler = logging.StreamHandler()
f_handler = RotatingFileHandler(os.path.join(os.path.join(BASE_DIR, 'logs'), 'data_extractor.log'),
                                maxBytes=10 * 1024 * 1024,
                                backupCount=10, encoding="utf-8")
c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
c_format = logging.Formatter(
    '%(asctime)s - %(name)s | %(levelname)s | %(message)s')
f_format = logging.Formatter(
    '%(asctime)s - %(name)s | %(levelname)s | %(message)s')

c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger = logging.getLogger("Student Data API")
logger.setLevel(logging.DEBUG)
logger.addHandler(c_handler)
logger.addHandler(f_handler)
