# FPL-Transfer-Analysis - ![Documentation](https://img.shields.io/badge/Docs-In%20Progress-blue) ![Development Status](https://img.shields.io/badge/Development-Active-lightgreen) ![Production Status](https://img.shields.io/badge/Production-Not%20Available-lightgrey)



## Overview
FPL-Transfer-Analysis is a tool designed to help Fantasy Premier League (FPL) managers make informed decisions on which players to transfer into their team. The project leverages past gameweek statistics and machine learning models to predict player performance. It includes a **backend** built with FastAPI for data processing and analysis, and a **frontend** built with React (using Vite) for visualizing insights.

## Features
- Fetch and preprocess player statistics from reliable data sources.
- Analyze team and player performance, including attack and defense patterns.
- Machine learning-based predictions for player performance.
- Interactive and intuitive web interface to display insights.

---

## Project Structure

```plaintext
FPL-Transfer-Analysis
├── backend/                  # Backend (FastAPI)
│   ├── src/                  # Source code for backend
│   └── tests/                # Unit tests for backend
│   ├── Dockerfile            # Backend Dockerfile
│   ├── __init__.py           # Backend package initializer
│   ├── requirements.txt      # Python dependencies
├── frontend/                 # Frontend (React + Vite)
│   ├── src/                  # React source code
│   ├── public/               # Static assets
│   ├── Dockerfile            # Frontend Dockerfile
│   ├── package.json          # Node.js dependencies
│   |── .env                  # Frontend Environment variables
├── notebooks/                # Jupyter notebooks for exploration
├── scraper/                  # Scraper for fetching data
│   ├── src/                  # Source code for scraper
│       ├── jobs/             # Scheduled jobs for scraping
│       └── scrapers/         # Individual scraper implementations
│   └── Dockerfile            # Scraper Dockerfile
│   ├── __init__.py           # Scraper package initializer
│   ├── config.py             # Configuration for scraper
│   ├── requirements.txt      # Python dependencies for scraper
└── shared/                   # Shared utilities and modules
  └── data_processing/        # Data processing scripts and modules
├── docker-compose.prod.yml   # Production Docker Compose
├── docker-compose.yml        # Development Docker Compose
├── README.md                 # Documentation
├── poetry.lock               # Poetry lock file for dependencies
├── pyproject.toml            # Poetry project configuration
├── requirements.txt          # Python dependencies
```
---

## Setup Instructions

### Prerequisites
- **Docker**: Ensure Docker is installed and running.
- **Python 3.10+**: For running backend scripts locally (optional).
- **Node.js**: For frontend development (optional).

---

### 1. Clone the Repository
```bash
git clone <repository-url>
cd FPL-Transfer-Analysis
```

### 2. Set Up Environment Variables

#### Frontend
Create a `.env` file in the project with the following content:

```env
VITE_BACKEND_URL=http://localhost:8000
```

---

### 3. Run the Project Locally (Development)
Use Docker Compose to start the backend and frontend with live reloading:

```bash
docker-compose up --build
```

- **Frontend**: Accessible at `http://localhost:5173`.
- **Backend**: Accessible at `http://localhost:8000`.

---

### 4. Run the Project in Production
Use the production Docker Compose file for an optimized setup:

```bash
docker-compose -f docker-compose.prod.yml up --build
```

- **Frontend**: Accessible at `http://localhost`.
- **Backend**: Accessible at `http://localhost:8000`.

---

### 5. Project Commands

#### Backend
- **Install dependencies locally**:
  ```bash
  pip install -r backend/requirements.txt
  ```
- **Run the backend locally**:
  ```bash
  cd backend
  uvicorn api:app --reload
  ```

#### Frontend
- **Install dependencies locally**:
  ```bash
  cd frontend
  npm install
  ```
- **Run the frontend locally**:
  ```bash
  npm run dev
  ```

---

## Contributing
Contributions are welcome! Please create a pull request for any enhancements or bug fixes.

---

## License
This project is licensed under the MIT License.


