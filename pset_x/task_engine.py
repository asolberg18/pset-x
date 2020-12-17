import asyncio


class TaskEngine:

    def __init__(self, max_tasks=10, monitor=False, logger=None):
        self.loop = asyncio.get_event_loop()
        self.started = 0
        self.pending = 0
        self.completed = 0
        self.stopped = False
        self.max_tasks = max_tasks
        self.logger = logger
        self.monitor = monitor
        if self.monitor:
            self.loop.create_task(self.__monitor())

    def run(self, driver, *args, **kwargs):
        self.loop.run_until_complete(self.__run(driver, *args, **kwargs))

    async def stop(self):
        print("\033[1K\rStopping...")
        self.stopped = True
        while self.monitor:
            await asyncio.sleep(0.01)

    def running(self):
        return not self.stopped

    async def start_task(self, task, *args, **kwargs):
        while self.running() and self.pending >= self.max_tasks:
            await asyncio.sleep(0.005)
        if self.running():
            self.__begin_task()
            self.loop.create_task(self.__start_task(task, *args, **kwargs))
        else:
            print("\033[1K\rNot starting task: engine stopped")

    async def run_until_complete(self):
        while self.pending > 0:
            await asyncio.sleep(0.01)

    async def __run(self, driver, *args, **kwargs):
        try:
            await driver(self, *args, **kwargs)
            await self.run_until_complete()
        finally:
            await self.stop()
            if self.logger:
                await self.logger.close()

    async def __start_task(self, task, *args, **kwargs):
        try:
            await task(*args, **kwargs)
        finally:
            self.__end_task()

    def __begin_task(self):
        self.pending += 1
        self.started += 1

    def __end_task(self):
        self.pending -= 1
        self.completed += 1

    async def __monitor(self):
        while self.running():
            print("\033[1K\rTask Monitor: Started: {} : Pending: {} : Completed: {}".format(
                self.started, self.pending, self.completed), end="")
            await asyncio.sleep(0.5)
        print("\033[1K\rTask Monitor: Started: {} : Pending: {} : Completed: {}".format(
            self.started, self.pending, self.completed))
        print("TaskEngine stopped.")
        self.monitor = False
