from typing import Callable

System: Callable[[str], None] = print
Silent: Callable[[str], None] = lambda v: None


class Console:
    def print(self, val: str) -> None:
        pass

    def println(self, val: str) -> None:
        pass


class SystemConsole(Console):
    def print(self, val: str) -> None:
        print(val, end='', flush=True)

    def println(self, val: str) -> None:
        print(val)


def get_console(console_type: str) -> Console:
    if console_type == 'System':
        return SystemConsole()
    elif console_type == 'Silent':
        return Console()
    else:
        raise Exception(f"Unknown console type {console_type}")
