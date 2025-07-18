from kedro.pipeline import Pipeline
from your_project.pipelines.data_exploration import pipeline as exploration_pipeline
from your_project.pipelines.modeling import pipeline as modeling_pipeline

def register_pipelines() -> dict[str, Pipeline]:
    return {
        "explore": exploration_pipeline.create_pipeline(),
        "model": modeling_pipeline.create_pipeline(),
        "__default__": exploration_pipeline.create_pipeline() + modeling_pipeline.create_pipeline(),
    }


# from kedro.framework.project import find_pipelines
# from kedro.pipeline import Pipeline


# def register_pipelines() -> dict[str, Pipeline]:
#     """Register the project's pipelines.

#     Returns:
#         A mapping from pipeline names to ``Pipeline`` objects.
#     """
#     pipelines = find_pipelines()
#     pipelines["__default__"] = sum(pipelines.values())
#     return pipelines

