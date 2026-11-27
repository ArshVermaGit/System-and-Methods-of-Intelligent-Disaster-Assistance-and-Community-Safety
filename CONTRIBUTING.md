# Contributing to Intelligent Disaster Assistance and Community Safety

Thank you for contributing to the **System and Methods of Intelligent Disaster Assistance and Community Safety** (EPICS Phase I, VIT Bhopal University).

This document outlines the development workflow, coding standards, pull request process, and data management rules for all team members and contributors.

---

## 1. Getting Started

### Prerequisites
- Python 3.10 or 3.11
- Node.js 18+ and npm (for frontend dashboard development)
- Git & Git LFS / DVC (Data Version Control)
- Docker & Docker Compose (for local PostgreSQL/PostGIS setup)

### Local Environment Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ArshVermaGit/System-and-Methods-of-Intelligent-Disaster-Assistance-and-Community-Safety.git
   cd System-and-Methods-of-Intelligent-Disaster-Assistance-and-Community-Safety
   ```

2. **Set up Python Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Install Pre-commit Hooks:**
   ```bash
   pip install pre-commit
   pre-commit install
   ```

4. **Configure Environment Variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your local credentials. NEVER commit .env to git!
   ```

---

## 2. Branching & Git Workflow

We use a feature-branch workflow. Direct pushes to `main` are restricted.

### Branch Naming Conventions
Create branches from `main` using descriptive prefixes:
- `feat/<feature-name>`: New capabilities (e.g., `feat/flood-segmentation-unet`)
- `fix/<bug-name>`: Bug fixes (e.g., `fix/postgis-query-timeout`)
- `ml/<experiment-name>`: Machine learning training & evaluation pipelines
- `geospatial/<task>`: Raster processing, OSM ingestion, DEM processing
- `docs/<topic>`: Documentation updates, architecture notes
- `refactor/<module>`: Code restructuring without functional changes

### Commit Messages (Conventional Commits)
All commit messages and PR titles must follow conventional commit formatting:
```
<type>: <short imperative summary>
```

**Allowed types:**
- `feat`: New feature or capability
- `fix`: Bug fix
- `model`: ML/DL architecture, weights, or pipeline adjustment
- `geospatial`: Geospatial data ingestion or raster transformation
- `refactor`: Code reorganization
- `perf`: Performance enhancement
- `test`: Adding or adjusting unit/integration tests
- `docs`: README, architecture specs, report documentation
- `ci`: GitHub Actions workflows or repository tooling
- `chore`: Maintenance tasks, dependencies

---

## 3. Pull Request Guidelines

### Opening a Pull Request
1. Ensure your local branch is updated with the latest `main`:
   ```bash
   git checkout main
   git pull origin main
   git checkout your-feature-branch
   git rebase main
   ```
2. Run pre-commit checks and tests locally:
   ```bash
   pre-commit run --all-files
   pytest
   ```
3. Push your branch and open a Pull Request using the pre-filled template.
4. Link any related issues (`Closes #123`).

### PR Review & Merge Process
- **Automated CI:** Every PR triggers the CI pipeline (Linting, syntax checks, large file scan, security scan). All checks must pass.
- **Review Requirement:** Every PR requires at least one peer approval from a team member before merging.
- **Merge Strategy:** Prefer **Squash and Merge** or **Rebase and Merge** to maintain a clean linear history on `main`.

---

## 4. Geospatial Data & ML Asset Policy (DVC)

To prevent repository bloat and performance degradation:

> **CRITICAL RULE:** Never commit raw dataset files (`.tif`, `.nc`, `.h5`, `.zip`, `.gpkg`, large `.csv` dumps) or model weights (`.pt`, `.pth`, `.bin`) directly to Git.

- Use **DVC (Data Version Control)** to track datasets:
  ```bash
  # Track raw imagery or masks
  dvc add data/raw/sentinel1_sample.tif
  # Commit the generated pointer file to Git
  git add data/raw/sentinel1_sample.tif.dvc .gitignore
  git commit -m "data: track sentinel-1 sample imagery via dvc"
  ```
- Store DVC caches in the shared remote storage designated by the team.

---

## 5. Security & Credentials

- Never commit passwords, API tokens, database URIs, or private keys.
- Always use environment variables read via `.env` and Pydantic Settings.
- If you accidentally commit a credential, immediately inform the team lead and revoke the compromised token.

---

## 6. Team Collaboration Standards

- Keep discussions constructive, respectful, and goal-oriented.
- When reviewing PRs, provide actionable, friendly feedback.
- Document any architectural decisions or experimental results in `docs/`.
