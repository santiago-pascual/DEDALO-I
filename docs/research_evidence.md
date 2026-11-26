# Research evidence and interpretation

Snapshot reviewed: 26 November 2026. Numerical evidence is presented at aggregate level only.

| Evidence | Result | Verification level |
|---|---|---|
| Frozen P4 common OOS, 2020-06-23 to 2026-06-19 | 3,255 trades; +289.661901R; PF 1.215771; expectancy 0.088990R; win rate 50.6605%; max DD −18.093472R | Archived reference; full inputs absent from reviewed snapshot |
| S2R stored outcomes within frozen entry-date bounds | 520 of 537 records; +26.932R; PF 1.116565; win rate 45.9615%; expectancy 0.051792R | Independently aggregated from archived net_R values |
| S2R entry-ordered drawdown | −16.7936R | Initial zero included; not mark-to-market drawdown |
| Frozen historical execution replay | 2,899 exact executions; 356 accounted-for risk/account-gated non-executions; no unexplained mismatches or extras reported | Archived report, not rerun |
| P5 | Five-strategy research portfolio, including NBM-B | Separate release artifacts required for matched comparison |
| Forward Paper | Fresh simulated account distinct from historical research | Latest authorized ledger not supplied; no performance claim |

Archived P4 strategy counts: MRL1 430, MRS2 863, S2R 520, ORB 1,442. Trade frequency is not profitability contribution. Strategy correlation, leave-one-out attribution and matched P4/P5 comparison are not established by these counts.

The private reproduction program aggregates frozen component outcomes; it does not independently regenerate original signals. Entry-date aggregation is distinct from daily mark-to-market returns. The public demo uses synthetic outcomes and does not reproduce the private research results.
