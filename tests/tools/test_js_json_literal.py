
from tdi._test_support import pure

from tdi.tools import javascript

def test_js_json_literal(capsys, pure):

    x = javascript.LiteralJSON(u'Andr\xe9 \u2028\u2029</---]]>')
    print repr(x)
    print repr(str(x))
    print repr(unicode(x))
    print repr(x.as_json())
    print repr(x.as_json(inlined=True))
    print repr(x.as_json(inlined=False))

    x = javascript.LiteralJSON(u'Andr\xe9 \u2028\u2029</---]]>', inlined=True)
    print repr(x)
    print repr(str(x))
    print repr(unicode(x))
    print repr(x.as_json())
    print repr(x.as_json(inlined=True))
    print repr(x.as_json(inlined=False))

    x = javascript.LiteralJSON('Andr\xc3\xa9 \xe2\x80\xa8\xe2\x80\xa9</---]]>',
        encoding='utf-8'
    )
    print repr(x)
    print repr(str(x))
    print repr(unicode(x))
    print repr(x.as_json())
    print repr(x.as_json(inlined=True))
    print repr(x.as_json(inlined=False))

    x = javascript.LiteralJSON('Andr\xc3\xa9 \xe2\x80\xa8\xe2\x80\xa9</---]]>',
        encoding='utf-8', inlined=True
    )
    print repr(x)
    print repr(str(x))
    print repr(unicode(x))
    print repr(x.as_json())
    print repr(x.as_json(inlined=True))
    print repr(x.as_json(inlined=False))

    x = javascript.LiteralJSON('Andr\xe9 \xe2\x80\xa8\xe2\x80\xa9</---]]>',
        encoding='utf-8'
    )
    print repr(x)
    try:
        print repr(str(x))
    except UnicodeError:
        print "UnicodeError - OK"
    try:
        print repr(unicode(x))
    except UnicodeError:
        print "UnicodeError - OK"
    try:
        print repr(x.as_json())
    except UnicodeError:
        print "UnicodeError - OK"
    try:
        print repr(x.as_json(inlined=True))
    except UnicodeError:
        print "UnicodeError - OK"
    try:
        print repr(x.as_json(inlined=False))
    except UnicodeError:
        print "UnicodeError - OK"

    x = javascript.LiteralJSON('Andr\xe9 \xe2\x80\xa8\xe2\x80\xa9</---]]>',
        encoding='utf-8', inlined=True
    )
    print repr(x)
    try:
        print repr(str(x))
    except UnicodeError:
        print "UnicodeError - OK"
    try:
        print repr(unicode(x))
    except UnicodeError:
        print "UnicodeError - OK"
    try:
        print repr(x.as_json())
    except UnicodeError:
        print "UnicodeError - OK"
    try:
        print repr(x.as_json(inlined=True))
    except UnicodeError:
        print "UnicodeError - OK"
    try:
        print repr(x.as_json(inlined=False))
    except UnicodeError:
        print "UnicodeError - OK"

    out, _ = capsys.readouterr()
    print out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
LiteralJSON(u'Andr\\xe9 \\u2028\\u2029</---]]>', inlined=False, encoding=None)
'Andr\\xc3\\xa9 \\\\u2028\\\\u2029</---]]>'
u'Andr\\xe9 \\\\u2028\\\\u2029</---]]>'
u'Andr\\xe9 \\\\u2028\\\\u2029</---]]>'
u'Andr\\xe9 \\\\u2028\\\\u2029<\\\\/-\\\\-\\\\-]\\\\]>'
u'Andr\\xe9 \\\\u2028\\\\u2029</---]]>'
LiteralJSON(u'Andr\\xe9 \\u2028\\u2029</---]]>', inlined=True, encoding=None)
'Andr\\xc3\\xa9 \\\\u2028\\\\u2029<\\\\/-\\\\-\\\\-]\\\\]>'
u'Andr\\xe9 \\\\u2028\\\\u2029<\\\\/-\\\\-\\\\-]\\\\]>'
u'Andr\\xe9 \\\\u2028\\\\u2029<\\\\/-\\\\-\\\\-]\\\\]>'
u'Andr\\xe9 \\\\u2028\\\\u2029<\\\\/-\\\\-\\\\-]\\\\]>'
u'Andr\\xe9 \\\\u2028\\\\u2029</---]]>'
LiteralJSON('Andr\\xc3\\xa9 \\xe2\\x80\\xa8\\xe2\\x80\\xa9</---]]>', inlined=False, encoding='utf-8')
'Andr\\xc3\\xa9 \\\\u2028\\\\u2029</---]]>'
u'Andr\\xe9 \\\\u2028\\\\u2029</---]]>'
u'Andr\\xe9 \\\\u2028\\\\u2029</---]]>'
u'Andr\\xe9 \\\\u2028\\\\u2029<\\\\/-\\\\-\\\\-]\\\\]>'
u'Andr\\xe9 \\\\u2028\\\\u2029</---]]>'
LiteralJSON('Andr\\xc3\\xa9 \\xe2\\x80\\xa8\\xe2\\x80\\xa9</---]]>', inlined=True, encoding='utf-8')
'Andr\\xc3\\xa9 \\\\u2028\\\\u2029<\\\\/-\\\\-\\\\-]\\\\]>'
u'Andr\\xe9 \\\\u2028\\\\u2029<\\\\/-\\\\-\\\\-]\\\\]>'
u'Andr\\xe9 \\\\u2028\\\\u2029<\\\\/-\\\\-\\\\-]\\\\]>'
u'Andr\\xe9 \\\\u2028\\\\u2029<\\\\/-\\\\-\\\\-]\\\\]>'
u'Andr\\xe9 \\\\u2028\\\\u2029</---]]>'
LiteralJSON('Andr\\xe9 \\xe2\\x80\\xa8\\xe2\\x80\\xa9</---]]>', inlined=False, encoding='utf-8')
UnicodeError - OK
UnicodeError - OK
UnicodeError - OK
UnicodeError - OK
UnicodeError - OK
LiteralJSON('Andr\\xe9 \\xe2\\x80\\xa8\\xe2\\x80\\xa9</---]]>', inlined=True, encoding='utf-8')
UnicodeError - OK
UnicodeError - OK
UnicodeError - OK
UnicodeError - OK
UnicodeError - OK
"""
