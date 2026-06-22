# LLM Client Standard

This standard promotes the API transport pattern from `3-smga` and `5-Telephone`
into `0-Tools`, so new projects can reuse one provider interface instead of
copying project-specific runners.

## Files

- `llm_client.py`: dependency-free Python client.
- `templates/llm_config.example.json`: real-provider config template.
- `templates/llm_config.mock.json`: no-key local smoke-test config.

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
