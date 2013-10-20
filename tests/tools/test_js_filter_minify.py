
from tdi._test_support import pure

from tdi import html
from tdi.tools import javascript

html = html.replace(eventfilters=[javascript.MinifyFilter])

def test_js_filter_minify(capsys, pure):
    tpl = html.from_string("""
<html>
<script src="foo"></script>
<script><!--
//--></script>
<script><!--
var x=1;
var y = 2;
alert( x + y );
//--></script>
<script tdi="bar"><!--
--></script>
</html>
""".lstrip())

    tpl.render()

    out, _ = capsys.readouterr()
    print out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
<html>
<script src="foo"></script>

<script>var x=1;var y=2;alert(x+y);</script>
<script></script>
</html>
"""
