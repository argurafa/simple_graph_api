from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import requests
import networkx as nx
from pyvis.network import Network

app = FastAPI()
g = nx.Graph()
net=Network()




class Item(BaseModel):
    Nodos: list
    Connexiones: list

@app.get("/", response_class=HTMLResponse)
async def root():
    net.from_nx(g)
    return net.generate_html("pvis.html")

@app.post("/grafo")
async def requestSwapi(obj:Item) -> str:

    for i in obj.Nodos:
        g.add_node(i)
    for i in obj.Connexiones:
        g.add_edge(*tuple(i))
    return str(g)