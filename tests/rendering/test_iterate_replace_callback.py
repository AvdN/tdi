
from tdi._test_support import pure
"""
Test if iterate->replace with callback works

Submitted by: Jens Michlo
"""
import warnings as _warnings
_warnings.resetwarnings()
_warnings.filterwarnings('error')

from tdi import html

template = html.from_string("""
<tdi tdi="-items">
<tdi tdi="-item">
<tdi tdi="-product">
           Produtcs
</tdi>
<tdi tdi="-offer">
           Offer
</tdi>
<tdi tdi="-leer">
           leer
</tdi>
</tdi>
</tdi>
""".lstrip())


class Model(object):
    def _render(self, subnode, item):
        print "OK", item

    def render_items(self, node):
        items = [1 ,2 ,3]
        for subnode,item in node.item.iterate(items):
            subnode.replace(self._render, subnode.product, item)



def test_model(capsys, pure):
    template.render_string(Model())
    out, _ = capsys.readouterr()
    print out, _out
    assert out == _out

############################################################

_out = u"""\
OK 1
OK 2
OK 3
"""
