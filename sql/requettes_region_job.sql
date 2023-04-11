SELECT first_name, job_tittle FROM employees JOIN jobs ON employees.job_id = jobs.job_id;
SELECT COUNT(*) FROM departments ;
SELECT MIN(min_salary) FROM jobs ;
SELECT MAX(max_salary) FROM jobs ;
SELECT AVG((min_salary + max_salary) / 2) AS avg_salary FROM jobs;

--Trier les résultats par une colonne particulière
--SELECT <column_name>,<column_name_2>,… FROM <table> ORDER BY <column_name> ASC
--ASC permet de trier dans l’ordre croissant
--SELECT <column_name>,<column_name_2>,… FROM <table> ORDER BY <column_name> DESC
--DESC permet de trier dans l’ordre décroissant