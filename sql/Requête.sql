ALTER TABLE locations
rename COLUMN stree_address to street_address;

/*5. Afficher les localisations (toutes les colonnes sauf les id), avec leur pays et régions associés*/
SELECT country_name, region_name, street_address, postal_code, city, state_province
FROM (countries INNER JOIN regions ON countries.region_id = regions.region_id)
	INNER JOIN locations ON ( locations.country_id = countries.country_id);


/*6. Afficher les jobs des employés ainsi que leur information >>>>>> 107 rows*/
/*SELECT employees.first_name, employees.last_name, jobs.*
FROM employees
JOIN jobs
ON employees.job_id = jobs.job_id;
SELECT count(employees.first_name, employees.last_name, jobs.*)
FROM employees
JOIN jobs
ON employees.job_id = jobs.job_id;

/*7. Afficher les employés avec leur information ainsi que leur région associée*/
/*8. Afficher les employés avec leur historique de travail*/
/*9. Afficher l’employé avec le salaire le plus bas*/
/*10. Afficher l’employé avec le salaire le plus haut*/
/*11. Afficher les jobs qui ne sont attribué à aucun salarié*/
/*12. Afficher les jobs qui sont attribués aux salariés*/
/*13. Afficher tous les salariés qui n’ont pas de manager*/
/*14. Afficher le nombre salarié ayant le manager avec l’id 100*/
/*15. Afficher l’id du manager ainsi que le nombre de salarié qu’il gère pour chaque id*/
/*16. Afficher les localisations et les pays */
/*17. Afficher la liste des employés embauchés entre le 17/06/03 et le 21/09/05*/
/*18. Afficher tous les employés embauchés à partir de l’année 2007*/
/*19. Afficher tous les employés embauchés le 21 de chaque mois*/
/*20. Afficher tous les employés même ceux qui n’ont pas de job*/
/*21. Afficher les employés dans le prénom commence par ‘A’ */
/*22. Afficher les employés avec leur région associés ayant un salaire supérieur à la moyenne*/
/*23. Afficher les employés ayant travaillé dans un même département au moins 2 fois*/



