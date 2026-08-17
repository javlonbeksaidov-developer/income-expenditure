# 💰 Income & Expenditure

<p align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&pause=1000&color=00C853&center=true&vCenter=true&width=700&lines=Income+%26+Expenditure;FastAPI+Backend+Project;Track+Your+Money+%F0%9F%92%B8" alt="Typing SVG" />

<br>

<img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
<img src="https://img.shields.io/badge/SQLite-3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
<img src="https://img.shields.io/badge/SQLAlchemy-2.x-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" />

<br><br>

<img src="https://img.shields.io/github/stars/javlonbeksaidov-developer/income-expenditure?style=social" />
<img src="https://img.shields.io/github/forks/javlonbeksaidov-developer/income-expenditure?style=social" />

</p>

---

## 🚀 About

**Income & Expenditure** — daromad va xarajatlarni boshqarish uchun yaratilgan **REST API backend** loyihasi.

Loyiha **FastAPI + SQLite + SQLAlchemy** yordamida ishlab chiqilgan va CRUD amallarini bajarishga mo‘ljallangan.

> 🎯 Maqsad: kirim va chiqimlarni qulay boshqarish, ma'lumotlarni SQLite bazasida saqlash va REST API orqali ulardan foydalanish.

---

## ✨ Features

| Feature             | Description              |
| :------------------ | :----------------------- |
| 💰 **Income**       | Kirimlarni boshqarish    |
| 💸 **Expenditure**  | Chiqimlarni boshqarish   |
| 🏢 **Departments**  | Bo‘limlarni boshqarish   |
| 👨‍💼 **Employees** | Xodimlar bilan ishlash   |
| ➕ **Create**        | Yangi ma'lumot qo‘shish  |
| 📋 **Read**         | Ma'lumotlarni olish      |
| ✏️ **Update**       | Ma'lumotlarni yangilash  |
| 🗑️ **Delete**      | Ma'lumotlarni o‘chirish  |
| 🗄️ **SQLite**      | Lokal ma'lumotlar bazasi |
| ⚡ **FastAPI**       | Tezkor REST API          |

---

## 🛠 Tech Stack

| Technology        | Purpose                            |
| :---------------- | :--------------------------------- |
| 🐍 **Python**     | Backend dasturlash tili            |
| ⚡ **FastAPI**     | REST API framework                 |
| 🗄️ **SQLite**    | Ma'lumotlar bazasi                 |
| 🔗 **SQLAlchemy** | ORM                                |
| 📦 **Pydantic**   | Schema va validation               |
| 🎨 **Static**     | Frontend/static fayllar            |
| 🧩 **FigJam**     | Project planning & database design |

---

## 📂 Project Structure

```text
income-expenditure/
│
├── database/
│   └── database.py
│
├── models/
│   └── models.py
│
├── routes/
│   └── router.py
│
├── schemas/
│   └── schemas.py
│
├── static/
│   ├── figjam.txt
│   └── tables.png
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔌 API

### CRUD Operations

|    Method   | Endpoint    | Action               |
| :---------: | :---------- | :------------------- |
|   🟢 `GET`  | `/...`      | Ma'lumotlarni olish  |
|   🟢 `GET`  | `/.../{id}` | Bitta ma'lumot       |
|  🔵 `POST`  | `/...`      | Yangi ma'lumot       |
|   🟡 `PUT`  | `/.../{id}` | Ma'lumotni yangilash |
| 🔴 `DELETE` | `/.../{id}` | Ma'lumotni o‘chirish |

> 📌 Endpointlar loyihaning `routes/` papkasida tashkil qilingan.

---

## ⚡ Installation

### 1️⃣ Clone

```bash
git clone https://github.com/javlonbeksaidov-developer/income-expenditure.git

cd income-expenditure
```

### 2️⃣ Virtual Environment

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run

```bash
uvicorn main:app --reload
```

---

## 📖 API Documentation

Server ishga tushgandan so‘ng:

```text
http://127.0.0.1:8000/docs
```

FastAPI avtomatik **Swagger UI** documentation yaratadi.

```text
http://127.0.0.1:8000/redoc
```

Qo‘shimcha **ReDoc** documentation.

---

## 🔄 CRUD Flow

```text
        POST
         │
         ▼
   ┌─────────────┐
   │   CREATE    │
   └──────┬──────┘
          │
          ▼
   ┌─────────────┐
   │   DATABASE  │
   └──────┬──────┘
          │
     ┌────┴────┐
     ▼         ▼
   GET        PUT
     │         │
     ▼         ▼
   READ      UPDATE
               │
               ▼
            DELETE
```

---

## 🎯 Project Goals

* ✅ FastAPI bilan REST API yaratish
* ✅ SQLAlchemy ORM bilan ishlash
* ✅ SQLite database bilan ishlash
* ✅ CRUD operatsiyalarini amalda qo‘llash
* ✅ Backend architecture'ni tushunish
* ✅ API documentation bilan ishlash

---

## 🧪 Development

Loyihani development rejimida ishga tushirish:

```bash
uvicorn main:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## 👨‍💻 Author

<p align="center">

<b>Javlonbek Saidov</b>

<br><br>

<a href="https://github.com/javlonbeksaidov-developer">
<img src="https://img.shields.io/badge/GitHub-Javlonbek%20Saidov-181717?style=for-the-badge&logo=github" />
</a>

<a href="https://www.linkedin.com/in/javlon-saidov-566572399/">
<img src="https://img.shields.io/badge/LinkedIn-Javlonbek%20Saidov-0A66C2?style=for-the-badge&logo=linkedin" />
</a>

</p>

---

<p align="center">

⭐ **If you like this project, don't forget to give it a star!**

<br><br>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer"/>

</p>
