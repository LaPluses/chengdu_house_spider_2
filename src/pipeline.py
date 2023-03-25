from __future__ import annotations
from src.spider import spide_house_source_page, spide_house_project_rule
from src.data import HouseData
from os import path
import asyncio
import itertools
import time
import json


async def update_project_rule(house_data: HouseData):
    print(f'- House({house_data.id}) project rule scheduled')
    json_response = json.loads(await spide_house_project_rule(house_data.id))
    house_data.parse_project_rule(json_response['message'])
    print(f'- House({house_data.id}) project rule done')


async def handle_single_page_task(page: int) -> list[HouseData]:
    # Graceful spider schedule
    await asyncio.sleep(page // 5 * 0.5)
    print(f'- Page({page}) task scheduled')
    html = await spide_house_source_page(page)
    all_house_data = HouseData.parse(html)
    await asyncio.gather(*map(lambda x: update_project_rule(x), all_house_data))
    print(f'- Page({page}) task done')
    return all_house_data


async def run_data_collect_pipeline(page_range: list[int]) -> list[HouseData]:
    with open(path.join('output', time.strftime("%Y-%m-%d")), "w") as f:
        json.dump(list(itertools.chain(*await asyncio.gather(*map(lambda page: handle_single_page_task(page),  page_range)))),
                  f, ensure_ascii=False, indent=4, cls=HouseData.Encoder)
