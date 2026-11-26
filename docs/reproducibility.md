# Reproducibility

| Level | Inputs | Execution and scope | Limitation |
|---|---|---|---|
| 1 — Public synthetic demo | Explicit synthetic R outcomes in Python | Standard library; commands below. Risk metrics, tests, figure generation and publication checks | No trading signals, historical return reproduction or account simulation |
| 2 — Approved aggregate reconciliation | Published P4/S2R aggregates and recovered P5-R2 report statistics | Check counts, expectancy, matched P&L differences and gross-minus-cost reconciliation; reproduce aggregate figures | Full trade tapes absent; PF, drawdown and causal results cannot be independently reconstructed |
| 3 — Full private reproduction | Versioned historical data, frozen manifests, trades, model seeds, calendars, costs and approved runtime snapshots | Not executable in this repository; requires separately authorized isolated research environment and matching dependencies | Independent full causal reproduction and native P5 integration incomplete |

## Public commands

Python 3.11–3.13 are CI targets. No external packages or market-data access are required.

```sh
python -B examples/risk_metrics.py
python -B -m unittest discover -s tests -v
python -B scripts/generate_figures.py --check
python -B scripts/validate_publication.py
```

Expected synthetic output: 5 trades, total 1R, expectancy 0.2R, profit factor 1.4, win rate 0.4, drawdown -1R. Profit factor is None for zero gross losses, including all-zero input; zero outcomes are not wins. Drawdown includes initial zero and uses supplied outcome order. Nonfinite or unrepresentable aggregates are rejected.

To regenerate SVG figures, run `python -B scripts/generate_figures.py`. A publication change requires a reviewed manifest update. The validator checks exact SHA-256 bytes; Git attributes enforce LF for text. Automated pattern checks are limited, not a security certification.

### Additional aggregate evidence

The October P5 final historical certification and November economic/accounting reports support the new matched and extended figures. Their numerical tables were transcribed and arithmetic cross-checked; figures are regenerated from those aggregate values. This does not validate source trade tapes, model fitting, native fills or the reported 112 private tests. The working paper is not redistributed.
