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

_modules = [("cjson", "encode", "EncodeError", "decode", "DecodeError"),
            ("jsonlib2", "write", "WriteError", "read", "ReadError"),
            ("jsonlib", "write", "WriteError", "read", "ReadError"),
            ("simplejson", "dumps", TypeError, "loads", ValueError),
            ("json", "dumps", TypeError, "loads", ValueError),
            ("django.utils.simplejson", "dumps", TypeError, "loads",
             ValueError)]


def _attempt_load(modname, encname, encerror, decname, decerror):
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
    for name, spec in [(e[0], e) for e in _modules]:
        print "spce:", spec
        if name == modname and _attempt_load(*spec):
            return

    raise ImportError(modname)


class JsonValueError(ValueError):
    pass


class JsonTypeError(TypeError):
    pass


def serialize(s):
    try:
        return _serialize(s)
    except _ser_error:
        raise JsonTypeError()


def deserialize(s):
    try:
        return _deserialize(s)
    except _des_error:
        raise JsonValueError()

for modspec in _modules:
    if _attempt_load(*modspec):
        break
else:
    raise ImportError("No json module found")
