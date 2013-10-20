
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
        node.replace(self.replace_item, node)
        return True

    def replace_item(self, node):
        node.content = u"whoa!"


def test_model(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<node>whoa!</node>
"""
