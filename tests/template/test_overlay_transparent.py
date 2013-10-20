
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
    def render_item(self, node):
        try:
            node.subnested.content = u"yeah."
        except AttributeError:
            pass


def test_overlay_transparent(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
<node>
    <znode>
        <ynode>yeah.</ynode>
    </znode>
</node>
"""
