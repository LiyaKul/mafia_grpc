import grpc
import logging
import asyncio
import random
import string
from enum import Enum
import os
import time
import sys
sys.path.append('protos/.')
import protos.engine_pb2 as engine_pb2
import protos.engine_pb2_grpc as engine_pb2_grpc
from aio_pika import ExchangeType, connect
from aio_pika.abc import AbstractIncomingMessage

from roles import *

class MessageType(Enum):
    INFO = 1
    DEATH = 2
    PUBLISH = 3
    END = 4


async def on_message(message: AbstractIncomingMessage) -> None:
    async with message.process():
        print(f"[x] {message.body!r}")

class RandomPlayer:
    def __init__(self, stub: engine_pb2_grpc.EngineServerStub):
        self.stub = stub
        self.name = ''.join(random.choice(string.ascii_uppercase) for _ in range(7)) # https://stackoverflow.com/questions/2030053/how-to-generate-random-strings-in-python
        self.request_type = 'day'
        self.action_cond = asyncio.Condition()
        self.checks = dict()
        self.check_name = None
        self.time = 'day'
        self.game_end = False
        self.is_alive = True

    async def join(self) -> None:
        response = await self.stub.Join(engine_pb2.JoinRequest(name=self.name, text='hello'))
        logging.info(self.name + ': ' + response.text)
        self.id = response.id
        return response.id != -1

    async def get_players(self) -> None:
        response = await self.stub.GetPlayers(engine_pb2.GetPlayersRequest(name=self.name, text='hello'))
        self.players = response.names.split('%')
        logging.info(self.name + ': Received players:' + response.names.replace('%', ', '))

    async def want_to_start(self):
        response = await self.stub.Start(engine_pb2.StartRequest(name=self.name, text='hello'))
        if not response.started:
            logging.info(self.name + ': Im not in game :(')
            return False
        logging.info(self.name + ': I got the %s role!' % response.role)
        self.players = response.players.split('%')
        if response.role == 'Sheriff':
            self.role = Sheriff(self.id, self.players, self.name)
        elif response.role == 'Mafia':
            self.role = Mafia(self.id, self.players, self.name, list(response.mafias.split('%')))
        elif response.role == 'Villager':
            self.role = Villager(self.id, self.players, self.name)
        else:
            print('Incorrect role')
            exit()
        return response.started
    
    async def kill(self):
        if self.role.role == 'Mafia':
            response = await self.stub.Kill(engine_pb2.KillRequest(name=self.name, kill_name=self.role.action()))
            logging.info(self.name + ': ' + response.text)

    async def check(self):
        if self.role.role == 'Sheriff':
            response = await self.stub.Check(engine_pb2.CheckRequest(name=self.name, check_name=self.role.action()))
            logging.info(self.name + ': ' + response.text)

    async def vote(self):
        response = await self.stub.Vote(engine_pb2.VoteRequest(name=self.name, vote_name=self.role.vote()))
        logging.info(self.name + ': ' + response.text)
    
    async def end_day(self):
        response = await self.stub.EndDay(engine_pb2.EndDayRequest(name=self.name))
        if response.ended:
            self.time = 'night'
            if response.text == 'end':
                self.game_end = True
        if response.dead_player_name:
            self.role.new_dead(response.dead_player_name)
            if response.dead_player_name == self.name:
                self.is_alive = False

    async def end_night(self):
        response = await self.stub.EndNight(engine_pb2.EndNightRequest(name=self.name))
        if response.ended:
            self.time = 'day'
            if response.text == 'end':
                self.game_end = True
            if response.dead_player_name:
                self.role.new_dead(response.dead_player_name)
                if response.dead_player_name == self.name:
                    self.is_alive = False
    
    async def start_game(self):
        # if not await self.want_to_start():
        #     exit()
        # await self.get_players()
        # await asyncio.sleep(3)
        for i in range(3):
            await self.send_to_chat()
        # for i in range(50):
        #     if not self.is_alive or self.game_end:
        #         break
        #     if self.time == 'night':
        #         if self.role.role == 'Sheriff':
        #             await self.check()
        #             await asyncio.sleep(1)
        #         elif self.role.role == 'Mafia':
        #             await self.kill()
        #             await asyncio.sleep(1)
        #         await self.end_night()
        #         await asyncio.sleep(1)
        #         self.time = 'day'
        #     elif self.time == 'day':
        #         await self.vote()
        #         await asyncio.sleep(1)
        #         await self.end_day()
        #         await asyncio.sleep(1)
        #         self.time = 'night'
        # if not self.game_end:
        #     logging.info(self.name + ': Too many iterations, game ended.')


    async def get_messages(self):
        messages = self.stub.GameInfo(engine_pb2.InfoRequest(name=self.name, text='hello'))
        async for message in messages:
            logging.info(self.name + ': "'+ message.text +'"')
            if message.type == 'info':
                continue
            if message.type == 'death':
                if message.dead_player_name == self.name:
                    self.is_alive = False
                self.role.new_dead(message.dead_player_name)
            elif message.type == 'end':
                self.game_end = True
                break

    async def send_to_chat(self):
        logging.info(self.name + ': send message to chat: "' + 'hello' +'"')
        # print('send to CHAT' + self.name)
        request = await self.stub.Chat(engine_pb2.ChatRequest(name=self.name, message=self.name + ':' + 'hello!'))
        print(request.result)
    
    async def chat(self):
        # Perform connection
        connection = await connect('127.0.0.1')
 
        async with connection:
            # Creating a channel
            channel = await connection.channel()
            await channel.set_qos(prefetch_count=1)
 
            logs_exchange = await channel.declare_exchange(
                "logs", ExchangeType.FANOUT,
            )
 
            # Declaring queue
            queue = await channel.declare_queue(exclusive=True)
 
            # Binding the queue to the exchange
            await queue.bind(logs_exchange)
 
            # Start listening the queue
            await queue.consume(on_message)
 
            print(" [*] Waiting for logs. To exit press CTRL+C")
            await asyncio.Future()

async def main() -> None:
    time.sleep(7)
    name = ''.join(random.choice(string.ascii_uppercase) for _ in range(7)) # https://stackoverflow.com/questions/2030053/how-to-generate-random-strings-in-python
    async with grpc.aio.insecure_channel('127.0.0.1:50050', options=(('grpc.enable_http_proxy', 0),)) as channel:
        stub =  engine_pb2_grpc.EngineServerStub(channel)
        player = RandomPlayer(stub)
        if not await player.join():
            print('Try lately')
            return
        await player.get_players()
        await asyncio.gather(
            player.start_game(),
            # player.get_messages(),
            player.chat()
        )
        

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main())
