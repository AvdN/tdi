
from tdi._test_support import pure

from tdi import html
from tdi.model_adapters import PreRenderWrapper, RenderAdapter

template = html.from_string("""
<foo>
    <bar tdi:overlay=">-foo"/>
</foo>
""".lstrip()).overlay(html.from_string("""
<tdi tdi:overlay="-foo">
    <script tdi="test">JAVASCRIPT</script>
</tdi>
""".lstrip()))

class Model(object):
    def render_test(self, node):
        node.raw.content = node.raw.content.replace('SCR', ' hey ')

def adapter(model):
    return PreRenderWrapper(RenderAdapter(model))


def test_model(capsys, pure):
    model = Model()
    html.from_string(template.render_string(None, adapter=adapter)).render(
        model, startnode="test"
    )
    print
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<script>JAVA hey IPT</script>
"""
