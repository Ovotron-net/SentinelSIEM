# SentinelSIEM

A lightweight, modular, open-source **SIEM (Security Information and Event Management)** platform for real-time log analysis and threat monitoring — built for SOC and blue-team workflows.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Issues](https://img.shields.io/github/issues/Ovotron-net/SentinelSIEM)](https://github.com/Ovotron-net/SentinelSIEM/issues)
[![Stars](https://img.shields.io/github/stars/Ovotron-net/SentinelSIEM)](https://github.com/Ovotron-net/SentinelSIEM/stargazers)
[![LinkedIn](https://shields.io/badge/LinkedIn-0077b5)](https://linkedin.com/in/bhavyakantawala/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BhavyaKantawala)


---

## About

SentinelSIEM aims to give small security teams and hobbyist blue-teamers a self-hostable, no-frills alternative to heavyweight commercial SIEM platforms. It ingests logs and events, normalizes and stores them, and surfaces alerts through a simple web dashboard — without requiring a dedicated data engineering team to stand up.

The project is intentionally modular: the pieces that ingest and process logs, the API that serves data, and the dashboard that visualizes it are separated so any piece can be swapped, scaled, or run independently.


## Project Management

SentinelSIEM uses GitHub's built-in project management features to plan, track, and review development.

* **GitHub Issues** are used to track features, bugs, enhancements, and technical tasks.
* **GitHub Projects** are used to organize work by sprint and monitor development progress.
* **Milestones** group issues into planned releases (e.g., `v0.2`, `v0.3`).
* **Pull Requests** are required for all code changes and serve as the primary code review mechanism.

The `docs/` directory is reserved for long-lived technical documentation such as architecture, engineering decisions, API documentation, roadmaps, and design artifacts. To avoid duplicate sources of truth, task tracking documentation is maintained exclusively through GitHub Issues rather than Markdown files within the repository.


## Features

- 🔍 **Real-time log ingestion** and event processing pipeline
- 🧩 **Modular architecture** — backend, processor, and frontend run as independent services
- 🔐 **JWT-based authentication** for API access
- 📊 **Web dashboard** for browsing events and reviewing alerts
- 🗄️ **MongoDB** for flexible, schema-light event storage
- ⚙️ Configurable via environment variables for easy deployment

> Some features above reflect the project's direction — check [open issues](https://github.com/Ovotron-net/SentinelSIEM/issues) and the [`docs`](docs) folder for the current state of implementation.

## Architecture

The repository is organized into independent modules:

```
SentinelSIEM/
├── backend/       # REST API — auth, data access, alert logic
├── processor/      # Log ingestion & event processing pipeline
├── frontend/        # Web dashboard (UI)
├── docs/            # Project documentation
├── .env.sample       # Example environment configuration
└── docker-compose.yml # Multi-service local orchestration
```

At a high level, logs flow from your sources into the **processor**, which normalizes and forwards events to the **backend**, which persists them to MongoDB and exposes them via API to the **frontend** dashboard.

## Tech Stack

- **Database:** MongoDB
- **Backend:** Node.js/Express-style REST API, JWT authentication
- **Frontend:** Web-based dashboard
- **Orchestration:** Docker Compose

## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (LTS recommended)
- [MongoDB](https://www.mongodb.com/) (local instance or Atlas)
- [Docker](https://www.docker.com/) & Docker Compose (optional, for containerized setup)
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Ovotron-net/SentinelSIEM.git
cd SentinelSIEM
```

### 2. Configure environment variables

Copy the sample environment file and update the values for your setup:

```bash
cp .env.sample .env
```

```env
MONGO_URI=mongodb://localhost:27017/sentinelsiem
JWT_SECRET=replace_me
PORT=5000
LOG_LEVEL=INFO
```

⚠️ **Always replace `JWT_SECRET` with a strong, unique secret before deploying anywhere beyond your local machine.**

### 3. Install dependencies

Install dependencies for each module you plan to run:

```bash
cd backend && npm install
cd ../frontend && npm install
cd ../processor && npm install
```

### 4. Start MongoDB with Docker Compose

The current Compose setup runs MongoDB, which the application uses for storage. It does not yet build or run the backend, processor, or frontend; run those from the source checkout once their modules are implemented.

```bash
docker compose up -d
docker compose ps
```

The database is available at `mongodb://localhost:27017/sentinelsiem`. Set `MONGO_URI` in `.env` to this value when running application modules on your host. This development database has no authentication enabled and is bound to localhost; do not change the bind address or expose it to untrusted networks.

To stop the container while keeping its data:

```bash
docker compose down
```

To also delete the stored database data:

```bash
docker compose down --volumes
```

### 5. Application modules (unavailable)

The backend, processor, and frontend are currently placeholders and cannot be started yet. The current setup provides MongoDB only.

## Project Structure Notes

- **`backend/`** — handles authentication, exposes REST endpoints, and talks to MongoDB.
- **`processor/`** — responsible for ingesting raw logs/events and normalizing them before they reach the backend.
- **`frontend/`** — the dashboard UI for reviewing events and alerts.
- **`docs/`** — supplementary documentation; check here for deeper dives as the project grows.

## Roadmap

- [ ] Expand detection rule support
- [ ] Add alerting integrations (email, Slack, webhook)
- [ ] Improve dashboard visualizations
- [ ] Add role-based access control
- [ ] Publish full API documentation

Have an idea? [Open an issue](https://github.com/Ovotron-net/SentinelSIEM/issues) to discuss it.

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to get set up, our branching/commit conventions, and how to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

Built and maintained by **Bhavya Kantawala** with the help of [Ovotron-net](https://github.com/Ovotron-net) and other contributors. Thanks to everyone who files issues, submits PRs, or spreads the word.
