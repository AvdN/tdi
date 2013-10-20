
from tdi._test_support import pure
from tdi.integration import wtf_service as _wtf_service

class Param(object):
    def multi(self, name):
        return []

def test_adapter_getlist(pure):
    param = Param()
    adapter = _wtf_service.RequestParameterAdapter(param)
    assert adapter.getlist == param.multi

def test_adapter_inherited(pure):
    class Inherited(_wtf_service.RequestParameterAdapter):
        pass
    param = Param()
    adapter = Inherited(param)
    assert adapter.getlist != param.multi
