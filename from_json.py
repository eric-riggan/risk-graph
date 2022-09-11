import networkx as nx
from networkx.readwrite import json_graph
import json
from pyvis.network import Network

with open('edge_list_mini.json', 'r') as infile:
    js_graph = json.load(infile)
    G = json_graph.node_link_graph(js_graph)

print(G)

nt = Network('1000px', '1000px', directed=True)
nt.from_nx(G)
# nt.show_buttons()
nt.set_options(
"""
const options = {
  "nodes": {
    "borderWidth": 0,
    "borderWidthSelected": 1,
    "opacity": 1,
    "font": {
      "strokeWidth": 4,
      "size": 20
    },
    "size": 1
  },
  "edges": {
    "arrowStrikethrough": false,
    "color": {
      "opacity": 0.8
    },
    "scaling": {
      "max": 8
    },
    "selfReferenceSize": null,
    "selfReference": {
      "angle": 0.7853981633974483
    },
    "smooth": {
      "forceDirection": "none"
    }
  },
  "physics": {
    "minVelocity": 0.75
  }
}
"""
)
nt.show('nx.html')
