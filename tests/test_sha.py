import pytest
from src.cryptography.masking import Masking 
from unittest.mock import MagicMock, patch

def test_postgres_insert():
    Masking.setMasker("SHA")
    data = "1.1.1.1"

    record = Masking.mask(data)

    assert record == "f1412386aa8db2579aff2636cb9511cacc5fd9880ecab60c048508fbe26ee4d9"