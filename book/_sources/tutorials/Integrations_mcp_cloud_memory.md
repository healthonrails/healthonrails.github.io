# Integrations: MCP, Memory, Cloud Storage & Security

Once you are comfortable with Annolid Bot inside the GUI, you can extend it into a full lab assistant — connecting external **Model Context Protocol (MCP)** tools, persistent **LanceDB Memory**, **Google Drive / Calendar**, **Box**, and **Codex / ACP** agents while keeping credentials and lab data locked down locally.

```{figure} ../images/diagrams/agent_mcp_security_architecture.png
---
name: agent-mcp-arch
alt: Architecture diagram connecting GUI Chat Dock, CLI, and Codex/ACP through the Guarded Annolid Agent Core to MCP Servers, LanceDB Memory, and Cloud/Lab Ops
width: 100%
---
Annolid's agent stack separates user interfaces from guarded tools, local vector memory, and external integrations.
```

## 1. Model Context Protocol (MCP) Servers

Connect external tools (scoped filesystem tools, lab databases, web/API bridges) by editing `~/.annolid/config.json`:

```json
{
  "tools": {
    "mcpServers": {
      "filesystem": {
        "command": "npx",
        "args": [
          "-y",
          "@modelcontextprotocol/server-filesystem",
          "/path/to/allowed/lab_project"
        ]
      }
    }
  }
}
```

Each MCP server entry supports `command`, `args`, `env`, or a remote HTTP/SSE `url`. Always scope filesystem servers strictly to your project folder rather than your entire home directory.

## 2. Local-First Memory Subsystem (`LanceDB`)

Annolid Memory stores reusable lab context — project notes, annotation conventions, workflow recipes, and saved **Settings Profiles** — while keeping your files and JSONs as the sole source of truth.

::::{tab-set}

:::{tab-item} Desktop GUI
Open **`Settings → Memory Manager…`** to:
- search notes and saved conventions by scope (`workspace:<id>`, `project:<id>`, `dataset:<id>`),
- save or apply one-click **Settings Profiles** across Settings panels, and
- migrate legacy JSON/Markdown notes via the built-in **Migration Dashboard**.
:::

:::{tab-item} CLI & Setup
```bash
# Install optional memory dependencies
pip install "annolid[memory]"

# Enable LanceDB local memory
export ANNOLID_MEMORY_ENABLED=true
export ANNOLID_MEMORY_BACKEND=lancedb
export ANNOLID_MEMORY_LANCEDB_PATH=~/.annolid/memory/lancedb

# Inspect and search memory from the terminal
annolid-run memory stats
annolid-run memory search "mouse083 zone layout"
```
:::

::::

## 3. Native Google Drive, Calendar & Box Integrations

Install the optional bot integrations bundle (`pip install "annolid[annolid_bot]"`):

- **Shared Google OAuth (Drive + Calendar + Colab)**: Store your OAuth client JSON once at `~/.annolid/agent/google_oauth_credentials.json` (`0600` permissions) and enable `google_drive` / `calendar` under `tools` in `~/.annolid/config.json`. Drive, Calendar, and Colab share one local token seamlessly.
- **Enterprise Box (`tools.box`)**: Configure `client_id`, `client_secret`, and `redirect_uri` (`http://localhost:8765/oauth/callback`), or bootstrap SSO/2FA auth via `annolid-run agent-box-auth-url --open-browser`.

## 4. Security Audits & Secret Hardening

Before enabling cloud bridges or shared-workstation automation, run Annolid's built-in security posture checks:

```bash
# Quick credential & permission hygiene check
annolid-run agent-security-check

# Full posture audit (permissions, secret refs, channel allowlists, tool guardrails)
annolid-run agent-security-audit

# Automatically tighten local file permissions (0600 / 0700) safely
annolid-run agent-security-audit --fix

# Migrate any plaintext keys out of config.json into the dedicated secret store
annolid-run agent-secrets-migrate
```

```{warning}
Never commit `~/.annolid/config.json`, OAuth tokens, API keys, or `.env` files into Git repositories. Annolid writes credentials atomically with `0600` permissions and keeps generated code execution inside its AST-checked subprocess sandbox.
```

For full configuration schemas, see [Agent & Automation](https://annolid.com/portal/agent_and_automation/), [MCP](https://annolid.com/portal/mcp/), [Memory Subsystem](https://annolid.com/portal/memory/), [Google Integrations](https://annolid.com/portal/agent_workspace/), [Box Integration](https://annolid.com/portal/agent_box/), and [Agent Security](https://annolid.com/portal/agent_security/) on the Docs Portal.
