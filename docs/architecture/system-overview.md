# SentinelSIEM - System Overview

## Introduction

SentinelSIEM is a lightweight, modular, open-source Security Information and Event Management (SIEM) platform designed for educational purposes and portfolio demonstration.

The project aims to simulate the core functionality of enterprise SIEM solutions by collecting security logs, parsing and normalizing events, detecting suspicious activity, storing security events, and presenting them through a web dashboard.

## Objectives

-   Understand SIEM architecture
-   Build modular cybersecurity software
-   Implement detection engineering concepts
-   Learn secure backend development
-   Demonstrate cloud-ready architecture

---

## High-Level Architecture

```mermaid
%%{init: {"theme": "dark"}}%%
flowchart LR
    sources[Log Sources] -->|raw events| collector[Collector]
    collector -->|raw logs| processor[Processor]
    processor -->|structured events| detection[Detection Engine]
    detection -->|events and alerts| backend
    backend[Backend API] <-->|query and persist| database
    frontend[Frontend Dashboard] -->|REST API requests| backend

    classDef component fill:#1f2937,stroke:#38bdf8,color:#f8fafc,stroke-width:2px
    classDef storage fill:#312e81,stroke:#a78bfa,color:#f8fafc,stroke-width:2px
    class sources,collector,processor,detection,backend,frontend component
    class database storage
```

---

## Components

### Collector

Responsible for receiving or generating logs.

Responsibilities:

-   Generate sample logs
-   Receive logs from different sources
-   Pass raw logs to the Processor

---

### Processor

Converts raw log text into structured JSON.

Responsibilities:

-   Parse logs
-   Normalize fields
-   Validate log format

---

### Detection Engine

Analyzes structured logs using security rules.

Responsibilities:

-   Detect brute force attacks
-   Detect suspicious logins
-   Generate alerts

---

### Database

Stores processed logs and alerts.

Collections:

-   logs
-   alerts
-   rules
-   users

---

### Backend API

Provides REST endpoints.

Examples:

GET /logs

GET /alerts

POST /rules

GET /stats

---

### Frontend Dashboard

Allows analysts to monitor events.

Features:

-   Dashboard
-   Log Viewer
-   Alert Viewer
-   Analytics
-   Rule Management

---

## Data Flow

```mermaid
%%{init: {"theme": "dark"}}%%
flowchart TD
    source[Security Event] --> collector[Collector receives event]
    collector --> processor[Processor parses and normalizes]
    processor --> detection{Detection rules match?}
    detection -->|yes| alert[Generate alert]
    detection -->|no| event[Keep processed event]
    alert --> api[Backend API]
    event --> api
    api <-->|query and persist| storage[(MongoDB)]
    api --> dashboard[Dashboard displays logs and alerts]

    classDef step fill:#1f2937,stroke:#38bdf8,color:#f8fafc,stroke-width:2px
    classDef decision fill:#713f12,stroke:#fbbf24,color:#f8fafc,stroke-width:2px
    classDef storage fill:#312e81,stroke:#a78bfa,color:#f8fafc,stroke-width:2px
    class source,collector,processor,alert,event,api,dashboard step
    class detection decision
    class storage storage
```

1. Log source creates a security event.

2. Collector receives the event.

3. Processor converts it into structured JSON.

4. Detection Engine evaluates the event.

5. Alerts are generated if rules match.

6. Data is stored in MongoDB.

7. Backend exposes REST APIs.

8. Dashboard displays results.

---

## Future Enhancements

-   Docker deployment
-   Kubernetes support
-   AWS CloudTrail ingestion
-   Sigma rule compatibility
-   Threat Intelligence integration

-   # Machine Learning anomaly detection
-   Machine Learning anomaly detection
