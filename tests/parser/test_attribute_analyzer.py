
from __future__ import with_statement

import pytest
from tdi._test_support import pure

import sys as _sys

from tdi.markup import _analyzer
from tdi.markup.soup import decoder as _decoder
from tdi._exceptions import TemplateAttributeError

#  pytest.skip("needs more conversion, pattern is there")")
def org_test(*args, **kwargs):
    for hidden in (False, True):
        for remove in (False, True):
            analyze = _analyzer.DEFAULT_ANALYZER(
                _decoder.HTMLDecoder('cp1252'),
                hidden=hidden,
                removeattribute=remove,
            )
            try:
                res = analyze(*args, **kwargs)
            except (SystemExit, KeyboardInterrupt):
                raise
            except:
                e = _sys.exc_info()[:2]
                print "%s: %s" % (e[0].__name__, e[1])
            else:
                print "%r, tdi=%r, scope=%r, overlay=%r" % (
                    res[0],
                    res[1].get('attribute'),
                    res[1].get('scope'),
                    res[1].get('overlay'),
                )

@pytest.fixture(params=[False, True])
def hidden(request):
    return request.param

@pytest.fixture(params=[False, True])
def remove(request):
    return request.param

def aat(*args, **kwargs):
    hidden = kwargs.pop('hidden', False)
    remove = kwargs.pop('remove', False)
    print hidden, remove
    analyze = _analyzer.DEFAULT_ANALYZER(
        _decoder.HTMLDecoder('cp1252'),
        hidden=hidden,
        removeattribute=remove,
    )
    try:
        res = analyze(*args, **kwargs)
    except (SystemExit, KeyboardInterrupt):
        raise
    except:
        e = _sys.exc_info()[:2]
        return "%s: %s" % (e[0].__name__, e[1])
    else:
        return "%r, tdi=%r, scope=%r, overlay=%r" % (
            res[0],
            res[1].get('attribute'),
            res[1].get('scope'),
            res[1].get('overlay'),
        )

def test_empty(remove, hidden):
    assert aat([], hidden=hidden, remove=remove) == \
           "[], tdi=None, scope=None, overlay=None"

