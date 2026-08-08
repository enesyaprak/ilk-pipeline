import pytest

from hesap import bol, topla


def test_topla():
    assert topla(2, 3) == 5

def test_bol():
    assert bol(10, 2) == 5

def test_sifira_bolme():
    with pytest.raises(ValueError):      # "bu kod hata fırlatmalı" testi
        bol(5, 0)
