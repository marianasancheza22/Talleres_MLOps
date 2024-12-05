# -*- coding: utf-8 -*-
"""Taller_2_MLops_Sanchez

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wvmwyvDPZWMeSbDwP2u8Vi9tPj5CmuM4

Elija un dataset de la siguiente lista y aplique la metodología CRISP-DM:
https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset

Entendimiento del negocio

Objetivo de negocio: El objetivo principal es desarrollar un modelo que prediga si un paciente tiene un alto riesgo de sufrir un ataque cardíaco.

Objetivo analítico: El objetivo analítico es construir un modelo predictivo que clasifique correctamente si un paciente tiene un alto riesgo de ataque cardíaco basado en variables clínicas como edad, presión arterial, colesterol, y otras medidas biométricas.
"""

import kagglehub

# Download latest version
path = kagglehub.dataset_download("rashikrahmanpritom/heart-attack-analysis-prediction-dataset")

print("Path to dataset files:", path)

pip install kaggle

# Importar librerías necesarias
import pandas as pd

# Rutas de los archivos en Google Drive
heart_file = "/content/heart.csv"
o2saturation_file = "/content/heart.csv"

# Cargar los archivos Excel
heart_df = pd.read_csv(heart_file)
o2saturation_df = pd.read_csv(o2saturation_file)

# Visualizar las primeras filas de cada dataset
print("Primeras filas del dataset 'Heart':")
print(heart_df.head())

print("\nPrimeras filas del dataset 'O2 Saturation':")
print(o2saturation_df.head())

# Información del dataset Heart
print("\nInformación del dataset 'Heart':")
print(heart_df.info())

# Resumen estadístico del dataset Heart
print("\nResumen estadístico del dataset 'Heart':")
print(heart_df.describe())

# Información del dataset O2 Saturation
print("\nInformación del dataset 'O2 Saturation':")
print(o2saturation_df.info())

# Resumen estadístico del dataset O2 Saturation
print("\nResumen estadístico del dataset 'O2 Saturation':")
print(o2saturation_df.describe())

# Entendimiento de los datos: distribuciones y valores faltantes

# Importar librerías necesarias
import seaborn as sns
import matplotlib.pyplot as plt

# Revisar valores faltantes
print("Valores faltantes en Heart:")
print(heart_df.isnull().sum())

print("\nValores faltantes en O2 Saturation:")
print(o2saturation_df.isnull().sum())

# Histograma para cada columna numérica en Heart
heart_df.hist(bins=20, figsize=(15, 10), color='skyblue')
plt.suptitle("Distribuciones - Dataset Heart")
plt.show()

# Histograma para cada columna numérica en O2 Saturation
o2saturation_df.hist(bins=20, figsize=(15, 10), color='orange')
plt.suptitle("Distribuciones - Dataset O2 Saturation")
plt.show()

# Entendimiento de los datos: Boxplots para identificar outliers

# Boxplots para las columnas numéricas en Heart
for column in heart_df.select_dtypes(include=['float64', 'int64']).columns:
    sns.boxplot(data=heart_df, x=column, color='lightblue')
    plt.title(f"Boxplot - {column}")
    plt.show()

# Boxplots para las columnas numéricas en O2 Saturation
for column in o2saturation_df.select_dtypes(include=['float64', 'int64']).columns:
    sns.boxplot(data=o2saturation_df, x=column, color='orange')
    plt.title(f"Boxplot - {column}")
    plt.show()

# Entendimiento de los datos: Análisis bivariante - Correlación y Heatmap

# Heatmap de correlación para Heart
plt.figure(figsize=(12, 8))
sns.heatmap(heart_df.corr(), annot=True, cmap='coolwarm')
plt.title("Matriz de Correlación - Dataset Heart")
plt.show()

# Heatmap de correlación para O2 Saturation
plt.figure(figsize=(12, 8))
sns.heatmap(o2saturation_df.corr(), annot=True, cmap='coolwarm')
plt.title("Matriz de Correlación - Dataset O2 Saturation")
plt.show()

