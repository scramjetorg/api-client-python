from client.host_client import HostClient
from urllib.parse import urlparse

import aiohttp


class ManagerClient:
    def __init__(self, url: str):
        self.url = urlparse(url)
    
    async def get(self, url: str) -> str:
        async with aiohttp.ClientSession() as session:
            url = f'{self.url.geturl()}{url}'
            async with session.get(url) as resp:
                return await resp.text()

    async def get_host_client(self, id: str, host_api_base: str = '/api/v1'):
        return HostClient(self.url.geturl() + '/sth/' + id + host_api_base)

    async def get_hosts(self) -> str:
        url = f'list'
        return await self.get(url)
    
    async def get_version(self) -> str:
        url = f'version'
        return await self.get(url)
    
    async def get_load(self) -> str:
        url = f'load'
        return await self.get(url)
    
    async def get_config(self) -> str:
        url = f'config'
        return await self.get(url)
    
    async def get_sequences(self) -> str:
        url = f'sequences'
        return await self.get(url)
    
    async def get_instances(self) -> str:
        url = f'instances'
        return await self.get(url)

    #TODO: to fix
    async def get_named_data(self, topic) -> str:
        url = f'topic/{topic}'
        return await self.get(url)
    
    async def get_log_stream(self) -> str:
        url = f'log'
        return await self.get(url)
