# coding: utf-8
from tdi._test_support import pure

from tdi.markup.text import encoder as _encoder


encoder = _encoder.TextEncoder('utf-8')

def test_text_encoder_starttag_00(pure):
    assert encoder.starttag('a', [('b', 'c'), ('d', None)], True) == \
           "[[a b=c d]]"

def test_text_encoder_starttag_01(pure):
    assert encoder.starttag('a', [('b1', None), ('c2', 'd3')], False) == \
           "[a b1 c2=d3]"

def test_text_encoder_endtag_00(pure):
    assert encoder.endtag('ff') == "[/ff]"

def test_text_encoder_name_unicode(pure):
    assert encoder.name(u'ggg') == "ggg"

def test_text_encoder_name(pure):
    assert encoder.name('ggg') == "ggg"

def test_text_encoder_attribute_quote(pure):
    assert encoder.attribute(u'\u20ac"') == '"€\\""'

def test_text_encoder_attribute(pure):
    assert encoder.attribute(u'\u20ac') == '"€"'

def test_text_encoder_attribute_quote_utf8(pure):
    assert encoder.attribute(u'\u20ac"'.encode('utf-8')) == '"€\\""'

def test_text_encoder_attribute_utf8(pure):
    assert encoder.attribute(u'\u20ac'.encode('utf-8')) == '"€"'

def test_text_encoder_content(pure):
    assert encoder.content(u'\u20ac') == "€"

def test_text_encoder_content_utf8(pure):
    assert encoder.content(u'\u20ac'.encode('utf-8')) == "€"

def test_text_encoder_encode(pure):
    assert encoder.encode(u'\u20ac') == "€"

def test_text_encoder_escape(pure):
    assert encoder.escape('lalala') == "lalala"

def test_text_encoder_escape_brackets(pure):
    assert encoder.escape('[lalala]') == "[]lalala]"

