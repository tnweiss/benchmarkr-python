import json
import uuid
from typing import List
from time import time

from benchmarkr.test_result import TestResult
from benchmarkr.version import BENCHMARKR_VERSION


class TestResults:
    def __init__(self):
        self.__results: List[TestResult] = []
        self.__id = str(uuid.uuid4())
        self.__local_test_context = {}

        self.__failure_count = 0
        self.__success_count = 0
        self.__significant_success_count = 0

    def id(self) -> str:
        return self.__id

    def add_result(self, result: TestResult) -> None:
        self.__results.append(result)

        if result.success():
            self.__success_count += 1

            if result.significant_success():
                self.__significant_success_count += 1
        else:
            self.__failure_count += 1

    def total_tests(self) -> int:
        return len(self.__results)

    def success_count(self) -> int:
        return self.__success_count

    def significant_success_count(self) -> int:
        return self.__significant_success_count

    def failure_count(self) -> int:
        return self.__failure_count

    def __dict__(self) -> dict:
        return {
            'ID': self.__id,
            'LocalTestContext': {
                'benchmarkrVersion': BENCHMARKR_VERSION,
                'language': 'python',
                'timestamp': int(time() * 1000)
            },
            'Results': [r.__dict__() for r in self.__results]
        }

    def __repr__(self):
        return json.dumps(self.__dict__(), indent=2)
