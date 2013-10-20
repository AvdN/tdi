
from tdi._test_support import pure

# BEGIN INCLUDE
from tdi import html, model_adapters
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


class Model3(object):
    def render_h1(self, node):
        node.content = u"yo!"

def adapter(m):
    return model_adapters.RenderAdapter(Model3())


class Model2(object):
    def render_h1(self, node):
        node.content = u"different."


class Model(object):
    def render_h1(self, node):
        node.content = u"My Heading"

    def render_script(self, node):
        html = node.html.render(adapter=adapter)
        javascript.fill(node.replace(None, node.script), dict(html=html))


def test_model(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    assert out == _out

############################################################

_out = u"""\
<html>
<body>
    <script>
        document.write('<div><h1>My Heading<\\/h1><\\/div>')
    </script>
</body>
</html>
"""