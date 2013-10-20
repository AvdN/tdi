
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node tdi="item">
    <znode tdi:overlay="foo">
        <ynode tdi="subnested"></ynode>
    </znode>
</node>
""".lstrip())

class Model(object):
    def render_subnested(self, node):
        node.content = u"yeah."


def test_overlay_transparent3(capsys, pure):
    model = Model()
    template.render(model, startnode="item.subnested")
    print
    out, _ = capsys.readouterr()
    print out, _out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
<ynode>yeah.</ynode>
"""
