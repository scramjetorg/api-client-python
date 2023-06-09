from client.host_client import HostClient
import json


# INSTANCE_OUTPUT_STREAM = (
#     'stdout',
#     'stderr',
#     'output',
#     'log'
# )

class InstanceClient:
    """
    A client for interacting with a Instances on a remote host.

    Attributes
    ----------
    id: str
        The unique identifier of the Sequence.
    host: HostClient
        The client for the remote host where the Sequence is located.

    Methods
    ----------

    stop(timeout, can_keep_alive)

    kill()

    send_event(event_name, message)

    get_next_event()

    get_event_stream()

    get_health()

    get_info()

    send_stdin(stream)

    send_input(stream, options)

    -------
    """
    def __init__(self, id: str, host: HostClient) -> None:
        self.id = id
        self.host = host
        self.instance_url = f'instance/{id}'

    def __repr__(self) -> str:
        return f'host: {self.host}, id: {self.id}, instance_url: {self.instance_url}'

    async def stop(self, timeout: int = 7000, can_keep_alive: bool = False) -> str:
        """
        Ends the Instance gracefully.

        Parameters
        -----------
        timeout: str
            Number of milliseconds before the Instance will be killed.

        can_keep_alive: bool
            If true, the Instance will prolong the running.

        Returns
        -----------
        str:
            String with the response.
        """
        url = f'{self.instance_url}/_stop'
        headers = {'Content-Type': 'application/json'}
        payload = {'timeout': timeout, 'canCallKeepalive': can_keep_alive}
        return await self.host._post(url, headers=headers, data=payload)

    async def kill(self) -> str:
        """
        Kills the Instance immediately.

        Returns
        -----------
        str:
            String with the response.
        """
        url = f'{self.instance_url}/_kill'
        headers = {'Content-Type': 'application/json'}
        return await self.host._post(url, headers=headers, data={})

    async def send_event(self, event_name: str, message: str = '') -> dict:
        """
        Sends event to the Instance.

        Parameters
        -----------
        event_name: str
            Name of an event.
        message: str
            Event payload.

        Returns
        -----------
        dict:
            Dict with the response.
        """
        url = f'{self.instance_url}/_event'
        headers = {'Content-Type': 'application/json'}
        event_code = 5001
        data = {'eventName': event_name, 'messagee': message}
        payload = [event_code, data]
        params = json.dumps({'json': 'true', 'parse': 'json'})
        return await self.host._post(url, headers=headers, data=payload, config=params)

    async def get_next_event(self) -> dict:
        """
        Get the last event sent by the Instance.

        Returns
        -----------
        dict:
            Dict with the response.
        """
        url = f'{self.instance_url}/once'
        return await self.host._get(url)

    async def get_event_stream(self) -> str:
        """
        Get the data stream with the events from the Instance.

        Returns
        -----------
        str:
            String with the response.
        """
        url = f'{self.instance_url}/event'
        return await self.host._get_stream(url)

    async def get_health(self) -> dict:
        """
        Check status about Instance health.

        Returns
        -----------
        dict:
            Dict with the Instance's health status
        """
        url = f'{self.instance_url}/health'
        return await self.host._get(url)

    async def get_info(self) -> dict:
        """
        Get informations about the Instance.

        Returns
        -----------
        dict:
            Dict with information about the Instance.
        """
        url = f'{self.instance_url}'
        return await self.host._get(url)

    async def send_input(self, stream: str, options: str = {}):
        """
        Send data to the input stream of the Instance to consume it

        Returns
        -----------
        """
        url = f'{self.instance_url}/input'
        data = {'type': 'text/plain', 'end': 'True', 'parse_response': 'stream'}
        data.update(options)
        return await self.host._send_stream(url, stream, data)

    async def send_stdin(self, stream: str):
        """
        Send to `process.stdin`.

        Parameters
        -----------
        stream: str
            Name of an event.

        Returns
        -----------
        """

        url = f'{self.instance_url}/stdin'
        return await self.host._send_stream(url, stream)
