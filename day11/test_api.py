from fastapi.testclient import TestClient
from main import app
from database import Base, engine

def setup_module():
    Base.metadata.create_all(bind=engine)

def teardown_module():
    Base.metadata.drop_all(bind=engine)

client = TestClient(app)

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200

def test_create_task():
    response = client.post("/tasks", json={
        "title": "Test task",
        "description": "Created by pytest"
    })
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == "Test task"

def test_get_task_by_id():
    client.post("/tasks", json={"title": "find me"})
    response = client.get("/tasks/1")
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1

def test_delete_task():
    test_add = client.post("/tasks", json={"title": "delete me"})
    add_response = test_add.json()
    response = client.delete(f"/tasks/{add_response['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data == {"message": f"ID: {add_response['id']} Task: {add_response['title']} has been deleted"}
    
def test_complete_task():
    test_add = client.post("/tasks", json={"title": "complete me"})
    add_response = test_add.json()
    response = client.patch(f"/tasks/{add_response['id']}")
    data = response.json()
    assert response.status_code == 200
    assert data == {"message": "complete me has been marked complete."}

def test_no_task():
    response = client.get("/tasks/-1")
    assert response.status_code == 404