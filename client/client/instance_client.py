from client.host_client import HostClient
import json

INSTANCE_INPUT_STREAM = (
    'stdin',
    'input'
)

INSTANCE_OUTPUT_STREAM = (
    'stdout',
    'stderr',
    'output',
    'log'
)


class InstanceClient:
    """
    A client for interacting with a specific Instance (running Sequence) of a host.

    Attributes
    -----------
    id: str
        The ID of the instance.
    host: HostClient
        The host client associated with the instance.

    Methods
    ----------
    stop(timeout: int, can_keep_alive: bool)
    
    kill()

    send_event(event_name: str, message: str) -> str:

    get_next_event(id: str) -> str:

    get_event(id: str) -> str:

    get_health() -> str:

    get_info() -> str:

    send_stream(stream_id: INSTANCE_INPUT_STREAM, stream: str, options: dict = {})

    send_input(stream: str, options: str = {})

    send_stdin(stream: str):

    """
    def __init__(self, id: str, host: HostClient) -> None:
        """
        Initializes a new Instance client.

        Parameters
        id: str
            The ID of the instance.
        host: HostClient
            The host client associated with the instance.
        """
        self.id = id
        self.host = host
        self.instance_url = f'instance/{id}'

    #TODO: 500
    async def stop(self, timeout: int = 7000, can_keep_alive: bool = False):
        """
        Stops the instance.

        Parameters
        -------------
        timeout: int
            The amount of time to wait for the instance to stop, in milliseconds.
        can_keep_alive: bool
            Whether to keep the instance running if it has a keepalive.

        Returns
        -------------
            The response from the server.
        """
        url = f'{self.instance_url}/_stop'
        headers = {'Content-Type': 'application/json'}
        payload = {'timeout': timeout, 'canCallKeepalive': can_keep_alive}
        return await self.host.post(url, headers=headers, data=payload)

    async def kill(self):
        """
        Kills the Instance.

        Returns
        ---------
            The response from the server.
        """
        url = f'{self.instance_url}/_kill'
        headers = {'Content-Type': 'application/json'}
        return await self.host.post(url, headers=headers, data={})
    
    async def send_event(self, event_name: str, message: str = '') -> str:
        """
        Sends an event to the instance.

        Parameters
        ------------
        event_name: str
            The name of the event.
        message: str
            The message to include in the event.

        Returns
        ---------
        str: 
            The response from the server.
        """
        url = f'{self.instance_url}/_event'
        headers = {"Content-Type": "application/json"}
        event_code = 5001
        data = {'eventName': event_name, 'message': message}
        payload = json.dumps([event_code, data])
        return await self.host.post(url, headers=headers, data=payload)
    
    async def get_next_event(self, id: str) -> str:
        """
        Gets the next event for the instance.

        Parameters
        ------------
        id: str
            The ID of the event.

        Returns
        ------------
        str: 
            The response from the server.
        """
        url = f'{self.instance_url}/once/{id}'
        return await self.host.get(url)

    async def get_event(self, id: str) -> str:
        """
        Gets an event for the instance.

        Parameters
        ------------
        id: str
            The ID of the event.

        Returns
        ------------
        str: 
            The response from the server.
        """
        url = f'{self.instance_url}/event/{id}'
        return await self.host.get(url)
    
    async def get_health(self) -> str:
        """
        Gets the health of the Instance.

        Returns
        ----------
        str: 
            The response from the server.
        """
        url = f'{self.instance_url}/health'
        return await self.__get(url)

    async def get_info(self) -> str:
        """
        Get informations about the Instance.

        Returns
        ----------
            The response from the server.
        """
        url = f'{self.instance_url}'
        return await self.host.get(url)

    async def send_stream(self, stream_id: INSTANCE_INPUT_STREAM, stream: str, options: dict = {}):
        """
        Send a stream of data to the Instance.

        Parameters
        -----------
        stream_id: INSTANCE_INPUT_STREAM
            The ID of the input stream to send the data to.
        stream: str 
            The data to send.??
        options: dict
            Any additional options for the request. Default is an empty dictionary.

        Returns
        ----------
            The response from the request.
        """
        url = f'{self.instance_url}/{stream_id}'
        return await self.host.send_stream(url, stream, options)

    async def send_input(self, stream: str, options: str = {}):
        """
        Send a input to the Instance.

        Parameters
        -----------
        stream: str
            The ID of the input stream to send the data to.
        stream: str 
            The data to send.
        options: dict
            Any additional options for the request. Default is an empty dictionary.

        Returns
        ----------
            The response from the request.
        """
        url = f'{self.instance_url}/input'
        return await self.send_stream(url, stream, options)
    
    async def send_stdin(self, stream: str):
        """
        Send a stream of data to the Instance's standard input stream.

        Parameters
        ----------
        stream : str
            The data to be sent to the instance's standard input.
        """
        url = f'{self.instance_url}/stdin'
        return await self.send_stream(url, stream)
