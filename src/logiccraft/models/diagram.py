from pydantic import BaseModel, Field
from typing import List, Optional

class PropertyModel(BaseModel):
    name: str
    type: str = "str"
    default: Optional[str] = None

class NodeModel(BaseModel):
    id: str
    type: str  # "class" или "state"
    name: str
    x: float
    y: float
    properties: List[PropertyModel] = []
    methods: List[str] = []

class EdgeModel(BaseModel):
    id: str
    source_id: str
    target_id: str
    label: Optional[str] = None

class DiagramModel(BaseModel):
    nodes: List[NodeModel] = []
    edges: List[EdgeModel] = []