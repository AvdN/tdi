
from tdi._test_support import pure

# BEGIN INCLUDE
from tdi import html
from tdi.tools import javascript

template = html.from_string("""
<html>
<body>
    <tdi tdi="-script">
    <div tdi="*html"><h1 tdi="h1">dynamic js-only-content</h1></div>
    <script tdi="*script">
        document.write('__html__')
    </script>
    </tdi>
</body>
</html>
""".lstrip())


class Model2(object):
    def render_h1(self, node):
        node.content = u"different."


class Model(object):
    def render_h1(self, node):
        node.content = u"My Heading"

    def render_script(self, node):
        node.html.h1['foo'] = 'bar'
        html = node.html.render(model=Model2())
        javascript.fill(node.replace(None, node.script), dict(html=html))


def test_model(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
<html>
<body>
    <script>
        document.write('<div><h1 foo=\\"bar\\">different.<\\/h1><\\/div>')
    </script>
</body>
</html>
"""
