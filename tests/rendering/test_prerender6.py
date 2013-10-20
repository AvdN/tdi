
import os, pytest
from tdi._test_support import pure

from tdi.model_adapters import RenderAdapter
from tdi import html

template = html.from_string("""
<anode tdi="anode"></anode>
""".lstrip())

class Model(object):
    def __init__(self, version):
        self._version = version

    def prerender_version(self, version):
        return version != self._version, self._version

    def render_anode(self, node):
        print "render_anode", self._version


def test_model_01(capsys, pure):
    if os.environ['TDI_NO_C_OVERRIDE'] != '1':
        pytest.skip("unclear output difference")
    print template.render_string(prerender=Model(1))
    print "---"
    print template.render_string(prerender=Model(1))
    out, _ = capsys.readouterr()
    _out = 'render_anode 1\n<anode></anode>\n\n---\n<anode></anode>\n\n'
    print out
    print _out
    assert out == _out

def test_model_02(capsys, pure):
    if os.environ['TDI_NO_C_OVERRIDE'] != '1':
        pytest.skip("unclear output difference")
    print template.render_string(prerender=Model(2))
    print "---"
    print template.render_string(prerender=Model(2))
    out, _ = capsys.readouterr()
    _out = 'render_anode 2\n<anode></anode>\n\n---\n<anode></anode>\n\n'
    print out
    print _out
    assert out == _out



############################################################

_out = u"""\
render_anode 1
<anode></anode>

---
<anode></anode>

---
render_anode 2
<anode></anode>

---
<anode></anode>

"""