# Entendimiento de los datos: Análisis bivariante - Relación entre variables clave

# Relación entre edad y ataque cardíaco
sns.boxplot(data=heart_df, x='output', y='age', palette='Set2')
plt.title("Relación entre Edad y Ataque Cardíaco (Output)")
plt.xlabel("Ataque Cardíaco (0=No, 1=Sí)")
plt.ylabel("Edad")
plt.show()

# Relación entre colesterol y frecuencia cardíaca máxima
sns.scatterplot(data=heart_df, x='chol', y='thalachh', hue='output', palette='cool')
plt.title("Relación entre Colesterol y Frecuencia Cardíaca Máxima")
plt.xlabel("Colesterol")
plt.ylabel("Frecuencia Cardíaca Máxima")
plt.legend(title="Output")
plt.show()

# Entendimiento de los datos: Normalización/Estandarización

from sklearn.preprocessing import StandardScaler

# Escalado para el dataset Heart
scaler = StandardScaler()
numerical_cols = heart_df.select_dtypes(include=['float64', 'int64']).columns
heart_df_scaled = heart_df.copy()
heart_df_scaled[numerical_cols] = scaler.fit_transform(heart_df[numerical_cols])

print("Primeras filas del dataset Heart escalado:")
print(heart_df_scaled.head())

# 3. Preparación de los datos: Transformaciones para variables de entrada - Manejo de valores faltantes

# Verificar valores faltantes
print("Valores faltantes en el dataset Heart:")
print(heart_df.isnull().sum())

# Imputar valores faltantes con la media (si aplica)
heart_df.fillna(heart_df.mean(), inplace=True)

# Confirmar que no hay valores faltantes
print("Valores faltantes después de la imputación:")
print(heart_df.isnull().sum())

# 3. Preparación de los datos: Transformaciones para variables de entrada - Codificación de variables categóricas
# Transformar variables categóricas en numéricas utilizando métodos como One-Hot Encoding o Label Encoding.

# Supongamos que 'cp' (tipo de dolor en el pecho) es categórica
heart_df = pd.get_dummies(heart_df, columns=['cp'], drop_first=True)

# Confirmar las columnas nuevas
print("Nuevas columnas después de One-Hot Encoding:")
print(heart_df.head())

# 3. Preparación de los datos: Transformaciones para variables de entrada - Escalado de variables numéricas
# Escalar o normalizar las variables numéricas para asegurar que estén en la misma escala.

from sklearn.preprocessing import StandardScaler

# Escalado de variables numéricas
numerical_cols = heart_df.select_dtypes(include=['float64', 'int64']).columns
scaler = StandardScaler()
heart_df[numerical_cols] = scaler.fit_transform(heart_df[numerical_cols])

# Verificar datos escalados
print("Primeras filas después del escalado:")
print(heart_df.head())

# 3. Preparación de los datos: Transformaciones para la variable de salida - Verificar la variable objetivo
# Supongamos que la variable objetivo es output en el dataset heart.

# Verificar valores únicos en la variable objetivo
print("Valores únicos en la variable 'output':")
print(heart_df['output'].unique())

# Asegurar que sea numérica (si no, convertirla)
heart_df['output'] = heart_df['output'].astype(int)

# 3. Preparación de los datos: Transformaciones para la variable de salida - Transformación binaria (si aplica)
# Si estás trabajando en un problema binario, la variable objetivo debe tener solo dos valores (0 y 1).

# Verificar que solo hay dos clases
assert len(heart_df['output'].unique()) == 2, "La variable objetivo debe ser binaria"

"""4. Modelación: Se aplicarán 5 modelos de Machine Learning, incluido uno de ensamble (como Random Forest), y se realizará una búsqueda de hiperparámetros para optimizar el rendimiento de los modelos. Además, PyCaret se puede usar para simplificar y automatizar gran parte del proceso."""

# Importar librerías
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# 4. Modelación: Dividir los datos en entrenamiento y prueba

