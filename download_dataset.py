import os
import kagglehub  # type: ignore
import shutil

# Guardar la data en la carpeta data del repositorio
data_dir = "./data"
os.makedirs(data_dir, exist_ok=True)

try:
    # Intentar descargar el dataset de detección de fraude
    path = kagglehub.dataset_download("kartik2112/fraud-detection")

    # Verificar si el dataset se descargó correctamente
    if not os.path.exists(path):
        raise FileNotFoundError(f"The dataset was not downloaded correctly. Check the dataset name or the connection.")

    # Mover los archivos a la carpeta data
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            shutil.move(file_path, data_dir)
        else:
            print(f"Warning: {file} is not a valid file to move.")

    print(f"Dataset moved to: '{os.path.abspath(data_dir)}'")

except kagglehub.KaggleHubError as e:
    print(f"Error while downloading the dataset: {e}")
except FileNotFoundError as e:
    print(f"Error: {e}")
except PermissionError as e:
    print(f"Permission error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
