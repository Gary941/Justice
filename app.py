import streamlit as st

# Set page config
st.set_page_config(
    page_title="Justice - AI Legal Case Manager",
    page_icon="⚖️",
    layout="centered"
)

# App title and subtitle
st.title("⚖️ Justice")
st.subheader("Your AI Legal Case Manager")

# Description block
st.markdown("""
**Justice** is your AI-powered legal case manager.  
She handles legal cases from **submission to settlement** —  
follows up, keeps everyone on track, and makes sure **you get paid**.

Focus on practicing law. Justice manages the rest.
""")

st.divider()

# Case submission simulation form
st.markdown("### 📝 Submit a New Case")

with st.form("case_form"):
    client_name = st.text_input("Client Name")
    case_type = st.selectbox("Case Type", ["Contract Dispute", "Personal Injury", "Employment", "IP", "Other"])
    case_summary = st.text_area("Case Summary")
    opposing_party = st.text_input("Opposing Party (if known)")
    urgency = st.radio("Urgency Level", ["Low", "Medium", "High"])

    submitted = st.form_submit_button("Submit Case")

    if submitted:
        st.success(f"✅ Case for **{client_name}** submitted successfully!")
        st.info(f"Justice will begin tracking this **{case_type}** case and keep all parties aligned.")
        st.write("🔍 Summary:", case_summary)
        if opposing_party:
            st.write("⚖️ Opposing Party:", opposing_party)
        st.write("🚦 Urgency Level:", urgency)

st.divider()

# Footer
st.markdown("""
Made with ❤️ by your AI assistant.  
_Justice is always on the case._
""")

