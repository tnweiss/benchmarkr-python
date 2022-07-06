import json
from typing import Optional
from time import time

from benchmarkr.test_result import TestResult


class Test:
    def __init__(self, func: callable, test_name: Optional[str] = None, lower_bound: Optional[int] = None,
                 upper_bound: Optional[int] = None, description: Optional[str] = None,
                 custom_properties: Optional[dict] = None):
        self._func: callable = func
        self._lower_bound: Optional[int] = lower_bound
        self._upper_bound: Optional[int] = upper_bound
        self._description: Optional[str] = description
        self._custom_properties: Optional[dict] = custom_properties

        if test_name is not None:
            self._test_name: str = test_name
        else:
            self._test_name: str = f'{func.__module__}.{func.__name__}'

        self._module = func.__module__
        self._function = func.__name__

    def test_name(self) -> str:
        return self._test_name

    def lower_bound(self) -> int:
        return self._lower_bound

    def upper_bound(self) -> int:
        return self._upper_bound

    def matches(self, package_name: str, module_name: str, function_name: str) -> bool:
        return (module_name == '' or f'{package_name}.{module_name}' == self._module) and \
               (function_name == '' or self._function == self._function)

    def run(self) -> TestResult:
        duration: Optional[int] = None
        outcome = None
        start = time()

        try:
            self._func()
            duration = int((time() - start) * 1000000)
        except Exception as ex:
            outcome = ex.__cause__

        return TestResult(
            self._test_name,
            int(start * 1000000),
            duration,
            outcome=outcome,
            lower_bound=self._lower_bound,
            upper_bound=self._upper_bound,
            description=self._description,
            custom_properties=self._custom_properties
        )

    def __repr__(self):
        return json.dumps({
            'lower_bound': self._lower_bound,
            'upper_bound': self._upper_bound,
            'description': self._description,
            'custom_properties': self._custom_properties,
            'test_name': self._test_name
        })
