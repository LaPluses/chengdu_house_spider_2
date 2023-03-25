from __future__ import annotations
from bs4 import BeautifulSoup
import json
from datetime import datetime


class HouseData:
    id: str
    area: str
    name: str
    count: int
    status: str
    phone_number: str
    price: int
    start_time: datetime
    end_time: datetime

    class Encoder(json.JSONEncoder):
        def default(self, o: HouseData):
            return {
                **o.__dict__,
                **{
                    'start_time': o.start_time.strftime('%Y-%m-%d %H:%M:%S'),
                    'end_time': o.end_time.strftime('%Y-%m-%d %H:%M:%S'),
                },
            }

    @staticmethod
    def create(id: str, area: str, name: str, count: int, status: str, price: int, start_time: str, end_time: str) -> HouseData:
        data = HouseData()
        data.id = id
        data.area = area
        data.name = name
        data.count = count
        data.status = status
        data.price = price
        data.start_time = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        data.end_time = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        return data

    def __str__(self) -> str:
        return str(self.__dict__)

    @staticmethod
    def parse(html: str) -> list[HouseData]:
        soup = BeautifulSoup(html, 'html.parser')
        all_body = soup.find(
            name='tbody', id='_projectInfo').find_all(name='tr')
        result: list[HouseData] = list()
        for body in all_body:
            item = body.find_all(name='td')
            result.append(
                HouseData.create(
                    id=item[0].get_text(),
                    area=item[2].get_text(),
                    name=item[3].get_text(),
                    count=int(item[6].get_text()),
                    status=item[13].get_text(),
                    start_time=item[8].get_text(),
                    end_time=item[9].get_text(),
                    price=0,
                )
            )
        return result
