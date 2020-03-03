# data-product-architecture-Project
Final project of Data product architecture class

# Análisis de las estaciones de metro de CDMX según su afluencia diaria

La base de datos a analizar concentra información sobre la alfuencia diaria en las estaciones del sistema de transporte colectivo Metro en la ciudad de México. Su frecuencia de actualización es mensual y los datos se encuentran detallados a nivel diario. Las columnas que componen la base son las siguientes:

- Fecha
- Día
- Mes
- Año
- Línea
- Estación
- Afluencia

## Fuente de datos

La base de datos a analizar se encuentra disponible [aquí](https://datos.cdmx.gob.mx/explore/dataset/afluencia-diaria-del-metro-cdmx/table/?sort=-fecha)

En esta base encontraremos información de tráfico diario en las líneas y estaciones de metro desde enero 2010 hasta octubre 2019.

Consumiremos este conjunto de datos a través de una API que permite buscar y descargar registros con diversos criterios.

## Pregunta a responder

**Aqui nos dijo que estamos siendo solamente descriptivos, pensemos bien las preguntas**

**la pregunta que quedó tentativa sería:** ¿Se puede optimizar el tiempo de llegada de los trenes mediante la predicción de la afluencia que tendrá cierta estación durante el día para mejorar la distribución de los trenes y como consecuencia mejorar el servicio del metro?

* ¿Cuales estaciones son las que presentan mayor afluencia?
* analisis de donde se tiene mas necesidad de contruir nuevas estaciones de metro
* Como optimizar el tiempo de espera en cada estacion con base a los flujos de personas 
* ¿Qué líneas necesitan mayor mantenimiento?

* ¿En qué líneas hay mayor tráfico de usuarios?

## ¿A quien va dirigido?

* Gobierno
	Para cuestiones de mejoras, modernizaciones y recursos utilizados dependiendo del uso de las líneas y estaciones.
		Por ejemplo: ¿En qué estaciones se necesitan más policias?
					 ¿Que lineas necesitan mayor presupuesto de mantenimiento?
					 ¿A que líneas asignar mayor número de trenes?



* Particulares

	Venta estratificada de espacios publicitarios dependiendo del flujo diario de personas.
    Colocación de comercios por estaciones.
	Investigación de mercados para estratificación de consumidores.

## ETL

**ETL MOCKUP (High-level)**
![ETL MOCKUP](https://1fykyq3mdn5r21tpna3wkdyi-wpengine.netdna-ssl.com/wp-content/uploads/2019/10/image1.png)

**ETL MOCKUP 2 (with details of technology to be used)**
![ETL-MOCKUP-2](https://1fykyq3mdn5r21tpna3wkdyi-wpengine.netdna-ssl.com/wp-content/uploads/2019/10/image9.png)

Acrónimo de Extract Transform Load, no siempre se ejecutan en este orden, por ejemplo es posible tener un ELT, o solo partes del proceso como EL.

La ingesta de datos se llevará a cabo mediante la API de la Afluencia diaria del metro de la CDMX. Debido a la pequeña cantidad de columnas del Data Set, se realizará la ingesta de datos ingresandolo en un _bucket S3_ en AWS con **Parquet**, debido a que tiene varias ventajas que nos servirán para optimizar la extracción de los datos:

![visulaizacion de API de Metro](https://raw.githubusercontent.com/valencig/data-product-architecture-Project/master/images/metroAPI.png)


* Las categorías de la mayoría de las columnas (excepto la que muestra la afluencia de personas) pueden ser reducidas de una forma muy eficiente, por lo que un formato columnar podría ser mejor.

Los datos son publicados de manera Mensual, por lo que la ingesta se realizaría de la misma manera.

Debido a que nuestros datos parecen estar más o menos estandarizados en cuanto a algunas categorías, no sería necesario realizar transformaciones de limpieza al momento de ingestarlos a la base de datos.

La ingesta de datos desde la API de afluencia diaria en estaciones de metro, se realizará usando el servicio _Amazon Kinesis Data Firehose_ que ofrece una solución de carga de datos de streaming de manera fiable en lagos de datos, almacenes de datos y herramientas de análisis. De esta manera, ingestaremos, transformaremos y cargaremos los datos en Amazon S3 por medio de la lectura de archivos JSON.

El proceso de ETL se realizará en una máquina pública, mientras que el procesamiento de la información y el modelo se implementarán en redes privadas con acceso limitado a grupos de usuarios. De la misma forma, los resultados del modelo se almacenarán en una máquina privada. 

-------------------------------------------------------


La parte de transfomración está asociada a los cambios que se les tienen que hacer a estos datos para que después puedan ser ocupados por otros (aplicaciones, servicios, scripts, otras personas, etc.). Estas transformaciones están más relacionadas a transformaciones de tipos de datos, formatos, estructura; que a transformción de datos para la parte de modelado.

Finalmente la parte de cargado está relacionada a tener los datos ordenados y estructurados en algún lugar para que todos los demás los puedan ocupar, generalmente esta parte está asociada a alamcenar los datos en bases de datos, sin embargo, en productos de datos pueden estar asociados a DataLakes, bases de datos no estructuradas, servicios de almacenamiento en la nube, servidios de DFS, etc.

Cuando estos 3 procesos ocurren en secuencia de forma automatizada se genera un pipeline, aunque todo el mundo le decimos ETL.

Tenemos los datos de la línea de petición de servicios del 311 de Chicago.

Nuestro producto estará asociado a poder priorizar los lugares que requerirán de inspección por alguna violación al codigo sanitario en propiedad privada (Garbage and recycling).

¿Con qué frecuencia se publican los datos?
¿Cada cuánto ingestaremos los datos?
¿Cómo ingestaremos los datos?
¿Dónde guardaremos los datos?
¿En qué formato?
¿Los transformamos antes de guardarlos?
AWS a través de Python
Boto3
Es la librería de Python que nos permite interactuar de manera programática con AWS, es decir, podemos crear scripts de python que nos permitan conectarnos a diferentes servicios de AWS.

Para instalar boto hay que ocupar pip pip install boto3, recuerda instalarlo en tu ambiente de la clase!! (pyenv).

Para poder acceder de forma programática a AWS requeriremos también de tener un IAM user de AWS y roles o permisos asociados a este usuario, estos roles estará determinados por los servicios a los que accederemos a través de boto. Por ejemplo, si almacenarás los datos de tu ingestión en un bucket de S3, entonces tendrás que darle acceso a tu usuario IAM al permiso AmazonS3FullAccess.

Configuración

Para ocupar boto3 necesitarás tener tu archivo de .aws/credentials en donde tengas los aws_access_key_id y aws_secret_access_key asociados a tu usuario IAM.

En boto hay 2 tipos de objetos base: client y resource. El objeto client nos permite tener un acceso de más bajo nivel y su interaccion es casi siempre a través de diccionarios o jsons. El objeto resource es de más alto nivel y por lo tanto más sencillo de interactuar con él, sin embargo muchas operaciones básicas son más sencillas de hacer a través del objeto client.

En nuestro caso ocuparemos el objeto resource para las interacciones más generales con el bucket y luego ocuparemos cliente para gestionar el contenido del bucket. Para tener un client a partir de un resource se necesita acceder a los metadatos: resource_object.meta.client.metodo_de_elección.

## Análisis

## Entregable

Dashboard desarrollado en Dash que tendrá las siguientes secciones:

- Top 10 estaciones con respecto a su tráfico anual
- Análisis de estacionalidad
- Análisis de afluencia diaria

![visulaizacion de API de Metro](https://raw.githubusercontent.com/valencig/data-product-architecture-Project/master/images/dashboard_mockup.png)

Otros proyectos similares:
https://www.kaggle.com/dashaa/a-geospatial-analysis-of-the-nyc-subway-in-r  

https://www.kaggle.com/thiagodsd/sao-paulo-metro/kernels  

https://www.kaggle.com/bigshane/simple-visualization-for-xgb  

https://www.kaggle.com/ramyahr/metro-interstate-traffic-volume  






