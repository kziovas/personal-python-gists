import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


class MyClass:
    def __init__(self) -> None:
        self.event_loop = None
        self.pool_executor = ThreadPoolExecutor(max_workers=8)
        self.words = ["one", "two", "three", "four", "five"]
        self.multiplier = int(2)

    async def subtask(self, letter: str):
        await asyncio.sleep(1)
        return letter * self.multiplier

    async def task_gatherer(self, subtasks: list):
        return await asyncio.gather(*subtasks)

    def blocking_task(self, word: str):
        time.sleep(1)
        subtasks = [self.subtask(letter) for letter in word]
        result = asyncio.run(self.task_gatherer(subtasks))
        return result

    async def master_method(self):
        self.event_loop = asyncio.get_running_loop()
        master_tasks = [
            self.event_loop.run_in_executor(
                self.pool_executor,
                self.blocking_task,
                word,
            )
            for word in self.words
        ]

        results = await asyncio.gather(*master_tasks)
        print(results)


if __name__ == "__main__":
    my_class = MyClass()
    asyncio.run(my_class.master_method())
