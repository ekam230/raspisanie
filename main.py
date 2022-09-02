#!/usr/bin/env python

# WS server example that synchronizes state across clients

import asyncio
import json
import logging
import websockets

import datetime

logging.basicConfig()

STATE = {"value": 0}

USERS = set()

SMS = {"id": 8,"time":"01:19","name":"Александр Пушкин","operator":"Водоход","terminal":7,"path":"Москва-соловки7-москва"}

MESSAGE = {0:{"id": 1,"time":"01:19","name":"Александр Пушкин","operator":"Водоход","terminal":5,"path":"Москва-соловки2-москва"},2:{"id": 2,"time":"01:19","name":"Октябрьская революция","operator":"Гама","terminal":5,"path":"Астрахань-Москва"},3:{"id": 2,"time":"01:19","name":"Сергей Есенин","operator":"Гама","terminal":5,"path":"Москва-соловки-москва"},4:{"id": 2,"time":"01:19","name":"Михаил Булгаков","operator":"Гама","terminal":5,"path":"Москва-соловки-москва"},5:{"id": 2,"time":"01:19","name":"Феликс Дзержинский","operator":"Гама","terminal":5,"path":"Москва-соловки-москва"},6:{"id": 2,"time":"01:19","name":"Михаил Танич","operator":"Гама","terminal":5,"path":"Москва-соловки-москва"}}


def state_event():
    return json.dumps({"type": "state", **STATE})


def state_event2():
    return json.dumps({"type": "list_data", **MESSAGE})


def users_event():
    return json.dumps({"type": "users", "count": len(USERS)})

def get_time():
    now = datetime.datetime.now()
    return now


async def notify_state():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event()
        await asyncio.wait([user.send(message) for user in USERS])

async def notify_state2():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = state_event2()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_event()
        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):
    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()

def shutdown():
    # Отменяем все задачи, кроме вызвавшей
    for task in asyncio.Task.all_tasks():
        if task is not asyncio.tasks.Task.current_task():
            task.cancel()


# Сопрограмма, выполняемая параллельно с ожиданием пользовательского ввода
async def task_manager():
    counter = 0
    while True:
        try:
            await asyncio.sleep(1)
        except asyncio.CancelledError:
            break # Выходим из цикла, если задачу отменили
        counter += 1
        print("I'm a task manager {} {}!".format(counter,MESSAGE))


async def user_io():
    loop = asyncio.get_event_loop()
    # Ждём действия от пользователя
    while True:
        # Запускаем input() в отдельном потоке и ждём его завершения
        command = await loop.run_in_executor(None, input, 'Для выхода введите C:\n')
        if command.lower() == 'c':
            shutdown() # Отменяем все задачи
            break      # и выходим из цикла
        elif command.lower() == 'obj':
            print(MESSAGE)
        else:
            i = len(MESSAGE)
            try:
                MESSAGE[i+1] = {"id": 8,"time":"01:19","name":"Александр Пушкин","operator":"Водоход","terminal":7,"path":"Москва-соловки7-москва"}
                # result = json.dumps(command)
                # MESSAGE[i+1]= json.loads(command)
                # print(MESSAGE2)
            except: pass
            await notify_state2()


async def counter(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        await websocket.send(state_event())
        await websocket.send(state_event2())
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "minus":
                STATE["value"] -= 1
                await notify_state()
            elif data["action"] == "plus":
                STATE["value"] += 1
                await notify_state()
            else:
                logging.error("unsupported event: %s", data)
    finally:
        await unregister(websocket)


start_server = websockets.serve(counter, "localhost", 6789)

main_task = asyncio.wait([user_io(), start_server]) #main_task = asyncio.wait([user_io(), task_manager(), start_server])
asyncio.get_event_loop().run_until_complete(main_task)
asyncio.get_event_loop().run_forever()

# if __name__ == "__main__":
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(main_task)