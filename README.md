MPJO – Multi-Day Patient Journey Optimizer 🏥
A Transactional AI-Logistics Engine for Shared Hospital Resources
MPJO is a proactive logistics platform designed to solve Dynamic Queue Management in Shared Resource Environments2. By treating hospital machine time as a finite inventory, the system ensures that complex, multi-day patient journeys are optimized and guaranteed

🚀 Key Features
Transactional Journey Planning: Uses an "Atomic Lock" mechanism to reserve every appointment in a health package across multiple days in a single transaction, preventing double-booking
Clinically-Aware Logic: Standardizes medical packages into smart sequences (e.g., Fasting Tests $\rightarrow$ Nutrition $\rightarrow$ Hydration) to prevent clinical errors
Two-Tier Dynamic Queuing: Features a Master Entry Queue for central check-in and localized Department Queues for real-time resource routing6666.+1Self-Healing Recovery: Automated no-show detection that releases idle machines and re-optimizes the remaining patient journey instantly7.AI Patient Concierge: A lightweight NLP assistant acting as an internal GPS for department directions and clinical prep-guidance8888.+1🛠️ Technology StackBackend: Python (FastAPI/Flask) for high-concurrency scheduling logic9.Frontend: Streamlit for the real-time Hospital Command Center dashboard.Data Strategy: PostgreSQL for transactional safety and Redis for live slot locking10.Intelligence: Lightweight NLP for Intent Classification and Navigation11.📦 Installation & UsageClone the repository:Bashgit clone https://github.com/YOUR_USERNAME/MPJO-Hospital-Optimizer.git
Install dependencies:Bashpip install -r requirements.txt
Run the application:Bashstreamlit run app.py
📈 ImpactPatients: 100% preparation accuracy and reduced wait times12.Staff: Optimized machine utilization and eliminated manual data entry13.Hospitals: Increased throughput for Health Checks, OP, and IP flows14.🎥 Project DemoWatch the full system walkthrough here
