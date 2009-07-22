from metadata import *
import sys

# explicitly pull in docstring from metadata. see comments there for why.
__doc__ = metadata.__doc__
implementation = None

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
_fields = ("modname", "encoder", "encerror", "decoder", "decerror")


class _JsonImplementation(object):
    """Incapsulates a JSON implementation"""

    def __init__(self, modspec):
        modinfo = dict(zip(_fields, modspec))

        # No try block. We want importerror to end up at caller
        module = self._attempt_load(modinfo["modname"])

        self.implementation = modinfo["modname"]
        self._encode = getattr(module, modinfo["encoder"])
        self._decode = getattr(module, modinfo["decoder"])
        self._encode_error = modinfo["encerror"]
        self._decode_error = modinfo["decerror"]

        if isinstance(modinfo["encerror"], basestring):
            self._encode_error = getattr(module, modinfo["encerror"])
        if isinstance(modinfo["decerror"], basestring):
            self._decode_error = getattr(module, modinfo["decerror"])

        self.name = modinfo["modname"]

    def _attempt_load(self, modname):
        """Attempt to load module name modname, returning it on success,
        throwing ImportError if module couldn't be imported"""
        __import__(modname)
        return sys.modules[modname]

    def serialize(self, data):
        """Serialize the datastructure to json. Returns a string. Raises
        TypeError if the object could not be serialized."""
        try:
            return self._encode(data)
        except self._encode_error, exc:
            raise TypeError(*exc.args)

    def deserialize(self, s):
        """deserialize the string to python data types. Raises
        ValueError if the string vould not be parsed."""
        try:
            return self._decode(s)
        except self._decode_error, exc:
            raise ValueError(*exc.args)


def force_implementation(modname):
    """Forces anyjson to use a specific json module if it's available"""
    global implementation
    for name, spec in [(e[0], e) for e in _modules]:
        if name == modname:
            implementation = _JsonImplementation(spec)
            return
    raise ImportError("No module named: %s" % modname)



def main():
    installed = []
    for modspec in _modules:
        try:
            __import__(modspec[0])
            installed.append(modspec[0])
        except ImportError:
            pass

    if installed:
        print "Supported JSON modules found:", ", ".join(installed)
        return 0
    else:
        print "No supported JSON modules found"
        return 1

if __name__ == "__main__":
    # If run as a script, we simply print what is installed that we support.
    # We do NOT try to load a compatible module because that may throw an
    # exception, which renders the package uninstallable with easy_install
    # (It trys to execfile the script when installing, to make sure it works)
    sys.exit(main())
else:
    for modspec in _modules:
        try:
            implementation = _JsonImplementation(modspec)
            break
        except ImportError:
            pass
        else:
            raise ImportError("No supported JSON module found")

    serialize = lambda value: implementation.serialize(value)
    deserialize = lambda value: implementation.deserialize(value)