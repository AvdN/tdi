# coding: utf-8
from tdi._test_support import pure

import re as _re

from tdi import html
from tdi.tools import javascript

def test_js_fill(capsys, pure):
    tpl = html.from_string("""
<script tdi="script">
    var count = __a__;
    var name = '__b__';
    var param = __c__;
</script>
""".lstrip())
    json = javascript.LiteralJSON(u'{"name": "Andr\xe9]]>"}')
    class Model(object):
        def render_script(self, node):
            javascript.fill(node, dict(
                a=10,
                b=u'Andr\xe9',
                c=json,
            ))
    tpl.render(Model())

    tpl = html.from_string("""
<meta charset=utf-8>
<script tdi="script">
    var count = __a__;
    var name = '__b__';
    var param = __c__;
</script>
""".lstrip())
    json = javascript.LiteralJSON(u'{"name": "Andr\xe9]]>"}')
    class Model(object):
        def render_script(self, node):
            javascript.fill(node, dict(
                a=10,
                b=u'Andr\xe9',
                c=json,
            ))
    tpl.render(Model())

    tpl = html.from_string("""
<meta charset=utf-8>
<script tdi="script">
    var count = __a__;
    var name = '__b__';
    var param = __c__;
</script>
""".lstrip())
    json = javascript.LiteralJSON(u'{"name": "Andr\xe9]]>"}')
    class Model(object):
        def render_script(self, node):
            javascript.fill(node, dict(
                a=10,
                b=u'Andr\xe9',
                c=json,
            ), as_json=False)
    tpl.render(Model())

    tpl = html.from_string("""
<meta charset=utf-8>
<script tdi="script">
    var count = @a@;
    var name = '@b@';
    var param = @c@;
</script>
""".lstrip())
    json = javascript.LiteralJSON(u'{"name": "Andr\xe9]]>"}')
    class Model(object):
        def render_script(self, node):
            javascript.fill(node, dict(
                a=10,
                b=u'Andr\xe9',
                c=json,
            ), pattern=ur'@(?P<name>[^@]+)@')
    tpl.render(Model())

    tpl = html.from_string("""
<meta charset=utf-8>
<script tdi="script">
    var count = @a@;
    var name = '@b@';
    var param = @c@;
</script>
""".lstrip())
    json = javascript.LiteralJSON(u'{"name": "Andr\xe9]]>"}')
    class Model(object):
        def render_script(self, node):
            javascript.fill(node, dict(
                a=10,
                b=u'Andr\xe9',
                c=json,
            ), pattern=_re.compile(ur'@(?P<name>[^@]+)@'))
    tpl.render(Model())

    tpl = html.from_string("""
<meta charset=utf-8>
<script tdi="script">
    var count = @a@;
    var name = '@b@';
    var param = @c@;
</script>
""".lstrip())
    json = javascript.LiteralJSON(u'{"name": "Andr\xe9]]>"}')
    class Model(object):
        def render_script(self, node):
            javascript.fill(node, dict(
                a=10,
                b=u'Andr\xe9',
                c=json,
            ), pattern=ur'@(?P<name>[^@]+)@', as_json=False)
    tpl.render(Model())

    out, _ = capsys.readouterr()
    print out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
<script>
    var count = 10;
    var name = 'Andr\\xe9';
    var param = {"name": "Andr\\u00e9]\\]>"};
</script>
<meta charset=utf-8>
<script>
    var count = 10;
    var name = 'Andr\\xe9';
    var param = {"name": "André]\\]>"};
</script>
<meta charset=utf-8>
<script>
    var count = 10;
    var name = 'Andr\\xe9';
    var param = {\\"name\\": \\"Andr\\xe9]\\]>\\"};
</script>
<meta charset=utf-8>
<script>
    var count = 10;
    var name = 'Andr\\xe9';
    var param = {"name": "André]\\]>"};
</script>
<meta charset=utf-8>
<script>
    var count = 10;
    var name = 'Andr\\xe9';
    var param = {"name": "André]\\]>"};
</script>
<meta charset=utf-8>
<script>
    var count = 10;
    var name = 'Andr\\xe9';
    var param = {\\"name\\": \\"Andr\\xe9]\\]>\\"};
</script>
"""
