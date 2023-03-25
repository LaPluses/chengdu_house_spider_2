from __future__ import annotations
from src.spider import spide_house_source_page
from src.data import HouseData
from os import path
import asyncio
import itertools
import time
import json


async def handle_single_page_task(page: int) -> list[HouseData]:
    # Graceful spider schedule
    await asyncio.sleep(page // 5 * 0.5)
    print(f'- Page({page}) task scheduled')
    html = await spide_house_source_page(page)
    all_house_data = HouseData.parse(html)
    print(f'- Page({page}) task done')
    return all_house_data


async def run_data_collect_pipeline(page_range: list[int]) -> list[HouseData]:
    with open(path.join('output', time.strftime("%Y-%m-%d")), "w") as f:
        json.dump(list(itertools.chain(*await asyncio.gather(*map(lambda page: handle_single_page_task(page),  page_range)))),
                  f, ensure_ascii=False, indent=4, cls=HouseData.Encoder)
