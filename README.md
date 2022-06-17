**1. Seleccionar Datos**
   
   - Seleccionar las tablas a usar
   - Modificar para tener 3 tablas y BCNF
   - Debe contar con al menos 10000 tuplas

   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:seleccionar_datos
   https://www.kaggle.com/datasets/joonasyoon/github-topics (datos usados)

**2. Acceso al Servidor**
   
   ##### Credenciales: ssh -l cc3201 -p 316 cc3201.dcc.uchile.cl; eesogh7Rah9f (password) 
   
   ##### Copiar archivos
   - scp -P 316 local.txt cc3201@cc3201.dcc.uchile.cl:/home/cc3201/ (computador al servidor)
   - scp -P 316 cc3201@cc3201.dcc.uchile.cl:/home/cc3201/remote.txt /local/carpeta/ (servidor al computador)

   ###### Descargar archivos en la máquina virtual
   - wget https://github.com/diegoalonsosm/CC3201/blob/main/repositories.csv
   - wget https://github.com/diegoalonsosm/CC3201/blob/main/topics.csv

   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:acceso_al_servidor

**3. Configurar Postgres**
   
   - Crear usuario cc3201 (listo)
   - Crear base de datos (listo)
   - Crear esquema github (listo)
   - Configurar searchpath (listo)

   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:configurar_postgres

**4. Cargar los datos**

   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:cargar_los_datos

**5. Optimización**

   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:optimizacion

**6. Conexión Externa**

   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:conexion_externa

**7. Armar La Aplicación**
  
   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:armar_la_aplicacion_inicial

**8. Entregas y Evaluación**
  
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
