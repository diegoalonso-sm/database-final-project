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

**Todos los propietarios + nombre de sus repositorios (resultados ordenados por el nombre de su propietario).**
- SELECT DISTINCT c1.owner, c1.full_name FROM created_by c1, created_by c2 WHERE c1.full_name <> c2.full_name AND c1.owner = c2.owner ORDER BY c1.owner;

**Todos los propietarios + cantidad de repositorios a su nombre (resultados ordenados de mayor a menor).**
- SELECT DISTINCT owner, count(owner) FROM created_by GROUP BY owner ORDER BY count(owner) DESC;

**Persona con máximo número de repositorios en la plataforma. IDEA: CREAR UNA VISTA.**

**Repositorios + fechas de creación (resultados ordenados desde el más antiguo al más nuevo).**
- SELECT created_at, full_name FROM created_by ORDER BY created_at;

**Número de repositorios que fueron creados el mismo día + fecha de creación (resultados ordenados desde el más antiguo al más nuevo).**
- SELECT created_at, count(full_name) FROM created_by GROUP BY created_at ORDER BY created_at;

**Intervalo entre el repositorio más antiguo y el más nuevo. IDEA: CREAR VISTA.**

**Repositorios creados el primer año registrado de la plataforma.**
- SELECT DISTINCT owner, created_at FROM created_by WHERE date_part('year', created_at) = (SELECT min(date_part('year', created_at)) FROM created_by) ORDER BY owner;

**Repositorios creados el último año registrado de la plataforma.**
- SELECT DISTINCT owner, created_at FROM created_by WHERE date_part('year', created_at) = (SELECT max(date_part('year', created_at)) FROM created_by) ORDER BY owner;

**Número de repositorios creados en un año en específico (Ejemplos: [año] = 2008).**
- SELECT date_part('year', created_at), count(full_name) FROM created_by WHERE date_part('year', created_at) = [año] GROUP BY date_part('year', created_at);

**Número de repositorios creados por año.**
- SELECT date_part('year', created_at), count(full_name) FROM created_by GROUP BY date_part('year', created_at) ORDER BY date_part('year', created_at) DESC;

**Años de actividad de propietarios. CREAR VISTA.**

**¡AGREGAR CONSULTAS ESPECIFICAS PARA REPOSITORIES!**
