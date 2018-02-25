'''Entry point to all things to avoid circular imports.'''
from project import app
from project.app import freezer, pages
from project.blockchain import *