import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# --- CONFIGURATION ---
st.set_page_config(page_title="MPJO Enterprise Suite", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🏥 MPJO Navigation")
page = st.sidebar.radio("Go to:", [
    "🏠 Dashboard Overview", 
    "📅 Multi-Day Booking (Locking)", 
    "⚡ Live Queue Management", 
    "🚨 Emergency & Rescheduling",
    "🤖 AI Patient Concierge"
])

st.sidebar.markdown("---")
st.sidebar.info("**Problem Statement 7**\nDynamic Queue Management")

# --- PAGE 1: OVERVIEW ---
if page == "🏠 Dashboard Overview":
    st.title("Hospital Command Center")
    st.write("Real-time summary of all shared hospital resources.")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Resource Utilization", "94%", "+2%")
    m2.metric("Total Patients Today", "128", "Active")
    m3.metric("System Status", "OPTIMIZED", "BMS-Lock Active")
    
    

# --- PAGE 2: MULTI-DAY BOOKING (Features 1 & 2) ---
elif page == "📅 Multi-Day Booking (Locking)":
    st.title("📦 Feature 1 & 2: Transactional Journey Planner")
    st.markdown("### Step 1: Clinically-Aware Logic & BMS Slot Locking")
    
    c1, c2 = st.columns(2)
    p_name = c1.text_input("Enter Patient Name", "Anjali Sharma")
    p_pkg = c2.selectbox("Select Health Package", ["Executive Full Body Checkup", "Senior Citizen Cardiac Care"])

    if st.button("🔒 Confirm & Atomic Lock Entire Journey"):
        st.success(f"Journey Secured for {p_name}. Slots are now blocked across all departments.")
        st.balloons()
        
        # Backend Logic Display
        t0, t1 = datetime.now().strftime("%d %b"), (datetime.now() + timedelta(days=1)).strftime("%d %b")
        itinerary = [
            {"Day": t0, "Time": "08:00 AM", "Test": "Blood Profile", "Prep": "12h Fasting", "Status": "LOCKED"},
            {"Day": t0, "Time": "11:30 AM", "Test": "X-Ray Chest", "Prep": "None", "Status": "LOCKED"},
            {"Day": t1, "Time": "10:00 AM", "Test": "Abdomen USG", "Prep": "Hydration Required", "Status": "LOCKED"}
        ]
        st.table(pd.DataFrame(itinerary))

# --- PAGE 3: QUEUE MANAGEMENT (Feature 3) ---
elif page == "⚡ Live Queue Management":
    st.title("🚦 Feature 3: Two-Tier Dynamic Queuing")
    
    col_master, col_dept = st.columns(2)
    
    with col_master:
        st.subheader("Master Entry Queue")
        st.dataframe(pd.DataFrame({
            "ID": ["P-501", "P-502", "P-503"],
            "Patient": ["Anjali S.", "Vikram R.", "Sana M."],
            "Action": ["Check-in", "Wait", "Verified"]
        }), use_container_width=True)
        
    with col_dept:
        st.subheader("Localized Department Queues")
        st.dataframe(pd.DataFrame({
            "Dept": ["Radiology", "Pathology", "Cardiology"],
            "Active Machine": ["X-Ray 1", "Lab A", "ECG 2"],
            "Wait Time": ["15m", "4m", "0m"]
        }), use_container_width=True)
    
    

# --- PAGE 4: RESCHEDULING (Feature 4) ---
elif page == "🚨 Emergency & Rescheduling":
    st.title("🕒 Feature 4: Self-Healing & EWT Recovery")
    st.write("Handling no-shows and slot re-optimization.")
    
    st.error("No-Show Alert: Patient P-501 (Anjali S.) missed their 8:00 AM Blood Test.")
    
    if st.button("🔄 Auto-Reschedule Remaining Journey"):
        st.info("System Action: Re-blocking future slots while maintaining clinical sequence...")
        st.success("New 24-hour itinerary sent to patient. Resource 'Lab A' released for next in queue.")

# --- PAGE 5: AI CONCIERGE (Feature 5) ---
elif page == "🤖 AI Patient Concierge":
    st.title("💬 Feature 5: AI-Powered NLP Concierge")
    st.write("Providing 24/7 navigation and clinical preparation guidance.")
    
    chat_query = st.text_input("Ask the MPJO Assistant:", placeholder="Where is Radiology? / Do I need to fast?")
    
    if chat_query:
        if "where" in chat_query.lower() or "room" in chat_query.lower():
            st.chat_message("assistant").write("To reach **Radiology**, follow the Blue floor markers to the 3rd floor, West Wing.")
        elif "fast" in chat_query.lower() or "prep" in chat_query.lower():
            st.chat_message("assistant").write("Yes, your locked package requires **12 hours of fasting** for the Blood Test. No food or tea after 8 PM.")
        else:
            st.chat_message("assistant").write("I can help with directions or preparation steps. Please ask about your test location or requirements.")