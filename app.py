import streamlit as st

# Función principal para convertir las temperaturas
def convertir_temperatura(valor, unidad_origen, unidad_destino):
    # Si la unidad de origen y destino son iguales, retornamos el mismo valor
    if unidad_origen == unidad_destino:
        return valor
    
    # Primero, convertimos el valor de origen a Celsius para simplificar la lógica
    if unidad_origen == "Fahrenheit":
        celsius = (valor - 32) * 5.0 / 9.0
    elif unidad_origen == "Kelvin":
        celsius = valor - 273.15
    else:
        celsius = valor # Ya está en Celsius

    # Luego, convertimos de Celsius a la unidad de destino deseada
    if unidad_destino == "Fahrenheit":
        return (celsius * 9.0 / 5.0) + 32
    elif unidad_destino == "Kelvin":
        return celsius + 273.15
    else:
        return celsius # El destino es Celsius

# Configuración de la página en Streamlit
st.set_page_config(page_title="Conversor de Temperaturas", page_icon="🌡️")

# Título y descripción de la aplicación
st.title("🌡️ Conversor de Temperaturas")
st.write("Convierte fácilmente entre grados Celsius, Fahrenheit y Kelvin.")

# Crear columnas para organizar el diseño
col1, col2 = st.columns(2)

# Lista de unidades disponibles
unidades = ["Celsius", "Fahrenheit", "Kelvin"]

with col1:
    # Campo para ingresar el valor numérico
    valor_input = st.number_input("Ingresa la temperatura:", value=0.0)
    # Selector de la unidad de origen
    unidad_origen = st.selectbox("Convertir de:", unidades, index=0)

with col2:
    # Espacio en blanco para alinear visualmente (opcional)
    st.write("") 
    st.write("")
    # Selector de la unidad de destino
    unidad_destino = st.selectbox("Convertir a:", unidades, index=1)

# Botón para ejecutar la conversión
if st.button("Convertir"):
    # Validación especial para Kelvin (no puede ser menor a 0)
    if unidad_origen == "Kelvin" and valor_input < 0:
        st.error("Error: La temperatura en Kelvin no puede ser menor que 0 (Cero Absoluto).")
    else:
        # Llamar a la función de conversión
        resultado = convertir_temperatura(valor_input, unidad_origen, unidad_destino)
        
        # Mostrar el resultado con un mensaje de éxito
        st.success(f"**Resultado:** {valor_input:.2f} {unidad_origen} = {resultado:.2f} {unidad_destino}")

# Pie de página o información adicional
st.markdown("---")
st.caption("Aplicación creada con ❤️ usando Streamlit")