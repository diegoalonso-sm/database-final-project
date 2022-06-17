### Plazos y acciones:

**1. Seleccionar Datos (plazo hasta: 29 de abril)**
   
   - Seleccionar las tablas a usar
   - Modificar para tener 3 tablas y BCNF
   - Debe contar con al menos 10000 tuplas

   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:seleccionar_datos

**2. Acceso al Servidor (plazo hasta: 4 de mayo)**
   
   ##### Credenciales: ssh -l cc3201 -p 316 cc3201.dcc.uchile.cl; eesogh7Rah9f (password) 
   
   ##### Copiar archivos
   - scp -P 316 local.txt cc3201@cc3201.dcc.uchile.cl:/home/cc3201/ (computador al servidor)
   - scp -P 316 cc3201@cc3201.dcc.uchile.cl:/home/cc3201/remote.txt /local/carpeta/ (servidor al computador)

   ###### Descargar archivos en la máquina virtual
   - wget https://github.com/diegoalonsosm/CC3201/blob/main/repositories.csv
   - wget https://github.com/diegoalonsosm/CC3201/blob/main/topics.csv

   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:acceso_al_servidor

**3. Configurar Postgres (plazo hasta: 6 de mayo)**
   
   - Crear usuario cc3201 (listo)
   - Crear base de datos (listo)
   - Crear esquema github (listo)
   - Configurar searchpath (listo)

   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:configurar_postgres

**4. Cargar Los Datos (plazo hasta: 13 de mayo)**

   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:cargar_los_datos

**5. Optimización (plazo hasta: 25 de mayo)**

   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:optimizacion

**6. Conexión Externa (plazo hasta: 27 de mayo)**

   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:conexion_externa

**7. Armar La Aplicación (plazo hasta: 10 de junio)**
  
   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:armar_la_aplicacion_inicial

**8. Entregas y Evaluación (plazo hasta: 16 de junio)**
  
   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:entregar_presentacione

##### Datos utilizados:
https://www.kaggle.com/datasets/joonasyoon/github-topics

##### Ejemplos de proyectos:
https://aidanhogan.com/teaching/cc3201-1-2021/projects/play.html

##### Credenciales
- Hostname: cc3201.dcc.uchile.cl
- Usuario: cc3201, Port: 316
- Contraseña: eesogh7Rah9f

##### Ingreso a la base de datos
ssh -l cc3201 -p 316 cc3201.dcc.uchile.cl
