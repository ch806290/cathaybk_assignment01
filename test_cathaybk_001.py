import pytest
import cathaybk_001


class TestPymarid:
    @pytest.mark.RAT
    def test_pymarid_001(self):
        index = 1 + 1
        assert index == 2


    def test_pymarid_002(self):
        index = 1 + 2
        assert index == 3


    def test_pymarid_003(self):
        index = 1 + 4
        assert index == 5


    def test_invalid_pymarid_001(self,monkeypatch: pytest.MonkeyPatch):
        user_input = iter(["110"])
        monkeypatch.setattr("builtins.input", lambda _: next(user_input))
        with pytest.raises(cathaybk_001.InputOutOfRangeException):
            cathaybk_001.get_input_value()
