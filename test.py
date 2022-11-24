import asyncio

from fcwslib import Server, Handler
from rich.console import Console

console = Console()


class MyHandler(Handler):
    async def on_connect(self) -> None:
        console.log('Connected.', style='yellow')
        await self.send_command('tellraw @a {"rawtext":[{"text":"Made in China."}]}', self.on_command_response)
        await self.subscribe('PlayerMessage', self.on_playermessage)

    async def on_receive(self, message) -> None:
        console.log('Received: {}'.format(message), style='green')

    async def on_command_response(self, message) -> None:
        console.log('Command response: {}'.format(message), style='red')

    async def on_playermessage(self, message) -> None:
        console.log('Subscribed event PlayerMessage: {}'.format(message), style='blue')
        
    async def on_disconnect(self) -> None:
        console.log('Disconnected.', style='yellow')


if __name__ == '__main__':
    server = Server(host='localhost')
    server.insert_handler(MyHandler)
    asyncio.run(server.run_forever())

