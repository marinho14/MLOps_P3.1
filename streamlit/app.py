import streamlit as st
import requests

API_URL = "http://10.43.101.151:8088/predict/modelo_base"

def predict(request_body):
    headers = {
        "Content-Type": "application/json",
    }

    response = requests.post(
        API_URL, json=request_body, headers=headers
    )
    return response.json()

def main():
    st.title("Aplicación de Streamlit para API POST")

    # Definir los valores por defecto basados en el esquema
    default_values = {
        "Elevation": 0,
        "Aspect": 0,
        "Slope": 0,
        "Horizontal_Distance_To_Hydrology": 0,
        "Vertical_Distance_To_Hydrology": 0,
        "Horizontal_Distance_To_Roadways": 0,
        "Hillshade_9am": 0,
        "Hillshade_Noon": 0,
        "Hillshade_3pm": 0,
        "Horizontal_Distance_To_Fire_Points": 0,
        "Wilderness_Area": "Rawah",
        "Soil_Type": "C7745",
        "Cover_Type": 0
    }

    # Crear campos de entrada para cada atributo
    input_values = {}
    for key, value in default_values.items():
        input_values[key] = st.text_input(key, value)

    # Convertir valores a los tipos de datos correctos
    request_body = {key: [int(value)] if key not in ["Wilderness_Area", "Soil_Type"] else [value] for key, value in input_values.items()}

    if st.button("Realizar Predicción"):
        st.write("Realizando predicción...")
        result = predict(request_body)
        st.write("Resultado de la predicción:", result)

if __name__ == "__main__":
    main()
