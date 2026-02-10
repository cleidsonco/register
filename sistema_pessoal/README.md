# 🧾 Personal Registration System

A simple **person registration system** developed in **Python**, featuring a graphical interface built with **Tkinter** and a database powered by **SQLite**.

---

## 📌 Features

✔ Register people  
✔ Search records by ID  
✔ Edit records  
✔ Delete records  
✔ Data validation  
✔ Modern blue and white interface  
✔ Automatic database creation  

---

## 🛠 Technologies Used

- Python 3
- Tkinter (Graphical User Interface)
- SQLite3 (Database)
- Regex (Data Validation)

---

## 📂 Project Structure

sistema_pessoal
│
├── banco
│ ├── init.py
│ └── registros_pessoas.py
│
├── interface
│ ├── init.py
│ ├── botoes.py
│ ├── telas.py
│ └── validacao.py
│
├── database
│ └── pessoas.db (created automatically)
│
├── init.py
└── main.py


---

## ▶ How to Run

### 1️⃣ Install Python

Make sure Python is installed:

https://www.python.org/downloads/


---

### 2️⃣ Download the Project

Clone or download the repository files.

---

### 3️⃣ Run the System

Open the terminal inside the project folder and run:

python main.py



---

## 💾 Database

The database is automatically created inside:

database/

Table structure:

| Field | Type |
|---------|------------|
| id | INTEGER |
| name | TEXT |
| age | INTEGER |
| email | TEXT |
| phone | TEXT |

---

## ✔ Validations

The system validates:

- Name cannot be empty
- Age must be a valid number
- Email must follow a valid format
- Phone must contain valid numbers

---

## 🎨 Interface

Modern interface theme using:

- Primary blue color
- Secondary blue color
- White background
- Centered card layout

---

## 🚀 Future Improvements

- Full record listing
- Search by name
- Phone input mask
- Dark mode theme
- Data export feature
- Multi-user system
- Convert to executable (.exe)

---

## 👨‍💻 Author

This project was developed for learning and practicing:

- Python programming
- GUI development
- Project organization
- CRUD operations with database

---

## 📜 License

Free for study and learning purposes.