# Definir variables de entrada y salida
X = heart_df.drop(columns=['output'])  # Características
y = heart_df['output']  # Variable objetivo

# Dividir los datos en entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Verifica la forma de los datos
print(f"Datos de entrenamiento: {X_train.shape}")
print(f"Datos de prueba: {X_test.shape}")

# 4. Modelación: Definir los modelos de Machine Learning

# Modelos que vamos a utilizar
models = {
    "Logistic Regression": LogisticRegression(),
    "SVM": SVC(),
    "Random Forest": RandomForestClassifier(),
    "K-Nearest Neighbors": KNeighborsClassifier(),
    "Decision Tree": DecisionTreeClassifier()
}

# 4. Modelación: Entrenar y evaluar los modelos


# Entrenar y evaluar los modelos
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Modelo: {name}")
    print(f"Precisión: {accuracy:.4f}")
    print(classification_report(y_test, y_pred))

# 4. Modelación: Búsqueda de hiperparámetros
# Utilizamos GridSearchCV para buscar los mejores hiperparámetros para cada modelo.
# Hiperparámetros para Random Forest

# Parámetros para Random Forest
param_grid_rf = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

# GridSearch para Random Forest
grid_search_rf = GridSearchCV(RandomForestClassifier(), param_grid_rf, cv=5, n_jobs=-1, scoring='accuracy')
grid_search_rf.fit(X_train, y_train)

# Imprimir los mejores parámetros
print(f"Mejores parámetros para Random Forest: {grid_search_rf.best_params_}")
best_rf = grid_search_rf.best_estimator_

# Evaluar el modelo con los mejores parámetros
y_pred_rf = best_rf.predict(X_test)
print("Mejores parámetros de Random Forest:")
print(classification_report(y_test, y_pred_rf))

# 4. Modelación: Búsqueda de hiperparámetros

# Parámetros para SVM
param_grid_svm = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf']
}

# GridSearch para SVM
grid_search_svm = GridSearchCV(SVC(), param_grid_svm, cv=5, n_jobs=-1, scoring='accuracy')
grid_search_svm.fit(X_train, y_train)

print(f"Mejores parámetros para SVM: {grid_search_svm.best_params_}")
best_svm = grid_search_svm.best_estimator_

# Evaluar el modelo con los mejores parámetros
y_pred_svm = best_svm.predict(X_test)
print("Mejores parámetros de SVM:")
print(classification_report(y_test, y_pred_svm))

from sklearn.metrics import classification_report
import pandas as pd

# Definir los modelos
models = {
    "Logistic Regression": LogisticRegression(),
    "SVM": SVC(),
    "Random Forest": RandomForestClassifier(),
    "K-Nearest Neighbors": KNeighborsClassifier(),
    "Decision Tree": DecisionTreeClassifier()
}

# Diccionario para almacenar resultados
results = {}

# Entrenar y evaluar los modelos
for name, model in models.items():
    model.fit(X_train, y_train)  # Entrenar el modelo
    y_pred = model.predict(X_test)  # Realizar predicciones
    report = classification_report(y_test, y_pred, output_dict=True)  # Obtener métricas

    # Almacenar métricas en el diccionario
    results[name] = {
        'Precision': report['accuracy'],  # Para obtener precisión global
        'Recall': report['macro avg']['recall'],
        'F1-score': report['macro avg']['f1-score'],
        'Support': report['macro avg']['support']
    }

# Convertir los resultados a un DataFrame
results_df = pd.DataFrame(results).T

# Mostrar la tabla consolidada de resultados
print(results_df)

# 4. Modelación: Uso de PyCaret (opcional)

!pip install pycaret

# Importar PyCaret
from pycaret.classification import *

# Asegurarse de que las columnas booleanas existen antes de convertirlas
columns_to_check = ['cp_1', 'cp_2', 'cp_3']
for col in columns_to_check:
    if col in heart_df.columns and heart_df[col].dtype == bool:
        heart_df[col] = heart_df[col].astype(int)

