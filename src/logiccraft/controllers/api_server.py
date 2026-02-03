from fastapi import FastAPI
from logiccraft.models.diagram import DiagramModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "LiveBlueprint API is running"}

@app.post("/simulate")
async def start_simulation(diagram: DiagramModel):
    # Сёма будет обрабатывать симуляцию здесь
    return {"message": "Simulation started", "nodes_count": len(diagram.nodes)}