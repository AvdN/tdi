
from tdi._test_support import pure

from tdi.tools import javascript

def test_js_cleanup(capsys, pure):
    x = javascript.cleanup(u"""<!-- script1
    //-->""")
    print repr(x)

    x = javascript.cleanup("""<!-- script1
    //-->""")
    print repr(x)

    x = javascript.cleanup("""<!-- script1 - \xc3\xa9
    //-->""", encoding='utf-8')
    print repr(x)

    x = javascript.cleanup(u"""<![CDATA[
        script2
    ]]>""")
    print repr(x)

    x = javascript.cleanup("""<![CDATA[
        script2
    ]]>""")
    print repr(x)

    x = javascript.cleanup("""<![CDATA[
        script2 - \xc3\xa9
    ]]>""", encoding='utf-8')
    print repr(x)

    x = javascript.cleanup(u"""//<![CDATA[
        script3
    //]]>""")
    print repr(x)

    x = javascript.cleanup("""//<![CDATA[
        script3
    //]]>""")
    print repr(x)

    x = javascript.cleanup("""//<![CDATA[
        script3 - \xc3\xa9
    //]]>""", encoding='utf-8')
    print repr(x)

    x = javascript.cleanup(u"""<!--//--><![CDATA[//><!--
        script4
    //--><!]]>""")
    print repr(x)

    x = javascript.cleanup("""<!--//--><![CDATA[//><!--
        script4
    //--><!]]>""")
    print repr(x)

    x = javascript.cleanup("""<!--//--><![CDATA[//><!--
        script4 - \xc3\xa9
    //--><!]]>""", encoding='utf-8')
    print repr(x)

    try:
        x = javascript.cleanup("""<!--//--><![CDATA[//><!--
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
u'script1'
'script1'
'script1 - \\xc3\\xa9'
u'script2'
'script2'
'script2 - \\xc3\\xa9'
u'script3'
'script3'
'script3 - \\xc3\\xa9'
u'script4'
'script4'
'script4 - \\xc3\\xa9'
UnicodeError - OK
"""
