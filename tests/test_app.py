from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email():
    activity_name = "Chess Club"
    email = "new.student@mergington.edu"

    signup_response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup_response.status_code == 200

    unregister_response = client.delete(f"/activities/{activity_name}/participants/{email}")
    assert unregister_response.status_code == 200

    payload = unregister_response.json()
    assert payload["message"] == f"Removed {email} from {activity_name}"

    activities_response = client.get("/activities")
    assert activities_response.status_code == 200
    activities = activities_response.json()
    assert email not in activities[activity_name]["participants"]


def test_activities_endpoint_disables_caching():
    response = client.get("/activities")

    assert response.status_code == 200
    assert "no-store" in response.headers.get("cache-control", "").lower()
