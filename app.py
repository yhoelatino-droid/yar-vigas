import streamlit as st
import math

st.set_page_config(
    page_title="YAR Structural", 
    page_icon="https://githubusercontent.com", 
    layout="centered"
)

st.title("📐 YAR Structural - Vigas")
st.subheader("Esquema Geométrico de Viga Peralta (3D)")

viga_3d_svg = """
<svg xmlns="http://w3.org" viewBox="0 0 600 300" width="100%">
  <rect width="600" height="300" fill="#11151c" rx="10"/>
  <polygon points="120,130 220,130 220,250 120,250" fill="#4a5568" stroke="#cbd5e1" stroke-width="2"/>
  <polygon points="120,130 450,50 550,50 220,130" fill="#718096" stroke="#cbd5e1" stroke-width="1.5"/>
  <polygon points="220,130 550,50 550,170 220,250" fill="#2d3748" stroke="#cbd5e1" stroke-width="2"/>
  <line x1="140" y1="235" x2="470" y2="155" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
  <line x1="200" y1="235" x2="530" y2="155" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
  <line x1="140" y1="145" x2="470" y2="65" stroke="#e11d48" stroke-width="3" stroke-linecap="round"/>
  <line x1="200" y1="145" x2="530" y2="65" stroke="#e11d48" stroke-width="3" stroke-linecap="round"/>
  <rect x="135" y="140" width="70" height="100" fill="none" stroke="#38bdf8" stroke-width="2" rx="3"/>
  <polygon points="465,60 535,60 535,160 465,160" fill="none" stroke="#38bdf8" stroke-width="2"/>
  <line x1="120" y1="265" x2="220" y2="265" stroke="#f8fafc" stroke-width="1.5"/>
  <line x1="120" y1="260" x2="120" y2="270" stroke="#f8fafc" stroke-width="1.5"/>
  <line x1="220" y1="260" x2="220" y2="270" stroke="#f8fafc" stroke-width="1.5"/>
  <text x="160" y="285" fill="#f8fafc" font-family="Arial" font-size="14" font-weight="bold" text-anchor="middle">Base (b)</text>
  <line x1="95" y1="130" x2="95" y2="250" stroke="#f8fafc" stroke-width="1.5"/>
  <line x1="90" y1="130" x2="100" y2="130" stroke="#f8fafc" stroke-width="1.5"/>
  <line x1="90" y1="250" x2="100" y2="250" stroke="#f8fafc" stroke-width="1.5"/>
  <text x="50" y="195" fill="#f8fafc" font-family="Arial" font-size="14" font-weight="bold">Peralte (h)</text>
  <text x="410" y="120" fill="#a7f3d0" font-family="Arial" font-size="14" font-weight="bold" transform="rotate(-13, 400, 120)">Longitud (L)</text>
</svg>
"""

st.markdown(viga_3d_svg, unsafe_allow_html=True)
st.write("---")
st.subheader("Datos de Entrada")

longitud_viga = st.number_input("Longitud de la viga (metros)", min_value=1.0, max_value=15.0, value=5.6, step=0.1)
tipo_viga = st.radio("Tipo de Viga:", ('Principal (L/10)', 'Secundaria (L/12)'), horizontal=True)

if st.button("Calcular Dimensiones ▶️", use_container_width=True):
    divisor = 10 if tipo_viga == 'Principal (L/10)' else 12
    peralte_exacto = longitud_viga / divisor
    peralte_final = math.ceil(peralte_exacto / 0.05) * 0.05
    base_calculada = peralte_final / 2
    base_final = 0.25 if base_calculada < 0.25 else base_calculada
        
    st.success("### 🧱 RESULTADOS DE DISEÑO")
    st.metric(label="📐 Peralte Redondeado (h)", value=f"{peralte_final:.2f} m  ({int(peralte_final * 100)} cm)")
    st.metric(label="🧱 Base Final Sugerida (b)", value=f"{base_final:.2f} m  ({int(base_final * 100)} cm)")
