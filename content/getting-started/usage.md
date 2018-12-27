+++
title = "Usage"
image = "images/getting-started/usage.png"
url = "/usage"
+++

Launch litecli.

<!--more-->

```
$ litecli --help
Usage: litecli [OPTIONS] [DATABASE]

  A SQLite terminal client with auto-completion and syntax highlighting.

  Examples:
     litecli sqlite_db_name

Options:
  -V, --version           Output litecli's version.
  -D, --database TEXT     Database to use.
  -R, --prompt TEXT       Prompt format (Default: "\d> ").
  -l, --logfile FILENAME  Log every query and its results to a file.
  --liteclirc FILE        Location of liteclirc file.
  --auto-vertical-output  Automatically switch to vertical output mode if the
                          result is wider than the terminal width.
  -t, --table             Display batch output in table format.
  --csv                   Display batch output in CSV format.
  --warn / --no-warn      Warn before running a destructive query.
  -e, --execute TEXT      Execute command and quit.
  --help                  Show this message and exit.
```
