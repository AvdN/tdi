
from tdi._test_support import pure

from tdi.tools import javascript

def test_js_cdata(capsys, pure):
    x = javascript.cdata(u"""<!-- script1
    //-->""")
    print repr(x)

    x = javascript.cdata("""<!-- script1
    //-->""")
    print repr(x)

    x = javascript.cdata("""<!-- script1 - \xc3\xa9
    //-->""", encoding='utf-8')
    print repr(x)

    x = javascript.cdata(u"""<![CDATA[
        script2
    ]]>""")
    print repr(x)

    x = javascript.cdata("""<![CDATA[
        script2
    ]]>""")
    print repr(x)

    x = javascript.cdata("""<![CDATA[
        script2 - \xc3\xa9
    ]]>""", encoding='utf-8')
    print repr(x)

    x = javascript.cdata(u"""//<![CDATA[
        script3
    //]]>""")
    print repr(x)

    x = javascript.cdata("""//<![CDATA[
        script3
    //]]>""")
    print repr(x)

    x = javascript.cdata("""//<![CDATA[
        script3 - \xc3\xa9
    //]]>""", encoding='utf-8')
    print repr(x)

    x = javascript.cdata(u"""<!--//--><![CDATA[//><!--
        script4
    //--><!]]>""")
    print repr(x)

    x = javascript.cdata("""<!--//--><![CDATA[//><!--
        script4
    //--><!]]>""")
    print repr(x)

    x = javascript.cdata("""<!--//--><![CDATA[//><!--
        script4 - \xc3\xa9
    //--><!]]>""", encoding='utf-8')
    print repr(x)

    try:
        x = javascript.cdata("""<!--//--><![CDATA[//><!--
            script4 - \xe9
        //--><!]]>""", encoding='utf-8')
    except UnicodeError:
        print "UnicodeError - OK"

    out, _ = capsys.readouterr()
    print out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
u'<!--//--><![CDATA[//><!--\\nscript1\\n//--><!]]>'
'<!--//--><![CDATA[//><!--\\nscript1\\n//--><!]]>'
'<!--//--><![CDATA[//><!--\\nscript1 - \\xc3\\xa9\\n//--><!]]>'
u'<!--//--><![CDATA[//><!--\\nscript2\\n//--><!]]>'
'<!--//--><![CDATA[//><!--\\nscript2\\n//--><!]]>'
'<!--//--><![CDATA[//><!--\\nscript2 - \\xc3\\xa9\\n//--><!]]>'
u'<!--//--><![CDATA[//><!--\\nscript3\\n//--><!]]>'
'<!--//--><![CDATA[//><!--\\nscript3\\n//--><!]]>'
'<!--//--><![CDATA[//><!--\\nscript3 - \\xc3\\xa9\\n//--><!]]>'
u'<!--//--><![CDATA[//><!--\\nscript4\\n//--><!]]>'
'<!--//--><![CDATA[//><!--\\nscript4\\n//--><!]]>'
'<!--//--><![CDATA[//><!--\\nscript4 - \\xc3\\xa9\\n//--><!]]>'
UnicodeError - OK
"""
