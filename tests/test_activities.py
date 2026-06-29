def test_get_activities_disables_caching(client):
    # Arrange: default activities are present

    # Act
    resp = client.get("/activities")

    # Assert
    assert resp.status_code == 200
    assert "no-store" in resp.headers.get("cache-control", "").lower()
    data = resp.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
