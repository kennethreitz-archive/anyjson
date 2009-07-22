"""Wraps the best available JSON implementation available in a common
interface

.. function:: serialize(obj)

    Serialize the object to JSON.

.. function:: deserialize(str)

    Deserialize JSON-encoded object to a Python object.

.. function:: force_implementation(name)

    Load a specific json module. This is useful for testing and not much else

.. attribute:: implementation

    The json implementation object. This is probably not useful to you,
    except to get the name of the implementation in use. The name is
    available through `implementation.name`.
"""

# Note: This module is neccessary so we can load the metadata in setup.py
# without risking that the module loading fails. It will fail if the user
# has no json module installed, causing ImportError when importing anyjson

__version__ = "0.2.1"
__author__ = "Rune Halvorsen <runefh@gmail.com>"
__homepage__ = "http://bitbucket.org/runeh/anyjson/"
__docformat__ = "restructuredtext"
