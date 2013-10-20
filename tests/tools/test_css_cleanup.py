
from tdi._test_support import pure

from tdi.tools import css

def test_css_cleanup(capsys, pure):
    x = css.cleanup(u"""<!-- style1
    -->""")
    print repr(x)

    x = css.cleanup("""<!-- style1
    -->""")
    print repr(x)

    x = css.cleanup("""<!-- style1 - \xc3\xa9
    -->""", encoding='utf-8')
    print repr(x)

    x = css.cleanup(u"""<![CDATA[
        style2
    ]]>""")
    print repr(x)

    x = css.cleanup("""<![CDATA[
        style2
    ]]>""")
    print repr(x)

    x = css.cleanup("""<![CDATA[
        style2 - \xc3\xa9
    ]]>""", encoding='utf-8')
    print repr(x)

    x = css.cleanup(u"""/*<![CDATA[*/
        style3
    /*]]>*/""")
    print repr(x)

    x = css.cleanup("""/*<![CDATA[*/
        style3
    /*]]>*/""")
    print repr(x)

    x = css.cleanup("""/*<![CDATA[*/
        style3 - \xc3\xa9
    /*]]>*/""", encoding='utf-8')
    print repr(x)

    x = css.cleanup(u"""<!--/*--><![CDATA[/*><!--*/
        style4
    /*]]>*/-->""")
    print repr(x)

    x = css.cleanup("""<!--/*--><![CDATA[/*><!--*/
        style4
    /*]]>*/-->""")
    print repr(x)

    x = css.cleanup("""<!--/*--><![CDATA[/*><!--*/
        style4 - \xc3\xa9
    /*]]>*/-->""", encoding='utf-8')
    print repr(x)

    try:
        x = css.cleanup("""<!--/*--><![CDATA[/*><!--*/
            style4 - \xe9
        /*]]>*/-->""", encoding='utf-8')
    except UnicodeError:
        print "UnicodeError - OK"

    out, _ = capsys.readouterr()
    print out, _out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
u'style1'
'style1'
'style1 - \\xc3\\xa9'
u'style2'
'style2'
'style2 - \\xc3\\xa9'
u'style3'
'style3'
'style3 - \\xc3\\xa9'
u'style4'
'style4'
'style4 - \\xc3\\xa9'
UnicodeError - OK
"""
