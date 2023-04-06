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
            
    async def _get(self, url: str, headers={})-> str:
        async with aiohttp.ClientSession(headers={**BaseClient.headers, **headers}) as session:
            url=url_normalize(f'{self.api_base}/{url}')
            async with session.get(url) as resp:
                return await resp.text()

    async def _get_stream(self, url: str, headers={})-> str:
            async with aiohttp.ClientSession(headers={**BaseClient.headers, **headers}) as session:
                url=url_normalize(f'{self.api_base}/{url}')
                async with session.get(url) as response:
                    async for line in response.content:
                        yield line.decode('utf-8')

    async def _post(self, url: str, headers = {}, data=None, config=None) -> str:
        async with aiohttp.ClientSession(headers={**BaseClient.headers, **headers}) as session:
            url=url_normalize(f'{self.api_base}/{url}')
            async with session.post(url, headers=headers, data=data, params=config) as resp:
                return await resp.text()

    async def _put(self, url: str, headers = {}, data=None, config=None) -> str:
        async with aiohttp.ClientSession(headers={**BaseClient.headers, **headers}) as session:
            url=url_normalize(f'{self.api_base}/{url}')
            async with session.put(url, headers=headers, data=data, params=config) as resp:
                return await resp.text()

    async def _delete(self, url: str, headers = {}) -> str:
        async with aiohttp.ClientSession(headers={**BaseClient.headers, **headers}) as session:
            url=url_normalize(f'{self.api_base}/{url}')
            async with session.delete(url, headers=headers) as resp:
                return await resp.text() 

    async def get_load_check(self) -> str:
        url = f'load-check'
        return await self._get(url)

    async def get_version(self) -> str:
        url = f'version'
        return await self._get(url)
   
    async def get_log_stream(self) -> str:
        url = f'log'
        return self._get_stream(url)
    
    async def get_config(self) -> str:
        url = f'config'
        return await self._get(url)
    
    async def get_info(self) -> str:
        url = f'info'
        return await self._get(url)
