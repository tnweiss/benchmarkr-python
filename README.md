![](images/BenchmarkrCPP.svg)

## Overview

Set standards for your software. 

This repository provides a benchmarking framework for the C++ language. Set standards, track progress, and aggregate 
results in an ELK stack.

The goal of this project is to track **relative performance**, not absolute performance. No two runs, even on the same machine,
will yield the same results. This project attempts to highlight significant trends and major anomalies by allowing 
developers to constantly benchmark their software.

The screenshot below shows the default dashboard that comes with this project. It provides basic information about
which tests have outperformed expectations and which have underperformed.

![](images/BenchmarkrDashboard.PNG)

The line graph, in the screenshot above, becomes more useful when you filter on a single test. In the screenshot below
we filtered by `TestName : NormalizeDataTest` and this is what our line graph looked like...

![](images/BenchmarkrDashboardLineGraph.PNG)

And then our table, gave us some insight into individual results that could then be further filtered and organized.

![](images/BenchmarkrDashboardTable.PNG)

## Related Benchmarkr Projects

- [Benchmarkr C++](https://github.com/tnweiss/Benchmarkr-cpp) -
  Benchmarkr client for c++
- [Benchmarkr Jetbrains Plugin](https://github.com/tnweiss/benchmarkr-jetbrains-plugin) -
  Jetbrains plugin for Intellij and CLION that makes it easier to run individual tests from the gutter
- [Benchmarkr Configuration](https://github.com/tnweiss/benchmarkr-configuration) -
  Centralized configuration for elastic dashboards and indices
- [Benchmarkr Java](https://github.com/tnweiss/benchmarkr-java) -
  Java libraries for benchmarkr
- [Benchmarkr Maven Plugin](https://github.com/tnweiss/benchmarkr-java-maven-plugin) -
  Benchmarkr plugin for maven
- [Benchmarkr Gradle Plugin](https://github.com/tnweiss/benchmarkr-java-gradle-plugin) -
  Benchmarkr plugin for gradle

## Installation

Clone the repository

```bash
git clone https://github.com/tnweiss/benchmarkr-python
```

Install the client

```bash
python setup.py install --user
```

## Usage

Create a simple test `test_benchmark.py`

```python
from benchmarkr.benchmarkr import benchmark


@benchmark()
def my_first_benchmark():
    pass

```

Test this benchmark by running ...

```bash
python -m benchmarkr
```

You can supply more metadata to the test ...

```python
from benchmarkr.benchmarkr import benchmark


@benchmark(
  lower_bound_s=1,
  upper_bound_s=2,
  test_name="test",
  custom_properties={
    "hello": "world"
  },
  description="A test that holds code accountable"
)
def my_first_benchmark():
    pass

```
