### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?  
    **PostgreSQL is an open source relational database system.**


- What is the difference between SQL and PostgreSQL?  
    **SQL or Structured Query Language, is a language used to communicate with databases. It is the standard language used in relational databases. PostgreSQL is relational database system relies on SQL as it's query language.**


- In `psql`, how do you connect to a database?  
    **To connect to a database in psql in the terminal you would use the following command:**

    **`\c database_name`**


- What is the difference between `HAVING` and `WHERE`?  
    **The `WHERE` clause is used to filer records based on a condition. The `HAVING` clause will filter data based on defined criteria and works with `GROUP BY`. The `WHERE` clause cannot be used with aggregate functions.**

- What is the difference between an `INNER` and `OUTER` join?  
    **`INNER` joins will combine two tables with only the records that overlap in both tables. A full `OUTER` join combines two tables for all records whether the records relate to the other table or not. And a left or right `OUTER` join will include all the records of the respective table and only the overlapping records from the other table.**


- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?  
  **A `LEFT OUTER` join includes all the records of the first table and from the second table only the records that relate to first. A `RIGHT OUTER` is just the opposite, all the records from the second table and just the records that relate the second from the first.**


- What is an ORM? What do they do?  
  **An ORM is an __Object-Relational-Mapper__ and they are frameworks for building objects that can deliver SQL to a database with out having to actually write the SQL. A popular ORM for Python/Flask is SQLAlchemy.**

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?  
  **Client Side requests using AJAX are rendered in the browser and they can retrieve files and data without reloading the page. Client side calls can also perform DOM operations.**  
  **Server Side requests using a library like `requests`, will cause the page to reload and won't perform DOM operations in the browser.**


- What is CSRF? What is the purpose of the CSRF token?  
    **Cross-Site Request Forgery is an attack that forces a user to submitted post request to malicious parties disguised as a trusted web application. A CSRF token is an authentication token designed to prevent this by ensuring web applications only accept requests that return tokens they have first issued**


- What is the purpose of `form.hidden_tag()`?  
    **In WTForms, the `form.hidden_tag()` contains the CSRF token in the value of a hidden input. This token is need for the form to be validated on the server with the validate_on_submit() function.**