def test_scope_none(remove, hidden, pure):
    assert aat([('tdi:scope', None)], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid short tdi:scope attribute"

def test_scope_empty_string(remove, hidden, pure):
    assert aat([('tdi:scope', '')], remove=remove, hidden=hidden) == \
        "TemplateAttributeEmptyError: Empty tdi:scope attribute"

def test_scope_blank_string(remove, hidden, pure):
    assert aat([('tdi:scope', '" "')], remove=remove, hidden=hidden) == \
        "TemplateAttributeEmptyError: Empty tdi:scope attribute"

def test_scope_single_letter(pure):
    arg = [('tdi:scope', '"x"')]
    assert aat(arg, remove=False, hidden=False) == \
        """[('tdi:scope', '"x"')], tdi=None, scope=('', 'x'), overlay=None"""
    assert aat(arg, remove=True, hidden=False) == \
        """[], tdi=None, scope=('', 'x'), overlay=None"""
    assert aat(arg, remove=False, hidden=True) == \
        """[('tdi:scope', '"x"')], tdi=None, scope=('-', 'x'), overlay=None"""
    assert aat(arg, remove=True, hidden=True) == \
        """[], tdi=None, scope=('-', 'x'), overlay=None"""

def test_scope_single_digit(remove, hidden, pure):
    assert aat([('tdi:scope', '"9"')], remove=remove, hidden=hidden) == \
      "TemplateAttributeError: Invalid tdi:scope attribute u'9'"

def test_scope_letter_digit(pure):
    arg = [('tdi:scope', '"x9"')]
    assert aat(arg, remove=False, hidden=False) == \
        """[('tdi:scope', '"x9"')], tdi=None, scope=('', 'x9'), overlay=None"""
    assert aat(arg, remove=True, hidden=False) == \
        """[], tdi=None, scope=('', 'x9'), overlay=None"""
    assert aat(arg, remove=False, hidden=True) == \
        """[('tdi:scope', '"x9"')], tdi=None, scope=('-', 'x9'), overlay=None"""
    assert aat(arg, remove=True, hidden=True) == \
        """[], tdi=None, scope=('-', 'x9'), overlay=None"""

def test_scope_dot_letter_digit(remove, hidden, pure):
    assert aat([('tdi:scope', '".x9"')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi:scope attribute u'.x9'"

def test_scope_letter_error_00(remove, hidden, pure):
    assert aat([('tdi:scope', '"x9.0"')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi:scope attribute u'x9.0'"


aat([('tdi:scope', '"x9.y"')])
#[('tdi:scope', '"x9.y"')], tdi=None, scope=('', 'x9.y'), overlay=None
#[], tdi=None, scope=('', 'x9.y'), overlay=None
#[('tdi:scope', '"x9.y"')], tdi=None, scope=('-', 'x9.y'), overlay=None
#[], tdi=None, scope=('-', 'x9.y'), overlay=None


aat([('tdi:scope', '"x9.A"')])
#[('tdi:scope', '"x9.A"')], tdi=None, scope=('', 'x9.A'), overlay=None
#[], tdi=None, scope=('', 'x9.A'), overlay=None
#[('tdi:scope', '"x9.A"')], tdi=None, scope=('-', 'x9.A'), overlay=None
#[], tdi=None, scope=('-', 'x9.A'), overlay=None


aat([('tdi:scope', '"x9.A0"')])
#[('tdi:scope', '"x9.A0"')], tdi=None, scope=('', 'x9.A0'), overlay=None
#[], tdi=None, scope=('', 'x9.A0'), overlay=None
#[('tdi:scope', '"x9.A0"')], tdi=None, scope=('-', 'x9.A0'), overlay=None
#[], tdi=None, scope=('-', 'x9.A0'), overlay=None


def test_scope_letter_error_01(remove, hidden, pure):
    assert aat([('tdi:scope', '"x9.A0."')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi:scope attribute u'x9.A0.'"


aat([('tdi:scope', '"=x9.A0"')])
#[('tdi:scope', '"=x9.A0"')], tdi=None, scope=('=', 'x9.A0'), overlay=None
#[], tdi=None, scope=('=', 'x9.A0'), overlay=None
#[('tdi:scope', '"=x9.A0"')], tdi=None, scope=('=-', 'x9.A0'), overlay=None
#[], tdi=None, scope=('=-', 'x9.A0'), overlay=None


aat([('tdi:scope', '"=+x9.A0"')])
#[('tdi:scope', '"=+x9.A0"')], tdi=None, scope=('=', 'x9.A0'), overlay=None
#[], tdi=None, scope=('=', 'x9.A0'), overlay=None
#[('tdi:scope', '"=+x9.A0"')], tdi=None, scope=('=', 'x9.A0'), overlay=None
#[], tdi=None, scope=('=', 'x9.A0'), overlay=None


aat([('tdi:scope', '"=-x9.A0"')])
#[('tdi:scope', '"=-x9.A0"')], tdi=None, scope=('=-', 'x9.A0'), overlay=None
#[], tdi=None, scope=('=-', 'x9.A0'), overlay=None
#[('tdi:scope', '"=-x9.A0"')], tdi=None, scope=('=-', 'x9.A0'), overlay=None
#[], tdi=None, scope=('=-', 'x9.A0'), overlay=None


def test_scope_error_02(remove, hidden, pure):
    assert aat([('tdi:scope', '"==-x9.A0"')], remove=remove, hidden=hidden) == \
      "TemplateAttributeError: Invalid tdi:scope attribute u'==-x9.A0'"

def test_scope_error_03(remove, hidden, pure):
    assert aat([('tdi:scope', '"=-+x9.A0"')], remove=remove, hidden=hidden) == \
      "TemplateAttributeError: Invalid tdi:scope attribute u'=-+x9.A0'"

aat([('tdi:scope', '"="')])
#[('tdi:scope', '"="')], tdi=None, scope=('=', ''), overlay=None
#[], tdi=None, scope=('=', ''), overlay=None
#[('tdi:scope', '"="')], tdi=None, scope=('=-', ''), overlay=None
#[], tdi=None, scope=('=-', ''), overlay=None



def test_overlay_error_00(remove, hidden, pure):
    assert aat([('tdi:overlay', None)], remove=remove, hidden=hidden) == \
       "TemplateAttributeError: Invalid short tdi:overlay attribute"

def test_overlay_error_01(remove, hidden, pure):
    assert aat([('tdi:overlay', '')], remove=remove, hidden=hidden) == \
        "TemplateAttributeEmptyError: Empty tdi:overlay attribute"

def test_overlay_error_02(remove, hidden, pure):
    assert aat([('tdi:overlay', '" "')], remove=remove, hidden=hidden) == \
        "TemplateAttributeEmptyError: Empty tdi:overlay attribute"

aat([('tdi:overlay', '"x"')])
#[('tdi:overlay', '"x"')], tdi=None, scope=None, overlay=('', 'x')
#[], tdi=None, scope=None, overlay=('', 'x')
#[('tdi:overlay', '"x"')], tdi=None, scope=None, overlay=('-', 'x')
#[], tdi=None, scope=None, overlay=('-', 'x')


def test_overlay_error_03(remove, hidden, pure):
    assert aat([('tdi:overlay', '"9"')], remove=remove, hidden=hidden) == \
      "TemplateAttributeError: Invalid tdi:overlay attribute u'9'"

aat([('tdi:overlay', '"x9"')])
#[('tdi:overlay', '"x9"')], tdi=None, scope=None, overlay=('', 'x9')
#[], tdi=None, scope=None, overlay=('', 'x9')
#[('tdi:overlay', '"x9"')], tdi=None, scope=None, overlay=('-', 'x9')
#[], tdi=None, scope=None, overlay=('-', 'x9')

def test_overlay_error_04(remove, hidden, pure):
    assert aat([('tdi:overlay', '"x9.0"')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi:overlay attribute u'x9.0'"

def test_overlay_error_05(remove, hidden, pure):
    assert aat([('tdi:overlay', '"x9.y"')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi:overlay attribute u'x9.y'"

aat([('tdi:overlay', '"x9_A"')])
#[('tdi:overlay', '"x9_A"')], tdi=None, scope=None, overlay=('', 'x9_A')
#[], tdi=None, scope=None, overlay=('', 'x9_A')
#[('tdi:overlay', '"x9_A"')], tdi=None, scope=None, overlay=('-', 'x9_A')
#[], tdi=None, scope=None, overlay=('-', 'x9_A')


aat([('tdi:overlay', '"x9_A0"')])
#[('tdi:overlay', '"x9_A0"')], tdi=None, scope=N#one, overlay=('', 'x9_A0')
#[], tdi=None, scope=None, overlay=('', 'x9_A0')#
#[('tdi:overlay', '"x9_A0"')], tdi=None, scope=None, overlay=('-', 'x9_A0')
#[], tdi=None, scope=None, overlay=('-', 'x9_A0')


aat([('tdi:overlay', '"x9_A0_"')])
#[('tdi:overlay', '"x9_A0_"')], tdi=None, scope=None, overlay=('', 'x9_A0_')
#[], tdi=None, scope=None, overlay=('', 'x9_A0_')
#[('tdi:overlay', '"x9_A0_"')], tdi=None, scope=None, overlay=('-', 'x9_A0_')
#[], tdi=None, scope=None, overlay=('-', 'x9_A0_')


def test_overlay_error_06(remove, hidden, pure):
    assert aat([('tdi:overlay', '"=x9_A0"')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi:overlay attribute u'=x9_A0'"

aat([('tdi:overlay', '"<x9_A0"')])
#[('tdi:overlay', '"<x9_A0"')], tdi=None, scope=None, overlay=('<', 'x9_A0')
#[], tdi=None, scope=None, overlay=('<', 'x9_A0')
#[('tdi:overlay', '"<x9_A0"')], tdi=None, scope=None, overlay=('<-', 'x9_A0')
#[], tdi=None, scope=None, overlay=('<-', 'x9_A0')


aat([('tdi:overlay', '">x9_A0"')])
#[('tdi:overlay', '">x9_A0"')], tdi=None, scope=None, overlay=('>', 'x9_A0')
#[], tdi=None, scope=None, overlay=('>', 'x9_A0')
#[('tdi:overlay', '">x9_A0"')], tdi=None, scope=None, overlay=('>-', 'x9_A0')
#[], tdi=None, scope=None, overlay=('>-', 'x9_A0')


def test_overlay_error_07(remove, hidden, pure):
    assert aat([('tdi:overlay', '"<>x9_A0"')], remove=remove, hidden=hidden) ==\
        "TemplateAttributeError: Invalid tdi:overlay attribute u'<>x9_A0'"

aat([('tdi:overlay', '"+X9_A0"')])
#[('tdi:overlay', '"+X9_A0"')], tdi=None, scope=None, overlay=('', 'X9_A0')
#[], tdi=None, scope=None, overlay=('', 'X9_A0')
#[('tdi:overlay', '"+X9_A0"')], tdi=None, scope=None, overlay=('', 'X9_A0')
#[], tdi=None, scope=None, overlay=('', 'X9_A0')


aat([('tdi:overlay', '"<-x9_A0"')])
#[('tdi:overlay', '"<-x9_A0"')], tdi=None, scope=None, overlay=('<-', 'x9_A0')
#[], tdi=None, scope=None, overlay=('<-', 'x9_A0')
#[('tdi:overlay', '"<-x9_A0"')], tdi=None, scope=None, overlay=('<-', 'x9_A0')
#[], tdi=None, scope=None, overlay=('<-', 'x9_A0')


def test_overlay_error_08(remove, hidden, pure):
    assert aat([('tdi:overlay', '"<<-x9_A0"')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi:overlay attribute u'<<-x9_A0'"



def test_overlay_error_09(remove, hidden, pure):
    assert aat([('tdi:overlay', '"<-+x9_A0"')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi:overlay attribute u'<-+x9_A0'"

def test_overlay_error_10(remove, hidden, pure):
    assert aat([('tdi:overlay', '"<"')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi:overlay attribute u'<'"


aat([('tdi:overlay', '"&lt;x"')])
#[('tdi:overlay', '"&lt;x"')], tdi=None, scope=None, overlay=('<', 'x')
#[], tdi=None, scope=None, overlay=('<', 'x')
#[('tdi:overlay', '"&lt;x"')], tdi=None, scope=None, overlay=('<-', 'x')
#[], tdi=None, scope=None, overlay=('<-', 'x')



def test_error_00(remove, hidden, pure):
    assert aat([('tdi', None)], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid short tdi attribute"


def test_error_01(remove, hidden, pure):
    assert aat([('tdi', '')], remove=remove, hidden=hidden) == \
        "TemplateAttributeEmptyError: Empty tdi attribute"

def test_error_02(remove, hidden, pure):
    assert aat([('tdi', '" "')], remove=remove, hidden=hidden) == \
        "TemplateAttributeEmptyError: Empty tdi attribute"

aat([('tdi', '"x"')])
#[('tdi', '"x"')], tdi=('', 'x'), scope=None, overlay=None
#[], tdi=('', 'x'), scope=None, overlay=None
#[('tdi', '"x"')], tdi=('-', 'x'), scope=None, overlay=None
#[], tdi=('-', 'x'), scope=None, overlay=None
#

aat([('tdi', '"-"')])
#[('tdi', '"-"')], tdi=('-', None), scope=None, overlay=None
#[], tdi=('-', None), scope=None, overlay=None#
#[('tdi', '"-"')], tdi=('-', None), scope=None, overlay=None
#[], tdi=('-', None), scope=None, overlay=None


def test_error_03(remove, hidden, pure):
    assert aat([('tdi', '"9"')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'9'"


aat([('tdi', '"x9"')])
#[('tdi', '"x9"')], tdi=('', 'x9'), scope=None, overlay=None
#[], tdi=('', 'x9'), scope=None, overlay=None
#[('tdi', '"x9"')], tdi=('-', 'x9'), scope=None, overlay=None
#[], tdi=('-', 'x9'), scope=None, overlay=None


def test_error_04(remove, hidden, pure):
    assert aat([('tdi', '"x9.0"')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'x9.0'"


def test_error_05(remove, hidden, pure):
    assert aat([('tdi', '"x9.y"')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'x9.y'"


aat([('tdi', '"x9_A"')])
#[('tdi', '"x9_A"')], tdi=('', 'x9_A'), scope=None, overlay=None
#[], tdi=('', 'x9_A'), scope=None, overlay=None
#[('tdi', '"x9_A"')], tdi=('-', 'x9_A'), scope=None, overlay=None
#[], tdi=('-', 'x9_A'), scope=None, overlay=None


aat([('tdi', '"x9_A0"')])
#[('tdi', '"x9_A0"')], tdi=('', 'x9_A0'), scope=None, overlay=None
#[], tdi=('', 'x9_A0'), scope=None, overlay=None
#[('tdi', '"x9_A0"')], tdi=('-', 'x9_A0'), scope=None, overlay=None
#[], tdi=('-', 'x9_A0'), scope=None, overlay=None


aat([('tdi', '"x9_A0_"')])
#[('tdi', '"x9_A0_"')], tdi=('', 'x9_A0_'), scope=None, overlay=None
#[], tdi=('', 'x9_A0_'), scope=None, overlay=None
#[('tdi', '"x9_A0_"')], tdi=('-', 'x9_A0_'), scope=None, overlay=None
#[], tdi=('-', 'x9_A0_'), scope=None, overlay=None


def test_error_06(remove, hidden, pure):
    assert aat([('tdi', '"=x9_A0"')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'=x9_A0'"


def test_error_07(remove, hidden, pure):
    assert aat([('tdi', '"<x9_A0"')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'<x9_A0'"


aat([('tdi', '"*x9_A0"')])
#[('tdi', '"*x9_A0"')], tdi=('*', 'x9_A0'), scope=None, overlay=None
#[], tdi=('*', 'x9_A0'), scope=None, overlay=None
#[('tdi', '"*x9_A0"')], tdi=('*-', 'x9_A0'), scope=None, overlay=None
#[], tdi=('*-', 'x9_A0'), scope=None, overlay=None


aat([('tdi', '":x9_A0"')])
#[('tdi', '":x9_A0"')], tdi=(':', 'x9_A0'), scope=None, overlay=None
#[], tdi=(':', 'x9_A0'), scope=None, overlay=None
#[('tdi', '":x9_A0"')], tdi=(':-', 'x9_A0'), scope=None, overlay=None
#[], tdi=(':-', 'x9_A0'), scope=None, overlay=None


aat([('tdi', '":*x9_A0"')])
#[('tdi', '":*x9_A0"')], tdi=(':*', 'x9_A0'), scope=None, overlay=None
#[], tdi=(':*', 'x9_A0'), scope=None, overlay=None
#[('tdi', '":*x9_A0"')], tdi=(':*-', 'x9_A0'), scope=None, overlay=None
#[], tdi=(':*-', 'x9_A0'), scope=None, overlay=None


aat([('tdi', '"+X9_A0"')])
#[('tdi', '"+X9_A0"')], tdi=('', 'X9_A0'), scope=None, overlay=None
#[], tdi=('', 'X9_A0'), scope=None, overlay=None
#[('tdi', '"+X9_A0"')], tdi=('', 'X9_A0'), scope=None, overlay=None
#[], tdi=('', 'X9_A0'), scope=None, overlay=None


aat([('tdi', '"*:-x9_A0"')])
#[('tdi', '"*:-x9_A0"')], tdi=('*:-', 'x9_A0'), scope=None, overlay=None
#[], tdi=('*:-', 'x9_A0'), scope=None, overlay=None
#[('tdi', '"*:-x9_A0"')], tdi=('*:-', 'x9_A0'), scope=None, overlay=None
#[], tdi=('*:-', 'x9_A0'), scope=None, overlay=None


def test_error_08(remove, hidden, pure):
    assert aat([('tdi', '"**-x9_A0"')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'**-x9_A0'"

def test_error_09(remove, hidden, pure):
    assert aat([('tdi', '"::-x9_A0"')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'::-x9_A0'"

def test_error_10(remove, hidden, pure):
    assert aat([('tdi', '"*-+x9_A0"')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'*-+x9_A0'"

def test_error_10(remove, hidden, pure):
    assert aat([('tdi', '"*"')], remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'*'"

aat([('tdi', '"&#42;x"')])
#[('tdi', '"&#42;x"')], tdi=('*', 'x'), scope=None, overlay=None
#[], tdi=('*', 'x'), scope=None, overlay=None
#[('tdi', '"&#42;x"')], tdi=('*-', 'x'), scope=None, overlay=None
#[], tdi=('*-', 'x'), scope=None, overlay=None


def test_empty_name_empty(remove, hidden, pure):
    assert aat([], name='', remove=remove, hidden=hidden) == \
        "[], tdi=None, scope=None, overlay=None"

aat([], name='x')
#[], tdi=('', 'x'), scope=None, overlay=None
#[], tdi=('', 'x'), scope=None, overlay=None
#[], tdi=('-', 'x'), scope=None, overlay=None
#[], tdi=('-', 'x'), scope=None, overlay=None


def test_empty_name_dash(remove, hidden, pure):
    assert aat([], name='-', remove=remove, hidden=hidden) == \
        "[], tdi=('-', None), scope=None, overlay=None"


def test_empty_name_number(remove, hidden, pure):
    assert aat([], name='9', remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'9'"

aat([], name='x9')
#[], tdi=('', 'x9'), scope=None, overlay=None
#[], tdi=('', 'x9'), scope=None, overlay=None
#[], tdi=('-', 'x9'), scope=None, overlay=None
#[], tdi=('-', 'x9'), scope=None, overlay=None


def test_empty_name_00(remove, hidden, pure):
    assert aat([], name='x9.0', remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'x9.0'"

def test_empty_name_01(remove, hidden, pure):
    assert aat([], name='x9.y', remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'x9.y'"

aat([], name='x9_A')
#[], tdi=('', 'x9_A'), scope=None, overlay=None
#[], tdi=('', 'x9_A'), scope=None, overlay=None
#[], tdi=('-', 'x9_A'), scope=None, overlay=None
#[], tdi=('-', 'x9_A'), scope=None, overlay=None


aat([], name='x9_A0')
#[], tdi=('', 'x9_A0'), scope=None, overlay=None
#[], tdi=('', 'x9_A0'), scope=None, overlay=None
#[], tdi=('-', 'x9_A0'), scope=None, overlay=None
#[], tdi=('-', 'x9_A0'), scope=None, overlay=None


aat([], name='x9_A0_')
#[], tdi=('', 'x9_A0_'), scope=None, overlay=None
#[], tdi=('', 'x9_A0_'), scope=None, overlay=None
#[], tdi=('-', 'x9_A0_'), scope=None, overlay=None
#[], tdi=('-', 'x9_A0_'), scope=None, overlay=None

def test_empty_name_02(remove, hidden, pure):
    assert aat([], name='=x9_A0', remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'=x9_A0'"
#aat([], name='=x9_A0')
#TemplateAttributeError: Invalid tdi attribute u'=x9_A0'
#TemplateAttributeError: Invalid tdi attribute u'=x9_A0'
#TemplateAttributeError: Invalid tdi attribute u'=x9_A0'
#TemplateAttributeError: Invalid tdi attribute u'=x9_A0'

def test_empty_name_03(remove, hidden, pure):
    assert aat([], name='<x9_A0', remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'<x9_A0'"

aat([], name='*x9_A0')
#[], tdi=('*', 'x9_A0'), scope=None, overlay=None
#[], tdi=('*', 'x9_A0'), scope=None, overlay=None
#[], tdi=('*-', 'x9_A0'), scope=None, overlay=None
#[], tdi=('*-', 'x9_A0'), scope=None, overlay=None


aat([], name=':x9_A0')
#[], tdi=(':', 'x9_A0'), scope=None, overlay=None
#[], tdi=(':', 'x9_A0'), scope=None, overlay=None
#[], tdi=(':-', 'x9_A0'), scope=None, overlay=None
#[], tdi=(':-', 'x9_A0'), scope=None, overlay=None


aat([], name=':*x9_A0')
#[], tdi=(':*', 'x9_A0'), scope=None, overlay=None
#[], tdi=(':*', 'x9_A0'), scope=None, overlay=None
#[], tdi=(':*-', 'x9_A0'), scope=None, overlay=None
#[], tdi=(':*-', 'x9_A0'), scope=None, overlay=None


def test_empty_name_04(remove, hidden, pure):
    assert aat([], name='+X9_A0', remove=remove, hidden=hidden) == \
        "[], tdi=('', 'X9_A0'), scope=None, overlay=None"


def test_empty_name_05(remove, hidden, pure):
    assert aat([], name='*:-x9_A0', remove=remove, hidden=hidden) == \
        "[], tdi=('*:-', 'x9_A0'), scope=None, overlay=None"

def test_empty_name_06(remove, hidden, pure):
    assert aat([], name='**-x9_A0', remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'**-x9_A0'"

def test_empty_name_07(remove, hidden, pure):
    assert aat([], name='::-x9_A0', remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'::-x9_A0'"

def test_empty_name_08(remove, hidden, pure):
    assert aat([], name='*-+x9_A0', remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'*-+x9_A0'"

def test_error_name_00(remove, hidden, pure):
    assert aat([], name='*', remove=remove, hidden=hidden) == \
        "TemplateAttributeError: Invalid tdi attribute u'*'"

aat([], name='&#42;x')
#[], tdi=('*', 'x'), scope=None, overlay=None
#[], tdi=('*', 'x'), scope=None, overlay=None
#[], tdi=('*-', 'x'), scope=None, overlay=None
#[], tdi=('*-', 'x'), scope=None, overlay=None



aat([('tdi', 'aa')], name='aa')
#[('tdi', 'aa')], tdi=('', 'aa'), scope=None, overlay=None
#[], tdi=('', 'aa'), scope=None, overlay=None
#[('tdi', 'aa')], tdi=('-', 'aa'), scope=None, overlay=None
#[], tdi=('-', 'aa'), scope=None, overlay=None


aat([('tdi', '+aa')], name='aa')
#[('tdi', '+aa')], tdi=('', 'aa'), scope=None, overlay=None
#[], tdi=('', 'aa'), scope=None, overlay=None
#TemplateAttributeError: tdi attribute value 'aa' must equal name
#TemplateAttributeError: tdi attribute value 'aa' must equal name


aat([('tdi', '+aa')], name='+aa')
#[('tdi', '+aa')], tdi=('', 'aa'), scope=None, overlay=None
#[], tdi=('', 'aa'), scope=None, overlay=None
#[('tdi', '+aa')], tdi=('', 'aa'), scope=None, overlay=None
#[], tdi=('', 'aa'), scope=None, overlay=None


aat([('tdi', '-aa')], name='aa')
#TemplateAttributeError: tdi attribute value 'aa' must equal name
#TemplateAttributeError: tdi attribute value 'aa' must equal name
#[('tdi', '-aa')], tdi=('-', 'aa'), scope=None, overlay=None
#[], tdi=('-', 'aa'), scope=None, overlay=None


def test_error_name_01(remove, hidden, pure):
    assert aat([('tdi', 'bb')], name='aa', remove=remove, hidden=hidden) == \
        "TemplateAttributeError: tdi attribute value 'aa' must equal name"




