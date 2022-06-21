SELECT full_name FROM languages WHERE lower(language) = lower('[nombre_lenguaje]') ORDER BY full_name;
SELECT full_name FROM topics WHERE lower(topic) = lower('[nombre_tópico]') ORDER BY full_name;
SELECT full_name FROM created_by WHERE date_part('year', created_at) = [año] ORDER BY full_name;
SELECT full_name FROM created_by WHERE lower(owner) = lower('[propietario]') ORDER BY full_name;

**Consultas básicas en repositories (Ejemplo: [nombre_completo] = 00-matt/moneropool)**
- SELECT is_archived FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');
- SELECT size FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');
- SELECT watchers FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');
- SELECT forks FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');
- SELECT stars FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');
- SELECT open_issues FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');

**Consultas básicas en owners (Ejemplo: [nombre_completo] = 00-matt/moneropool)**
- SELECT owner_type FROM owners WHERE lower(owner) = lower('[propietario]');

**Consultas básicas en topics (Ejemplo: [nombre_completo] = 00-matt/moneropool)**
**Consultas básicas en languages (Ejemplo: [nombre_completo] = 00-matt/moneropool)**
**Consultas básicas en created_by (Ejemplo: [nombre_completo] = 00-matt/moneropool)**

1) Todos los tópicos referenciados en la plataforma (resultados ordenados alfabéticamente).
SELECT DISTINCT topic FROM topics ORDER BY topic;

2) Encontrar repositorios usando un tópico (resultados ordenados alfabéticamente).
SELECT full_name FROM topicos WHERE string(topic) = sint([]) ORDER BY full_name;

2) Todos los lenguajes utilizados en la plataforma (resultados ordenados alfabéticamente).
SELECT DISTINCT language FROM languages ORDER BY language;

3) Todos los propietarios + nombre de sus repositorios (resultados ordenados por el nombre de su propietario).
SELECT DISTINCT c1.owner, c1.full_name FROM created_by c1, created_by c2 WHERE c1.full_name <> c2.full_name AND c1.owner = c2.owner ORDER BY c1.owner;

4) Todos los propietarios + cantidad de repositorios a su nombre (resultados ordenados de mayor a menor).
SELECT DISTINCT owner, count(owner) FROM created_by GROUP BY owner ORDER BY count(owner) DESC;

5) Persona con máximo número de repositorios en la plataforma. CREAR UNA VISTA.

6) Repositorios + fechas de creación (resultados ordenados desde el más antiguo al más nuevo).
SELECT created_at, full_name FROM created_by ORDER BY created_at;

7) Propietario de repositorio + primer repositorio creado + último repositorio creado (resultados ordenados por el nombre de su propietario).

8) Número de repositorios que fueron creados el mismo día + fecha de creación (resultados ordenados desde el más antiguo al más nuevo).
SELECT count(full_name), created_at FROM created_by GROUP BY created_at ORDER BY created_at;

9) Intervalo entre el repositorio más antiguo y el más nuevo. CREAR VISTA.

10) Número de repositorios creados el primer año de la plataforma.
SELECT DISTINCT owner FROM created_by WHERE date_part('year', created_at) = (SELECT min(date_part('year', created_at)) FROM created_by) ORDER BY owner;

11) Número de repositorios creados el año = ''.
SELECT DISTINCT owner FROM created_by WHERE date_part('year', created_at) = ORDER BY owner;

12) Años de actividad de propietarios. CREAR VISTA.

13) Número de repositorios creados por año.
SELECT date_part('year', created_at) AS year, count(full_name) AS repositories_number FROM created_by GROUP BY date_part('year', created_at) ORDER BY year DESC;