# Verificar si las columnas especificadas existen antes de pasarlas a PyCaret
categorical_features = [col for col in columns_to_check if col in heart_df.columns]

# Inicializar el entorno de PyCaret
clf = setup(
    data=heart_df,
    target='output',              # Variable objetivo
    session_id=42,                # Semilla para reproducibilidad
    normalize=True,               # Normalización de datos
    categorical_features=categorical_features,  # Columnas categóricas
    ignore_features=['age'] if 'age' in heart_df.columns else None,  # Ignorar 'age' si existe
    log_experiment=False          # Evitar registro de experimentos
)

# Comparar los modelos
best_model = compare_models()

# Mostrar el mejor modelo encontrado
print("Mejor modelo:", best_model)

# Importar las librerías necesarias
from pycaret.classification import *
import pandas as pd

# Asumimos que ya tienes el dataset cargado en 'heart_df'
# Revisamos las primeras filas para asegurarnos que los datos son correctos
print(heart_df.head())

# Verificar si la columna 'cp' existe en el DataFrame
if 'cp' in heart_df.columns:
    # Realizar One-Hot Encoding en la columna 'cp' si existe
    heart_df = pd.get_dummies(heart_df, columns=['cp'], prefix=['cp'])
else:
    # Imprimir un mensaje si la columna 'cp' no se encuentra
    print("La columna 'cp' no se encuentra en el DataFrame.")

# Convert boolean columns to integers before passing to PyCaret
for column in heart_df.select_dtypes(include=['bool']).columns:
    heart_df[column] = heart_df[column].astype(int)

# Inicializar el entorno de PyCaret
clf = setup(
    data=heart_df,
    target='output',
    session_id=42,
    normalize=True,
    # Usar las columnas codificadas (e.g., 'cp_0', 'cp_1', 'cp_2', etc.)
    categorical_features=[col for col in heart_df.columns if col.startswith('cp_')],
    ignore_features=['age'],
    log_experiment=False
)

# Comparar todos los modelos disponibles para identificar el mejor
best_model = compare_models()

# Evaluar el mejor modelo con métricas clave (recall, precision, f1-score)
evaluate_model(best_model)

# Hacer predicciones con el mejor modelo
# 'X_test' es el conjunto de datos de prueba, si no está definido, usa un 20% de los datos del 'setup'
predictions = predict_model(best_model) # Corrected predict_mode to predict_model

# Imprimir las primeras filas de las predicciones para ver los resultados
print(predictions.head())

# 5.Evaluación: Defina el mejor modelo.


# Comparar los modelos disponibles en PyCaret y seleccionar el mejor basado en el rendimiento
best_model = compare_models()

# Evaluar el mejor modelo para obtener detalles adicionales sobre su rendimiento
evaluate_model(best_model)

# Obtener el reporte de clasificación
from sklearn.metrics import classification_report
y_true = heart_df['output']  # Etiqueta real (target)

# Get predictions using the best model.
predictions = predict_model(best_model, data=heart_df) #Make sure to pass the data to predict_model

# Access predictions using 'prediction_label' or 'Label' based on PyCaret version
y_pred = predictions['prediction_label']  # Predicciones del modelo - Updated to use 'prediction_label'

# Imprimir el reporte de clasificación
print(classification_report(y_true, y_pred))

