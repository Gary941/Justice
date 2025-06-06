import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Justice - Litigation AI Agent",
    page_icon="⚖️",
    layout="centered",
)

# Title Section
st.title("⚖️ Meet Justice")
st.subheader("Your Litigation AI Agent")

# Main Description
st.markdown("""
### What Justice Does:

**Justice** is your relentless AI agent built to manage litigation cases from **start to settlement**.

---

**✅ Submission to Settlement:**
- Submits new cases and logs all progress
- Tracks weekly and monthly follow-ups

**📬 Attorney Communication:**
- Follows up via email to confirm case status
- Tracks demand letters, filings, and settlements

**📲 Client Communication:**
- Uses text, email, and voice for updates
- Gets missing documents and signatures fast

**🚨 Issue Resolution:**
- Flags delays or problems instantly
- Notifies Gary and takes steps to resolve them

**💰 Payment Tracking:**
- Confirms signed settlements
- Follows up until your payment is received

---

### Why Justice?
Because your time is too valuable to babysit lawsuits. Justice stays on it — so you don’t have to.

""")

# --------------------------------
# Add New Case Intake Form
# --------------------------------
st.markdown("---")
st.subheader("📂 Submit a New Legal Case")

with st.form("case_submission_form"):
    st.markdown("### Client Info")
    client_name = st.text_input("Client Name")
    client_email = st.text_input("Client Email")
    phone_number = st.text_input("Phone Number")
    date_of_birth = st.date_input("Date of Birth")

    st.markdown("### Case Details")
    case_type = st.selectbox("Case Type", ["FCRA", "FDCPA"])
    company_name = st.text_input("Company Involved (Credit Bureau or Debt Collector Name)")
    attorney_name = st.text_input("Attorney Name")
    attorney_email = st.text_input("Attorney Email")
    case_description = st.text_area("Case Description")

    st.markdown("### Consent")
    consent = st.checkbox("I confirm that the client has consented to this submission.")

    submitted = st.form_submit_button("Submit Case")

    if submitted:
        if consent:
            st.success(f"✅ Case for {client_name} has been submitted successfully!")
        else:
            st.error("❌ Please confirm that the client has consented to this submission.")


st.caption("Built for New Generational Wealth Solutions | Powered by AI automation.")

