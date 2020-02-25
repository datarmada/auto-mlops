from typing import Callable, List, Union, Any

from sklearn.pipeline import make_pipeline, Pipeline


class PipelineElement:

    def __init__(self, func: Callable):
        self.func = func

    def transform(self, *arg, **kwargs):
        return self.func(*arg, **kwargs)

    def fit(self, x, y):
        return self


def pipeline_wrapper(pipeline: List[Union[Callable, Any]]) -> Pipeline:
    clean_pipeline = []
    transformers = pipeline[:-1]
    estimator = pipeline[-1]

    for elt in transformers:
        if not (callable(elt) or has_method(elt, "transform")):
            raise TypeError(f'{elt} should be either callable or implement a transform method')
        if callable(elt):
            clean_pipeline.append(PipelineElement(elt))
            continue
        if not has_method(elt, "fit"):
            elt.fit = lambda self, x, y: self
        clean_pipeline.append(elt)

    if not (has_method(estimator, "predict") and has_method(estimator, "fit")):
        raise TypeError('Last element of the pipeline must have fit and predict methods')

    clean_pipeline.append(estimator)

    return make_pipeline(*clean_pipeline)


def has_method(x: Any, method_name: str) -> bool:
    return getattr(x, method_name, None) is not None
