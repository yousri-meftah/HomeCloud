import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "HomeCloud - Personal Cloud Platform",
  description: "Deploy and manage your own VPS instances from a personal homelab",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
