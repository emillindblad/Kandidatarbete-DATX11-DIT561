# SQL-Injection

> Emil Lindblad

## What is a SQL-Injection?

SQL-Injection (SQLi) is a vulnerability that allows a user to perform queries to a database in ways not intended by the developer. SQLi can be used to modify
or access data that the end user is not supposed to have access to, such as credentials for other users.

## Solving the challenge
This challenge was solved "by hand", ie not using any scripts or tools that can automate SQLi.

### Initial observations

This challenge drops you into a very basic webpage, containing a simple form with a single input. Based on the data returned, the database contains data about
fruits. The search returns data divided into 3 columns:

|Fruit|Price|Current stock|
|----|-----|--------|


The first step is to figure out if the website is vulnerable to SQLi, this can be done by trying to break the underlying query that runs on the backend.
After trying to search for different fruits we can imagine the query might look something like this:

```sql
SELECT ?,?,? FROM ? WHERE ? LIKE '%{input}%';
```

Since we receive 3 columns, we can assume that 3 unknown items are selected from some unknown table.
If we input something like `pple` we still get back `Apple` and `Pineapple`, meaning that the query uses wildcards around the input, resulting in
partial searches being possible, this is denoted by the `%` in the query above. We cant change anything about the query except what we put in the promt, which
corresponds to `{input}`.

### Breaking the query
Submitting a single `'` results in a server error. This is because the resulting query is not valid SQL and the server throws an error. Receiving
this type of server error usually means that the server directly takes the user input and adds it to the query, leaving it vulnerable to SQLi. A non-vulnerable
server would instead say something like: `There are no products with name '`

Knowing that the webpage is vulnerable and we have broken the query, we can start manipulating it with the end goal of making the server return data from
another table. Firstly we have to "repair" our now broken query. This is achieved with terminating the rest of the query after our own input.

Submitting `';--` will result in the query looking like:

```sql
SELECT ?,?,? FROM ? WHERE ? LIKE '%';--'%';
```

Looking on the syntax highlighting in the codeblock above, everything after `;` is now commented out and we have a valid query. Since `%` is a wildcard, the
query will return everything from the table.

### Appending data
We can now start appending data to our results using `UNION` which takes two
tables with the same amount of columns and puts them directly after each other.

We can do ` Pear' UNION SELECT 1,2,3 ;-- `
To append a new row with 1,2,3 to our search results:

|Fruit|Price|Current stock|
|----|-----|--------|
|1|2|3|
|Pear|84.86|26|

### Table of tables

The goal is to extract data from another table, so how do you know which tables are present in the database? In most database
management systems (MySQL, PostgresSQL, SQLite etc) there exists a "schema table" which contains information about all other tables.
In SQlite we can query this table with:

```sql
Pear' UNION SELECT 1,name,sql FROM sqlite_schema ;--
```
This is will give us the names of each table and the SQL query that was used to create it, which also shows each column name.

We can now select our perfered columns from the users table and we have gained acess to user information and credentials.

```sql
Pear' UNION SELECT email,password, name FROM user ;--
```
