
from tdi._test_support import pure

from tdi.tools import css


def test_css_minify(capsys, pure):
    x = css.minify(u"""
    body {
        background-color: #fff;
    }
    """)
    print repr(x)

    x = css.minify("""
    .eacute:after {
        content: "\xe9";
    }
    """)
    print repr(x)

    try:
        x = css.minify("""
        .eacute:after {
            content: "\xe9";
        }
        """, encoding='utf-8')
    except UnicodeError:
        print "UnicodeError - OK"

    x = css.minify("""
    .eacute:after {
        content: "\xc3\xa9";
    }
    """, encoding='utf-8')
    print repr(x)

    out, _ = capsys.readouterr()
    print out, _out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
u'body{background-color:#fff}'
'.eacute:after{content:"\\xe9"}'
UnicodeError - OK
'.eacute:after{content:"\\xc3\\xa9"}'
"""
