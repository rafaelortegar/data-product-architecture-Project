# Pasos del algoritmo:
* Extraer datos de la API del metro (linea 22)
* Extracción y carga de metadatos del extract (línea 63)
* CopyToPostgres para cargar los datos en una instancia RDS (línea 154)
* Metadatos de CopyToPostgres (Metadata_load) (línea 210)
* Create_clean_schema (linea 334)
* Metadatos de la creación del clean schema (Rafa) (línea 462)
* Create Semantic Schema (línea 472)
* Metadatos de la creación del schema semantic (Rafa) (línea 653)

############# ############## ############## ############## ############


* SeparaBase (línea 664) (Javi)
* CreaCategorias (Alfie)
* FeatureEngineering & imputación (Javi)
* Definicion de modelo (probabilidad con cada una de las etiquetas) y guardar en un pickle (Javi propone)
* Metadatos Modelado (Mario)
* Predicción Final (predict con test set) y calcular el error (Alfie)
* Metadatos Predicción Final (Mario)
* Revisión de métricas  no meter 
* run_all (Rafa)

* dash

- -[ ] Metadata modelado
- -[ ] Modelado
- -[ ] Metadata Prueba Unitaria de Feature Engineering  --> prueba unitaria, booleano de si pasó o no, cuando se corrió
- -[ ] Prueba Unitaria Feature Engineering 
- -[ ] Metadata Feature Engineering
- -[ ] Feature Engineering
- -[ ] Metadata Prueba Unitaria Clean Task   --> prueba unitaria, booleano de si pasó o no, cuando se corrió
- -[ ] Prueba Unitaria Clean Task
- -[ ] Metadata Clean Task
- -[x] Clean Task
- -[ ] Metadata de la Prueba Unitaria Load  --> prueba unitaria, booleano de si pasó o no, cuando se corrió
- -[ ] Prueba unitaria Load
- -[x] Metadata Load
- -[x] Load Task
- -[ ] Metadata de la Prueba Unitaria Extract  --> prueba unitaria, booleano de si pasó o no, cuando se corrió
- -[ ] Prueba unitaria Extract
- -[x] Metadata Extract
- -[x] Extract Task