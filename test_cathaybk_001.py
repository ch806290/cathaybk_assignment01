# This test case is for cathaybk_001
import pytest
from cathaybk_001 import get_input_value,InputOutOfRangeException


class TesthTriangle:

    @pytest.mark.FET
    @pytest.mark.parametrize("user_input, expected_exception", [
    ("abc", InputOutOfRangeException("輸入的不是一個有效的整數!")),
    ("11", InputOutOfRangeException("輸入的數字超出範圍!")),
    ("0", InputOutOfRangeException("輸入的數字超出範圍!")),
    ])
    def test_invalid_Triangle_001(self,user_input,expected_exception,monkeypatch: pytest.MonkeyPatch):
        user_inputs = iter([user_input])
        monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))
        with pytest.raises(InputOutOfRangeException) as exec_info:
            get_input_value()

        assert str(exec_info.value) == str(expected_exception)
