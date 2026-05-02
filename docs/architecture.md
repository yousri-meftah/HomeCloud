# HomeCloud Architecture

## System Overview

HomeCloud is a personal cloud platform built on a homelab machine running Proxmox VE. It provides a self-service web interface for VPS provisioning.

## Layers

1. **Frontend** (Next.js on Cloudflare Workers) - User dashboard and management UI
2. **Backend API** (FastAPI) - Business logic, provisioning orchestration
3. **Virtualization** (Proxmox VE 8) - KVM VM management
4. **Networking** (Cloudflare Tunnel) - Per-VM public access without port forwarding
5. **Storage** (PostgreSQL + Cloudflare R2) - Structured and unstructured data
6. **Observability** (Sentry + Elasticsearch) - Error tracking and search

## Data Flow

User -> Cloudflare Workers (Next.js) -> Cloudflare Tunnel -> FastAPI (homelab) -> Proxmox VE -> VM
