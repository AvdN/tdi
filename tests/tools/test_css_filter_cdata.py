
from tdi._test_support import pure, dedent

from tdi import html
from tdi.tools import css

html = html.replace(eventfilters=[css.CDATAFilter])


def test_css_filter_cdata(capsys, pure):
    tpl = html.from_string("""
<html>
<style><!--
--></style>
<style><!--
a b c{
    foo: bar;
    baz: blub;
}
--></style>
<style tdi="bar"><!--
--></style>
</html>
""".lstrip())

    tpl.render()
    out, _ = capsys.readouterr()
    assert out == _out

############################################################

_out = u"""\
<html>

<style><!--/*--><![CDATA[/*><!--*/
a b c{
    foo: bar;
    baz: blub;
}
/*]]>*/--></style>
<style></style>
</html>
"""
