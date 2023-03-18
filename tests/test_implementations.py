import pytest
import anyjson

modnames = [e[0] for e in anyjson._modules]

def test_default_serialization():
    assert anyjson.serialize([1,2,3]).replace(" ", "") == "[1,2,3]"
    assert anyjson.dumps([1,2,3]).replace(" ", "") == "[1,2,3]"


def test_default_deserialization():
    assert anyjson.deserialize("[1,2,3]") == [1,2,3]
    assert anyjson.loads("[1,2,3]") == [1,2,3]


def test_forced_serialization():
    for name in modnames:
        try:
            anyjson.force_implementation(name)
        except ImportError:
            continue # module can't be tested, try next

        assert anyjson.serialize([1,2,3]).replace(" ", "") == "[1,2,3]"
        assert anyjson.dumps([1,2,3]).replace(" ", "") == "[1,2,3]"


def test_forced_deserialization():
    for name in modnames:
        try:
            anyjson.force_implementation(name)
        except ImportError:
            continue # module can't be tested, try next

        assert anyjson.deserialize("[1,2,3]") == [1,2,3]
        assert anyjson.loads("[1,2,3]") == [1,2,3]


def test_exceptions():
    for name in modnames:
        try:
            anyjson.force_implementation(name)
        except ImportError:
            continue # module can't be tested, try next

        with pytest.raises(TypeError):
            anyjson.serialize([object()])
        with pytest.raises(TypeError):
            anyjson.dumps([object()])
        with pytest.raises(ValueError):
            anyjson.deserialize("[")
        with pytest.raises(ValueError):
            anyjson.loads("[")
