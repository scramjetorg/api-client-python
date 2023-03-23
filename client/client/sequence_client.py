from client.host_client import HostClient
from client.instance_client import InstanceClient

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
    -------
    """
    def __init__(self, id: str, host: HostClient) -> None:
        self.id = id
        self.host = host
        self.sequence_url = f'/sequence/{id}'
    
    async def start(self) -> str:
        """
        Start the Sequence
        """
        url = f'{self.sequence_url}/start'
        headers = {'Content-Type': 'application/json'}
        return await self.host.post(url, headers=headers, data={})
    
    async def list_instances(self) -> str:
        """
        List all Instances of the Sequence.

        Returns
        ----------
        str: 
            The text of the response.
        """
        url = f'{self.sequence_url}/instances'
        return await self.host.get(url)

    async def get_instance(id: str, host: HostClient) -> InstanceClient:
        """
        Get the Instance with the specified ID.

        Parameters
        -----------
        id: str
            The ID of the Instance.
        Returns
        -----------
        InstanceClient: 
            Instance Client.
        """
        return InstanceClient(id, host)

    async def get_info(self) -> str:
        """
        Retrieve information about the Sequence.

        Returns
        -----------
        str: 
            Response body with information about the Sequence.
        """
        url = f'{self.sequence_url}'
        return await self.host.get(url)
