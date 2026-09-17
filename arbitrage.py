from dataclasses import dataclass

@dataclass
class ArbitrageOpportunity:
    outcomes: list[str]
    odds: list[float]
    stakes: list[float]
    total_stake: float
    guaranteed_return: float
    roi: float


def detect_arbitrage(outcomes: list[str], odds: list[float], total_stake: float = 1000.0) -> ArbitrageOpportunity| None:
    """looks for an arbitrage opportunity"""

    implied_probability_sum = sum(1/o for o in odds)

    if implied_probability_sum >= 1:
        return None

    stakes = [total_stake * (1/o) / implied_probability_sum for o in odds]
    guaranteed_return = total_stake / implied_probability_sum
    roi = (guaranteed_return - total_stake) / total_stake

    return ArbitrageOpportunity(
        outcomes = outcomes,
        odds = odds,
        stakes = stakes,
        total_stake = total_stake,
        guaranteed_return = guaranteed_return,
        roi = roi,
    )

if __name__ == "__main__":
    # Quick sanity check using the Arsenal/Chelsea example from the README
    result = detect_arbitrage(
        outcomes=["Arsenal", "Chelsea"],
        odds=[2.10, 2.00],
        total_stake=1000.0,
    )
    print(result)

  



