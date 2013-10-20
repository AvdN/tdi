
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node tdi="item">
    <znode tdi="nested">
        <ynode tdi="subnested"></ynode>
    </znode>
    <xnode tdi="a"></xnode>
</node>
""".lstrip())

class Model(object):
    def render_item(self, node):
        node.replace(self.replace_nested, node.nested)
        return True

    def replace_nested(self, node):
        node.replace(self.replace_subnested, node.subnested)
        return True

    def replace_subnested(self, node):
        node.content = "yay..."


def test_model(capsys, pure):
    model = Model()
    template.render(model)
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<ynode>yay...</ynode>
"""
