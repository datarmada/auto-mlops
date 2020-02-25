from typing import Callable, List, Union, Any

from sklearn.pipeline import Pipeline, make_pipeline


class PipelineElement:

    def __init__(self, func: Callable):
        self.func = func

    def transform(self, *arg, **kwargs):
        return self.func(*arg, **kwargs)


def pipeline_wrapper(pipeline: List[Union[Callable, Any]]):
    clean_pipeline = []

    for idx, elt in enumerate(pipeline[:-1]):
        if not (callable(elt) or has_method(elt, "transform")):
            raise TypeError(f'{elt} should be either callable or implement a transform method')
        if callable(elt):
            clean_pipeline.append(PipelineElement(elt))
        elif not has_method(elt, "fit"):
            elt.fit = lambda self, x, y: self
            clean_pipeline.append(elt)
        else:
            clean_pipeline.append(elt)

    if not (has_method(pipeline[-1], "predict") and has_method(pipeline[-1], "fit")):
        raise TypeError('Last element of the pipeline must have fit and predict methods')

    clean_pipeline.append(pipeline[-1])

    return make_pipeline(*clean_pipeline)


def has_method(x: Any, method_name: str):
    return getattr(x, method_name, None) is not None
