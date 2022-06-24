### Consultas finales

**Vista materializada**

- CREATE MATERIALIZED VIEW github.usersdata AS (SELECT DISTINCT owner AS username, count(repositories.full_name) AS repositories_number, SUM(size) AS total_size, SUM(watchers) AS total_watchers, SUM(forks) AS total_forks, SUM(stars) AS total_stars, SUM(open_issues) AS total_open_issues FROM created_by, repositories WHERE created_by.full_name = repositories.full_name GROUP BY owner);

**Buscar por owner el resumen de su actividad en github**

- SELECT * FROM usersdata WHERE username = '[owner]';

**Muestra los repositorios junto con todos los lenguajes utilizados y tópicos asociados**

- SELECT DISTINCT repositories.full_name, string_agg( DISTINCT topics.topic, ', ' ORDER BY topics.topic) AS topics, string_agg(DISTINCT languages.language, ', ' ORDER BY languages.language) AS languages FROM repositories, languages, topics WHERE repositories.full_name = languages.full_name AND repositories.full_name = topics.full_name GROUP BY repositories.full_name; (nuevo)

**Entrega ordena fecha (más nuevo a más antiguo) el número de repositorios subidos a la plataforma**

- SELECT date_part('year', created_at) AS year, count(created_by.full_name) AS repositories_number FROM created_by GROUP BY date_part('year', created_at) ORDER BY date_part('year', created_at) DESC;

### Consultas básicas

**En repositories (Ejemplo: [nombre_completo] = 00-matt/moneropool)**

- SELECT full_name, is_archived FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');
- SELECT full_name, size FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');
- SELECT full_name, watchers FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');
- SELECT full_name, forks FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');
- SELECT full_name, stars FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');
- SELECT full_name, open_issues FROM repositories WHERE lower(full_name) = lower('[nombre_completo]');

**En owners (Ejemplos: [propietario] = 00-matt, [tipo_propietario] = User)**

- SELECT owner, owner_type FROM owners WHERE lower(owner) = lower('[propietario]');
- SELECT owner, owner_type FROM owners WHERE lower(owner_type) = lower('[tipo_propietario]') ORDER BY owner;

**En topics (Ejemplos: [nombre_tópico] = sql, [nombre_completo] = 00-matt/moneropool)**

- SELECT full_name, topic FROM topics WHERE lower(topic) = lower('[nombre_tópico]') ORDER BY full_name;
- SELECT topic, full_name FROM topics WHERE lower(full_name) = lower('[nombre_completo]') ORDER BY topic;

**En languages (Ejemplos: [nombre_lenguaje] = python, [nombre_completo] = 00-matt/moneropool)**

- SELECT full_name, language FROM languages WHERE lower(language) = lower('[nombre_lenguaje]') ORDER BY full_name;
- SELECT language, full_name FROM languages WHERE lower(full_name) = lower('[nombre_completo]') ORDER BY language;

**En created_by (Ejemplos: [año] = 2008, [propietario] = 00-matt, [nombre_completo] = 00-matt/moneropool)**

- SELECT created_at, full_name FROM created_by WHERE date_part('year', created_at) = [año] ORDER BY created_at;
- SELECT created_at, full_name FROM created_by WHERE date_part('year', created_at) <= [año] AND date_part('year', created_at) >= [año] ORDER BY created_at;
- SELECT full_name, owner FROM created_by WHERE lower(owner) = lower('[propietario]') ORDER BY full_name;
- SELECT full_name, created_at FROM created_by WHERE lower(full_name) = lower('[nombre_completo]');
- SELECT full_name, owner FROM created_by WHERE lower(full_name) = lower('[nombre_completo]');

### Consultas específicas

**Todos los tópicos referenciados en la plataforma (resultados ordenados alfabéticamente).**
- SELECT DISTINCT topic FROM topics ORDER BY topic;

**Todos los lenguajes utilizados en la plataforma (resultados ordenados alfabéticamente).**
- SELECT DISTINCT language FROM languages ORDER BY language;

**Todos los propietarios + nombre de sus repositorios (resultados ordenados por el nombre de su propietario).
ESTO FUNCIONA, PERO ES LO MISMO QUE LA TABLA NORMAL PERO ORDENADA :c**
- SELECT DISTINCT c1.owner, c1.full_name FROM created_by c1, created_by c2 WHERE c1.full_name <> c2.full_name AND c1.owner = c2.owner ORDER BY c1.owner;

**Todos los propietarios + cantidad de repositorios a su nombre (resultados ordenados de mayor a menor).**
- SELECT DISTINCT owner, count(owner) FROM created_by GROUP BY owner ORDER BY count(owner) DESC;

**Repositorios + fechas de creación (resultados ordenados desde el más antiguo al más nuevo).**
- SELECT created_at, full_name FROM created_by ORDER BY created_at;

**Número de repositorios que fueron creados el mismo día + fecha de creación (resultados ordenados desde el más antiguo al más nuevo).**
- SELECT created_at, count(full_name) FROM created_by GROUP BY created_at ORDER BY created_at;
**Repositorios creados el primer año registrado de la plataforma.**
- SELECT DISTINCT owner, created_at FROM created_by WHERE date_part('year', created_at) = (SELECT min(date_part('year', created_at)) FROM created_by) ORDER BY owner;

**Repositorios creados el último año registrado de la plataforma.**
- SELECT DISTINCT owner, created_at FROM created_by WHERE date_part('year', created_at) = (SELECT max(date_part('year', created_at)) FROM created_by) ORDER BY owner;

**Número de repositorios creados en un año en específico (Ejemplos: [año] = 2008).**
- SELECT date_part('year', created_at), count(full_name) FROM created_by WHERE date_part('year', created_at) = [año] GROUP BY date_part('year', created_at);

**Número de repositorios creados por año.**
- SELECT date_part('year', created_at), count(full_name) FROM created_by GROUP BY date_part('year', created_at) ORDER BY date_part('year', created_at) DESC;
