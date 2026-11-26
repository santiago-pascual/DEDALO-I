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

    def test_all_winning(self):
        r = summarize([1, 2, 3])
        self.assertEqual((r['total_r'], r['win_rate'], r['max_drawdown_r']), (6, 1, 0))
        self.assertIsNone(r['profit_factor'])

    def test_all_losing(self):
        r = summarize([-1, -2, -3])
        self.assertEqual((r['total_r'], r['win_rate'], r['max_drawdown_r'], r['profit_factor']), (-6, 0, -6, 0))

    def test_zero(self):
        r = summarize([0, 0])
        self.assertEqual((r['total_r'], r['win_rate'], r['max_drawdown_r']), (0, 0, 0))
        self.assertIsNone(r['profit_factor'])

    def test_multiple_cycles(self):
        self.assertEqual(summarize([3, -2, 4, -4, 5, -1])['max_drawdown_r'], -4)

    def test_precision(self):
        self.assertAlmostEqual(summarize([0.1] * 10)['total_r'], 1)
        self.assertEqual(summarize([1e16, 1, -1e16])['total_r'], 1)

    def test_break_even_and_generator(self):
        r = summarize(iter([1, -1, 0]))
        self.assertEqual(r['profit_factor'], 1)
        self.assertAlmostEqual(r['win_rate'], 1/3)

    def test_negative_infinity(self):
        with self.assertRaises(ValueError):
            summarize([float('-inf')])

    def test_overflow(self):
        with self.assertRaises(ValueError):
            summarize([1e308, 1e308])
        with self.assertRaises(ValueError):
            summarize([1e308, -1e-308])
