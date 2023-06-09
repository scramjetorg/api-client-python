from client_utils.base_client import BaseClient
from manager_client.manager_client import ManagerClient


class MiddlewareClient(BaseClient):
    def __init__(self, url: str):
        super().__init__(url=url)

    async def get_manager_client(self, id: str, manager_api_base: str = '/api/v1'):
        return ManagerClient(f'{self.url.geturl()}/space/{id}{manager_api_base}')

    async def list_managers(self) -> list:
        """
        List informations about Managers.

        Returns
        -----------
        list:
            List with informations about Managers.
        """
        url = 'spaces'
        return await self._get(url)
