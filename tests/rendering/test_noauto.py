
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<anode tdi="level1">
    <node tdi="*level2">
        <node tdi="level3">
            hey.
        </node>
    </node>
</anode>
""".lstrip())

class Model(object):
    def render_level2(self, node):
        node['foo'] = 'bar'

    def render_level3(self, node):
        node.content = 'sup.'


def test_model(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<anode>
    <node>
        <node>sup.</node>
    </node>
</anode>
"""
