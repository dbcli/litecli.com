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

The output 
