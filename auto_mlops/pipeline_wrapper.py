from typing import Callable, List, Type, Union

from sklearn.pipeline import Pipeline


class PipelineElement():

    def __init__(self, func: Callable):
        self.func = func

    def transform(*arg, **kwargs):
        return self.func(*arg, **kwargs)

def pipeline_wrapper(pipeline: List[Union[Callable, Type[BaseEstimator]]]):
    # Vars
    pipeline_length = len(pipeline)
    clean_pipeline = []

    # Utils
    last = lambda idx: idx == pipeline_length
    has_fit = lambda x: getattr(x, "fit", None) != None
    has_transform = lambda x: getattr(x, "transform", None) != None
    has_fit_and_transform = lambda x: has_fit(x) and has_transform(x)

    for idx, elt in enumerate(pipeline):
        if not (callable(elt) or has_transform(elt)):
            raise TypeError(f'{elt} should be either callable or implement a transform function')
        if last(idx) and has_fit_and_transform(elt):
            raise ValueError(f'{elt} should implement fit and transform functions')

        if callable(elt):
            clean_pipeline.append(PipelineElement(elt))
        else:
            clean_pipeline.append(elt)

    return Pipeline(clean_pipeline)
