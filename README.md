# 🖥 SkillSwap Dashboard — Streamlit Frontend

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Streamlit Cloud](https://img.shields.io/badge/Deployed_on-Streamlit_Cloud-red?style=for-the-badge\&logo=streamlit\&logoColor=white)](https://streamlit.io/cloud)

The **SkillSwap Dashboard** is a **Streamlit frontend application** that connects to the SkillSwap FastAPI backend.

The platform allows users to **view, add, search, update, and match skills** through an interactive dashboard.

---

# 🌐 Live Application

Frontend Dashboard

https://skillswapfrontendbychinmay.streamlit.app/

Backend API

https://fastapi-project-5-skillswap-platform.onrender.com

---

# 🚀 Features

* 📊 Interactive analytics dashboard
* 👥 View all skill profiles
* ➕ Add new users and skills
* 🔎 Search users by skill
* 🤝 View skill exchange matches
* ✏️ Update skill profiles
* ❌ Delete users
* 📈 Skill popularity visualization

The dashboard provides a **clean interface for interacting with the SkillSwap API**.

---

# 🏗 Architecture

```
Streamlit Dashboard
        │
        ▼
   FastAPI REST API
        │
        ▼
   Skill Data Store
```

The frontend communicates with the backend via **HTTP REST requests**.

---

# 📂 Project Structure

```
skillswap-frontend
│
├── frontend.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Local Development

Clone repository

```
git clone https://github.com/iqroguerex-cpu/skillswap-frontend
```

Navigate into project

```
cd skillswap-frontend
```

Install dependencies

```
pip install -r requirements.txt
```

Run the Streamlit app

```
streamlit run frontend.py
```

Open in browser

```
http://localhost:8501
```

---

# 📦 Dependencies

Main libraries used:

* Streamlit
* Requests
* Pandas
* Plotly

Install manually if needed

```
pip install streamlit requests pandas plotly
```

---

# ☁️ Deployment

The frontend is deployed using **Streamlit Community Cloud**.

Deployment steps:

1. Push code to GitHub
2. Connect repository to Streamlit Cloud
3. Select `frontend.py` as the main file
4. Deploy the application

---

# 🔗 Backend API

The frontend communicates with the SkillSwap FastAPI backend.

API Base URL

https://fastapi-project-5-skillswap-platform.onrender.com

---

# 👨‍💻 Author

**Chinmay V Chatradamath**

GitHub
https://github.com/iqroguerex-cpu

---

⭐ If you like this project, consider **starring the repository**.
