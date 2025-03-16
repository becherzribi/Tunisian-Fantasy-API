# ⚽ Tunisian Fantasy API

## 🚀 Project Overview
The **Tunisian Fantasy API** is a web-based platform designed to empower Tunisian football fans by enabling them to create and manage fantasy teams based on the **Tunisian Ligue 1**. This localized solution bridges the gap in fantasy sports for Tunisia’s football league, offering secure, scalable, and engaging features tailored to local enthusiasts.

## 👥 Team & Supervision
- **Developer:** Becher Zribi
- **Supervisor:** Montassar Ben Messaoud
- **Module:** IT 325
- **Institution:** Tunis Business School, University of Tunis

## 🏆 Why This Project?
- 🌍 **Football Unites Tunisia:** A national passion with no dedicated fantasy platform.
- ⚡ **Global Inspiration:** Fans currently use international leagues (e.g., Premier League Fantasy).
- 🔥 **Local Opportunity:** Celebrate Tunisian football culture and enhance fan engagement.

## ✨ Key Features
### ✅ Secure Authentication
- 🔑 **JWT-based** user registration, login, refresh, and logout.
- 🛡️ **Role-based access control** (admin vs. regular users).

### 🧩 Fantasy Team Management
- ➕ **Create, update, and delete fantasy teams.**
- 📊 **Track team performance and points.**

### 👥 Player & Match Management
- ⚽ **Add/update players** and retrieve live match details (home team, away team, score).

### 🏆 Leaderboard & Social Sharing
- 📈 **Real-time rankings** of fantasy teams.
- 🐦 **Twitter Integration:** Share achievements directly on Twitter.

### 👑 Admin Dashboard
- 🛠️ **Manage users**, promote admins, and delete accounts.

## 📜 Workflow
### 🔹 1. User Registration & Authentication
- Users register with email/password and receive a **JWT token**.
- Admins can promote users or manage accounts.

### 🔹 2. Team Creation & Management
- Users **build fantasy teams** by selecting Tunisian Ligue 1 players.
- Update **team names** or **player rosters** via API endpoints.

### 🔹 3. Matchday Interaction
- View **live match data** (scores, teams).
- Earn points based on **player performance**.

### 🔹 4. Track & Share Progress
- Climb the **leaderboard** and share milestones on **Twitter**.

## 🛠 Tech Stack
### 🔧 Backend & Database
- **Python Flask** 🐍 - Lightweight RESTful API framework.
- **SQLite + SQLAlchemy** 🗃️ - Database management with ORM.
- **Flask-Smorest** 📡 - API route organization and documentation.

### 🔒 Security & Tools
- **JWT** 🔐 - Secure token-based authentication.
- **Swagger UI** 📝 - Interactive API documentation.
- **Flask-Limiter** ⏳ - Rate limiting for abuse prevention.

## 🚧 Challenges & Future Work
- 🚩 **Limited Real-Time Data:** Reliance on seed data due to lack of free Tunisian league APIs.
- 🚀 **Scalability:** Optimize for high traffic and integrate live match updates.
- 📱 **Mobile App:** Future goal to expand into a cross-platform application.

## 📥 Setup & Installation
### 📌 Prerequisites
- **Python 3.8+**, Pip, SQLite

### 📝 Steps to Run
1. **Clone the repository:**
   ```sh
   git clone https://github.com/becherzribi/tunisian-fantasy-api.git  
   ```
2. **Install dependencies:**
   ```sh
   pip install flask flask-smorest flask-jwt-extended sqlalchemy  
   ```
3. **Start the server:**
   ```sh
   flask run  
   ```
4. **Access Swagger UI:**
   - Visit: [http://localhost:5000/api/docs](http://localhost:5000/api/docs) to explore endpoints.
## 📄 Research Paper  
You can read the full paper detailing the **Tunisian Fantasy API** project here:  
[📑 Read the Paper](./path-to-your-paper.pdf)  

## 📩 Contact
📌 **Becher Zribi**
- ✉️ Email: [zribibecher.tn@gmail.com](mailto:zribibecher.tn@gmail.com)
- 🔗 LinkedIn: [Becher Zribi](https://www.linkedin.com/in/becher-zribi/)
- 🌐 GitHub Repository: [Tunisian Fantasy API](https://github.com/becherzribi/tunisian-fantasy-api)

---
**⚽ Tunisian Fantasy API - Empowering Football Fans, One Match at a Time! 🏆**
