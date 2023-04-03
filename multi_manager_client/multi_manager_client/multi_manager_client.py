from manager_client.manager_client.manager_client import ManagerClient
import json
from client_utils.base_client import BaseClient


class MultiManagerClient(BaseClient):
    def __init__(self, url: str) -> None:
        super().__init__(url=url)

    async def get_manager_client(self, id: str, manager_api_base: str = '/api/v1') -> ManagerClient:
        return ManagerClient(f'{self.url.geturl()}/cpm/{id}{manager_api_base}')
    
    async def start_manager(self, config: dict, manager_api_base: str = '/api/v1') -> ManagerClient:
        resp = await self.post(
            url='start',
            headers={'content-type': 'application/json'},
            data=config
        )
        json_data = json.loads(resp)
        if 'error' in json_data:
            raise Exception(json_data.get('error'))
        return ManagerClient(f"{self.url.geturl()}/cpm/{json_data.get('id')}{manager_api_base}")

    async def get_managers(self) -> str:
        url = f'list'
        return await self.get(url)
