def test_signup_adds_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "new.student@example.com"
    assert email not in client.get("/activities").json()[activity]["participants"]

    # Act
    resp = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert resp.status_code in (200, 201)
    activities = client.get("/activities").json()
    assert email in activities[activity]["participants"]


def test_signup_duplicate_returns_400(client):
    # Arrange
    activity = "Chess Club"
    email = "duplicate.student@example.com"
    # ensure first signup succeeds
    first = client.post(f"/activities/{activity}/signup?email={email}")
    assert first.status_code in (200, 201)

    # Act
    second = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert second.status_code == 400