"""# 5.Evaluación: ¿Valdría la pena usar el mejor modelo en el día a día de una empresa/institución?

# La decisión de implementar el mejor modelo en el día a día de una empresa o institución, especialmente en el contexto de predicción de riesgo de ataque cardíaco, debe tener en cuenta varios factores, que incluyen la precisión del modelo, su facilidad de implementación, las implicaciones éticas y legales, y su capacidad para integrarse de manera efectiva en el flujo de trabajo diario.  A continuación se analizan aspectos claves antes de tomar la decisión de implementación:

#1. Impacto en la salud y beneficios desde la perspectiva de prevención temprana, mejor asigación de recursos y optimización de procesos.
#2. Viabilidad técnica y financiera para establecer los costos iniciales de desarrollo e implementación y mantenimiento del modelo y también los costos a largo plazo de reducción de costos médicos y escalabilidad.
#3. Implicaciones éticas y regulatorias.
#4. Integración en el flujo de trabajo diario, si existe facilidad de integración, compatibilidad con los sistemas existentes e interacción con los usuarios.

#Finalmente, consideramos que si vale la pena implementarlo con precauciones, dado que tener un modelo de predicción de ataque cardíaco en una institución médica podría ser muy beneficioso, especialmente en términos de prevención temprana y optimización de recursos y teniendo en cuenta los aspectos claves plasmados.
"""

# 6. Despliegue: Cree el pipeline del mejor modelo.

# Guardar el modelo
from pycaret.classification import save_model

# Guardar el mejor modelo en un archivo
save_model(best_model, 'heart_attack_model')

# Cargar el modelo guardado
from pycaret.classification import load_model
model = load_model('heart_attack_model')

# 6. Despliegue: Utilice FastAPI para crear un endpoint en el que se pueda llamar el pipeline creado

!pip install fastapi uvicorn pycaret

# 6. Despliegue: Utilice FastAPI para crear un endpoint en el que se pueda llamar el pipeline creado

# Importar librerías necesarias
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from pycaret.classification import load_model, predict_model
import os

# Define model path directly, assuming it's in the same directory as the notebook
# Assuming your model is saved as 'heart_attack_model.pkl' in the current directory
# Remove the '.pkl' extension from the model path
model_path = 'heart_attack_model'

# If the model is in a different directory, adjust the path accordingly
# For example:
# model_path = '/path/to/your/model/heart_attack_model'

# Cargar el modelo guardado, providing the full path
model = load_model(model_path)

# Crear la aplicación FastAPI
app = FastAPI()

# Definir el formato de entrada utilizando Pydantic
class HeartData(BaseModel):
    sex: int
    trtbps: float
    chol: float
    fbs: int
    restecg: int
    thalachh: float
    exng: int
    oldpeak: float
    slp: int
    caa: int
    thall: int
    cp_1: int
    cp_2: int
    cp_3: int

@app.post("/predict/")
async def predict_heart_disease(data: HeartData):
    # Convertir los datos de entrada a un DataFrame
    input_data = pd.DataFrame([data.dict()])

    # Hacer predicción usando el modelo cargado
    predictions = predict_model(model, data=input_data)

    # Retornar la predicción (puedes ajustar el formato según lo que necesites)
    return {"prediction": int(predictions['Label'][0])}

from pycaret.classification import save_model

# Guardar el modelo
save_model(model, 'heart_attack_model')

from google.colab import files
files.download('heart_attack_model.pkl')

!pip install fastapi uvicorn pycaret pandas pydantic
!pip install pyngrok  # Para usar ngrok

# Importar librerías necesarias
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from pycaret.classification import load_model, predict_model
import os
import uvicorn

# Cargar el modelo
# Remove the '.pkl' extension from the model path, as load_model will add it automatically
model_path = '/content/heart_attack_model'  # Ruta donde tienes el modelo en Colab
model = load_model(model_path)

# Crear la aplicación FastAPI
app = FastAPI()

# Definir la clase de entrada para los datos de predicción
class HeartData(BaseModel):
    sex: int
    trtbps: float
    chol: float
    fbs: int
    restecg: int
    thalachh: float
    exng: int
    oldpeak: float
    slp: int
    caa: int
    thall: int
    cp_1: int
    cp_2: int
    cp_3: int

@app.post("/predict/")
async def predict_heart_disease(data: HeartData):
    # Convertir los datos de entrada a un DataFrame
    input_data = pd.DataFrame([data.dict()])

    # Hacer la predicción
    predictions = predict_model(model, data=input_data)

    # Retornar la predicción
    return {"prediction": int(predictions['Label'][0])}

!pip install uvicorn
!pip install pyngrok