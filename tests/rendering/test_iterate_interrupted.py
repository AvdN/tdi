
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<node tdi="item">
    <node tdi="nested">
        <node tdi="subnested"></node>
    </node><tdi tdi=":-nested">
    </tdi>
</node>
""".lstrip())

class Model(object):
    def render_item(self, node):
        for subnode, item in node.nested.iterate([1, 2, 3, 4]):
            subnode['j'] = item
            subnode.content = u'should be here %s' % item
            if item == 3:
                break


def test_model(capsys, pure):
    model = Model()
    template.render(model)
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<node>
    <node j="1">should be here 1</node>
    <node j="2">should be here 2</node>
    <node j="3">should be here 3</node>
</node>
"""
