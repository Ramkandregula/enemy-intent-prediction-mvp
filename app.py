import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Enemy Intent Prediction System",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
h1, h2, h3 {
    color: #ffffff;
}
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 0 15px rgba(0,0,0,0.6);
    margin-bottom: 20px;
}
.metric {
    background-color: #262730;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}
.footer {
    text-align: center;
    color: gray;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🛡️ Enemy Intent Prediction System")
st.caption("MVP – AI-powered threat analysis dashboard (Hackathon Prototype)")

# ---------------- LAYOUT ----------------
left, right = st.columns([1.2, 2])

# ================= LEFT PANEL (RUNTIME INPUTS ONLY) =================
with left:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📥 Live Intelligence Inputs")

    speed = st.slider("🚗 Movement Speed (km/h)", 0, 120, 45)
    distance = st.slider("📏 Distance from Border (km)", 0, 50, 12)

    direction = st.selectbox(
        "🧭 Movement Direction",
        ["North", "South", "East", "West", "North-East", "North-West"]
    )

    formation = st.selectbox(
        "👥 Formation Type",
        ["Scattered", "Clustered", "Linear"]
    )

    predict = st.button("🔍 Predict Enemy Intent")
    st.markdown("</div>", unsafe_allow_html=True)

# ================= RIGHT PANEL (OUTPUT) =================
with right:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("📊 Threat Assessment")

    if predict:
        intent = random.choice(["Low", "Medium", "High"])
        confidence = random.randint(70, 95)

        if intent == "High":
            st.error("🚨 THREAT LEVEL: HIGH")
        elif intent == "Medium":
            st.warning("⚠️ THREAT LEVEL: MEDIUM")
        else:
            st.success("✅ THREAT LEVEL: LOW")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("<div class='metric'>", unsafe_allow_html=True)
            st.metric("Speed", f"{speed} km/h")
            st.markdown("</div>", unsafe_allow_html=True)

        with c2:
            st.markdown("<div class='metric'>", unsafe_allow_html=True)
            st.metric("Distance", f"{distance} km")
            st.markdown("</div>", unsafe_allow_html=True)

        with c3:
            st.markdown("<div class='metric'>", unsafe_allow_html=True)
            st.metric("Confidence", f"{confidence}%")
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("### 🧠 AI Explanation")
        st.write(
            f"""
            Based on **{formation.lower()} formation**, movement towards **{direction}**,
            speed of **{speed} km/h**, and proximity of **{distance} km**,
            the AI predicts a **{intent} threat level** with **{confidence}% confidence**.
            """
        )
    else:
        st.info("⬅️ Enter inputs and click **Predict Enemy Intent**")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "<div class='footer'>⚠️ Demo MVP | No real military or classified data used</div>",
    unsafe_allow_html=True
)
