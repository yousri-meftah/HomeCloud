// TypeScript type definitions

export interface User {
  id: string;
  email: string;
  is_verified: boolean;
  created_at: string;
}

export interface VPSInstance {
  id: string;
  plan: "small" | "medium" | "large";
  status: "provisioning" | "running" | "stopped" | "deleting" | "error";
  hostname: string | null;
  ssh_username: string | null;
  internal_ip: string | null;
  created_at: string;
  started_at: string | null;
}

export interface VPSPlan {
  name: string;
  cpu: number;
  ram_mb: number;
  disk_gb: number;
  price_monthly: number;
}

export interface AuthTokens {
  access_token: string;
  refresh_token: string;
  token_type: string;
}
