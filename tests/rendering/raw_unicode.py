#!/usr/bin/env python
import warnings as _warnings
_warnings.resetwarnings()
_warnings.filterwarnings('error')

from tdi import html

template = html.from_string("""
<node>
    <xnode tdi="foo"></xnode>
</node>
""".lstrip())

class Model(object):
    def render_foo(self, node):
        node.raw.content = u'Andr\xe9 <>'
        node.raw[u'foo'] = u"'Mal\xf3<>'"

template.render(Model())
