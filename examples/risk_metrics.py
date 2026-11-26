"""Standalone synthetic demonstration, not trading or private research code."""
import math


def summarize(outcomes):
    """Summarize finite R outcomes in supplied order; zero initial equity.

    PF is None when there are no losses (including all-zero samples).
    Win rate counts strictly positive outcomes over all outcomes.
    Drawdown is signed, additive R, not mark-to-market account drawdown.
    Unrepresentable aggregates raise ValueError.
    """
    values = [float(x) for x in outcomes]
    if not values or not all(math.isfinite(x) for x in values):
        raise ValueError('Expected nonempty finite outcomes')
    try:
        gains = math.fsum(x for x in values if x > 0)
        losses = math.fsum(-x for x in values if x < 0)
        total = math.fsum(values)
        # Compensated accumulation preserves small changes in long sequences.
        equity = correction = peak = max_drawdown = 0.0
        for x in values:
            t = equity + x
            correction += (equity - t) + x if abs(equity) >= abs(x) else (x - t) + equity
            equity = t
            current = equity + correction
            peak = max(peak, current)
            max_drawdown = min(max_drawdown, current - peak)
            if not all(map(math.isfinite, (equity, correction, current, max_drawdown))):
                raise ValueError('Unrepresentable equity or drawdown')
        pf = gains / losses if losses else None
        if pf is not None and not math.isfinite(pf):
            raise ValueError('Unrepresentable profit factor')
    except OverflowError as exc:
        raise ValueError('Unrepresentable aggregate') from exc
    return dict(trades=len(values), total_r=total, expectancy=total / len(values),
                profit_factor=pf, win_rate=sum(x > 0 for x in values) / len(values),
                max_drawdown_r=max_drawdown)


if __name__ == '__main__':
    print('SYNTHETIC outcomes only:')
    print(summarize([-1, 1.5, -0.5, 2, -1]))
