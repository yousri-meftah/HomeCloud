# HomeCloud Platform

> Personal cloud VPS provisioning platform built on a homelab.

HomeCloud is a self-service platform that lets you register accounts, request Virtual Private Servers (VPS), and receive full remote access through an automated web interface. Built on Proxmox VE with Cloudflare Tunnel for public access.

## Architecture

- **Frontend**: Next.js 14 App Router, deployed to Cloudflare Workers
- **Backend**: Python + FastAPI, running on the homelab
- **Virtualization**: Proxmox VE 8 managing KVM VMs
- **Networking**: Cloudflare Tunnel per VM (no port forwarding)
- **Database**: PostgreSQL (Docker Compose)
- **Search**: Elasticsearch (Docker Compose)
- **Storage**: Cloudflare R2 (S3-compatible)

## Quick Start

### Prerequisites
- Proxmox VE 8 installed on homelab machine
- Cloudflare account with custom domain
- Stripe account (test mode)
- Docker and Docker Compose

### Setup

1. **Configure environment variables**
   \\\ash
   cp backend/.env.example backend/.env
   cp frontend/.env.example frontend/.env.local
   # Fill in your values
   \\\

2. **Start infrastructure services**
   \\\ash
   docker compose up -d
   \\\

3. **Backend**
   \\\ash
   cd backend
   uv sync
   uv run uvicorn src.main:app --reload
   \\\

4. **Frontend**
   \\\ash
   cd frontend
   npm install
   npm run dev
   \\\

## Project Structure

\\\
homecloud/
├── backend/              # FastAPI backend
│   ├── src/              # Application source
│   │   ├── auth/         # Authentication module
│   │   ├── vps/          # VPS lifecycle module
│   │   ├── billing/      # Stripe billing module
│   │   ├── ai/           # Gemini AI module
│   │   ├── admin/        # Admin panel module
│   │   ├── services/     # Proxmox, Tunnel, SSH services
│   │   ├── db/           # Models, schemas, engine
│   │   └── core/         # Security, encryption
│   └── tests/            # Backend tests
├── frontend/             # Next.js frontend
│   ├── src/
│   │   ├── app/          # App Router pages
│   │   ├── components/   # Reusable UI components
│   │   ├── lib/          # Utilities, API client
│   │   ├── hooks/        # React hooks
│   │   └── types/        # TypeScript types
│   └── tests/            # Frontend tests
├── infra/                # Infrastructure scripts
│   ├── proxmox/          # Proxmox setup scripts
│   └── cloudflare/       # Cloudflare configs
├── docs/                 # Documentation
├── scripts/              # Deployment scripts
└── docker-compose.yml    # PostgreSQL + Elasticsearch
\\\

## Implementation Plan

See \PLAN.md\ in the project root for the complete step-by-step implementation plan.

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 14, shadcn/ui, Tailwind CSS |
| Backend | Python 3.12, FastAPI, uv |
| Virtualization | Proxmox VE 8, KVM |
| Networking | Cloudflare Tunnel |
| Database | PostgreSQL 16, SQLAlchemy, Alembic |
| Search | Elasticsearch 8 |
| Storage | Cloudflare R2 |
| Payments | Stripe (test mode) |
| AI | Google Gemini |
| Monitoring | Sentry |
| CI/CD | GitHub Actions |

## License

Educational prototype - not for production use.
