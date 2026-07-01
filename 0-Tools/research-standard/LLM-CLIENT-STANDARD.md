# LLM Client Standard

This standard promotes the API transport pattern from `3-smga` and `5-Telephone`
into `0-Tools`, so new projects can reuse one provider interface instead of
copying project-specific runners.

## Files

- `llm_client.py`: dependency-free Python client.
- `templates/llm_config.example.json`: real-provider config template.
- `templates/llm_config.mock.json`: no-key local smoke-test config.
- `templates/llm_config.deepseek.json`: DeepSeek via the OpenAI-compatible
  yunwu.ai gateway.

## Supported Contract

Project code should depend on this small wrapper:

```python
from llm_client import LLM

llm = LLM("configs/llm_config.json")
text = llm.complete(system="You are concise.", user="Say hello.")
data = llm.complete_json(system="Return JSON.", user='{"task": "ping"}')
```

The standard supports:

- `provider: "mock"` for local tests with no API key.
- OpenAI-compatible `chat_completions`.
- OpenAI-compatible `responses`.
- explicit `model`, `temperature`, `base_url`, `wire_api`, timeout, retries.
- `json_mode` for JSON-object responses.
- `transport: "urllib"` or `transport: "curl"` for Responses-style endpoints.

## Experiment Telemetry

Every `LLM.complete()` and `LLM.complete_json()` call appends one record to
`llm.telemetry`. The record includes latency, retry attempts, a prompt hash,
input/output character counts, token counts, usage provenance, and success or
failure. Prompt text and API keys are never written to telemetry.

Use `llm.telemetry_summary()` to obtain run-level totals. Token counts come
from provider usage fields when available; otherwise they are explicitly
labelled `character_estimate`. Experiment runners should archive both the
per-call records and summary so cost and latency are auditable.

Transport failures are sanitized before they leave the client. In particular,
curl timeout exceptions never include the authorization command or API key.

Any OpenAI-compatible gateway is reachable by pointing `base_url` at it and
naming the key var with `api_key_env`. No code change is needed per provider.

### DeepSeek (yunwu.ai gateway)

`templates/llm_config.deepseek.json` routes to DeepSeek through the
OpenAI-compatible yunwu.ai gateway:

- `wire_api: "chat_completions"`, `model: "deepseek-v4-flash"`.
- `base_url: "https://yunwu.ai"` — **not** `https://yunwu.ai/v1`. The client's
  `normalize_endpoint()` appends `/v1/chat/completions`, so a `/v1` in the base
  URL would be doubled.
- `api_key_env: "DEEPSEEK_API_KEY"` — set this env var to the yunwu key
  (`sk-...`); never commit it.

## API Keys

Never store keys in project configs or results.

The client resolves keys in this order:

1. `api_key_env` from the config, if set.
2. `<PROVIDER>_API_KEY`, for example `FHL_API_KEY`.
3. `OPENAI_API_KEY`.

For provider `mock`, no key is required.

## Recommended Project Layout

Each project that calls models should keep a local config such as:

```text
<project>/
|-- configs/
|   `-- llm_config.json
```

The config should be copied from `0-Tools/research-standard/templates/`, then
the exact model version should be pinned before a reported experiment.

## Smoke Tests

No-key test:

```bash
python D:/0-Research/0-Tools/research-standard/llm_client.py ^
  --config D:/0-Research/0-Tools/research-standard/templates/llm_config.mock.json
```

Real-provider test after setting the relevant key:

```bash
python D:/0-Research/0-Tools/research-standard/llm_client.py ^
  --config D:/0-Research/0-Tools/research-standard/templates/llm_config.example.json
```

## Migration Note

`3-smga` currently owns the fuller `model_calling_runner.py`, which also handles
prompt-bundle IO and result drafts. Keep that experiment runner local, but route
new project-level API calls through this standard client.

`5-Telephone/sim/llm.py` already shows the intended wrapper shape; future
projects should import or vendor this standard client instead of pointing back
to `3-smga`.
