# F1 Hub

A full-stack, production-style web platform for Formula 1 analytics, race replay, and predictive insights.

F1 Hub is designed as a scalable system that ingests historical race data, exposes it through a structured backend API, and delivers an interactive frontend experience with analytics dashboards, race replay, and ML-powered predictions.

---

## Overview

F1 Hub is not just a data science project—it is a software engineering–focused system that demonstrates:

* Backend API design and architecture
* Data modeling and pipeline design
* Event-driven and real-time systems
* Full-stack application development
* Optional machine learning integration

The project is intentionally built to resemble a real-world production application rather than a standalone notebook or demo.

---

## Core Features

### Analytics Dashboard

* Race-level and driver-level statistics
* Lap time analysis
* Tire stint breakdowns
* Position changes over time
* Teammate comparisons
* Aggregated performance metrics

---

### Race Replay Engine

* Replay historical races as if they were live
* Timeline-based playback (lap-by-lap or event-driven)
* Visualization of:

  * position changes
  * pit stops
  * gaps between drivers
* Playback controls:

  * pause / play
  * speed adjustment
  * timeline scrubbing

---

### Prediction Engine

* ML-powered predictions such as:

  * podium probability
  * position gain/loss likelihood
  * race outcome distributions
* Feature engineering from historical race data
* Model inference exposed via API

---

### AI Assistant (Chatbot)

* Natural language interface for querying F1 data
* Grounded in internal datasets and predictions
* Example queries:

  * “Compare tire degradation between two drivers”
  * “Who had the strongest race pace in this event?”
  * “Why does the model favor this driver?”

---

## System Architecture

F1 Hub follows a service-oriented architecture with clear separation of concerns.

### Frontend

* Framework: Next.js
* Responsibilities:

  * UI rendering
  * Data visualization
  * User interaction
  * Communication with backend APIs

### Backend API

* Framework: FastAPI
* Responsibilities:

  * Expose REST endpoints
  * Serve analytics data
  * Provide replay data streams
  * Handle prediction requests

### Database

* PostgreSQL
* Stores:

  * races
  * drivers
  * lap data
  * results
  * precomputed aggregates

### Cache Layer

* Redis
* Used for:

  * caching frequent queries
  * reducing API latency
  * storing temporary replay state

### Background Workers

* Task queue (e.g., Celery)
* Responsibilities:

  * data ingestion
  * feature generation
  * model training
  * scheduled data updates

---

## Data Pipeline

The system includes a data pipeline responsible for transforming raw F1 data into structured, queryable formats.

### Data Sources

* Historical race data (public datasets or APIs)
* Telemetry and lap timing data (when available)

### Pipeline Stages

1. Ingestion

   * Fetch raw race data
   * Normalize formats

2. Processing

   * Clean and validate data
   * Handle missing or inconsistent values

3. Feature Engineering

   * Generate lap-based metrics
   * Compute stint and tire degradation features
   * Aggregate race-level statistics

4. Storage

   * Persist processed data in PostgreSQL
   * Cache frequently accessed data in Redis

---

## API Design

The backend exposes structured REST endpoints.

### Example Endpoints

* `GET /health`
* `GET /races`
* `GET /races/{race_id}`
* `GET /races/{race_id}/laps`
* `GET /races/{race_id}/events`
* `GET /replay/{race_id}`
* `POST /predict`
* `POST /chat/query`

The API is designed with:

* clear resource-based routing
* separation of concerns
* stateless request handling

---

## Technology Stack

### Frontend

* Next.js
* React
* Charting libraries (e.g., Recharts, D3)

### Backend

* FastAPI
* Python

### Data and Storage

* PostgreSQL
* Redis

### Infrastructure

* Docker (planned)
* Docker Compose (local development)

### Background Processing

* Celery or equivalent task queue

### Machine Learning (Optional)

* scikit-learn / XGBoost / PyTorch
* Feature pipelines and model versioning

---

## Project Structure

```text
f1-hub/
  frontend/
  backend/
    app/
      api/
      models/
      services/
      schemas/
      main.py
    requirements.txt
  infra/
  docs/
  README.md
```

---

## Development Setup

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
pip install fastapi uvicorn
pip freeze > requirements.txt
```

Run the server:

```bash
uvicorn app.main:app --reload
```

Test endpoint:

```text
http://127.0.0.1:8000/health
```

---

### Frontend (planned)

```bash
cd frontend
npx create-next-app
npm run dev
```

---

## Roadmap

### MVP

* Backend API with race data
* Frontend shell
* Race list and race detail pages
* Basic analytics charts

### Phase 2

* Replay engine
* Prediction API
* Data pipeline improvements

### Phase 3

* AI assistant
* Caching and performance optimizations
* Background workers and scheduling

### Phase 4

* Deployment and infrastructure hardening
* Monitoring and observability
* Scalability improvements

---

## Goals

* Build a production-style system, not a prototype
* Demonstrate strong software engineering practices
* Integrate ML in a meaningful, system-oriented way
* Create a project suitable for SWE-focused roles

---

## License

This project is for educational and portfolio purposes.
