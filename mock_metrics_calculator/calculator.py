from core.metrics_calculator import (
    MetricsCalculator,
    MetricsCalculatorConfigShape,
    TreeMetricResult,
    TreeMetrics,
)


class MockMetricsCalculatorConfigShape(MetricsCalculatorConfigShape):
    pass


class MockMetricsCalculator(
    MetricsCalculator[MockMetricsCalculatorConfigShape],
    config_shape=MockMetricsCalculatorConfigShape,
):
    async def calculate(self) -> TreeMetrics:
        return TreeMetrics(
            type='tree',
            name='',
            path='',
            metric_results=[
                TreeMetricResult(
                    metric_name='MccabeCC', subject_path='', value=3, result_scope='package'
                )
            ],
            trees=[],
            blobs=[],
        )
