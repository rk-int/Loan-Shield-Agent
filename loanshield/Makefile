.PHONY: install playground run test custom-ui

install:
	uv sync

playground:
	uv run adk web app --host 127.0.0.1 --port 18081 --reload_agents

run:
	uv run python3 -m app.agent_runtime_app

test:
	uv run pytest tests/

custom-ui:
	uv run python3 -m app.custom_web_server
