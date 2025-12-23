import streamlit as st
import time
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Para ti mi lobito❤️", page_icon="🎁", layout="centered")

conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(worksheet="Hoja 1", ttl=0)

st.title("🎄 Regalo de Navidad par mi lobito❤️😘 🎄")
st.write("😘 Hola amoooor, esta cuponera está hecha para que eligas lo que quieras cuando quieras 😘")

for index, row in df.iterrows():
    regalo = row['Regalo']
    estado = row['Canjeado'] # Debe ser TRUE o FALSE en el Excel
    mensaje = row['Mensaje']

    # Creamos un contenedor para que se vea bonito
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.subheader(f"🎁 {regalo}")
        if estado:
            st.caption("❌ ESTE CUPÓN YA FUE CANJEADO")
    
    with col2:
        # El botón es único gracias a la 'key=index'
        # Si estado es TRUE, el botón aparece desactivado (disabled=True)
        if st.button("Canjear", key=index, disabled=bool(estado)):
            
            # 1. Actualizamos el DataFrame localmente
            df.at[index, 'Canjeado'] = True
            
            # 2. Escribimos el cambio en Google Sheets
            conn.update(worksheet="Hoja 1", data=df)
            
            # 3. Mostramos mensaje de éxito y lluvia de corazones
            st.balloons()
            st.success(f"¡Disfrútalo! {mensaje}")
            
            # 4. Recargamos la página para que el botón se bloquee visualmente
            st.rerun()

st.markdown("---")
if st.button("🔄 Actualizar lista (si algo falla)"):
    st.cache_data.clear()
    st.rerun()














"""
# --- FUNCIÓN DE LLUVIA DE CORAZONES ---
def lluvia_corazones():
    rain(
        emoji="❤️",
        font_size=54,
        falling_speed=5,
        animation_length="5s",
    )

# --- GENERAR LOS BOTONES ---
for titulo, mensaje in cupones.items():
    if st.button(titulo):
        st.session_state.cupon_abierto = mensaje
        lluvia_corazones() # ¡Activa la animación!

# --- MOSTRAR EL RESULTADO ---
if st.session_state.cupon_abierto:
    st.markdown("---")
    st.success(f"### 🎉 {st.session_state.cupon_abierto}")
    if st.button("Cerrar Cupón"):
        st.session_state.cupon_abierto = None
        st.rerun()

# --- PIE DE PÁGINA ---
st.markdown("---")
st.markdown("<p class='big-font'>Hecho con ❤️ por tu lobita 🐺🩷", unsafe_allow_html=True)
"""
