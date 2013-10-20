
from tdi._test_support import pure

from tdi.tools import javascript

def test_js_minify(capsys, pure):
    x = javascript.minify(u"""
    var x=1;
    var y = 2; \xe9
    alert( x + y );
    """)
    print repr(x)

    x = javascript.minify("""
    var x=1;
    var y = 2; \xe9
    alert( x + y );
    """)
    print repr(x)

    try:
        x = javascript.minify("""
        var x=1;
        var y = 2; \xe9
        alert( x + y );
        """, encoding='utf-8')
    except UnicodeError:
        print "UnicodeError - OK"

    x = javascript.minify("""
    var x=1;
    var y = 2; \xc3\xa9
    alert( x + y );
    """, encoding='utf-8')
    print repr(x)

    out, _ = capsys.readouterr()
    assert out == _out

############################################################

_out = u"""\
u'var x=1;var y=2;\\xe9\\nalert(x+y);'
'var x=1;var y=2;\\xe9\\nalert(x+y);'
UnicodeError - OK
'var x=1;var y=2;\\xc3\\xa9\\nalert(x+y);'
"""
