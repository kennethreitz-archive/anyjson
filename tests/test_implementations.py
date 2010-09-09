from nose.tools import assert_raises
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

        assert_raises(TypeError, anyjson.serialize, [object()])
        assert_raises(TypeError, anyjson.dumps, [object()])
        assert_raises(ValueError, anyjson.deserialize, "[")
        assert_raises(ValueError, anyjson.loads, "[")

