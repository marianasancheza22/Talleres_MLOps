# -*- coding: utf-8 -*-
"""Taller_3_MLops_Sanchez_punto_2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_VQMe0fQ-MfnaV33CyCVrDHBJdh-LPg1

# Students Performance Dataset
"""

!pip install kagglehub
import kagglehub

path = kagglehub.dataset_download("rabieelkharoua/students-performance-dataset")
print("Path to dataset files:", path)

import pandas as pd

# Cargar el dataset
file_path = f"{path}/StudentsPerformance.csv"
df = pd.read_csv("/content/Student_performance_data _.csv")

# Visualizar las primeras filas del dataset
print(df.head())

print("\nInformación general del dataset:")
print(dataset.info())

!pip install --upgrade pycaret

import pandas as pd
from pycaret.regression import setup, compare_models, tune_model, plot_model, finalize_model

dataset = pd.read_csv("Student_performance_data _.csv")


regression_setup = setup(
    data=dataset,
    target='GPA',
    numeric_features=['Age', 'StudyTimeWeekly', 'Absences', 'Tutoring', 'Extracurricular', 'Sports', 'Music', 'Volunteering'],
    categorical_features=['Gender', 'Ethnicity', 'ParentalSupport'],
    normalize=True,
    transformation=True,

)


# Compare models and choose the best
best_model = compare_models()

# Tune the best model
tuned_model = tune_model(best_model)

# Evaluate the tuned model
plot_model(tuned_model, plot='residuals')
plot_model(tuned_model, plot='error')

# Finalize model for production
final_model = finalize_model(tuned_model)

# Display details of the final model
print(final_model)

!pip install mlflow optuna

# Importar librerías
# ... (rest of your imports remain the same)

# ... (data loading and preprocessing remain the same)

# --- Definir modelos y funciones de búsqueda con Optuna ---
def objective_linear_regression(trial):
    # Start a new MLflow run for each trial, ensuring it's nested
    with mlflow.start_run(nested=True):  # <-- This line is changed
        # Hiperparámetros a optimizar
        normalize = trial.suggest_categorical('normalize', [True, False])

        # Modelo
        model = LinearRegression()

        # Apply normalization if selected by Optuna
        if normalize:
            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)
            model.fit(X_train_scaled, y_train)
            predictions = model.predict(X_test_scaled)
        else:
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)

        # Evaluación
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        # Registrar en MLflow
        mlflow.log_param('normalize', normalize)
        mlflow.log_metric('mse', mse)
        mlflow.log_metric('r2', r2)
        mlflow.sklearn.log_model(model, "linear_regression_model")

!pip install mlflow

!mlflow ui --host 0.0.0.0 --port 5000 &