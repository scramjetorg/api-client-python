from urllib.parse import urlparse
from url_normalize import url_normalize
import aiohttp
import json


class BaseClient:
    headers = {}
    
    def __init__(self, url: str) -> None:
        self.url = urlparse(url)
        self.api_base = url

    def __repr__(self) -> str:
        return f'host: {self.host}, API base: {self.api_base}, headers: {self.headers}'
    
    @staticmethod
    def setDefaultHeaders(headers):
        BaseClient.headers = headers   
            
    async def _get(self, url: str, headers={})-> str:
        async with aiohttp.ClientSession(headers={**BaseClient.headers, **headers}) as session:
            url=url_normalize(f'{self.api_base}/{url}')
            async with session.get(url) as resp:
                return await resp.json()

    async def _get_stream(self, url: str, headers={})-> str:
            async with aiohttp.ClientSession(headers={**BaseClient.headers, **headers}) as session:
                url=url_normalize(f'{self.api_base}/{url}')
                async with session.get(url) as response:
                    async for line in response.content:
                        yield line.decode('utf-8')

    async def _post(self, url: str, headers = {}, data=None, config=None) -> str:
        async with aiohttp.ClientSession(headers={**BaseClient.headers, **headers}) as session:
            url=url_normalize(f'{self.api_base}/{url}')
            if type(data) != bytes:
                data = json.dumps(data)
            async with session.post(url, headers=headers, data=data, params=config) as resp:
                return await resp.json()

    async def _put(self, url: str, headers = {}, data=None, config=None) -> str:
        async with aiohttp.ClientSession(headers={**BaseClient.headers, **headers}) as session:
            url=url_normalize(f'{self.api_base}/{url}')
            async with session.put(url, headers=headers, data=json.dumps(data), params=config) as resp:
                return await resp.json()

    async def _delete(self, url: str, headers = {}) -> str:
        async with aiohttp.ClientSession(headers={**BaseClient.headers, **headers}) as session:
            url=url_normalize(f'{self.api_base}/{url}')
            async with session.delete(url, headers=headers) as resp:
                return await resp.json() 

    async def get_load_check(self) -> dict:
        """
        Retrieves the load of the host.

        Returns
        -----------
        dict: 
            Dict with load check informations.
        """
        url = f'load-check'
        return await self._get(url)

    async def get_version(self) -> dict:
        """
        Retrieves the version of the host.

        Returns
        -----------
        dict:
            Dict with the version of the host.
        """
        url = f'version'
        return await self._get(url)
   
    async def get_log_stream(self) -> str:
        """
        Retrieves and yields logs from the host.
        Should be called as async generator.

        Returns
        -----------
        str: 
            String with stream logs (UTF-8).
        """
        url = f'log'
        return self._get_stream(url)
    
    async def get_config(self) -> dict:
        """
        Retrieves the log stream of the STH.

        Returns
        -----------
        dict: 
            Dict with config informations.
        """
        url = f'config'
        return await self._get(url)
