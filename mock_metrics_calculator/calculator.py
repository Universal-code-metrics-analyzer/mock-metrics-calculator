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
            metricResults=[
                TreeMetricResult(
                    metricName='MccabeCC', subjectPath='', value=3, resultScope='package'
                )
            ],
            trees=[],
            blobs=[],
        )
