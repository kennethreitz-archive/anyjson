"""Wraps the best available JSON implementation available in a common
interface"""

# Note: This module is neccessary so we can load the metadata in setup.py
# without risking that the module loading fails. It will fail if the user
# has no json module installed, causing ImportError when importing anyjson

__version__ = "0.2.1"
__author__ = "Rune Halvorsen <runefh@gmail.com>"
__homepage__ = "http://bitbucket.org/runeh/anyjson/"
__docformat__ = "restructuredtext"
