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

La ingesta de datos se llevará a cabo mediante la API de la **Afluencia diaria del metro de la CDMX**. Debido a la pequeña cantidad de columnas del Data Set, se realizará la ingesta de datos ingresandolo en un _bucket_ en AWS con **Parquet**, debido a que tiene varias ventajas que nos servirán para optimizar la extracción de los datos, como lo es la velocidad y la compresión en comparación con _Avro_.

![visulaizacion de API de Metro](https://raw.githubusercontent.com/valencig/data-product-architecture-Project/master/images/metroAPI.png)


* Las categorías de la mayoría de las columnas (excepto la que muestra la afluencia de personas) pueden ser reducidas de una forma muy eficiente, por lo que un formato columnar podría ser mejor.

Los datos son publicados de manera **Mensual**, por lo que la ingesta se realizaría de la misma manera.

Debido a que nuestros datos parecen estar más o menos estandarizados en cuanto a algunas categorías, no sería necesario realizar transformaciones de limpieza al momento de ingestarlos a la base de datos.

**Compresión**

Para la parte de compresión se tomaron en cuenta las herramientas vistas en clase; de las cuales se piensa que para el proyecto las que mejor se adecuarían sería **Snappy** o **GZ**. Aunque no sean _spittables_, se utilizará _parquet_ como ya se había mencionado, lo cual resuelve esa característica para ambas. Dependiendo de la compresión que se necesite en el proyecto se decantará por una u otra o opción.  


-------------------------------------------------------


La parte de **transformación** está asociada a los cambios que se les tienen que hacer a estos datos para que después puedan ser ocupados por otros (aplicaciones, servicios, scripts, otras personas, etc.). Estas transformaciones están más relacionadas a transformaciones de tipos de datos, formatos, estructura; que a transformción de datos para la parte de modelado.

Finalmente, la parte de **cargado** está relacionada a tener los datos ordenados y estructurados en algún lugar para que todos los demás los puedan ocupar, generalmente esta parte está asociada a alamcenar los datos en bases de datos, sin embargo, en productos de datos pueden estar asociados a DataLakes, bases de datos no estructuradas, servicios de almacenamiento en la nube, servidios de DFS, etc.

Cuando estos 3 procesos ocurren en secuencia de forma automatizada se genera un _pipeline_, aunque todo el mundo le decimos ETL.

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

Dashboard desarrollado en Dash que tendrá las siguientes secciones:

- Top 10 estaciones con respecto a su tráfico anual
- Análisis de estacionalidad
- Análisis de afluencia diaria

### Entrega 3 de marzo

- Set de datos que están ocupando
Para el proyecto se utilizará la base de datos de la **afluencia diaria del metro CDMX**. El cual es un data set con los datos agregados por estación de la afluencia diaria del metro de la Ciudad de México. El histórico de datos es desde enero de 2010.
https://datos.cdmx.gob.mx/explore/dataset/afluencia-diaria-del-metro-cdmx/table/?sort=-fecha
- Pregunta de Ciencia de Datos que quieren contestar (predictiva)


Queremos predecir la saturación diaria en estaciones de metro (vs la media/mediana de afluencia mensual) a partir de las siguientes variables: 
    - Mes 
    - Día de la semana 
    - Línea 
    - Estación


- Frecuencia de actualización del dataset original
Mensualmente

- Breve resúmen de qué implica su producto de datos

El producto de datos está dirigido principalmente para los diirectivos encargados de la movilidad de la ciudad. El producto ayudaría al STC a mejorar la administración de los recursos en cuanto a la mejora de sus gastos. El conocer qué días y en qué horarios existe una mayor demanda del servicio puede ayudar a enfocar los esfuerzos de los trabajadores para mejorar el servicio. 

Además de la creación de presupuestos con base en los pronósticos de entradas y número de usuarios para prevenir pérdidas por usuarios que no pagan un boleto.

https://www.excelsior.com.mx/comunidad/hasta-un-millon-de-usuarios-no-pagan-en-el-metro/1353684

Igualmente, en el tema de venta de espacios publicitarios, para realizar discriminación de precios por las temporadas para mejorar el ingreso en ese rubro.

Pero sería de gran ayuda para los usuarios del sistema al momento de planear sus viajes.

- Capa de interacción con el usuario/cliente/partner: Dashboard, App, API, etc. Mostrar el diseño mockup que ya hicieron.

https://github.com/valencig/data-product-architecture-Project

- Cada cuándo emitirán una recomendación/predicción
Debido a que la actualización de los datos es de forma mensual, las recomendaciónes se podrían dar en el mismo tiempo. Para que se conociera el estimado de afluencia diaria durante un mes determinado. 

### Lista de implicaciones éticas de su producto
En cuanto a implicaciones éticas del producto no identificamos alguna importante ya que los datos que estamos usando son publicos y no tienen información personal o sensible. Solo tendríamos que preocuparnos de que la información mostrada sea precisa para que los tomadores de decisiones no tomen una decisión equivocada que impacte a personas de manera negativa. 

Pensamos durante un largo timepo como podría usarse para hacer daño esta información y lo único que identificamos fue que **podría usarse para planear un atentado terrorista**.    

Se está utilizando un algoritmo de balanceo y se corré el riesgo de enviar demasiada gente a una estación y satuararla.

  [Major ethical issues in conducting research:](http://www.hsj.gr/medicine/what-are-the-major-ethical-issues-in-conducting-research-is-there-a-conflict-between-the-research-ethics-and-the-nature-of-nursing.php?aid=3485)
  Informed consent, Beneficence- Do not harm, Respect for anonymity and confidentiality, Respect for privacy, Vulnerable groups of people. 
 
  
  [Data ethics is concerned with the following principles:](https://en.wikipedia.org/wiki/Big_data_ethics)

- [x]**Ownership** - Individuals own their own data.
- [x]**Transaction transparency** - If an individuals personal data is used, they should have transparent access to the algorithm design used to generate aggregate data sets
- [x]**Consent** - If an individual or legal entity would like to use personal data, one needs informed and explicitly expressed consent of what personal data moves to whom, when, and for what purpose from the owner of the data.
- [x]**Privacy** - If data transactions occur all reasonable effort needs to be made to preserve privacy.
- [x]**Currency** - Individuals should be aware of financial transactions resulting from the use of their personal data and the scale of these transactions.
- [x]**Openness** - Aggregate data sets should be freely available
  
- Diseño de su DataPipeline a como lo tienen hasta este momento (arquitectura)

**Data Pipeline**

![Pipeline](https://raw.githubusercontent.com/valencig/data-product-architecture-Project/master/images/pipeline_metro.png)

A falta de determinar si es necesario la utilización de herramientas como Spark para el manejo de los datos; puesto que, la base de datos no es muy grande se ha realizado un pipeline general sin especificar las herramientas específicas a utilizar.

Para la parte de la visualización de los resultados se evaluaron las opciones de Powerbi, Tableau o un servicio web (Flask).   

 **Mockup visualizacion informacion**
 
Aquí un ejemplo cómo luciría una visualización de afluencia utilizando PorwerBi.
 
 ![Imagen dashboard-PowerBI](https://raw.githubusercontent.com/valencig/data-product-architecture-Project/master/images/metro.png)

## Data governance

Tiene la función de diseñar y garantizar los estándares que asuguren el flujo de información constante y calidad a través de los sistemas y fuentes de la empresa.

El gobierno de datos conforma una unidad que funciona de forma coordinada para aumentar la eficiencia en el uso y gestión de la información.

El gobierno de datos se ocupa:

- Cumplir los objetivos relacionados con los datos de la empresa.

- Gestión y administración de los datos como un activo estratégico de la organización.

- Cumplimiento eficiente a reducir costos.

- Planificar, establecer procesos, desarrollos y supervisar la gestión de datos para un uso óptimo.

- Encontrar la tecnología adecuada para cubrir las distintas necesidades.

### Metadata
-  Raw
    - Día/mes/año de acceso
    - Hora de acceso
    - Cuenta de quien accede (usuario)
    - Lugar de acceso (ip, instancia EC2)
    - Nombre del archivo generado
    - Nombres de la bases de datos
    - Tipos de datos
    - Variables
    - Tipo de Archivos

- Preprocessed
    - Día/mes/año de acceso
    - Hora de acceso
    - Cuenta de quien accede (usuario)
    - Lugar de acceso (ip, instancia EC2)
    - Nombre del archivo generado
    - Nombres de la bases de datos
    - Tipos de datos
    - Variables
    - Tipo de Archivos
    - Modificaciones a variables
    - Número de modificaciones
    - Estatus de ejecución: fallido, exitoso, etc.

- Clean
    - Día/mes/año de acceso
    - Hora de acceso
    - Cuenta de quien accede (usuario)
    - Lugar de acceso (ip, instancia EC2)
    - Nombre del archivo generado
    - Nombres de la bases de datos
    - Tipos de datos
    - Variables
    - Tipo de Archivos
    - Modificaciones a variables
    - Número de modificaciones
    - Estatus de ejecución: fallido, exitoso, etc.


### Linaje de datos

El linaje de datos es sumamente importante debido a que los datos durante el proceso de análisis son transformados en repetidas ocasiones. Lo cual crea una especie de telefono descompuesto, los datos originales no se parecen a los finales y puede crear confusión. Para evitar eso está el linaje de datos que le da confiabilidad a los datos a través de las diversas transformaciones que se realicen.

Describe el origen, movimientos, características y calidad de los datos. Dónde comienza cada dato y cómo se transforma hasta llegar a resultados en distintos proyectos empresariales.

### Bias and Fairness

La variable estación podría estar sujeta a sesgo. Para poder estimarlo podría agregarse al conjunto de datos la geolocalización de las estaciones, información con la cual se podría identificar la distribución de nivel socioeconómico que más frecuenta cada estación.

Seleccionamos una variable protegida:  Afluencianivel que es la variable que que clasifica las estaciones de metro con base en la prediccion del nivel de afluencia, esta variable es protegida porque no queremos que discrimine las estaciones donde hay mas usuarios de grupos etnicos marginales, o de algun nivel socio economico en especifico. 
Un ejemplo, es que con base en la predicción de la Afluencia de la estación se van a distribuir los recursos del metro, que son finitos,
si el modelo tiene un sesgo en estaciones en las cuales la mayoria de los usuarios son de clase media o alta podría tener un efecto punitivo en estaciones con ususarios de un nivel socio economico bajo.

La métrica que nos interesa usar es la siguiente False Positive Parity, la razon es que las decisiones realizadas con base en la predicción SI son punitivas y NO estamos interviniendo en un porcentaje bajo de la población. 
Nos equivocamos en la misma proporción en la clasificación del nivel de afluencia en las estaciones con usuarios de un nivel socio economico alto y bajo por ejemplo.

 ![BiasandFairnessTree](http://www.datasciencepublicpolicy.org//wp-content/uploads/2018/05/metrictree-1200x750.png)
tomado de la pagina de Aequitas

**Otros proyectos similares:**

https://www.kaggle.com/dashaa/a-geospatial-analysis-of-the-nyc-subway-in-r  

https://www.kaggle.com/thiagodsd/sao-paulo-metro/kernels  

https://www.kaggle.com/bigshane/simple-visualization-for-xgb  

https://www.kaggle.com/ramyahr/metro-interstate-traffic-volume  


**Referencias**

https://blog.powerdata.es/el-valor-de-la-gestion-de-datos/bid/243575/data-governance-el-gobierno-de-la-gesti-n-de-datos

https://blog.powerdata.es/el-valor-de-la-gestion-de-datos/entendiendo-lo-que-es-data-lineage






