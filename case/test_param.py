

import pytest


def addr(a,b):
    return a+b
#标准格式
@pytest.mark.parametrize("test_input,expect",
                         [[{"a": 1,"b": 2},3],
                          [{"a": "1","b": "2"},"12"]
                          ])
def test_addr(test_input,expect):
    result = addr(test_input["a"],test_input["b"])
    expect = expect
    assert result == expect


