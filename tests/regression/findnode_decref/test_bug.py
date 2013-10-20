
from tdi._test_support import pure
"""
Submitted by: Roland Sommer <roland.sommer@gmx.org>

segfault in tdi.c
"""
#import warnings as _warnings
#_warnings.resetwarnings()
#_warnings.filterwarnings('error')

import os
from tdi import html


def test_bug(capsys, pure):
    template = html.from_files([
        '_baselayout.html', 'results.html', '_widgets.html',
    ], basedir=os.path.dirname(os.path.abspath(__file__)))

    for _ in xrange(10):
        template.render(startnode="resulttable")
    print
    out, _ = capsys.readouterr()
    print out
    print '========'
    print _out
    assert out == _out

############################################################

_out = u"""\
<span>Here i am</span><span>Here i am</span><span>Here i am</span><span>Here i am</span><span>Here i am</span><span>Here i am</span><span>Here i am</span><span>Here i am</span><span>Here i am</span><span>Here i am</span>
"""
