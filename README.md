# FPL-Transfer-Analysis

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
FPL-Transfer-Analysis/
├── backend/                  # Backend (FastAPI)
│   ├── Dockerfile            # Backend Dockerfile
│   ├── requirements.txt      # Python dependencies
│   ├── api.py                # Main FastAPI app
│   ├── data_ingestion.py     # Script for fetching data
│   ├── preprocessing.py      # Script for data preprocessing
│   ├── model.py              # ML model implementation
│   ├── utils.py              # Utility functions
│   |── .env                  # Backend Environment variables
├── frontend/                 # Frontend (React + Vite)
│   ├── Dockerfile            # Frontend Dockerfile
│   ├── package.json          # Node.js dependencies
│   ├── src/                  # React source code
│   ├── public/               # Static assets
│   |── .env                  # Frontend Environment variables
├── data/                     # Data folder (raw/processed data)
├── notebooks/                # Jupyter notebooks for exploration
├── tests/                    # Unit tests for backend
├── docker-compose.yml        # Development Docker Compose
├── docker-compose.prod.yml   # Production Docker Compose
├── README.md                 # Documentation
└── .env                      # Shared Environment variables
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


