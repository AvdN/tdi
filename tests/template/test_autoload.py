
import pytest
from tdi._test_support import pure

import sys
import tempfile
import time

from tdi import html

# AvdN: use monkeypatching here?
html = html.replace(autoupdate=True)

def test_autoload(capsys, pure):

    tfile = tempfile.NamedTemporaryFile()
    try:
        tfile.write("""<html><body tdi="body">Yey</body></html>""")
        tfile.flush()

        # 2) Load the template from_file
        template = html.from_file(tfile.name)
        print template.tree

        # (... wait for low-timer-resolution systems ...)
        time.sleep(3)

        # 3) Update the file
        tfile.seek(0)
        tfile.truncate()
        tfile.write("""<html><body tdi="nobody">Yup!</body></html>""")
        tfile.flush()

        # 4) Voila
        print template.tree

    finally:
        tfile.close()
    out, _ = capsys.readouterr()
    assert out == _out


############################################################

_out = u"""\
/
  '<html>'
  body
    'Yey'
  '</html>'
\\

/
  '<html>'
  nobody
    'Yup!'
  '</html>'
\\

"""
