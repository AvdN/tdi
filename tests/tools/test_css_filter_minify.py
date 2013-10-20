
from tdi._test_support import pure

from tdi import html
from tdi.tools import css

html = html.replace(eventfilters=[css.MinifyFilter])



def test_css_filter_minify(capsys, pure):
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
    print out, _out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
<html>

<style>a b c{foo:bar;baz:blub}</style>
<style></style>
</html>
"""
