
from tdi._test_support import pure

from tdi.tools import html as _html_tools
from tdi import html

html_compressed = html.replace(eventfilters=[_html_tools.MinifyFilter])

template = html_compressed.from_string("""
<html>
<head>
    <title>Boo! </title>
    <script>
        Some script
    </script>
    <style><!--
        Some style
    --></style>
</head>
<body>
    <p>Hello <b>YOU!</b> reader!

    Now...      <br />
    <form>
        <textarea   >Some
text
in     here.
        </textarea >
    </form>

    <!-- Comment! -->
    <pre>
        More text

            in


                here.
    </pre>
</body>
</html  >
abc

""")


def test_filter_whitespace(capsys, pure):
    template.render()
    print
    out, _ = capsys.readouterr()
    assert out == _out

############################################################

_out = u"""\
<html><head><title>Boo!</title><script>Some script</script><style><!--
        Some style
    --></style></head><body><p>Hello <b>YOU!</b> reader! Now... <br /><form><textarea>Some
text
in     here.
        </textarea></form><pre>
        More text

            in


                here.</pre></body></html>abc
"""
