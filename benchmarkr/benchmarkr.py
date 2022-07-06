import importlib
import platform
import os
import re
import sys
import uuid
from datetime import datetime
from typing import List, Optional

from benchmarkr.test import Test
from benchmarkr.test_results import TestResults
from benchmarkr.consoles import get_console


tests: List[Test] = []
python_file_regex = re.compile("(.*)\\.py")

LINUX_DATA_DIR = '/etc/benchmarkr'
WINDOWS_DATA_DIR = 'C:\\ProgramData\\Benchmarkr'


def output_file(test_id: str):
    sub_path = ['results', f'{datetime.now().strftime("%Y%m%d%H%M%f")}.{test_id}']

    return os.path.join(
        WINDOWS_DATA_DIR if platform.system() == 'Windows' else LINUX_DATA_DIR,
        *sub_path)


def in_us(s: Optional[int], ms: Optional[int], us: Optional[int]) -> Optional[int]:
    if s is not None:
        return s * 1000000
    elif ms is not None:
        return ms * 1000
    elif us is not None:
        return us
    return None


def benchmark(lower_bound_s: Optional[int] = None, lower_bound_ms: Optional[int] = None,
              lower_bound_us: Optional[int] = None, upper_bound_s: Optional[int] = None,
              upper_bound_ms: Optional[int] = None, upper_bound_us: Optional[int] = None,
              custom_properties: Optional[dict] = None, description: Optional[str] = None,
              test_name: Optional[str] = None):
    def inner(f):
        tests.append(
            Test(f,
                 lower_bound=in_us(lower_bound_s, lower_bound_ms, lower_bound_us),
                 upper_bound=in_us(upper_bound_s, upper_bound_ms, upper_bound_us),
                 description=description,
                 test_name=test_name,
                 custom_properties=custom_properties)
        )

    return inner


def valid_file(filename: str, module_name: str) -> bool:
    return filename.endswith('.py') and filename != '__init__.py' and \
        (module_name == '' or filename == module_name + '.py')


def execute(directory: str = '.', package_name: str = '', module_name: str = '', method_name: str = '',
            iterations: int = 1, console_type: str = 'System', record: bool = True, fail: bool = False) -> None:

    sys.path.append(directory)

    for root, sub_folders, files in os.walk(os.path.join(directory, package_name)):
        files[:] = [f for f in files if valid_file(f, module_name)]

        for file in files:
            file_name = f'.{python_file_regex.match(file).group(1)}'
            print(file_name)
            importlib.import_module(file_name, package_name)

    console = get_console(console_type)

    console.println(f"\n\n\n{40 * '#'} {20 * '#'} {20 * '#'} {20 * '#'}")
    console.println("{:40s} {:20s} {:20s} {:20s}".format("Test Name", "Lower Bound", "Upper Bound", "Duration"))
    console.println(f"{40 * '#'} {20 * '#'} {20 * '#'} {20 * '#'}")

    test_results: TestResults = TestResults()
    for i in range(0, iterations):
        for test in [t for t in tests if t.matches(package_name, module_name, method_name)]:
            # print test name and expectations
            console.print("{:40s} {:<20n} {:<20n} ".format(test.test_name(), test.lower_bound(), test.upper_bound()))
            test_result = test.run()
            console.println("{:<20n}".format(test_result.duration()))
            test_results.add_result(test_result)

    console.println(f"\n\n{30 * '#'}")
    console.println(f"Test Results")
    console.println(f"{30 * '#'}")

    console.println(f"Success:             {test_results.success_count()}/{test_results.total_tests()}")
    console.println(f"Significant Success: {test_results.significant_success_count()}/{test_results.total_tests()}")
    console.println(f"Failures:            {test_results.failure_count()}/{test_results.total_tests()}\n\n")

    if record:
        with open(output_file(test_results.id()), 'w') as f:
            f.write(str(test_results))

    if fail and test_results.failure_count() > 0:
        exit(1)
