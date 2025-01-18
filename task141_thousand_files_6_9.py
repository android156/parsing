import os
import time
import asyncio
import aiofiles

# Создание директории для файлов, если она не существует
os.makedirs('test_files', exist_ok=True)


# Создание 1000 текстовых файлов
def create_files():
    for i in range(1000):
        with open(f'test_files/file_{i}.txt', 'w') as f:
            f.write('Hello, world!\n' * 100)  # Запись некоторого количества строк для создания содержимого

create_files()  # Создание файлов

# Синхронное чтение файлов
def sync_read_files():
    start = time.perf_counter()
    for i in range(1000):
        with open(f'test_files/file_{i}.txt', 'r') as f:
            lines = f.readlines()
    sync_time = time.perf_counter() - start
    return sync_time


# Асинхронное чтение файлов
async def async_read_file(file_path):
    async with aiofiles.open(file_path, mode='r') as f:
        await f.readlines()


async def async_read_files():
    start = time.perf_counter()
    tasks = [async_read_file(f'test_files/file_{i}.txt') for i in range(1000)]
    await asyncio.gather(*tasks)
    async_time = time.perf_counter() - start
    return async_time


def main():
    sync_time = sync_read_files()                 # Синхронное чтение
    async_time = asyncio.run(async_read_files())  # Асинхронное чтение

    print(f"Синхронное чтение 1000 файлов заняло {sync_time:.5f} секунд")
    print(f"Асинхронное чтение 1000 файлов заняло {async_time:.5f} секунд")


if __name__ == '__main__':
    main()