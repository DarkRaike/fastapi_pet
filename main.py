from fastapi import FastAPI
from fastapi.responses import Response
from pydantic import BaseModel


class Item(BaseModel):
    name: str = "Michail"
    description: str | None = None
    tax: float | None = None
    price: float = 3

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id} | item.model_dump()



# инициализация FastAPI приложения

# app = FastAPI()
#
# BALANCE = {}
#
# class OperationRequest(BaseModel):
#     wallet_name: str
#     amount: float
#     description: str | None = None
#
#
# @app.get("/balance/")
# def get_balance(wallet_name: str | None = None):
#     # проверяем, есть ли wallet_name в BALANCE
#     if wallet_name is None:
#         return {"total_balance": sum(BALANCE.values())}
#     if wallet_name not in BALANCE:
#         raise HTTPException(status_code=404, detail="Wallet not found")
#     # возвращаем баланс wallet_name
#     return {"wallet": wallet_name, "balance": BALANCE[wallet_name]}
#
# @app.post("/wallets/{name}")
# def create_wallet(name: str, initial_balance: float = 0):
#     if name in BALANCE:
#         raise HTTPException(status_code=404, detail="Wallet already exists")
#     BALANCE[name] = initial_balance
#
#     return {
#         "message": f"Wallet {name} created",
#         "wallet": name,
#         "balance": BALANCE[name]
#     }
#
# @app.post("/operations/income")
# def add_income(operation: OperationRequest):
#     if operation.wallet_name not in BALANCE:
#         raise HTTPException(status_code=404, detail="Wallet not found")
#
#     if operation.amount <= 0:
#         raise HTTPException(status_code=400, detail="Amount cannot be negative")
#
# @app.post("/operations/expense")
# def add_expense():
#     pass




# @app.post("/wallet/{name}")
# def receive_money(name: str, amount: int):
#     # проверяем, есть ли wallet_name в BALANCE
#     if name not in BALANCE:
#         BALANCE[name] = 0
#     # добавляем amount к балансу wallet_name
#     BALANCE[name] += amount
#     # возвращаем информацию о балансе wallet_name
#     return {
#         "message": f"Added {amount} to {name}",
#         "wallet": name,
#         "balance": BALANCE[name]
#     }