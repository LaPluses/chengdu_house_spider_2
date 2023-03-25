import aiohttp
import asyncio

SPIDER_DOMAIN = 'https://zw.cdzjryb.com'

SPIDER_HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'accept_language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'accept_encoding': 'gzip, deflate, br',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
}


async def spide_house_source_page(page: int) -> str:
    url = f'{SPIDER_DOMAIN}/lottery/accept/projectList?pageNo={page}'
    async with aiohttp.ClientSession(headers=SPIDER_HEADER) as session:
        async with session.get(url) as response:
            return await response.text()
