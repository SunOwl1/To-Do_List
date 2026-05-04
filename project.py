from fastapi import FastAPI, HTTPException

app = FastAPI()

#данные пользователей
fake_user = {
    "user": "example_user",
    "password": "f3245tg35543"
}

fake_db = [
    {
    "name":"Owl",
    "age":23,
    "id":0
    },
    {
    "name":"Vit",
    "age":24,
    "id":1
    }
]

@app.get("/users")
def get_all_users():
    return fake_db

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in fake_db:
        if user["id"] == user_id:
            return user
    raise HTTPException (status_code=404, detail="User not found")

@app.post("/users")
def create_user(user: dict):
    new_user = {
        "name": user["name"],
        "age": user["age"],
        "id": len(fake_db)
    }
    fake_db.append(new_user)
    return {"message": "User created", "user": new_user}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: dict):
    for index, existing_user in enumerate(fake_db):
        if existing_user["id"] == user_id:
            existing_user.update(user)
            existing_user["id"] = user_id
            fake_db[index] = existing_user
            return existing_user
    raise HTTPException(status_code=404, detail="User not found")