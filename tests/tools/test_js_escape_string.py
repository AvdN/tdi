
from __future__ import with_statement
import pytest
from tdi._test_support import pure

from tdi.tools import javascript

# AvdN: first try at splitting
def test_js_escape_string_00(pure):
    x = javascript.escape_string(u'\xe9--"\'\\-----]]></script>')
    assert isinstance(x, str)
    assert x == """\\xe9-\\-\\"\\'\\\\-\\-\\-\\-\\-]\\]><\\/script>"""

def test_js_escape_string_01(pure):
    x = javascript.escape_string(u'\xe9---"\'\\----]]></script>', inlined=False)
    assert isinstance(x, str)
    assert x == """\\xe9---\\"\\'\\\\----]]></script>"""

def test_js_escape_string_02(pure):
    x = javascript.escape_string('\xe9--"\'\\-----]]></script>')
    assert isinstance(x, str)
    assert x == """\\xe9-\\-\\"\\'\\\\-\\-\\-\\-\\-]\\]><\\/script>"""

def test_js_escape_string_03(pure):
    x = javascript.escape_string('\xe9---"\'\\----]]></script>', inlined=False)
    assert isinstance(x, str)
    assert x == """\\xe9---\\"\\'\\\\----]]></script>"""

def test_js_escape_string_unicode_error_00(pure):
    with pytest.raises(UnicodeError):
        x = javascript.escape_string('\xe9--"\'\\-----]]></script>',
            encoding='utf-8'
        )

def test_js_escape_string_unicode_error_01(pure):
    with pytest.raises(UnicodeError):
        x = javascript.escape_string('\xe9--"\'\\-----]]></script>',
            inlined=False, encoding='utf-8'
        )

def test_js_escape_string(capsys, pure):

    x = javascript.escape_string('\xc3\xa9---"\'\\----]]></script>',
        encoding='utf-8'
    )
    print type(x).__name__, x

    x = javascript.escape_string('\xc3\xa9---"\'\\----]]></script>',
        inlined=False, encoding='utf-8'
    )
    print type(x).__name__, x

    # Bigunicode test: &afr; - MATHEMATICAL FRAKTUR SMALL A
    # 1st: the real character must be replaced by surrogates.
    # 2nd: The unreal one must stay.
    a, s = u'a', u'\\'
    for u in ('5\xd8\x1e\xdd'.decode("utf-16-le"), u'\\U0001d51e'):
        for c in xrange(5):
            x = javascript.escape_string(s * c + u + u'--"\'\\-----]]></script>')
            print type(x).__name__, x

            x = javascript.escape_string(s * c + u + u'--"\'\\-----]]></script>',
                inlined=False
            )
            print type(x).__name__, x

            x = javascript.escape_string(a + s * c + u + u'-"\'\\---]]></script>')
            print type(x).__name__, x

            x = javascript.escape_string(a + s * c + u + u'-"\'\\---]]></script>',
                inlined = False
            )
            print type(x).__name__, x

    out, _ = capsys.readouterr()
    print out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
