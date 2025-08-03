# Internal Process Tracker

A Python + PostgreSQL–based internal automation and reporting tool that simulates employee task management, time tracking, and weekly reporting — similar to real-world tools used in business process automation.

---

## 🚀 Project Overview

This tool mimics the backend of a company's internal operations system. It enables:

- Managing employees, tasks, and time logs
- Storing and querying relational data using PostgreSQL
- Automating weekly reporting using Python scripts
- Generating `.csv` summaries (e.g., hours per employee per task)

Built as a portfolio project to demonstrate backend automation and data-driven process tracking using modern tools.

---

## 🧰 Technologies Used

- **Python 3.10+**
- **PostgreSQL**
- **pandas**
- **psycopg2**
- **pgAdmin** (for manual DB inspection)

---


---

## 🗃️ Database Schema

```sql
-- Tables:
employees(id, name, department, hire_date)
tasks(id, name, deadline, assigned_to)
time_logs(id, employee_id, task_id, log_date, hours_logged)
tools(id, name, last_used, assigned_to)

📦 Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/Abhinanda0209/internal_process_tracker.git
cd internal_process_tracker
2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
3. Install dependencies
pip install -r requirements.txt
4. Set up the PostgreSQL database
Create a new database named tracker_db in pgAdmin.

Run database/schema.sql using pgAdmin’s Query Tool to create the tables.

5. Add your PostgreSQL credentials
Update scripts/config.py:

python
Copy
Edit
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'dbname': 'tracker_db',
    'user': 'your_username',
    'password': 'your_password'
}
6. Ingest data
python scripts/ingest_data.py
7. Generate the weekly time report
python scripts/generate_report.py
The summary will be saved to reports/time_summary.csv.

📈 Example Report Output
employee	task	total_hours
Alice Schmidt	Website Redesign	7.5
Bob Maier	Marketing Strategy	2.5
Carla Neumann	Audit Prep	5.0

📌 Future Improvements
Schedule weekly report generation using schedule or cron

Add .env file for safer credentials

Build a simple Flask dashboard for viewing data

Expand schema with tool usage analytics