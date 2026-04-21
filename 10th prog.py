!pip install fastapi uvicorn nest_asyncio gradio

from fastapi import FastAPI, Body
import uvicorn, threading, nest_asyncio
import gradio as gr, requests

app = FastAPI()
db = []

# API
@app.get("/")
def home():
    return {"info": "IPC"}

@app.post("/ipc")
def add(x: dict = Body(...)):
    db.append(x)
    return x

@app.get("/{i}")
def get(i: int):
    return db[i] if i < len(db) else {"error": "Invalid"}

# Run server
nest_asyncio.apply()
threading.Thread(target=lambda: uvicorn.run(app, port=8000)).start()

# Functions for UI
def show(): return requests.get("http://127.0.0.1:8000/").json()

def add_ipc(ipc, case, pun):
    return requests.post("http://127.0.0.1:8000/ipc",
                         json={"IPC": ipc, "case": case, "punishment": pun}).json()

def get_ipc(i):
    return requests.get(f"http://127.0.0.1:8000/{int(i)}").json()

# UI
with gr.Blocks() as demo:
    gr.Markdown("# IPC Chatbot")

    gr.Button("Info").click(show, outputs=gr.Textbox())

    ipc = gr.Textbox(label="IPC")
    case = gr.Textbox(label="Case")
    pun = gr.Textbox(label="Punishment")
    gr.Button("Add").click(add_ipc, [ipc, case, pun], gr.Textbox())

    idx = gr.Number(label="Index")
    gr.Button("Get").click(get_ipc, idx, gr.Textbox())

demo.launch()
