
from tdi._test_support import pure

from tdi.tools import html


def test_html_minify_cdata(capsys, pure):
    print html.minify(u"""
    <html>
    <head>
        <!-- Here comes the title -->
        <title>Hello World!</title>
        <style>
            Some style.
        </style>
    </head>
    <body>
        <!-- foo -->
        <script>
            Some script.
        </script>
        <h1>Hello World!</h1>
        <!-- bar -->
    </body>
    """.lstrip(), cdata_containers=True)

    out, _ = capsys.readouterr()
    assert out == _out

############################################################

_out = u"""\
<html><head><title>Hello World!</title><style><!--/*--><![CDATA[/*><!--*/
Some style.
/*]]>*/--></style></head><body><script><!--//--><![CDATA[//><!--
Some script.
//--><!]]></script><h1>Hello World!</h1></body>
"""
