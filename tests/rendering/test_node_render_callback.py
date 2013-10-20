
import pytest
from tdi._test_support import pure

from tdi import html

template = html.from_string("""
<html>
<body>
<div tdi="some">
content <tdi tdi="-count" />
</div>
</body>
</html>
""".strip())

class Model(object):
    def render_some(self, node):
        def callback(node, *fixed):
            node['fixed'] = ' '.join(map(str, fixed))
        print repr(node.render(callback))
        print repr(node.render(callback, decode=False))
        print repr(node.render(callback, 1, 2, 'a'))
        print repr(node.render(callback, 3, 4, 'b', decode=False))

    def render_count(self, node):
        node.content = self.count = getattr(self, 'count', 0) + 1

@pytest.skip("ordering of output issue")
def test_model(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out
    print '====='
    print _out
    assert out == _out

############################################################

_out = u"""\
u'<div fixed="">\\ncontent 1\\n</div>'
'<div fixed="">\\ncontent 2\\n</div>'
u'<div fixed="1 2 a">\\ncontent 3\\n</div>'
'<div fixed="3 4 b">\\ncontent 4\\n</div>'
<html>
<body>
<div>
content 5
</div>
</body>
</html>
"""
