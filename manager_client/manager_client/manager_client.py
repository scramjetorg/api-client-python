from client.host_client import HostClient
from client_utils.base_client import BaseClient


class ManagerClient(BaseClient):
    def __init__(self, url: str) -> None:
        super().__init__(url=url)

    async def get_host_client(self, id: str, host_api_base: str = '/api/v1') -> HostClient:
        return HostClient(f'{self.url}/sth/{id}{host_api_base}')

    async def list_hosts(self) -> list:
        """
        List informations about Hosts.

        Returns
        -----------
        list:
            List with informations about Hosts.
        """
        url = 'list'
        return await self._get(url)

    async def list_sequences(self) -> list:
        """
        List informations about Sequences.

        Returns
        -----------
        list:
            List with informations about Sequences.
        """
        url = 'sequences'
        return await self._get(url)

    async def list_instances(self) -> list:
        """
        List informations about Instances.

        Returns
        -----------
        list:
            List with informations about Instances.
        """
        url = 'instances'
        return await self._get(url)

    async def get_named_data(self, topic: str):
        """
        Retrieves named data from the specified topic and yields the response body.
        Should be called as async generator.

        Parameters
        ------------
        topic: str
            The topic to get the data from.

        Returns
        -----------
        str:
            String with topic data (UTF-8).
        """
        url = f'topic/{topic}'
        return self._get_stream(url)
