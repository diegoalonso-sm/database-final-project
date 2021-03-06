### Ingreso a la máquina virtual
ssh -l cc3201 -p 316 cc3201.dcc.uchile.cl

### Credenciales
- Hostname: cc3201.dcc.uchile.cl
- Usuario: cc3201, Port: 316
- Contraseña: eesogh7Rah9f

### Datos utilizados:
https://www.kaggle.com/datasets/joonasyoon/github-topics

### Ejemplos de proyectos:
https://aidanhogan.com/teaching/cc3201-1-2021/projects/play.html

### Etapas del proyecto

**1. Seleccionar Datos (terminado)** 
   
   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:seleccionar_datos
   
   - Seleccionar las tablas a usar (terminado)
   - Modificar para tener 3 tablas y BCNF (terminado)
   - Debe contar con al menos 10000 tuplas (terminado)
   
   https://www.kaggle.com/datasets/joonasyoon/github-topics (datos usados)

**2. Acceso al Servidor (terminado)**

   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:acceso_al_servidor
   
   **Copiar archivos**
   - scp -P 316 local.txt cc3201@cc3201.dcc.uchile.cl:/home/cc3201/ (computador al servidor)
   - scp -P 316 cc3201@cc3201.dcc.uchile.cl:/home/cc3201/remote.txt /local/carpeta/ (servidor al computador)

   **Descargar archivos en la máquina virtual**
   - wget https://github.com/diegoalonso-sm/database-final-project/tree/main/data/Normalized

**3. Configurar Postgres (terminado)**

   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:configurar_postgres
   
   - Crear usuario cc3201 (terminado)
   - Crear base de datos (terminado)
   - Crear esquema GitHub (terminado)
   - Configurar searchpath (terminado)

**4. Cargar los datos (terminado)**

   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:cargar_los_datos
   
   - Subir las tablas normalizadas en formato CSV (terminado) 
   - Finalizar el diseño relacional con llaves y restricciones (terminado)
   - Limpiar, normalizar y cargar los datos en la base de datos (terminado)
   - Escribir al menos 10 consultas base para la aplicación (terminado)

**5. Optimización (en proceso)**

   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:optimizacion

   - Definir índices adecuados para trabajar (en proceso)
   - Crear al menos una vista (virtual o materializada) (terminado)

**6. Conexión Externa (terminado)**

   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:conexion_externa

**7. Armar La Aplicación (terminado)**
  
   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:armar_la_aplicacion_inicial

**8. Entregas y Evaluación (terminado)**
  
   https://wiki.dcc.uchile.cl/cc3201/doku.php?id=proyecto:entregar_presentacione
