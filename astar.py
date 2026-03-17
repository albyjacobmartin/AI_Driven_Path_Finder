import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------------------------------------------
# 1. Campus Graph Definition
# ---------------------------------------------------

G = nx.Graph()

edges = [
("Entrance","A",101),
("Admin block","A",58),

("A","Library",96),
("Library","B",36),
("B","C",32),
("C","D",61),
("D","Engineering block",50),
("D","E",91),
("E","Auditorium",96),

("B","F",88),
("F","G",75),
("G","Business block",62),
("Business block","H",56),
("H","I",117),

("I","Activity centre",40),
("Activity centre","Law block",35),
("Law block","N",25),

("N","O",75),
("O","Food court",32),
("O","Department store",43),

("N","M",110),
("M","L",80),
("L","K",70),
("K","J",60)
]

for u,v,w in edges:
    G.add_edge(u,v,weight=w)

# ---------------------------------------------------
# 2. Node Positions (approximate campus layout)
# ---------------------------------------------------

pos = {
"Entrance":(0,8),
"A":(1,7),
"Admin block":(0.5,6),

"Library":(2,7),
"B":(3,6.5),
"C":(3.5,7),
"D":(4,7.8),
"Engineering block":(4,9),

"E":(5.5,7.8),
"Auditorium":(7,7.5),

"F":(4,6),
"G":(5.5,6),
"Business block":(6.8,5.8),
"H":(8,5.5),

"I":(8.5,4.5),
"Activity centre":(8.5,3.5),
"Law block":(8.5,2.7),

"N":(8.5,2),
"O":(9.5,2),
"Food court":(9.5,2.8),
"Department store":(10.5,2),

"M":(7.5,1),
"L":(8.5,1),
"K":(9,0),
"J":(10,0)
}

# ---------------------------------------------------
# 3. A* Path Planning
# ---------------------------------------------------

def heuristic(a,b):
    (x1,y1)=pos[a]
    (x2,y2)=pos[b]
    return ((x1-x2)**2+(y1-y2)**2)**0.5

start="Entrance"
goal="J"

path = nx.astar_path(G,start,goal,heuristic=heuristic,weight="weight")

print("Optimal Path:",path)

# ---------------------------------------------------
# 4. Visualization
# ---------------------------------------------------

fig, ax = plt.subplots(figsize=(8,8))

nx.draw(G,pos,
        with_labels=True,
        node_size=700,
        node_color="lightgray",
        font_size=8,
        ax=ax)

# highlight path
path_edges=list(zip(path,path[1:]))
nx.draw_networkx_edges(G,pos,
                       edgelist=path_edges,
                       width=3,
                       edge_color='red')

# ---------------------------------------------------
# 5. Vehicle Animation
# ---------------------------------------------------

vehicle, = ax.plot([],[], 'bo', markersize=12)

def init():
    vehicle.set_data([],[])
    return vehicle,

def update(frame):
    node=path[frame]
    x,y=pos[node]
    vehicle.set_data(x,y)
    return vehicle,

ani=FuncAnimation(fig,update,
                  frames=len(path),
                  init_func=init,
                  interval=800,
                  repeat=False)

plt.title("Autonomous Kart Path Planning using A*")
plt.show()