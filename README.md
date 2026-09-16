# Sports Arbitrage Scanner

A Python tool that detects arbitrage opportunities across UK sportsbooks by comparing odds from multiple bookmakers on the same football matches.

## What is Arbitrage?
Sports arbitrage is a betting strategy where you place bets on different possible outcomes of the same sporting event with different bookmakers. The aim is to find a combination of odds where, after accounting for the amount staked on each outcome, the total payout is greater than the total amount bet. This allows the bettor to lock in a profit without needing to correctly predict which team or player will win.

Sports arbitrage exists because bookmakers do not always agree on the probabilities of different outcomes. Each bookmaker sets its own odds based on factors such as its trading models, available information, betting patterns and risk management; implied probabilities from a single bookmaker sum to more than 100% (their margin). As a result, when you take the best available odds for each outcome across different bookmakers, the implied probabilities can sometimes add up to less than 100%. When this happens, there is an arbitrage opportunity because the available odds are collectively offering more value than the market's fair probability distribution.

A "guaranteed profit regardless of outcome" means that the stakes are calculated so that whichever possible outcome occurs, the total payout from the winning bet is greater than the total amount originally staked. For example, if £100 is split across the outcomes of an event and the winning outcome returns £105, the bettor makes £5 profit whether outcome A or outcome B wins. The key point is that the profit comes from the difference between the bookmakers' prices rather than from predicting the result correctly.

## The Math behind Arbitrage Detection
The implied probability of an outcome with decimal odds O is 1/O. In a fair market with no bookmaker margin, implied probabilities across all outcomes sum to exactly 1.
An arbitrage opportunity exists when the sum of the implied probabilities of all outcomes is less than 1:

```
1/O₁ + 1/O₂ + ... + 1/Oₙ < 1
```

Here, Oᵢ represents the decimal odds for outcome i. If this condition is met, the available odds allow the total stake to be split between the outcomes so that the same return is achieved regardless of which outcome wins.

### Optimal Stake Split:

For a total stake of S, the amount placed on outcome i is:

### Stakeᵢ = (S/Oᵢ) ÷ (1/O₁ + 1/O₂ + ... + 1/Oₙ)

The guaranteed return is:

```
Return = S ÷ (1/O₁ + 1/O₂ + ... + 1/Oₙ)
```

### ROI:

The return on investment is:

```
ROI = (Return − S) / S
```

### Worked Example:

Suppose Arsenal is available at odds of 2.10 and Chelsea at odds of 2.00.

First, check for an arbitrage opportunity:
1/2.10 + 1/2.00 = 0.4762 + 0.5000 = 0.9762

Since 0.9762 < 1, an arbitrage opportunity exists.

If the total stake is £100:

Arsenal stake = (100/2.10) ÷ 0.9762 = £48.78

Chelsea stake = (100/2.00) ÷ 0.9762 = £51.22

If Arsenal wins:

£48.78 × 2.10 = £102.44

If Chelsea wins:

£51.22 × 2.00 = £102.44

In either case, the return is approximately £102.44 from an initial £100 stake.

Therefore:

Profit = £102.44 − £100 = £2.44

ROI = £2.44 / £100 = 2.44%

This means the bettor can theoretically make a 2.44% return regardless of which team wins.


## Architecture

The project is split into separate modules so the math, the data fetching, and the orchestration each live in one place.

- `arbitrage.py` — Contains the core arbitrage detection logic. It calculates implied probabilities, checks whether an arbitrage opportunity exists, calculates the optimal stake for each outcome, and determines    the expected ROI.
- `odds_client.py` — Connects to The Odds API and fetches the latest odds from different bookmakers. It handles the API request and returns the relevant odds data to the rest of the program.
- `scanner.py` — Acts as the main controller of the system. It requests the latest odds using odds_client.py, passes the data to arbitrage.py for analysis, and identifies any available arbitrage opportunities.
- `config.py` — Stores configuration settings such as the API key and the bookmakers or sports markets being monitored. Keeping these settings separate makes the rest of the code easier to manage.
- `tests/` — Unit tests for the individual components, primarily verifying arbitrage detection and stake calculations.

## Setup + How to Run

### 1. Prerequisites

Make sure the following are installed:

* **Python 3.10 or newer**
* **Git**
* A **The Odds API** account and API key

The Odds API currently provides a free tier, which requires signing up for an account and obtaining an API key.

### 2. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/your-username/sports-arbitrage.git
cd sports-arbitrage
```

Replace the repository URL with the actual GitHub repository URL.

### 3. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Or on macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 5. Set Up the API Key

Sign up for a free account with **The Odds API** and obtain an API key. The API provides current and upcoming odds from multiple bookmakers, including UK bookmakers.

Create a `.env` file in the project root:

```text
ODDS_API_KEY=your_api_key_here
```

Do **not** commit the `.env` file to GitHub. Add it to `.gitignore` so the API key remains private.

### 6. Run the Scanner

Once the environment is activated and the API key has been configured, run:

```bash
python scanner.py
```

The scanner will fetch the latest odds through `odds_client.py`, pass the data to the arbitrage calculations, and display any opportunities where the combined implied probability is below 1.

For example:

```text
Arbitrage opportunity found
Arsenal: 2.10
Chelsea: 2.00
ROI: 2.44%
```

The exact output will depend on the live odds returned by The Odds API. The API's current documentation uses version 4 and supports odds requests by sport, bookmaker region and market.

## Phase 1 Scope and Limitations

The first phase of the project is intentionally limited to the core arbitrage detection system. The aim is to build a reliable scanner before adding more advanced features in later phases.

### In scope:

- Football (soccer) markets
- UK bookmakers
- 2 way and 3 way markets
- Fetching live odds through The Odds API
- Detecting arbitrage opportunities
- Calculating optimal stake sizes and expected ROI
- Printing opportunities directly to the terminal

### Out of scope:

- Other sports
- Other market types, such as spreads and totals
- Automated bet placement or execution
- A graphical user interface or dashboard
- Backtesting on historical data (planned for Phase 2)

## Future Phases

The next phase will focus on building a backtester to evaluate the strategy using historical odds data. This will allow the system to measure how often arbitrage opportunities occurred, expected returns, and how the strategy would have performed over time.

Further phases may extend the scanner to additional sports and market types, add continuous monitoring, and explore automated execution.