from json import dumps
from typing import Optional
from uuid import uuid4


class TestResult:
    def __init__(self, test_name: str, timestamp: int, duration: int, lower_bound: Optional[int] = None,
                 upper_bound: Optional[int] = None, description: Optional[str] = None,
                 custom_properties: Optional[dict] = None, outcome: Optional[str] = None):
        self._timestamp = timestamp
        self._test_id = str(uuid4())
        self._lower_bound: Optional[int] = lower_bound
        self._upper_bound: Optional[int] = upper_bound
        self._description: Optional[str] = description
        self._duration: Optional[int] = duration
        self._custom_properties: Optional[dict] = custom_properties
        self._test_name: str = test_name
        self._outcome = outcome

        self._success = (lower_bound is None) or (duration < upper_bound)

        if upper_bound is None:
            self._significant_success = None
            self._performance_delta = None
        else:
            self._significant_success = duration < upper_bound
            self._performance_delta = 0 - ((float(duration) - float(upper_bound)) / float(upper_bound))

    def test_id(self) -> str:
        return self._test_id

    def duration(self) -> int:
        return self._duration

    def success(self) -> bool:
        return self._success

    def significant_success(self) -> bool:
        return self._significant_success

    def __dict__(self) -> dict:
        return {
            'Timestamp': self._timestamp,
            'TestID': self._test_id,
            'TestName': self._test_name,
            'CustomProperties': self._custom_properties,
            'LowerBound': self._lower_bound,
            'UpperBound': self._upper_bound,
            'PerformanceDelta': self._performance_delta,
            'Duration': self._duration,
            'Success': self._success,
            'SignificantSuccess': self._significant_success
        }

    def __repr__(self):
        return dumps(self.__dict__(), indent=2)
