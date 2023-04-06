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
    def __init__(self, id: str, host: HostClient) -> None:
        self.id = id
        self.host = host
        self.instance_url = f'instance/{id}'

    def __repr__(self) -> str:
        return f'host: {self.host}, id: {self.id}, instance_url: {self.instance_url}'

    #TODO: 500
    async def stop(self, timeout: int = 7000, can_keep_alive: bool = False):
        url = f'{self.instance_url}/_stop'
        headers = {'Content-Type': 'application/json'}
        payload = {'timeout': timeout, 'canCallKeepalive': can_keep_alive}
        return await self.host._post(url, headers=headers, data=payload)

    async def kill(self):
        url = f'{self.instance_url}/_kill'
        headers = {'Content-Type': 'application/json'}
        return await self.host._post(url, headers=headers, data={})
    
    async def send_event(self, event_name: str, message: str = '') -> str:
        url = f'{self.instance_url}/_event'
        headers = {"Content-Type": "application/json"}
        event_code = 5001
        data = {'eventName': event_name, 'message': message}
        payload = json.dumps([event_code, data])
        return await self.host._post(url, headers=headers, data=payload)
    
    async def get_next_event(self, id: str) -> str:
        url = f'{self.instance_url}/once/{id}'
        return await self.host._get(url)

    async def get_event(self, id: str) -> str:
        url = f'{self.instance_url}/event/{id}'
        return await self.host._get(url)
    
    async def get_health(self) -> str:
        url = f'{self.instance_url}/health'
        return await self.host._get(url)

    async def get_info(self) -> str:
        url = f'{self.instance_url}'
        return await self.host._get(url)

    async def send_stream(self, stream_id: INSTANCE_INPUT_STREAM, stream: str, options: dict = {}):
        url = f'{self.instance_url}/{stream_id}'
        return await self.host.send_stream(url, stream, options)

    async def send_input(self, stream: str, options: str = {}):
        url = f'{self.instance_url}/input'
        return await self.send_stream(url, stream, options)
    
    async def send_stdin(self, stream: str):
        url = f'{self.instance_url}/stdin'
        return await self.send_stream(url, stream)
