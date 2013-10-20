
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
        print repr(node.render())
        print repr(node.render(decode=False))
        node.remove()

    def render_count(self, node):
        node.content = self.count = getattr(self, 'count', 0) + 1


def test_model(capsys, pure):
    print template.render_string(Model())
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
u'<div>\\ncontent 1\\n</div>'
'<div>\\ncontent 2\\n</div>'
<html>
<body>

</body>
</html>
"""
