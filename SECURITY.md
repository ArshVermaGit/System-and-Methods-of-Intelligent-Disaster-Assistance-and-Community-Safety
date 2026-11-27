# Security Policy

## Supported Versions

| Project Phase | Supported |
|---|---|
| Phase I (Development) | :white_check_mark: |

## Reporting Vulnerabilities & Credential Exposures

The security of this project and the integrity of our geospatial infrastructure is important.

### 1. Accidental Credential Exposure
If you discover that API keys, database credentials (PostgreSQL / PostGIS), Copernicus/NASA Earthdata tokens, or server secrets have been committed:
- **Do not** open a public GitHub issue.
- Immediately notify repository administrators (@ArshVermaGit) or team members.
- Immediately revoke and rotate the affected credential in the corresponding provider console.

### 2. Software Vulnerabilities
If you identify a security vulnerability in the backend services (FastAPI), geospatial pipelines, or frontend dashboard:
- Create a private advisory via GitHub Security Advisories, or contact the team leads directly.
- Provide a summary of the issue, potential impact, and steps to reproduce.

### 3. Data Integrity & Geospatial Scope
- Model predictions and hazard assessments produced by this project are intended for research, preparedness, and academic evaluation under EPICS Phase I.
- This platform does not replace official meteorological or government disaster warning authorities.
