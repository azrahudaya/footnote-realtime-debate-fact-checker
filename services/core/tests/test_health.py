import httpx
import pytest

from footnote.api.app import create_app


@pytest.mark.asyncio
async def test_health_returns_status_version_and_uptime() -> None:
    app = create_app()
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        response = await client.get("/api/v1/health")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["version"] == "0.1.0"
    assert isinstance(payload["uptime_s"], int)
    assert payload["uptime_s"] >= 0
