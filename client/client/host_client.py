from client_utils.base_client import BaseClient
import json

class HostClient(BaseClient):
    """
    A client for communicating with a host server.

    Attributes
    -----------
    url : str
        The URL of the host server.
        
    Methods
    --------
    get_data(seq_path)

    send_stream(url, stream, options)

    list_entities()

    list_sequences()

    list_instances()

    send_sequence(file, app_config = None)

    get_sequence_info(id: str)

    delete_sequence(id: str)

    get_instance_info(id: str)

    get_load_check()

    get_version()

    get_log_stream()

    send_named_data(topic, stream, content_type, end)

    get_named_data(topic)
    """

    def __init__(self, url: str) -> None:
        super().__init__(url=url)
    
    async def load_sequence(self, seq_path: str) -> bytes:
        """
        Read the Sequence and return it as bytes.

        Parameters
        ----------
        seq_path : str
            Path to the Sequence

        Returns
        ----------
        bytes:
            The bytes read from the Sequence.
        """
        with open(seq_path, 'rb') as f:
            return f.read()
    
    async def _send_stream(self, url: str, stream: str, options: dict):
        headers = {
            'content-type': options.get('type'),
            'x-end-stream': options.get('end')
        }
        config = { 'parse': options.get('parse_response') }
        return await self._post(url, headers, stream, config)
 
    async def list_sequences(self) -> str:
        """
        Lists all the Sequences from the server.

        Returns
        ----------
        str:
            Lists of dicts with informations about all Sequences.
        """
        url = f'/sequences'
        return await self._get(url)

    async def list_entities(self) -> str:
        """
        List all Instances and Sequences from the server.

        Returns
        ----------
        str: 
            Dict with informations about all entities.
        """
        url = f'entities'
        return await self._get(url) 

    async def list_instances(self) -> str:
        """
        List all Instances from the server.

        Returns
        ----------
        str: 
            List of dicts with informations about all Instances.
        """
        url = f'instances'
        return await self._get(url)

    async def send_sequence(self, file: bytes, app_config = None) -> str:
        """
        Sends a binary Sequence file to the server.
        
        Parameters
        -----------
        file: bytes
            The Sequence (binary).

        app_config: 
            The configuration settings for the request.

        Returns
        ----------
        str: 
            String with the Sequence ID.
        """
        url = f'sequence'
        resp = await self._post(url, data=file)
        json_resp = json.loads(resp)
        if 'error' in json_resp:
            raise Exception(json_resp.get('error'))
        return json_resp['id']

    async def get_sequence_info(self, id: str) -> dict:
        """
        Get informations about specified Sequence.

        Parameters
        -----------
        id: str
            The ID of the Sequence.
            
        Returns
        -----------
        dict: 
            Dict with information about the Sequence.
        """
        url = f'sequence/{id}'
        return await self._get(url)

    async def delete_sequence(self, id: str) -> str:
        """
        Delete the Sequence with the specified ID.

        Parameters
        -----------
        id: str
            The ID of the Sequence.
            
        Returns
        -----------
        str: 
            The text of the response.
        """
        url = f'sequence/{id}'
        headers = {'Content-Type': 'application/json'}
        return await self._delete(url, headers=headers)

    async def get_instance_info(self, id: str) -> dict:
        """
        Get informations about specified Instance.

        Parameters
        -----------
        id: str
            The ID of the Instance.
            
        Returns
        -----------
        dict: 
            Dict with information about the Instance.
        """
        url = f'instance/{id}'
        return await self._get(url)

    async def send_named_data(self, topic: str, stream: str, content_type: str, end: bool):
        """
        Sends named data to the specified topic using the specified stream and content type.

        Parameters
        ------------
        topic: str
            The topic to send the data to.

        stream: str
            The stream containing the data to send.

        content_type: str
            The content type of the data.
                e.g. 'text/plain'

        end: bool
            Indicates whether or not this is the last chunk of data in the stream.
        """
        data = {'type': content_type, 'end': str(end), 'parse_response': 'stream'}
        return await self._send_stream(f'topic/{topic}', stream, options=data)

    async def get_named_data(self, topic: str):
        """
        Retrieves named data from the specified topic and returns the response body.

        Parameters
        ------------
        topic: str
            The topic to get the data from.

        Returns
        -----------
            Async generator with topic data.
        """
        return self._get_stream(f'topic/{topic}')
