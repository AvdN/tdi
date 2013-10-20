
from tdi._test_support import pure

from tdi.tools import html as html_tools
from tdi import html

template = html.from_string("""
<anode tdi="level1">
    <!-- Comment! -->
    <bnode tdi="foo"></bnode>
</anode>
""".lstrip())

class PreModel(object):
    def __init__(self, version):
        self._version = version

    def prerender_version(self, oldversion):
        return self._version != oldversion, self._version

    def render_foo(self, node):
        node.content = u'hey'


class FilteredPreModel(PreModel):
    def prerender_filters(self):
        return dict(eventfilters=[html_tools.CommentStripFilter])



def test_prerender_filter(capsys, pure):
    template.render(None, prerender=PreModel(1))
    template.render(None, prerender=FilteredPreModel(1))
    template.render(None, prerender=FilteredPreModel(2))
    out, _ = capsys.readouterr()
    print out, _out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
<anode>
    <!-- Comment! -->
    <bnode>hey</bnode>
</anode>
<anode>
    <!-- Comment! -->
    <bnode>hey</bnode>
</anode>
<anode>
    \n\
    <bnode>hey</bnode>
</anode>
"""
