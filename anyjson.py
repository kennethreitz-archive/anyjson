"""
Get the best JSON encoder/decoder available on this system.
"""

__version__ = "0.2.0"
__author__ = "Rune Halvorsen <runefh@gmail.com>"
__homepage__ = "http://bitbucket.org/runeh/anyjson/"
__docformat__ = "restructuredtext"

"""

.. function:: serialize(obj)

    Serialize the object to JSON.

.. function:: deserialize(obj)

    Deserialize JSON-encoded object to a Python object.

.. function:: force_implementation(obj)

    Load a specific json module. This is useful for testing and not much else

.. attribute:: implementation

    Name of the json implementation that is being used
"""

import sys
from inspect import isclass

implementation = None

_serialize = None
_deserialize = None
_ser_error = None
_des_error = None

"""
.. data:: _modules

    List of known json modules, and the names of their serialize/unserialize
    methods, as well as the exception they throw. Exception can be either
    an exception class or a string.
"""
_modules = [("cjson", "encode", "EncodeError", "decode", "DecodeError"),
            ("jsonlib2", "write", "WriteError", "read", "ReadError"),
            ("jsonlib", "write", "WriteError", "read", "ReadError"),
            ("simplejson", "dumps", TypeError, "loads", ValueError),
            ("json", "dumps", TypeError, "loads", ValueError),
            ("django.utils.simplejson", "dumps", TypeError, "loads",
             ValueError)]


def _attempt_load(modname, encname, encerror, decname, decerror):
    """Tries to load a module and assign the enc/dec stuff to globals"""
    try:
        global _serialize, _deserialize, _ser_error, _des_error
        global implementation
        __import__(modname)
        mod = sys.modules[modname]
        _serialize = getattr(mod, encname)
        _deserialize = getattr(mod, decname)

        if isclass(encerror) and issubclass(encerror, Exception):
            _ser_error = encerror
        else:
            _ser_error = getattr(mod, encerror)

        if isclass(decerror) and issubclass(decerror, Exception):
            _des_error = decerror
        else:
            _des_error = getattr(mod, decerror)

        implementation = modname
        return True
    except ImportError:
        return False


def force_implementation(modname):
    """Forces anyjson to use a specific json module if it's available"""
    for name, spec in [(e[0], e) for e in _modules]:
        if name == modname and _attempt_load(*spec):
            return

    raise ImportError(modname)


def serialize(data):
    """Serialise the object data into a json string"""
    try:
        return _serialize(data)
    except _ser_error:
        raise TypeError()


def deserialize(string):
    """Deserialize a string of json into python data types"""
    try:
        return _deserialize(string)
    except _des_error:
        raise ValueError()

for modspec in _modules:
    if _attempt_load(*modspec):
        break
else:
    raise ImportError("No json module found")
