"""Standalone synthetic demonstration; not trading or private research code."""
import math
from statistics import fmean


def summarize(outcomes):
    values = [float(x) for x in outcomes]
    if not values or not all(math.isfinite(x) for x in values):
        raise ValueError('Expected nonempty finite outcomes')
    gains = sum(x for x in values if x > 0)
    losses = -sum(x for x in values if x < 0)
    equity = peak = max_drawdown = 0.0
    for x in values:
        equity += x
        peak = max(peak, equity)
        max_drawdown = min(max_drawdown, equity - peak)
    return dict(trades=len(values), total_r=sum(values), expectancy=fmean(values),
                profit_factor=gains / losses if losses else None,
                win_rate=sum(x > 0 for x in values) / len(values),
                max_drawdown_r=max_drawdown)


if __name__ == '__main__':
    print('SYNTHETIC outcomes only:')
    print(summarize([-1, 1.5, -0.5, 2, -1]))
