
from tdi._test_support import pure

from tdi import filters as _filters
from tdi import html as _html

from textwrap import dedent

class Count(_filters.BaseEventFilter):
    def __init__(self, builder):
        super(Count, self).__init__(builder)
        self.tags = {}

    def handle_starttag(self, name, attr, closed, data):
        self.tags[name] = self.tags.get(name, 0) + 1
        self.builder.handle_starttag(name, attr, closed, data)

    def finalize(self):
        keys = self.tags.keys()
        keys.sort()
        for key in keys:
            print "%s: %d" % (key, self.tags[key])
        return self.builder.finalize()

def test_model(capsys, pure):
    html = _html.replace(overlay_eventfilters=[Count])

    print "Before Loading"
    template = html.from_string(dedent("""
    <anode tdi:overlay="foo"></anode>
    """)).overlay(html.from_string(dedent("""
    <bnode tdi:overlay="foo">
    <cnode />
    </bnode>
    """)))

    print ">>> Between Loading and Rendering"

    template.render()

    print ">>> Between Rendering"

    template.render()

    print ">>> After Rendering"

    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
Before Loading
>>> Between Loading and Rendering
bnode: 1
cnode: 1

<bnode>
<cnode />
</bnode>
>>> Between Rendering

<bnode>
<cnode />
</bnode>
>>> After Rendering
"""
