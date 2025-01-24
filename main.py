from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# 定义数据模型
class User(BaseModel):
    id: int
    name: str

# 示例数据
users = [
    User(id=1, name="Alice"),
    User(id=2, name="Bob"),
]

@app.get("/users", response_model=List[User])
def get_users():
    return users

@app.post("/users", response_model=User)
def add_user(user: User):
    users.append(user)
    return user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
