from arbitrage import ArbitrageOpportunity, detect_arbitrage  
import pytest

def test_two_way_arbitrage_arsenal_chelsea():

    outcomes = ["Arsenal", "Chelsea"]
    odds = [2.10 , 2.00]
    total_stake = 1000.0 

    result = detect_arbitrage(outcomes, odds, total_stake)

    assert result is not None
    assert result.outcomes == ["Arsenal", "Chelsea"]
    assert result.odds == [2.10, 2.00]
    assert result.total_stake == 1000.0
    assert result.stakes[0] == pytest.approx(487.80, abs=0.01)
    assert result.stakes[1] == pytest.approx(512.20, abs=0.01)
    assert result.guaranteed_return == pytest.approx(1024.39, abs=0.01)
    assert result.roi == pytest.approx(0.0244, abs=0.001)


def test_no_arbitrage_returns_none():

    outcomes = ["Team A", "Team B"]
    odds = [1.90, 1.90]

    result = detect_arbitrage(outcomes, odds)
    assert result is None

def test_three_way_arbitrage():

    outcomes = ["Home","Draw", "Away"]
    odds = [3.50, 3.60, 2.60]
    total_stake = 1000.0

    result = detect_arbitrage(outcomes, odds, total_stake)

    assert result is not None
    assert result.outcomes == ["Home","Draw", "Away"]
    assert result.total_stake == 1000.0
    assert result.stakes[0] == pytest.approx(301.30, abs=0.1)
    assert result.stakes[1] == pytest.approx(292.90, abs=0.1)
    assert result.stakes[2] == pytest.approx(405.70, abs=0.1)
    assert result.guaranteed_return == pytest.approx(1054.74, abs=0.1)
    assert result.roi == pytest.approx(0.0547, abs=0.001)