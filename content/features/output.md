+++
title = "Output"
image = "images/features/output.png"
url = "/output"
+++

Tables & Pagers

<!--more-->

## Tabular Output

The output of an SQL query is displayed as a table. 

eg:

```
History> select * from segments limit 5;
+----+--------------------------+--------+
| id | name                     | url_id |
+----+--------------------------+--------+
| 1  | http://gmail.com/        | 401    |
| 6  | http://twitter.com/      | 256    |
| 10 | http://news.google.com/  | 24     |
| 20 | https://twitter.com/     | 444    |
+----+--------------------------+--------+
5 rows in set
Time: 0.010s
```

There are multiple table formats:

```
ascii, double, github, psql, plain, simple, grid, fancy_grid, pipe, orgtbl,
rst, mediawiki, html, latex, latex_booktabs, textile, moinmoin, jira,
```

The table format can be changed temporarily at runtime from the litecli prompt
using the `\T table_format` special command.

eg: 

```
\T fancy
```

To change the table format permanently, check your [config](/features/config) file for the `table_format` entry.

## Pager

The output of the SQL query is displayed using a pager (e.g. `less`, `more`).

### Configuring the Pager

You can choose which pager to use in the config file. Look for the `pager` option.

Once litecli is started, you can use the `pager` command to change which pager
litecli uses. Or, `nopager` will disable the pager.

```
> pager less -XRF
PAGER set to less -XRF.
> nopager
Pager disabled.
```

### Disable Paging

You can disable the pager by adding `enable_pager = False` to your litecli config
file. See [Configuration](/config) for more information.

### Pager Behavior

On macOS and Linux, the pager will default to `less` for most users. `less`
sometimes has less-than-desirable behavior like clearing the screen, cutting
lines off, etc. You can configure `less` through environment variables in your
shell configuration files. Here are some common `less` options and
configuration examples:

- `-X` leaves file contents on the screen when less exits.
- `-F` makes `less` quit if the entire output can be displayed on one
  screen.
- `-R` displays ANSI color escape sequences in "raw" form.
- `-S` disables line wrapping. Side-scroll to see long lines.
