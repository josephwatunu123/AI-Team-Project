import networkx as nx
import matplotlib.pyplot as plt
from classes.bfs import BfsTraverser
G = nx.Graph()
nodes=["SportsComplex","Siwaka","Ph.1A","Ph.1B","Phase2","J1","Mada","STC","Phase3","ParkingLot"]
G.add_nodes_from(nodes)
G.nodes()

G.add_edge("SportsComplex","Siwaka",weight="450")
G.add_edge("Siwaka","Ph.1A",weight="10")
G.add_edge("Siwaka","Ph.1B",weight="230")
G.add_edge("Ph.1A","Mada",weight="850")
G.add_edge("Ph.1A","Ph.1B",weight="100")
G.add_edge("Ph.1B","Phase2",weight="100")
G.add_edge("Ph.1B","STC",weight="50")
G.add_edge("Phase2","J1",weight="600")
G.add_edge("Phase2","STC",weight="50")
G.add_edge("Phase2","Phase3",weight="500")
G.add_edge("J1","Mada",weight="200")
G.add_edge("Mada","ParkingLot",weight="700")
G.add_edge("STC","ParkingLot",weight="250")
G.add_edge("Phase3","ParkingLot",weight="350")


G.nodes["SportsComplex"]['pos']=(0,3)
G.nodes["Siwaka"]['pos']=(1,3)
G.nodes["Ph.1A"]['pos']=(2,3)
G.nodes["Ph.1B"]['pos']=(2,2)
G.nodes["Phase2"]['pos']=(3,2)
G.nodes["J1"]['pos']=(4,2)
G.nodes["Mada"]['pos']=(5,2)
G.nodes["STC"]['pos']=(2,1)
G.nodes["Phase3"]['pos']=(4,1)
G.nodes["ParkingLot"]['pos']=(4,0)

node_pos = nx.get_node_attributes(G,'pos')

route_bfs = BfsTraverser()
routes = route_bfs.BFS(G,"SportsComplex","ParkingLot")
print(route_bfs.visited)
route_list = route_bfs.visited

node_col = ['grey' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list,route_list[1:]))

edge_col = ['grey' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=1500)
nx.draw_networkx_edges(G, node_pos,width=1,edge_color= edge_col)


nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()
