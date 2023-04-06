from client.host_client import HostClient
from client_utils.base_client import BaseClient


class ManagerClient(BaseClient):
    def __init__(self, url: str) -> None:
        super().__init__(url=url)

    async def get_host_client(self, id: str, host_api_base: str = '/api/v1') -> HostClient:
        return HostClient(f'{self.url}/sth/{id}{host_api_base}')

    async def get_hosts(self) -> str:
        url = f'list'
        return await self._get(url)
    
    async def get_sequences(self) -> str:
        url = f'sequences'
        return await self._get(url)
    
    async def get_instances(self) -> str:
        url = f'instances'
        return await self._get(url)

    #TODO: to fix
    async def get_named_data(self, topic: str) -> str:
        url = f'topic/{topic}'
        return await self._get(url)