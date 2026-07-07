# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog**, and this project adheres to **Semantic Versioning (SemVer)**.

---

## [Unreleased]

### Added

* Established GitHub-based project management workflow using Issues, Projects, Milestones, and Pull Requests.
* Introduced the `develop` branch workflow for feature-based development.
* Began implementation planning for the Log Generator Framework (Sprint 1).

---

## [v0.1.0] - 2026-07-07

### Added

#### Repository Initialization

* Initialized the SentinelSIEM repository.
* Established the project directory structure.
* Added licensing information.
* Added contributor guidelines.
* Configured Git and repository settings.

#### Documentation

* Added the project README.
* Documented the system architecture.
* Created the development roadmap.
* Added coding standards and engineering guidelines.
* Added the initial Architecture Decision Record (ADR-001).
* Introduced the engineering decision log.

#### Architecture

* Defined the modular SIEM architecture.
* Selected Python for log processing.
* Selected Node.js and Express for the backend API.
* Selected React and Vite for the frontend dashboard.
* Selected MongoDB for event storage.
* Planned JWT-based authentication.
* Planned Socket.IO for real-time event updates.
* Planned Docker-based deployment.

#### Engineering Standards

* Adopted Conventional Commits.
* Established the Git workflow (`main` → `develop` → `feature/*`).
* Adopted documentation-first development.
* Established modular architecture principles.
* Adopted type hints and PEP 8 coding standards.
* Established configuration-over-hardcoding philosophy.
* Adopted security-by-default and testability principles.

#### Project Planning

* Defined the phased roadmap from `v0.1` through `v1.0`.
* Planned the reusable Log Generator Framework.
* Designed the initial component architecture for the collector, processor, backend, frontend, and database.
* Defined future support for multiple log sources including SSH, Apache, Windows Event Logs, AWS CloudTrail, Azure Activity Logs, and Kubernetes Audit Logs.

#### GitHub

* Migrated the repository to a GitHub Organization.
* Adopted GitHub Issues as the single source of truth for task tracking.
* Began using GitHub Projects and Milestones for sprint and release planning.

---

<!--
Release Format

## [vX.Y.Z] - YYYY-MM-DD

### Added
-

### Changed
-

### Deprecated
-

### Removed
-

### Fixed
-

### Security
-
-->
