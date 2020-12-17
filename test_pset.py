#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for 'pset_x' package."""

from datetime import datetime
from unittest import TestCase
from elastic_logger.task_engine import TaskEngine


class MockLogger:
    logged = 0
    events = []

    async def __call__(self, event, silent=False):
        self.logged += 1
        self.events.append(event)

    async def close(self):
        pass


class MockEvent:
    logged = 0

    def __init__(self, i):
        self.i = i

    async def log(self, logger, silent=True):
        await logger(self.__dict__, silent=silent)
        MockEvent.logged += 1


async def mock_task(engine):
    for i in range(0, 10):
        event = MockEvent(i)
        await engine.start_task(event.log, engine.logger)


class ElasticLoggerTests(TestCase):

    def test_task_engine(self):
        logger = MockLogger()
        engine = TaskEngine(monitor=False, logger=logger)
        engine.run(mock_task)
        assert engine.started == 10
        assert engine.pending == 0
        assert engine.completed == 10
        assert engine.stopped
        assert MockEvent.logged == 10
        assert logger.logged == 10