str \\xe9-\\-\\-\\"\\'\\\\-\\-\\-\\-]\\]><\\/script>
str \\xe9---\\"\\'\\\\----]]></script>
str \\ud835\\udd1e-\\-\\"\\'\\\\-\\-\\-\\-\\-]\\]><\\/script>
str \\ud835\\udd1e--\\"\\'\\\\-----]]></script>
str a\\ud835\\udd1e-\\"\\'\\\\-\\-\\-]\\]><\\/script>
str a\\ud835\\udd1e-\\"\\'\\\\---]]></script>
str \\\\\\ud835\\udd1e-\\-\\"\\'\\\\-\\-\\-\\-\\-]\\]><\\/script>
str \\\\\\ud835\\udd1e--\\"\\'\\\\-----]]></script>
str a\\\\\\ud835\\udd1e-\\"\\'\\\\-\\-\\-]\\]><\\/script>
str a\\\\\\ud835\\udd1e-\\"\\'\\\\---]]></script>
str \\\\\\\\\\ud835\\udd1e-\\-\\"\\'\\\\-\\-\\-\\-\\-]\\]><\\/script>
str \\\\\\\\\\ud835\\udd1e--\\"\\'\\\\-----]]></script>
str a\\\\\\\\\\ud835\\udd1e-\\"\\'\\\\-\\-\\-]\\]><\\/script>
str a\\\\\\\\\\ud835\\udd1e-\\"\\'\\\\---]]></script>
str \\\\\\\\\\\\\\ud835\\udd1e-\\-\\"\\'\\\\-\\-\\-\\-\\-]\\]><\\/script>
str \\\\\\\\\\\\\\ud835\\udd1e--\\"\\'\\\\-----]]></script>
str a\\\\\\\\\\\\\\ud835\\udd1e-\\"\\'\\\\-\\-\\-]\\]><\\/script>
str a\\\\\\\\\\\\\\ud835\\udd1e-\\"\\'\\\\---]]></script>
str \\\\\\\\\\\\\\\\\\ud835\\udd1e-\\-\\"\\'\\\\-\\-\\-\\-\\-]\\]><\\/script>
str \\\\\\\\\\\\\\\\\\ud835\\udd1e--\\"\\'\\\\-----]]></script>
str a\\\\\\\\\\\\\\\\\\ud835\\udd1e-\\"\\'\\\\-\\-\\-]\\]><\\/script>
str a\\\\\\\\\\\\\\\\\\ud835\\udd1e-\\"\\'\\\\---]]></script>
str \\\\U0001d51e-\\-\\"\\'\\\\-\\-\\-\\-\\-]\\]><\\/script>
str \\\\U0001d51e--\\"\\'\\\\-----]]></script>
str a\\\\U0001d51e-\\"\\'\\\\-\\-\\-]\\]><\\/script>
str a\\\\U0001d51e-\\"\\'\\\\---]]></script>
str \\\\\\\\U0001d51e-\\-\\"\\'\\\\-\\-\\-\\-\\-]\\]><\\/script>
str \\\\\\\\U0001d51e--\\"\\'\\\\-----]]></script>
str a\\\\\\\\U0001d51e-\\"\\'\\\\-\\-\\-]\\]><\\/script>
str a\\\\\\\\U0001d51e-\\"\\'\\\\---]]></script>
str \\\\\\\\\\\\U0001d51e-\\-\\"\\'\\\\-\\-\\-\\-\\-]\\]><\\/script>
str \\\\\\\\\\\\U0001d51e--\\"\\'\\\\-----]]></script>
str a\\\\\\\\\\\\U0001d51e-\\"\\'\\\\-\\-\\-]\\]><\\/script>
str a\\\\\\\\\\\\U0001d51e-\\"\\'\\\\---]]></script>
str \\\\\\\\\\\\\\\\U0001d51e-\\-\\"\\'\\\\-\\-\\-\\-\\-]\\]><\\/script>
str \\\\\\\\\\\\\\\\U0001d51e--\\"\\'\\\\-----]]></script>
str a\\\\\\\\\\\\\\\\U0001d51e-\\"\\'\\\\-\\-\\-]\\]><\\/script>
str a\\\\\\\\\\\\\\\\U0001d51e-\\"\\'\\\\---]]></script>
str \\\\\\\\\\\\\\\\\\\\U0001d51e-\\-\\"\\'\\\\-\\-\\-\\-\\-]\\]><\\/script>
str \\\\\\\\\\\\\\\\\\\\U0001d51e--\\"\\'\\\\-----]]></script>
str a\\\\\\\\\\\\\\\\\\\\U0001d51e-\\"\\'\\\\-\\-\\-]\\]><\\/script>
str a\\\\\\\\\\\\\\\\\\\\U0001d51e-\\"\\'\\\\---]]></script>
"""
