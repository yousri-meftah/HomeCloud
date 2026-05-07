import { globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";

const eslintConfig = [
  ...nextVitals,
  globalIgnores([
    ".next/**",
    ".open-next/**",
    "out/**",
    "next-env.d.ts",
    "cloudflare-env.d.ts",
  ]),
];

export default eslintConfig;
