from src.binance_api import get_usdc_pairs

def test_get_usdc_pairs():
    pairs = get_usdc_pairs()
    assert "BTCUSDC" in pairs  # Example test case
