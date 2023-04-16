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
SELECT COUNT(*) FROM regions
/*2. Afficher tous les pays>>>>>> 25 rows*/
SELECT * FROM countries;
SELECT COUNT(* FROM countries;)
/*3. Afficher uniquement les noms des pays>>>>>> 25 rows*/
SELECT country_name FROM countries;
SELECT COUNT(country_name) FROM countries;
/*4. Afficher les noms des pays et des régions correspondantes>>>>>>>>> 25 rows*/
SELECT countries.country_name, regions.region_name FROM countries, regions WHERE countries.region_id = regions.region_id;
SELECT COUNT(countries.country_name, regions.region_name FROM) countries, regions WHERE countries.region_id = regions.region_id;


/*5. Afficher les localisations (toutes les colonnes sauf les id), avec leur pays et régions associés*/
SELECT country_name, region_name, street_address, postal_code, city, state_province
FROM (countries INNER JOIN regions ON countries.region_id = regions.region_id)
	INNER JOIN locations ON ( locations.country_id = countries.country_id);

/*6. Afficher les jobs des employés ainsi que leur information >>>>>> 107 rows*/
SELECT employees.first_name, employees.last_name, jobs.job_tittle, jobs.min_salary, jobs.max_salary
FROM employees
JOIN jobs
ON employees.job_id = jobs.job_id;

/*7. Afficher les employés avec leur information ainsi que leur région associée*/

SELECT employees.first_name, employees.last_name, employees.email, employees.phone_number, employees.hire_date, employees.salary, regions.region_name
FROM employees 
	INNER JOIN departments ON employees.department_id = departments.department_id
		INNER JOIN locations ON departments.location_id = locations.location_id
			INNER JOIN countries ON locations.country_id = countries.country_id
				INNER JOIN regions ON countries.region_id = regions.region_id;



/*7. Afficher les employés avec leur information ainsi que leur région associée*/

SELECT employees.first_name, employees.last_name, employees.email, employees.phone_number, employees.hire_date, employees.salary, regions.region_name
FROM employees 
	INNER JOIN departments ON employees.department_id = departments.department_id
		INNER JOIN locations ON departments.location_id = locations.location_id
			INNER JOIN countries ON locations.country_id = countries.country_id
				INNER JOIN regions ON countries.region_id = regions.region_id;
	
		
/*8. Afficher les employés avec leur historique de travail*/
SELECT employees.first_name, employees.last_name, job_history.start_date, job_history.end_date
FROM employees
	INNER JOIN job_history ON employees.employee_id = job_history.employee_id;

/*9. Afficher l’employé avec le salaire le plus bas*/
SELECT employees.first_name, employees.last_name, employees.salary
FROM employees
	WHERE salary = (SELECT MIN(salary) FROM employees);

/*10. Afficher l’employé avec le salaire le plus haut*/
SELECT employees.first_name, employees.last_name, employees.salary
FROM employees
	WHERE salary = (SELECT MAX(salary) FROM employees);

/*11. Afficher les jobs qui ne sont attribué à aucun salarié*/
SELECT jobs.job_tittle
	FROM jobs
		LEFT JOIN employees ON jobs.job_id = employees.job_id
			WHERE employees.employee_id IS NULL;
			
/*12. Afficher les jobs qui sont attribués aux salariés*/
SELECT jobs.job_tittle
	FROM jobs
		LEFT JOIN employees ON jobs.job_id = employees.job_id
			WHERE employees.employee_id IS NOT NULL;

/*13. Afficher tous les salariés qui n’ont pas de manager*/
SELECT employees.first_name, employees.last_name
	FROM employees
		WHERE manager_id IS NULL;

/*14. Afficher le nombre salarié ayant le manager avec l’id 100*/
SELECT COUNT (employees.first_name, employees.last_name)
	FROM employees
		WHERE manager_id ;
/*15. Afficher l’id du manager ainsi que le nombre de salarié qu’il gère pour chaque id*/
/*16. Afficher les localisations et les pays */
/*17. Afficher la liste des employés embauchés entre le 17/06/03 et le 21/09/05*/
/*18. Afficher tous les employés embauchés à partir de l’année 2007*/
/*19. Afficher tous les employés embauchés le 21 de chaque mois*/
/*20. Afficher tous les employés même ceux qui n’ont pas de job*/
/*21. Afficher les employés dans le prénom commence par ‘A’ */
/*22. Afficher les employés avec leur région associés ayant un salaire supérieur à la moyenne*/
/*23. Afficher les employés ayant travaillé dans un même département au moins 2 fois*/

