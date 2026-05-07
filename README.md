# HomeCloud Platform

> Personal cloud VPS provisioning platform built on a homelab.

HomeCloud is a self-service platform that lets you register accounts, request Virtual Private Servers (VPS), and receive full remote access through an automated web interface. Built on Proxmox VE with Cloudflare Tunnel for public access.

## Architecture

- **Frontend**: Next.js App Router + shadcn/ui, deployed to Cloudflare Pages/Workers
- **Backend**: Python 3.12 + FastAPI, layered architecture (api → controllers → services → models)
- **Virtualization**: Proxmox VE 8 managing KVM VMs
- **Networking**: Cloudflare Tunnel per VM (no port forwarding)
- **Database**: PostgreSQL 16 (Docker Compose)
- **Search**: Elasticsearch 8 (Docker Compose)
- **Storage**: Cloudflare R2 (S3-compatible)
- **Payments**: Stripe (test mode)
- **AI**: Google Gemini

## Quick Start

### Prerequisites

- Python 3.12+, [uv](https://docs.astral.sh/uv/) package manager
- Node.js 20+
- Docker & Docker Compose
- Proxmox VE 8 on homelab machine
- Cloudflare account with custom domain

### 1. Start infrastructure

```bash
docker compose up -d
```

This starts PostgreSQL 16 and Elasticsearch 8.

### 2. Backend

```bash
cd backend
cp envs/database.example envs/.env.database
cp envs/proxmox.example envs/.env.proxmox
cp envs/cloudflare.example envs/.env.cloudflare
cp envs/stripe.example envs/.env.stripe
cp envs/email.example envs/.env.email
cp envs/monitoring.example envs/.env.monitoring
uv sync
uv run alembic upgrade head
uv run uvicorn src.main:app --reload
```

API available at `http://localhost:8000`, docs at `/docs`.

### 3. Frontend

```bash
cd frontend
npm install
npm run dev
```

App available at `http://localhost:3000`.

### 4. Deploy frontend to Cloudflare

```bash
cd frontend
npm run build:cf
npm run deploy
```

## Project Structure

```
homecloud/
├── backend/                    # FastAPI backend
│   ├── src/
│   │   ├── api/                # Router definitions (topology only)
│   │   ├── controllers/        # Request handlers
│   │   ├── services/           # Business logic stubs
│   │   ├── models/             # SQLAlchemy ORM models
│   │   ├── schemas/            # Pydantic request/response schemas
│   │   ├── enums/              # Enumerations (VPSPlan, VPSStatus, UserRole)
│   │   ├── config/             # Settings + env loader
│   │   ├── db/                 # Engine, session, Base
│   │   └── main.py             # FastAPI app entry
│   ├── migrations/             # Alembic async migrations
│   ├── docker/                 # Dockerfile + entrypoint
│   ├── envs/                   # Scoped .env.* files (gitignored)
│   ├── tests/
│   └── pyproject.toml
├── frontend/                   # Next.js App Router
│   ├── src/
│   │   ├── app/
│   │   │   ├── (auth)/         # Auth route group (login, register, verify)
│   │   │   └── (dashboard)/    # Dashboard route group (vps, billing, ai, admin)
│   │   ├── components/         # UI components
│   │   ├── hooks/              # React hooks
│   │   ├── lib/                # Utilities, API client
│   │   ├── styles/             # Global styles
│   │   └── types/              # TypeScript types
│   ├── wrangler.jsonc
│   └── package.json
├── docker-compose.yml          # PostgreSQL + Elasticsearch + Backend
└── README.md
```

## Environment Variables

Backend env files are scoped by service in `backend/envs/`. Commit only the `*.example`
templates and keep the real `.env.*` files local:

| File | Purpose |
|------|---------|
| `.env.database` | PostgreSQL connection |
| `.env.proxmox` | Proxmox VE API credentials |
| `.env.cloudflare` | Cloudflare API token + zone |
| `.env.stripe` | Stripe keys + price IDs |
| `.env.email` | SMTP credentials |
| `.env.monitoring` | Sentry DSN, Elasticsearch URL |

All real `.env.*` files are gitignored. Copy the templates and fill in your values.

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js, shadcn/ui, Tailwind CSS |
| Backend | Python 3.12, FastAPI, uv |
| Virtualization | Proxmox VE 8, KVM |
| Networking | Cloudflare Tunnel |
| Database | PostgreSQL 16, SQLAlchemy 2, Alembic |
| Search | Elasticsearch 8 |
| Storage | Cloudflare R2 |
| Payments | Stripe (test mode) |
| AI | Google Gemini |
| Monitoring | Sentry |

## License

Educational prototype — not for production use.
