import unittest
from examples.risk_metrics import summarize


class RiskMetricsTest(unittest.TestCase):
    def test_synthetic(self):
        result = summarize([-1, 1.5, -0.5, 2, -1])
        self.assertEqual(result['total_r'], 1)
        self.assertAlmostEqual(result['profit_factor'], 1.4)
        self.assertEqual(result['win_rate'], 0.4)
        self.assertEqual(result['max_drawdown_r'], -1)

    def test_initial_zero(self):
        self.assertEqual(summarize([-2, 1])['max_drawdown_r'], -2)

    def test_no_losses(self):
        self.assertIsNone(summarize([0, 1])['profit_factor'])

    def test_invalid(self):
        for sample in ([], [float('nan')], [float('inf')]):
            with self.subTest(sample=sample), self.assertRaises(ValueError):
                summarize(sample)
