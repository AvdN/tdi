
import pytest
from tdi._test_support import pure

from tdi import text

template = text.from_string("""
[? encoding latin-1 ?]Hello [[name]]!

Look, hey, this is a text []template]. And here's a list:

[item]* some stuff[/item][tdi=":item"]
[/]

Thanks for [[+listening]].
""".lstrip())

class Model(object):
    def render_name(self, node):
        node.content = u"Andr\xe9"

    def render_item(self, node):
        for snode, fruit in node.iterate((u'apple', u'pear', u'cherry')):
            snode.content = u'* %s' % fruit

@pytest.skip("extra newline inserted")
def test_model(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    print out, _out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
Hello Andr\xe9!
Look, hey, this is a text [template]. And here's a list:

* apple
* pear
* cherry

Thanks for [[+listening]].
"""
