### Consultas básicas

**En repositories (Ejemplo: [nombre_completo] = 00-matt/moneropool)**

- SELECT is_archived FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');
- SELECT size FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');
- SELECT watchers FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');
- SELECT forks FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');
- SELECT stars FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');
- SELECT open_issues FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');

- SELECT is_archived FROM repositories WHERE lower(full_name) = lower('00-matt/moneropool');
- SELECT size FROM repositories WHERE lower(full_name) = lower('00-matt/moneropool');
- SELECT watchers FROM repositories WHERE lower(full_name) = lower('00-matt/moneropool');
- SELECT forks FROM repositories WHERE lower(full_name) = lower('00-matt/moneropool');
- SELECT stars FROM repositories WHERE lower(full_name) = lower('00-matt/moneropool');
- SELECT open_issues FROM repositories WHERE lower(full_name) = lower('00-matt/moneropool');

**En owners (Ejemplos: [propietario] = 00-matt, [tipo_propietario] = User)**

- SELECT owner_type FROM owners WHERE lower(owner) = lower('[propietario]');
- SELECT owner FROM owners WHERE lower(owner_type) = lower('[tipo_propietario]');

- SELECT owner_type FROM owners WHERE lower(owner) = lower('00-matt');
- SELECT owner FROM owners WHERE lower(owner_type) = lower('User');

**En topics (Ejemplos: [nombre_tópico] = sql, [nombre_completo] = 00-matt/moneropool)**

- SELECT full_name FROM topics WHERE lower(topic) = lower('[nombre_tópico]') ORDER BY full_name;
- SELECT topic FROM topics WHERE lower(full_name) = lower('[nombre_completo]') ORDER BY full_name;

- SELECT full_name FROM topics WHERE lower(topic) = lower('sql') ORDER BY full_name;
- SELECT topic FROM topics WHERE lower(full_name) = lower('00-matt/moneropool') ORDER BY full_name;

**En languages (Ejemplos: [nombre_lenguaje] = python, [nombre_completo] = 00-matt/moneropool)**

- SELECT full_name FROM languages WHERE lower(language) = lower('[nombre_lenguaje]') ORDER BY full_name;
- SELECT language FROM languages WHERE lower(full_name) = lower('[nombre_completo]') ORDER BY full_name;

- SELECT full_name FROM languages WHERE lower(language) = lower('python') ORDER BY full_name;
- SELECT language FROM languages WHERE lower(full_name) = lower('00-matt/moneropool') ORDER BY full_name;

**En created_by (Ejemplos: [año] = 2008, [propietario] = 00-matt, [nombre_completo] = 00-matt/moneropool)**

- SELECT full_name FROM created_by WHERE date_part('year', created_at) = [año] ORDER BY full_name;
- SELECT full_name FROM created_by WHERE lower(owner) = lower('[propietario]') ORDER BY full_name;
- SELECT created_at FROM created_by WHERE lower(full_name) = lower('[nombre_completo]') ORDER BY full_name;
- SELECT owner FROM created_by WHERE WHERE lower(full_name) = lower('[nombre_completo]') ORDER BY full_name;

- SELECT full_name FROM created_by WHERE date_part('year', created_at) = 2008 ORDER BY full_name;
- SELECT full_name FROM created_by WHERE lower(owner) = lower('00-matt') ORDER BY full_name;
- SELECT created_at FROM created_by WHERE lower(full_name) = lower('00-matt/moneropool') ORDER BY full_name;
- SELECT owner FROM created_by WHERE lower(full_name) = lower('00-matt/moneropool') ORDER BY full_name;

### Consultas específicas

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
