from manager_client.manager_client.manager_client import ManagerClient
from client_utils.base_client import BaseClient


class MiddlewareClient(BaseClient):
    def __init__(self, url: str):
        super().__init__(url=url)
    
    async def get_manager_client(self, id: str, manager_api_base: str = '/api/v1'):
        return ManagerClient(f'{self.url.geturl()}/space/{id}{manager_api_base}')

    async def get_managers(self) -> str:
        url = f'spaces'
        return await self.get(url)
