from client_utils.base_client import BaseClient
import json

class HostClient(BaseClient):
    def __init__(self, url: str) -> None:
        super().__init__(url=url)
    
    async def get_data(self, seq_path: str) -> bytes:
        with open(seq_path, 'rb') as f:
            return f.read()
    
    async def send_stream(self, url: str, stream: str, options: dict):
        headers = {
            'content-type': options.get('type'),
            'x-end-stream': options.get('end')
        }
        config = { 'parse': options.get('parse_response') }
        return await self.post(url, headers, stream, config)
    
    async def get_stream(self, url: str, options: dict)-> str:
        headers = {
            'content-type': options.get('type')
        }
        return await self.get(url, headers)
 
    async def list_sequences(self) -> str:
        url = f'/sequences'
        return await self.get(url)
    
    async def list_instances(self) -> str:
        url = f'instances'
        return await self.get(url)

    async def send_sequence(self, file, app_config = None) -> str:
        url = f'sequence'
        data = await self.get_data(file)
        resp = await self.post(url, data=data)
        json_resp = json.loads(resp)
        if 'error' in json_resp:
            raise Exception(json_resp.get('error'))
        return json_resp['id']

    async def get_sequence(self, id: str) -> str:
        url = f'sequence/{id}'
        return await self.get(url)

    async def delete_sequence(self, id: str) -> str:
        url = f'sequence/{id}'
        headers = {'Content-Type': 'application/json'}
        return await self.delete(url, headers=headers)

    async def get_instance_info(self, id: str) -> str:
        url = f'instance/{id}'
        return await self.get(url)

    async def send_named_data(self, topic: str, stream: str, content_type: str, end: bool):
        data = {'type': content_type, 'end': str(end), 'parse_response': 'stream'}
        return await self.send_stream(f'topic/{topic}', stream, options=data)

    async def get_named_data(self, topic: str):
        return await self.get(f'topic/{topic}')
