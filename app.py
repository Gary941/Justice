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

# Footer
st.markdown("---")
st.caption("Built for New Generational Wealth Solutions | Powered by AI automation.")
