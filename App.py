import streamlit as st
import time
from streamlit_extras.let_it_rain import rain

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Para ti mi lobito❤️", page_icon="🎁", layout="centered")

# --- ESTILOS CSS PERSONALIZADOS (Para que se vea bonito en celular) ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
        font-weight: bold;
        height: 60px;
        margin-bottom: 10px;
    }
    .stButton>button:hover {
        background-color: #ff0000;
        color: white;
        border: 2px solid white;
    }
    h1 {
        text-align: center;
        color: #d63031;
    }
    .big-font {
        font-size: 20px !important;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNCIÓN DE LLUVIA DE CORAZONES ---
def lluvia_corazones():
    rain(
        emoji="❤️",
        font_size=54,
        falling_speed=5,
        animation_length="5s",
    )

# --- ENCABEZADO ---
st.title("🎄 Regalo de Navidad par mi lobito❤️😘 🎄")
st.write("😘 Hola amoooor, esta cuponera está hecha para que eligas lo que quieras cuando quieras 😘")

# --- ESTADO DE LA APLICACIÓN (Para recordar qué cupón se abrió) ---
if 'cupon_abierto' not in st.session_state:
    st.session_state.cupon_abierto = None

# --- LOS CUPONES ---
# Puedes agregar o quitar cupones aquí
cupones = {
    "🏔️ Vale por una salida al cerro": "Llevamos cositas panzonas para comer y mucha awita 🍪🥤",
    "💆 Vale por un masaje": "Masaje relajante de 30 minutos con cremita para mi lobito porque se lo merece 😘",
    "🧺 Vale por un picnic": "En el lugar que quieras amor, como recomendación es muy romántico en la playa 🏖️",
    "🏕️ Vale por acampar en agua de honor": "Hacemos un fuegito y contamos historias de terror mientras comemos ammmm 🌃",
    "🐎 Vale por andar a caballo (con casco 🪖)": "Quiero aprender bien a andar a caballo para poder salir juntitos ❤️",
    "🍕 Vale por una cena romántica": "Yo la preparo para tí amorcito, lo que tu quieras 😋",
    "🎬 Vale por una tarde de cine": "Compro las palomitas y más cositas panzonas y tu eliges la película 🍿",
    "🫂 Vale por estar como lapa hacia tí un día completo": "muchos besitos, abrazos y estar muy muy juntitos 🥰",
    "🎡 Vale por ir a serena aventura o al jumping": "Pasar la tarde y/o noche en los juegos pasando un bonito día 🎠",
    "🔍👀 Vale por ir a conocer lugares nuevos en La Serena": "A lugares que no hemos estado antes, tu eligees! 🏙️",
    "🔍👀 Vale por ir a conocer lugares nuevos en Coquimbo": "Es a elección tuya pero la recomendación es a la cruz o lugares para ir a comer 🌞",
    "🚌 Vale por ir a perdernos en micro": "Tu eliges, puede ser en La Serena o Coquimbo, luego de andar en micro nos vamos a caminar y nos perdemos mientras conversamos de todo 🛴",
    "🍸 Vale por ir a tomar algo rico": "En la noche y en la playa, luego caminamos por la arena ⛱️",
    "😋 Vale por ir a un tenedor libre": "Y quedamos panzones por todo el día ammmm 🍔",
    "🎮 Vale por una tarde de videojuegos juntitos": "Día de tarreo con mi lobito 👾",
    "🫣 Vale por Sí a todo por 24 horas": "Todo lo que me digas te tengo que decir que si😃",
    "🍛 Vale por cocinar tu comida favorita": "Preparo lo que te guste, puede ser comida, postre o ambaaaas! 😮",
    "🛖 Vale por arrendar una cabaña en el Valle ": "Nos escapamos un fin de semana y nos vamos al valle para arrendar algo, yo invito el arriendo 👀",
    "💻 Vale por comenzar una serie juntos": "Ver una serie o anime de inicio a fin o en transmisión mientras comemos cosas panzonas ammm 😋",
    "🤔 Vale Misterioso": "Este es un comodín, ocupalo para lo que tu quieras 😉."
}

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