# Sistema de Recomendación de Productos (Alicorp) 🛒

Implementación, optimización y evaluación de un sistema de recomendación de productos para los clientes de un mercado de bienes de consumo. Este sistema será de utilidad para priorizar la producción y disposición de ciertos productos sobre otros en función de las preferencias de los clientes. 

# Herramientas 🔧

* Python 
* Spotlight
* Pytorch 
* Numpy 
* Pandas
* Optuna

# Extracción de datos 🗃️

 Extraemos los datos de la fuente y los disponemos en dataframes para su posterior procesamiento. Este proceso corresponde al script _**data_wraling.ipynb**_.

# Prueba y optimización del modelo 🏁

Para el sistema de recomendación utilizamos un filtro colaborativo implementado con GPU para acelerar el entrenamiento del modelo. La métrica de evaluación será el Recall Promediado entre todos los clientes. Para una primera aproximación obtenemos un rendimiento del 74%. Esta primera aproximación puede observarse en el script _**model_baseline.ipynb**_. 

Posteriormente optimizamos los hiperparametros con el objetivo de maximizar la métrica de evaluación. Al culminar este proceso alcanzamos una calificación del 79% sobre la data de testeo. Esto puede seguirse en el script _**model_opt.ipynb**_.

# Finalización del sistema de recomendación 🛍️ 

Por último utilizando los mejores hiperparametros y usando el 90% de la data para el entrenamiento, obtenemos el modelo para usar en producción. Obteniendo un Recall promedio del 77% para 30 productos y del 84% para 50 productos con  la data de testeo. 

El entrenamiento del modelo final se realizo en el Notebook _**model_prod.ipynb**_, mientras que la prueba para el modelo de produccion se realizo en el Notebook _**predict.ipynb**_. 


