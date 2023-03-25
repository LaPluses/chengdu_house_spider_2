from src.pipeline import run_data_collect_pipeline
import asyncio


asyncio.run(run_data_collect_pipeline(range(1, 2)))
