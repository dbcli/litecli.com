+++
title = "Output"
image = "images/features/output.png"
+++

Tables & Pagers

<!--more-->

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
