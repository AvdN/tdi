
from tdi._test_support import pure

from tdi.tools import css

# AvdN: should split out
def test_css_cdata(capsys, pure):

    x = css.cdata(u"""<!-- style1
    -->""")
    print repr(x)

    x = css.cdata("""<!-- style1
    -->""")
    print repr(x)

    x = css.cdata("""<!-- style1 - \xc3\xa9
    -->""", encoding='utf-8')
    print repr(x)

    x = css.cdata(u"""<![CDATA[
        style2
    ]]>""")
    print repr(x)

    x = css.cdata("""<![CDATA[
        style2
    ]]>""")
    print repr(x)

    x = css.cdata("""<![CDATA[
        style2 - \xc3\xa9
    ]]>""", encoding='utf-8')
    print repr(x)

    x = css.cdata(u"""/*<![CDATA[*/
        style3
    /*]]>*/""")
    print repr(x)

    x = css.cdata("""/*<![CDATA[*/
        style3
    /*]]>*/""")
    print repr(x)

    x = css.cdata("""/*<![CDATA[*/
        style3 - \xc3\xa9
    /*]]>*/""", encoding='utf-8')
    print repr(x)

    x = css.cdata(u"""<!--/*--><![CDATA[/*><!--*/
        style4
    /*]]>*/-->""")
    print repr(x)

    x = css.cdata("""<!--/*--><![CDATA[/*><!--*/
        style4
    /*]]>*/-->""")
    print repr(x)

    x = css.cdata("""<!--/*--><![CDATA[/*><!--*/
        style4 - \xc3\xa9
    /*]]>*/-->""", encoding='utf-8')
    print repr(x)

    try:
        x = css.cdata("""<!--/*--><![CDATA[/*><!--*/
            style4 - \xe9
        /*]]>*/-->""", encoding='utf-8')
    except UnicodeError:
        print "UnicodeError - OK"

    out, _ = capsys.readouterr()
    assert out == _out

############################################################

_out = u"""\
u'<!--/*--><![CDATA[/*><!--*/\\nstyle1\\n/*]]>*/-->'
'<!--/*--><![CDATA[/*><!--*/\\nstyle1\\n/*]]>*/-->'
'<!--/*--><![CDATA[/*><!--*/\\nstyle1 - \\xc3\\xa9\\n/*]]>*/-->'
u'<!--/*--><![CDATA[/*><!--*/\\nstyle2\\n/*]]>*/-->'
'<!--/*--><![CDATA[/*><!--*/\\nstyle2\\n/*]]>*/-->'
'<!--/*--><![CDATA[/*><!--*/\\nstyle2 - \\xc3\\xa9\\n/*]]>*/-->'
u'<!--/*--><![CDATA[/*><!--*/\\nstyle3\\n/*]]>*/-->'
'<!--/*--><![CDATA[/*><!--*/\\nstyle3\\n/*]]>*/-->'
'<!--/*--><![CDATA[/*><!--*/\\nstyle3 - \\xc3\\xa9\\n/*]]>*/-->'
u'<!--/*--><![CDATA[/*><!--*/\\nstyle4\\n/*]]>*/-->'
'<!--/*--><![CDATA[/*><!--*/\\nstyle4\\n/*]]>*/-->'
'<!--/*--><![CDATA[/*><!--*/\\nstyle4 - \\xc3\\xa9\\n/*]]>*/-->'
UnicodeError - OK
"""
