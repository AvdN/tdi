
import pprint as _pprint
import sys as _sys

from tdi import filters as _filters

class Collector(object):
    def __init__(self):
        self.events = []
        self.canary = 'bla'
    def __getattr__(self, name):
        if name.startswith('handle_'):
            def method(*args):
                self.events.append((name, args))
            return method
        raise AttributeError(name)


class Foo(_filters.BaseEventFilter):
    def __init__(self, builder):
        super(Foo, self).__init__(builder)

    def finalize(self):
        self.builder.handle_blob(self.canary)


class Bar(_filters.BaseEventFilter):
    def __init__(self, builder):
        super(Bar, self).__init__(builder)

    def __getattr__(self, name):
        if name == 'canary':
            raise AttributeError('lol')
        return getattr(self.builder, name)

    def finalize(self):
        self.builder.handle_blob(self.canary)


def otest(cls, method, capsys, *inp):
    def inner(*expected):
        c = Collector()
        f = cls(c)
        try:
            getattr(f, method)(*inp)
        except (SystemExit, KeyboardInterrupt):
            raise
        except:
            e = _sys.exc_info()[:2]
            c.events.append((e[0].__name__, str(e[1])))
        if c.events == list(expected):
            print "OK", method, inp
        else:
            print "FAIL", method, inp
            _pprint.pprint(tuple(c.events))
        out, _ = capsys.readouterr()
        if out and out[-1] == '\n':
            out = out[:-1]  # strip trailing linefeed
        return out
    return inner

#_test, test = test, lambda *a, **k: lambda *e: None

def test_00(capsys):
    assert otest(Foo, 'foo', capsys, 'bar', 'baz')(('AttributeError', 'foo'),) \
           == u"OK foo ('bar', 'baz')"

def test_01(capsys):
    assert otest(Foo, 'handle_blub', capsys, 'plop', 'poeh')(
        ('handle_blub', ('plop', 'poeh')),) \
           == u"OK handle_blub ('plop', 'poeh')"

def test_02(capsys):
    assert otest(Foo, 'finalize', capsys)(('handle_blob', ('bla',)),) \
           == u"OK finalize ()"

def test_03(capsys):
    assert otest(Bar, 'foo', capsys, 'bar', 'baz')(('AttributeError', 'foo'),) \
           == u"OK foo ('bar', 'baz')"

def test_04(capsys):
    assert otest(Bar, 'handle_blub', capsys, 'plop', 'poeh')(
        ('handle_blub', ('plop', 'poeh')),) \
           == u"OK handle_blub ('plop', 'poeh')"

def test_05(capsys):
    assert otest(Bar, 'finalize', capsys)(('AttributeError', 'lol'),) \
           == u"OK finalize ()"
