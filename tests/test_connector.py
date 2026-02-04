import pytest
from src.connector import FabricClient

def test_fabric_client():
    client = FabricClient()
    assert client is not None