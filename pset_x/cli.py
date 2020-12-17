import random
import time
import argparse
import json
import sys
import os

from .task_engine import TaskEngine
from .log_event import LogEvent
from .es_logger import ElasticLogger


parser = argparse.ArgumentParser(description="Command description.")
parser.add_argument("command", choices=[
                    "generate", "init", "query", "delete", "show"])
parser.add_argument("--timestamp", type=str, default="todayT?:?:?")
parser.add_argument("--count", type=int, default="1")

random.seed(time.time())


def main(args):

    args = parser.parse_args(args)
    num_events = args.count
    ts_mask = LogEvent.ParseTimestampMask(args.timestamp)

    async def non_blocking_logger(engine):
        print("\033[1K\rGenerating {} log events in {}".format(
            num_events, os.getenv("ELASTIC_INDEX")))
        while engine.started < num_events:
            event = LogEvent.random_event(ts_mask)
            await engine.start_task(event.log, engine.logger)

    async def init_logger(engine):
        await engine.start_task(engine.logger.init_schema)

    async def query_logger(engine):
        # The query json is read from standard in
        # This can be piped in the command line
        query = json.load(sys.stdin)
        await engine.start_task(engine.logger.query, query)

    async def delete_index(engine):
        await engine.start_task(engine.logger.delete_index)

    async def show_index(engine):
        await engine.start_task(engine.logger.get_schema)

    engine = TaskEngine(monitor=True, logger=ElasticLogger(LogEvent.schema))

    if args.command == 'generate':

        engine.run(non_blocking_logger)
        print("{} log events generated".format(LogEvent.logged))

    elif args.command == 'init':

        engine.run(init_logger)
        print("Schema generated")

    elif args.command == 'query':

        engine.run(query_logger)
        print("Query finished")

    elif args.command == 'delete':

        engine.run(delete_index)
        print("Index deleted")

    elif args.command == 'show':

        engine.run(show_index)
