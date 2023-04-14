/*test et bidouille*/

SELECT first_name, job_tittle FROM employees JOIN jobs ON employees.job_id = jobs.job_id;
SELECT COUNT(*) FROM departments ;
SELECT MIN(min_salary) FROM jobs ;
SELECT MAX(max_salary) FROM jobs ;
SELECT AVG((min_salary + max_salary) / 2) AS avg_salary FROM jobs;
SELECT postal_code, city FROM locations ORDER BY postal_code ASC;
SELECT * FROM employees ORDER BY last_name DESC;

/*TP3 

Partie TP – Indiquer le nombre de ligne obtenus avec la requête utilisée*/


/*1. Afficher toutes les régions>>>>>> 4 rows*/ 
SELECT * FROM regions;
/*2. Afficher tous les pays>>>>>> 25 rows*/
SELECT * FROM countries;
/*3. Afficher uniquement les noms des pays>>>>>> 25 rows*/
SELECT country_name FROM countries;