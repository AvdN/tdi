
from __future__ import with_statement  # needed for Python 2.5

import pytest
from tdi._test_support import pure

import warnings

from tdi import NodeWarning
from tdi import html

warnings.filterwarnings("error", category=NodeWarning)

def test_model(capsys, pure):
    with pytest.raises(NodeWarning) as e:
        template = html.from_string("""
        <node tdi="item">
            <node tdi="nested">
                <node tdi="subnested"></node>
            </node><tdi tdi=":-nested">
            </tdi><tdi tdi=":-nested2">
            </tdi>
        </node>
        """.lstrip())
    assert e.exconly().split(': ', 1)[1] == "Ignoring separator node(s) "  \
           "without accompanying content node: 'nested2'"

############################################################

_out = u"""\
OK: Nodewarning: Ignoring separator node(s) without accompanying content node: 'nested2'
"""
