import streamlit as st

# Website UI settings
st.set_page_config(page_title="Aakriti Hair Salon AI", page_icon="💇‍♂️")
st.title("🤖 Aakriti Hair Salon - AI Assistant")
st.write("Soham dwara sanchalit Aakriti Hair Salon me aapka swagat hai!")

# Chat history system
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input box
if user_input := st.chat_input("Ask about hairstyles, prices, or timings..."):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    text = user_input.lower()
    
    # 1. GREETINGS RESPONSE (Hello/Hi me perks nahi dikhenge - Rule 2)
    if any(x in text for x in ["hi", "hello", "hey", "namaste", "halo", "ram ram"]):
        bot_reply = "👋 Hello! Welcome to Aakriti Hair Salon AI Assistant. How can I help you with your hair styling, pricing, or salon information today?"
        
    # 2. TIMING & LOCATION RESPONSE (Aapke rules ke hisab se timing aur blank location)
    elif any(x in text for x in ["time", "timing", "open", "close", "samay", "kholna", "band", "location", "address", "pata", "kahan"]):
        bot_reply = "⏳ Salon Timing:\n* 10:00 AM to 10:00 PM (Every day)\n\n📍 Location:\n* "
        
    # 3. PRICING & HAIRSTYLES RESPONSE (Isme pricing ke sath premium perks trigger honge - Rule 2)
    elif any(x in text for x in ["price", "rate", "cost", "haircut", "style", "cut", "daam", "paise", "men", "women", "kids", "fade", "combo", "beard"]):
        bot_reply = """
💇‍♂️ Aakriti Hair Salon Premium Services & Pricing:

🧔 Men's Haircuts & Styling:
* Standard Haircut / Trim: Starting from ₹150
* Trending Styles (Fade, Undercut, Crop Cut, Pompadour): Starting from ₹250
* Beard Styling / Shaving: Starting from ₹100
* Men's Combo (Haircut + Beard Styling): Special Combo starting from ₹200

👶 Kids Haircuts:
* Boys & Girls Haircut (Children): Starting from ₹100 - ₹150

👩 Women's Short Hair:
* Pixie Cut / Classic Bob / Blunt Bob / Textured Layers: Starting from ₹400
* *Maintenance Tip:* Keeps short hair looking sharp!

🪮 Women's Long Hair:
* Advanced Cuts (Layer Cut, Step Cut, Butterfly Cut, Curtain Bangs, U/V Cut): Starting from ₹600
* *Styling Tip:* Great for managing volume and protecting your ends.

✨ Our Premium Complimentary Perks (Included Free with Services):
* ☕ Chai-Paani: Free tea, coffee, or packaged drinking water during your visit.
* 🔍 Free Consultation: 100% free expert hair health and scalp analysis before starting.
* ❄️ Premium Comfort: Fully air-conditioned salon, comfortable modern styling chairs, and 100% sanitized tools.
* 🧴 Post-Cut Styling: Free basic hair setting and serum application after every haircut.
        """
        
    # 4. HOME SERVICE POLICY RESPONSE (Rule 3)
    elif any(x in text for x in ["home", "ghar", "visit", "home service", "ghar pe"]):
        bot_reply = "🚫 No Home Service Policy:\nWe strictly do not provide home services. All services are exclusively available at our salon. Please visit Aakriti Hair Salon to get the best premium experience!"
        
    # 5. OUT OF TOPIC / BOOKING / COMPLEX MEDICAL QUERIES (Rule 5 & Guardrails)
    else:
        bot_reply = "For more details, please contact Soham.\n\nअधिक जानकारी के लिए कृपया सोहम से संपर्क करें।\n\nવધુ વિગતો માટે કૃપા કરીને સોહમનો સંપર્ક કરો."

    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
