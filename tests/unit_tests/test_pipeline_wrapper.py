import unittest

from auto_mlops.pipeline_wrapper import pipeline_wrapper
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


class TestPipelineWrapper(unittest.TestCase):
    def test_only_estimator(self):
        pipeline = pipeline_wrapper([LogisticRegression()])
        self.assertTrue(isinstance(pipeline, Pipeline))

    def test_estimator_without_fit(self):
        class EstimatorWithoutFit:
            pass

        self.assertRaises(TypeError, lambda: pipeline_wrapper([EstimatorWithoutFit()]))

    def test_callable(self):
        def function():
            return

        pipeline = pipeline_wrapper([function, LogisticRegression()])
        self.assertTrue(isinstance(pipeline, Pipeline))
        self.assertRaises(TypeError, lambda: pipeline_wrapper([function]))

    def test_transformer(self):
        class TransformerWithoutTransform:
            pass

        self.assertRaises(TypeError, lambda x: pipeline_wrapper([TransformerWithoutTransform()]))
        transformer = TransformerWithoutTransform()
        transformer.transform = lambda x: x
        self.assertTrue(isinstance(pipeline_wrapper([transformer, LogisticRegression()]), Pipeline))
