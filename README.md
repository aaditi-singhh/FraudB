<div align="center">
  
# 🚀 FraudB | AI-Driven Fraud Analytics & Assistant
**Intelligent Transaction Monitoring, Predictive Analytics, and Live AI Assistance**

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.1-092E20.svg?logo=django)](https://www.djangoproject.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248.svg?logo=mongodb)](https://www.mongodb.com/)

**[🟢 View the Live Application Here!](https://fraudb-fj6xtuf9o-aaditi-singhhs-projects.vercel.app/)**

</div>

---

## 🌟 Overview
**FraudB** is a full-featured fraud analytics platform designed to help businesses monitor, analyze, and act on potentially fraudulent transactions. By combining transaction-level risk scoring, predictive machine learning, and dynamic AI guidance, FraudB empowers organizations with informed decision-making tools.

### 🔥 Key Highlights:
- 🤖 **AI Assistant**: Get actionable guidance based on live analytics and historical trends.
- 📊 **Fraud Analytics**: Monitor dynamic metrics across custom time windows, risk levels, and channel insights.
- 🔮 **Predictive ML**: Execute single or batch transaction predictions with contextual descriptive summaries.
- 🔒 **Secure Auth & Alerts**: Bulletproof OTP-based email verification, user profile management, and live alert notifications.
- 🚀 **Production-Ready**: Hosted seamlessly on Vercel with CSRF protection, environment-driven configuration, and HTTPS-ready protocols.

---

## 🛠️ Tech Stack
| Tier | Technology |
|---|---|
| **Backend** | Django 5, Gunicorn, WhiteNoise |
| **Database** | MongoDB (Atlas or self-hosted) |
| **AI Orchestration** | n8n Webhook Integration |
| **Frontend** | Bootstrap 5, Modern CSS Animations |
| **Infrastructure** | Vercel Serverless, HTTPS, Environment Configured |

---

## 📁 Project Architecture
```text
📦 FraudB/
├── 📂 project_settings/ # Environment-driven configuration (email, hosts, security)
├── 📂 core/             # Dashboard, analytics, and primary application logic
├── 📂 api_app/          # Core Native API and ML bridging endpoints
├── 📂 accounts/         # Authentication, OTP, and user sessions
├── 📂 ml/               # Machine learning pipelines and rule engines
└── 📄 vercel.json       # Production deployment configuration
```

---

## ⚡ Quick Start (Local Development)

1. **Clone & Virtual Env:**
   ```bash
   git clone https://github.com/aaditi-singhh/FraudB.git
   cd FraudB
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment:**
   Create a `.env` file based on the generated template:
   ```bash
   cp .env.example .env
   ```
   *Ensure you provide your exact MongoDB Atlas URI and App Passwords for full functionality!*

4. **Run Server:**
   ```bash
   python manage.py collectstatic --noinput
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000` to dive in!

---

## 🔗 n8n AI Integration
- The platform emits transaction payloads directly to an `N8N_WEBHOOK_URL`.
- Expects a strict JSON response: `{ "reply": "..." }`.
- Readily supports token-based webhook security using `N8N_WEBHOOK_TOKEN`.

---

## � License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
