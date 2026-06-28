import streamlit as st

# Website ka Title
st.title("🤖 Mera Personal Chatbot")
st.write("Aapka swagat hai! Mujhse koi bhi sawal puchein.")

# Chat history ko store karne ke liye (taki messages gayab na hon)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purane messages ko screen par dikhane ke liye
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User se input lene ke liye box
if user_input := st.chat_input("Yahan apna message likhein..."):
    
    # User ka message screen par dikhein
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # --- YAHAN AAP APNE CHATBOT KA LOGIC/DIMAG JO DEIN ---
    # Abhi ke liye hum ek simple reply set kar rahe hain
    bot_reply = f"Aapne kaha: {user_input}. (Mera dimag jaldi hi yahan connect hoga!)"
    # --------------------------------------------------

    # Bot ka reply screen par dikhein
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
