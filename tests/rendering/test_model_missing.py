
from __future__ import with_statement  # needed for Python 2.5
import pytest
from tdi._test_support import pure

from tdi import ModelMissingError
from tdi import html
from tdi.model_adapters import RenderAdapter

template = html.from_string("""
<node tdi="nested">
    <xnode tdi="a"></xnode>
</node>
""".lstrip())

class Model(object):

    def render_a(self, node):
        node.content = u'hey'

class DevNull(object):
    def write(self, s):
        pass

def test_model(pure):
    model = Model()

    def adapter(model):
        return RenderAdapter(model, requiremethods=True)

    with pytest.raises(ModelMissingError) as e:
        template.render(model, stream=DevNull(), adapter=adapter)
    assert e.exconly().split(': ', 1)[1] == 'render_nested'

