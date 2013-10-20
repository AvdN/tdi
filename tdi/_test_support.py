
import os
import sys
import textwrap

import pytest

# select here  which versions get tested with C extension or not
if sys.version_info < (2, 5):
    _params = [1] # only pure python
else:
    _params = [0, 1] # both C and pure python

@pytest.fixture(params=_params)
def pure(request, monkeypatch):
    monkeypatch.setenv('TDI_NO_C_OVERRIDE', request.param)

# you can test the pure fixture with:
#def test_fixture(pure):
#    print 'TDI_NO_C_OVERRIDE', repr(os.environ['TDI_NO_C_OVERRIDE'])
#    assert 0

def dedent(txt, normalize=False):
    if normalize:
        txt = txt.replace('\r\n', '\n').replace('\r', '\n')
    ret_val = textwrap.dedent(txt)
    if normalize:
        ret_val = ret_val.strip()
    return ret_val
