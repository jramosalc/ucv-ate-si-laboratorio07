from typing import Dict
from kedro.pipeline import Pipeline
from si_image_processing.pipelines.image_processing import pipeline as img_proc

def register_pipelines() -> Dict[str, Pipeline]:
    image_processing_pipeline = img_proc.create_pipeline()
    return {
        "__default__": image_processing_pipeline,
        "image_processing": image_processing_pipeline,
    }