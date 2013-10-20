# coding: utf-8
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<?xml version="1.0" encoding="utf-8" ?>
<node>
    <xnode tdi="foo"></xnode>
</node>
""".lstrip())

class Model(object):
    def render_foo(self, node):
        try:
            node.raw[u'b\xe9lah'] = 'blargh'
        except UnicodeError:
            node.raw[u'blah'] = 'blargh'


def test_model(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
<?xml version="1.0" encoding="utf-8" ?>
<node>
    <xnode bélah=blargh></xnode>
</node>
"""
