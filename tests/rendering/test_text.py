# coding: utf-8

from tdi._test_support import pure

from tdi import text

template = text.from_string("""
Hello [[name]]!

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


def test_model(capsys, pure):
    template.render(Model())
    out, _ = capsys.readouterr()
    assert out == _out

############################################################

_out = u"""\
Hello André!

Look, hey, this is a text [template]. And here's a list:

* apple
* pear
* cherry

Thanks for [[+listening]].
"""
