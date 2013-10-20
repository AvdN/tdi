
from tdi._test_support import pure

from tdi import _htmldecode
def d(*a, **k):
    try:
        return repr(_htmldecode.decode(*a, **k))
    except UnicodeError:
        return "unicodeerror"
    except ValueError, e:
        return str(e)

_RANGE = 10

def test_htmldecode(capsys, pure):
    for _ in xrange(_RANGE):
        print d('xx&#66;&&aleph;&lalalala;', errors='strict')
        print d('xx&#66;&&aleph;&lalalala;')
        print d('xx&#66;&lt;&&aleph;&lalalala;', errors='ignore')
        print d('xx&#66;&lt;&&aleph;&lalalala;', errors='replace')
        print d('&x;&x;&x;', entities={u'x': u'AAAAAAAAAA'})
        print d('&#;')
        print d('&#x;')
        print d('&#x41;')
        print d('&#xffFFffFF;')
        print d('&#1234567890;')
        print d('&#xffFFffFF;', errors='ignore')
        print d('&#1234567890;', errors='ignore')
        print d('&#xffFFffFF;', errors='replace')
        print d('&#1234567890;', errors='replace')
        print d('\xe9', encoding='utf-8')
        print d('\xe9', encoding='utf-8', errors='ignore')
        print d('\xe9', encoding='utf-8', errors='replace')
        print d('\xc3\xa9', encoding='utf-8')

    out, _ = capsys.readouterr()
    assert out == _out

############################################################

_out = u"""\
Unresolved entity u'&lalalala;'
Unresolved entity u'&lalalala;'
u'xxB<&\\u2135&lalalala;'
u'xxB<&\\u2135\\ufffd'
u'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
Unresolved entity u'&#;'
Unresolved entity u'&#x;'
u'A'
Unresolved entity u'&#xffFFffFF;'
Unresolved entity u'&#1234567890;'
u'&#xffFFffFF;'
u'&#1234567890;'
u'\\ufffd'
u'\\ufffd'
unicodeerror
u''
u'\\ufffd'
u'\\xe9'
""" * _RANGE
