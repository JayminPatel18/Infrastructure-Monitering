# Infrastructure Monitoring & Incident Management System

## Setup
1. Create virtual environment
2. Install dependencies
3. Run server

## Commands
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

cd Infra_monitering
python -m venv venv        # only if venv missing
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload