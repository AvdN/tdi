# coding: utf-8
from tdi._test_support import pure

import re as _re

from tdi import html
from tdi.tools import javascript

def test_js_fill_attr(capsys, pure):
    tpl = html.from_string("""
<a tdi="link" onclick="alert('__what__'); return false">Click me</a>
""".lstrip())
    json = javascript.LiteralJSON(u'{"name": "Andr\xe9]]>"}')
    class Model(object):
        def render_link(self, node):
            javascript.fill_attr(node, u'onclick', dict(
                what = u'Andr\xe9',
            ))
    tpl.render(Model())

    tpl = html.from_string("""
<a tdi="link" onclick="alert('__what__'); return false">Click me</a>
""".lstrip())
    json = javascript.LiteralJSON(u'{"name": "Andr\xe9]]>"}')
    class Model(object):
        def render_link(self, node):
            javascript.fill_attr(node, u'onclick', dict(
                what = json,
            ))
    tpl.render(Model())

    tpl = html.from_string("""
<meta charset=utf-8>
<a tdi="link" onclick="alert('__what__'); return false">Click me</a>
""".lstrip())
    json = javascript.LiteralJSON(u'{"name": "Andr\xe9]]>"}')
    class Model(object):
        def render_link(self, node):
            javascript.fill_attr(node, u'onclick', dict(
                what = json,
            ))
    tpl.render(Model())

    tpl = html.from_string("""
<meta charset=utf-8>
<a tdi="link" onclick="alert('__what__'); return false">Click me</a>
""".lstrip())
    json = javascript.LiteralJSON(u'{"name": "Andr\xe9]]>"}')
    class Model(object):
        def render_link(self, node):
            javascript.fill_attr(node, u'onclick', dict(
                what = json,
            ), as_json=False)
    tpl.render(Model())

    tpl = html.from_string("""
<meta charset=utf-8>
<a tdi="link" onclick="alert('@what@'); return false">Click me</a>
""".lstrip())
    json = javascript.LiteralJSON(u'{"name": "Andr\xe9]]>"}')
    class Model(object):
        def render_link(self, node):
            javascript.fill_attr(node, u'onclick', dict(
                what = json,
            ), pattern=ur'@(?P<name>[^@]+)@', as_json=False)
    tpl.render(Model())

    tpl = html.from_string("""
<meta charset=utf-8>
<a tdi="link" onclick="alert('@what@'); return false">Click me</a>
""".lstrip())
    json = javascript.LiteralJSON(u'{"name": "Andr\xe9]]>"}')
    class Model(object):
        def render_link(self, node):
            javascript.fill_attr(node, u'onclick', dict(
                what = json,
            ), pattern=_re.compile(ur'@(?P<name>[^@]+)@'), as_json=False)
    tpl.render(Model())

    tpl = html.from_string("""
<meta charset=utf-8>
<a tdi="link" onclick="alert('@what@'); return false">Click me</a>
""".lstrip())
    json = javascript.LiteralJSON(u'{"name": "Andr\xe9]]>"}')
    class Model(object):
        def render_link(self, node):
            javascript.fill_attr(node, u'onclick', dict(
                what = json,
            ), pattern=_re.compile(ur'@(?P<name>[^@]+)@'))
    tpl.render(Model())

    out, _ = capsys.readouterr()
    print out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
<a onclick="alert('Andr\\xe9'); return false">Click me</a>
<a onclick="alert('{&quot;name&quot;: &quot;Andr\\u00e9]]&gt;&quot;}'); return false">Click me</a>
<meta charset=utf-8>
<a onclick="alert('{&quot;name&quot;: &quot;André]]&gt;&quot;}'); return false">Click me</a>
<meta charset=utf-8>
<a onclick="alert('{\\&quot;name\\&quot;: \\&quot;Andr\\xe9]]&gt;\\&quot;}'); return false">Click me</a>
<meta charset=utf-8>
<a onclick="alert('{\\&quot;name\\&quot;: \\&quot;Andr\\xe9]]&gt;\\&quot;}'); return false">Click me</a>
<meta charset=utf-8>
<a onclick="alert('{\\&quot;name\\&quot;: \\&quot;Andr\\xe9]]&gt;\\&quot;}'); return false">Click me</a>
<meta charset=utf-8>
<a onclick="alert('{&quot;name&quot;: &quot;André]]&gt;&quot;}'); return false">Click me</a>
"""
