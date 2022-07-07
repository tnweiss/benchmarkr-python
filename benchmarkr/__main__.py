import argparse

from benchmarkr.benchmarkr import execute


parser = argparse.ArgumentParser(description="Run Benchmarkr Tests")
parser.add_argument('directory', default='.', type=str, nargs='?')
parser.add_argument('--package-name', default=None, help='Name of the package to search for tests in', type=str)
parser.add_argument('--module-name', default='', help='Name of the module to search for tests in', type=str)
parser.add_argument('--method-name', default='', help='Name of the method to run', type=str)
parser.add_argument('--iterations', default=1, help='Number of times to run each test', type=int)
parser.add_argument('--console', default='System', help="The console type ('System', 'Silent')", type=str)
parser.add_argument('--record', default='True', help='Whether or not to record the results', type=str)
parser.add_argument('--ignore-failures', default=False, help='ignore failed tests', action='store_true')


if __name__ == '__main__':
    args = parser.parse_args()

    execute(
        directory=args.directory,
        package_name=args.package_name,
        module_name=args.module_name,
        method_name=args.method_name,
        iterations=args.iterations,
        console_type=args.console,
        record=bool(args.record),
        fail=args.ignore_failures
    )
