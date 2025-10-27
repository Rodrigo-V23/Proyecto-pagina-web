# Proyecto-pagina-web
Integrantes: Rodrigo Venegas, Benjamin Iribarren

# Descripcion
La pagina realizada para este proyecto constara de un inicio donde el usuario se registrara con su nombre y su rut,
despues se le mostrara una serie de preguntas para que responda relacionado a si ha tenido algun problema de salud mental en algun momento de su vida
se le mostrara unas metricas en base a un dataset y por ultimo se le mostrara una serie de especialistas donde el podra escojer a alguno para fijar una cita 
o una actividad para aliviar su situacion actual

# Instrucciones

1.- Instalar streamlit "pip install streamlit"

2.- poner en el terminal "streamlit run app.py"

3.- interactuar con los datos entregados en la plataforma para su analisis

## Problema a Resolver
Actualmente no existen suficientes herramientas digitales simples para analizar datos de **estrés en estudiantes** y clasificarlos según factores de salud mental.  
Esto dificulta la gestión y clasificación de los casos para una **intervención temprana en situaciones de riesgo psicológico**.

## Usuarios Afectados
Estudiantes ya sea nivel estudiantes de basica, media o superior
 
## Necesidad Actual
Contar con una **plataforma que centralice la información de estrés**, la clasifique y permita una **exploración rápida** para tomar las medidas necesarias

## Objetivo Principal
Desarrollar un sistema web de análisis exploratorio que clasifique a estudiantes según niveles de estrés y factores asociados.

## Alcances y Fuera de Alcance

### Alcances
- Cargar y procesar datasets.  
- Visualizar estadísticas exploratorias (gráficos, distribuciones).  
- Clasificar estudiantes según variables de estrés y diagnóstico.  
- Consultar información de los usuarios.  

### Fuera de Alcance
- No se realizará un diagnóstico médico real, solo una clasificación de casos.  
- No se generarán predicciones.  
- No incluye historial clínico ni seguimiento a largo plazo.  

## Paradigmas de Programación

### Programación Orientada a Objetos (POO)  
Lo utilizaremos para modelar entidades como Usuarios, Pacientes,Consulta con atributos (edad, género, diagnóstico) y métodos (clasificar, mostrar estadísticas).  

### Programación Funcional  
Para operaciones matemáticas y transformar datos.

## Programacion orientada a eventos
Para que el usuario interactue con la pagina o en este caso con los datos y pueda verlos de distintas maneras

La necesidad de usar estos paradigmas se justifica con el dominio del problema, el cual requiere objetos (usuarios, diagnósticos) y, a la vez, operaciones puras sobre datos para análisis y  clasificación.

### Que puedes hacer?  

En esta plataforma se utlizo un dataset de kaggle, y con este se puede interactiar de distintas maneras

1.- se visualizan los datos en 3 tipos de graficos, estos pueden ser filtrados por genero del estudiante
o tambien por la variable que se quiera analizar 

2.- Se puede ver el dataframe utilizado en esta pagina

3.- se hace un EDA para observar el comportamiento de las variables utilizando la media, percentiles o minimos y maximos
ademas de una correlacion entre la ansiedad, depresion y estres, un analisis del bienestar general de los estudiantes por casos
y por ultimo se muestra la estadistica separada por genero.


