import aiohttp
from urllib.parse import urlparse


class HostClient:
    """
    A client for communicating with a host server.

    Attributes
    -----------
    url : str
        The URL of the host server.
        
    Methods
    --------
    get(url: str) -> str:

    post(url: str, headers: str = None, data=None, config=None) -> str:

    delete(url: str, headers: str = None) -> str:

    get_data(seq_path: str) -> bytes:

    send_stream(url: str, stream: str, options: dict):

    list_sequences() -> str:

    list_instances() -> str:

    send_sequence(file, app_config = None) -> str:

    get_sequence(id: str) -> str:

    delete_sequence(id: str) -> str:

    get_instance_info(id: str) -> str:

    get_load_check() -> str:

    get_version() -> str:

    get_log_stream() -> str:

    send_named_data(topic: str, stream: str, content_type: str, end: bool)

    get_named_data(topic: str)
    """
    def __init__(self, url: str) -> None:
        """
        Initialize the HostClient object with a URL.

        Parameters
        ----------
        url: str
            The URL to connect to.
        """
        self.url = urlparse(url)

    async def get(self, url: str) -> str:
        """
        Make a GET request to the given URL.

        Parameters
        ----------
        url: str
            The URL to connect to.

        Returns
        ----------
        str:
            The text of the response.
        """
        async with aiohttp.ClientSession() as session:
            url = f'{self.url.geturl()}{url}'
            async with session.get(url) as resp:
                return await resp.text()
    
    async def post(self, url: str, headers: str = None, data=None, config=None) -> str:
        """
        Make a POST request to the given URL.

        Parameters
        ----------

        url: str   
            The URL to POST to.
        headers: str
            Headers to include in the request.
        data: 
            The data to include in the request.
        config: 
            Configuration options for the request.
        
        Returns
        ----------
        str:
            The text of the response.
        """
        async with aiohttp.ClientSession() as session:
            url = f'{self.url.geturl()}{url}'
            async with session.post(url, headers=headers, data=data, params=config) as resp:
                return await resp.text()
    
    async def delete(self, url: str, headers: str = None) -> str:
        """
        Make a DELETE request to the given URL.

        Parameters
        ----------
        url : str
            The URL to DELETE.

        headers: str
            Headers to include in the request.

        Returns
        ----------
        str:
            The text of the response.
        """
        async with aiohttp.ClientSession() as session:
            url = f'{self.url.geturl()}{url}'
            async with session.delete(url, headers=headers) as resp:
                return await resp.text()
    
    async def get_data(self, seq_path: str) -> bytes:
        """
        Read the Sequence and return it as bytes.

        Parameters
        ----------
        seq_path : str
            The URL to DELETE.

        Returns
        ----------
        bytes:
            The bytes read from the sequence.
        """
        with open(seq_path, 'rb') as f:
            return f.read()
    
    async def send_stream(self, url: str, stream: str, options: dict):
        """
        Send a stream of data to the given URL.

        Parameters
        ----------
        url: str
            The URL to send the stream to
        stream: str
            The stream of data to send.
        options: dict
            Options to configure the request.
        Returns
        ----------
            The text of the response.
        """
        headers = {
            'content-type': options.get('type'),
            'x-end-stream': options.get('end')
        }
        config = { 'parse': options.get('parse_response') }
        return await self.post(url, headers, stream, config)
 
    async def list_sequences(self) -> str:
        """
        Lists all the Sequences from the server.

        Returns
        ----------
        str:
            String with informations about all Sequences.
        """
        url = f'/sequences'
        return await self.get(url)
    
    async def list_instances(self) -> str:
        """
        List all Instances from the server.

        Returns
        ----------
        str: 
            String with informations about all Instances.
        """
        url = f'/instances'
        return await self.get(url)


    async def send_sequence(self, file, app_config = None) -> str:
        """
        Sends a binary Sequence file to the server.

        Parameters
        -----------
        file: The Sequence (binary).
        app_config: The configuration settings for the request.

        Returns
        ----------
        str: 
            String with the Sequence ID.
        """
        url = f'/sequence'
        data = await self.get_data(file)
        return await self.post(url, data=data)

    async def get_sequence(self, id: str) -> str:
        """
        Get the Sequence with the specified ID.

        Parameters
        -----------
        id: str
            The ID of the Sequence.
        Returns
        -----------
        str: 
            The text of the response.
        """
        url = f'/sequence/{id}'
        return await self.get(url)

    async def delete_sequence(self, id: str) -> str:
        """
        Delete the Sequence with the specified ID and returns the response body.

        Parameters
        ------------
        id: str
            Sequence ID

        Returns
        -----------
        str: 
            The text of the response.
        """
        url = f'/sequence/{id}'
        headers = {'Content-Type': 'application/json'}
        return await self.delete(url, headers=headers)

    async def get_instance_info(self, id: str) -> str:
        """
        Sends a GET request to retrieve information about the Instance with the specified ID and returns the response body.

        Parameters
        -----------
        id: str
            The ID of the Instance.

        Returns
        -----------
        str: 
            Response body with information about the Instance.
        """
        url = f'/instance/{id}'
        return await self.get(url)

    async def get_load_check(self) -> str:
        """
        Sends a GET request to check the load of the host and returns the response body.

        Returns
        -----------
        str: 
            The text of the response.
        """
        url = f'/load-check'
        return await self.get(url)

    async def get_version(self) -> str:
        """
        Sends a GET request to retrieve the version of the host.

        Returns
        -----------
        str:
            Response body with the version of the host.
        """
        url = f'/version'
        return await self.get(url)
   
    async def get_log_stream(self) -> str:
        """
        Sends a GET request to retrieve the log stream of the host and returns the response body.

        Returns
        -----------
        str: 
            Response body with stream logs.
        """
        url = f'/log'
        return await self.get(url)

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
        end: bool
            Indicates whether or not this is the last chunk of data in the stream.
        """
        data = {'type': content_type, 'end': end, 'parse_response': 'stream'}
        return await self.send_stream(f'topic/{topic}', stream, options=data)

    async def get_named_data(self, topic: str):
        """
        Sends a GET request to retrieve named data from the specified topic and returns the response body.

        Parameters
        ------------
        topic: str
            The topic to get the data from.
        """
        return await self.get(f'topic/{topic}')
