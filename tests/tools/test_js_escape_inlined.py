
from tdi._test_support import pure

from tdi.tools import javascript

def test_js_escape_inlined(capsys, pure):
    x = javascript.escape_inlined(u'\xe9-------]]></script>')
    print repr(x)

    x = javascript.escape_inlined('\xe9-------]]></script>')
    print repr(x)

    try:
        javascript.escape_inlined('\xe9-------]]></script>', encoding='utf-8')
    except UnicodeError:
        print "UnicodeError - OK"

    x = javascript.escape_inlined('\xc3\xa9-------]]></script>', encoding='utf-8')
    print repr(x)

    out, _ = capsys.readouterr()
    assert out == _out

############################################################

_out = u"""\
u'\\xe9-\\\\-\\\\-\\\\-\\\\-\\\\-\\\\-]\\\\]><\\\\/script>'
'\\xe9-\\\\-\\\\-\\\\-\\\\-\\\\-\\\\-]\\\\]><\\\\/script>'
UnicodeError - OK
'\\xc3\\xa9-\\\\-\\\\-\\\\-\\\\-\\\\-\\\\-]\\\\]><\\\\/script>'
"""
