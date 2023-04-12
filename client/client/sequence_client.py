from client.host_client import HostClient
from client.instance_client import InstanceClient
import json


class SequenceClient:
    """
    A client for interacting with a Sequences on a remote host.

    Attributes
    ----------
    id: str
        The unique identifier of the Sequence.
    host: HostClient
        The client for the remote host where the Sequence is located.

    Methods

    start() -> str:

    list_instances() -> str:

    get_instance(id: str, host: HostClient ) -> InstanceClient:

    get_info() -> str:

    -------
    """
    def __init__(self, id: str, host: HostClient) -> None:
        self.id = id
        self.host = host
        self.sequence_url = f'/sequence/{id}'
    
    def __repr__(self) -> str:
        return f'host: {self.host}, id: {self.id}, sequence_url: {self.sequence_url}'

    async def start(self) -> InstanceClient:
        """
        Starts the Sequence and returns InstanceClient

        Returns
        ----------
        InstanceClient:
            InstanceClient object
        """
        url = f'{self.sequence_url}/start'
        headers = {'Content-Type': 'application/json'}    
        resp = await self.host._post(url, headers=headers, data={})
        json_resp = json.loads(resp)
        if 'error' in json_resp:
            raise Exception(json_resp.get('error'))
        return InstanceClient(json_resp['id'], host=self.host)
        
    
    async def list_instances(self) -> list:
        """
        Lists Instances of SequenceClient

        Returns
        ----------
        list:
            List with Instances IDs.
        """
        url = f'{self.sequence_url}/instances'
        return await self.host._get(url)

    async def get_instance(id: str, host: HostClient) -> InstanceClient:
        """
        Get InstanceClient.

        Parameters
        ----------
        id: str
            Path to the Sequence

        host: HostClient
            Path to the Sequence

        Returns
        ----------
        InstanceClient:
            InstanceClient object
        """
        return InstanceClient(id, host)

    async def get_info(self) -> dict:
        """
        Get informations about the Sequence.

        Returns
        ----------
        dict:
            Dict with information about the Sequence.
        """
        url = f'{self.sequence_url}'
        return await self.host._get(url)
