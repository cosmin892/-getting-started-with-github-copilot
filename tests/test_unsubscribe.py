def test_unregister_removes_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "remove.me@example.com"
    signup = client.post(f"/activities/{activity}/signup?email={email}")
    assert signup.status_code in (200, 201)

    # Act
    resp = client.delete(f"/activities/{activity}/participants/{email}")

    # Assert
    assert resp.status_code == 200
    activities = client.get("/activities").json()
    assert email not in activities[activity]["participants"]


def test_unregister_missing_returns_404(client):
    # Arrange
    activity = "Chess Club"
    email = "not.there@example.com"

    # Act
    resp = client.delete(f"/activities/{activity}/participants/{email}")

    # Assert
    assert resp.status_code == 404
