+++
title = "Auto-Completion"
image = "images/features/autocompletion.png"
+++

Context-sensitive completion.

<!--more-->

Auto-completion is on by default. The REPL will pop up a suggestion menu as soon as you start typing. The suggestions are context sensitive based on the position of the cursor. eg: Only tables are suggested after the FROM keyword, only column names are suggested after the WHERE clause.


### Table

Only table names from the current database are suggested after the FROM keyword.

![Table](/images/docs/table.png)

### Column

Column names from the current table are suggested after the WHERE clause.

![Column](/images/docs/column.png)

### Insert 

Insert statement will suggest the column names.

![Insert](/images/docs/insert.png)

### Alias

Aliases in the query are resolved and the columns from the table aliases are suggested.

![Alias](/images/docs/alias.png)

### Fuzzy Match

The completions are matched using a [fuzzy algorithm](http://blog.amjith.com/fuzzyfinder-in-10-lines-of-python). For example typing 'djmi' will match the table 'django_migrations' because 'djmi' has parts of matching substrings. Here's an example:

![FuzzyMatch](/images/docs/fuzzy.png)

### Auto-Suggestion

Suggest commands from the history that can be auto-completed by pressing the right arrow key (or Ctrl-F). If you have used Fish-shell you will be familiar with this feature. Here is an example:

![AutoSuggestion](/images/docs/suggestion.png)
