# LOG ANALYZER

## Installation

[install uv!](https://docs.astral.sh/uv/getting-started/installation/)

Clone repository

```bash
git clone https://github.com/VEGAMETA/LOG_ANALYZER.git
cd LOG_ANALYZER
```

## Running

to get some help

```bash
uv run main.py -h
```

base syntax

```bash
uv run main.py --file <file1> [<file2> ...] --report <report_type> [--date <date>]
```

Promtp patameters
|Param|Description|
|-|-|
|-f, --file | Path to your report file(s)
|-r, --report | Report types (see below)
|-d, --date | [Optional] Date filter, format: YYYY-DD-MM|

Report types:

- average - avg response time for endpoints
- user-agent(TODO) - user-agent (TBD)

Run example

```bash
uv run main.py -f ./logs/example1.log ./logs/example2.log -r average
```
