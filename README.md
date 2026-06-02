# OpenAI API Template

A minimal Python starter template for the Anthropic API using [uv](https://docs.astral.sh/uv/) for dependency management.

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)
- An [Anthropic API key](https://platform.claude.com/settings/keys)

## Install uv

**macOS**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell)**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

After installation, restart your terminal so the `uv` command is available.

## Setup

1. **Clone the repository**

   ```bash
   git clone <repo-url>
   cd anthropic-template
   ```

2. **Install dependencies**

   ```bash
   uv sync
   ```

   This creates a `.venv` virtual environment and installs all dependencies.

3. **Configure your API key**

   Copy `.env.template` to `.env` and add your key:

   ```bash
   cp .env.template .env   # macOS / Linux
   ```

   ```powershell
   copy .env.template .env   # Windows
   ```

   Then open `.env` and replace the placeholder with your actual key:

   ```
   ANTHROPIC_API_KEY="sk-..."
   ```

## Run

```bash
uv run main.py
```

## Project structure

```
openai_api/
├── main.py           # Entry point
├── pyproject.toml    # Project metadata and dependencies
├── uv.lock           # Locked dependency versions
├── .env.template     # API key template (safe to commit)
└── .env              # Your API key (never commit this)
```

## Dependencies

| Package         | Purpose                                 |
|-----------------|-----------------------------------------|
| `anthropic`     | Anthropic Python SDK                    |
| `python-dotenv` | Loads environment variables from `.env` |
