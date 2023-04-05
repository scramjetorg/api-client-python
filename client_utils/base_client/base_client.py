import aiohttp
from urllib.parse import urlparse
from url_normalize import url_normalize


class BaseClient:
    def __init__(self, url: str) -> None:
        self.url = urlparse(url)
        self.api_base = url
    headers = {}

    @staticmethod
    def setDefaultHeaders(headers):
        BaseClient.headers = headers   
            
    async def get(self, url: str, headers={})-> str:
        async with aiohttp.ClientSession(headers={**BaseClient.headers, **headers}) as session:
            url=url_normalize(f'{self.api_base}/{url}')
            async with session.get(url) as resp:
                return await resp.text()

    async def get_stream(self, url: str, headers={})-> str:
            async with aiohttp.ClientSession(headers={**BaseClient.headers, **headers}) as session:
                url=url_normalize(f'{self.api_base}/{url}')
                async with session.get(url) as response:
                    async for line in response.content:
                        yield line.decode('utf-8')

    async def post(self, url: str, headers = {}, data=None, config=None) -> str:
        async with aiohttp.ClientSession(headers={**BaseClient.headers, **headers}) as session:
            url=url_normalize(f'{self.api_base}/{url}')
            async with session.post(url, headers=headers, data=data, params=config) as resp:
                return await resp.text()

    async def put(self, url: str, headers = {}, data=None, config=None) -> str:
        async with aiohttp.ClientSession(headers={**BaseClient.headers, **headers}) as session:
            url=url_normalize(f'{self.api_base}/{url}')
            async with session.put(url, headers=headers, data=data, params=config) as resp:
                return await resp.text()

    async def delete(self, url: str, headers = {}) -> str:
        async with aiohttp.ClientSession(headers={**BaseClient.headers, **headers}) as session:
            url=url_normalize(f'{self.api_base}/{url}')
            async with session.delete(url, headers=headers) as resp:
                return await resp.text() 

    async def get_load_check(self) -> str:
        url = f'load-check'
        return await self.get(url)

    async def get_version(self) -> str:
        url = f'version'
        return await self.get(url)
   
    async def get_log_stream(self) -> str:
        url = f'log'
        return await self.get(url)
    
    async def get_config(self) -> str:
        url = f'config'
        return await self.get(url)
    
    async def get_info(self) -> str:
        url = f'info'
        return await self.get(url)
