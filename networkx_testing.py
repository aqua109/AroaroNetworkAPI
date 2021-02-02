import networkx as nx
from networkx.readwrite import json_graph
import json
import sqlite3


class Node:
    def __init__(self, id):
        self.id = id
        self.degree = 0
        self.closeness = 0
        self.betweenness =0


with open("graph.json") as f:
    data = json.load(f)

g = json_graph.node_link_graph(data)

degree_dict = nx.degree_centrality(g)
closeness_dict = nx.closeness_centrality(g)
betweenness_dict = nx.betweenness_centrality(g)

node_list = []

for node in g.nodes:
    temp_node = Node(node)
    temp_node.degree = degree_dict[node]
    temp_node.closeness = closeness_dict[node]
    temp_node.betweenness = betweenness_dict[node]
    node_list.append(temp_node)

node_list.sort(key=lambda x: x.id)

#for node in node_list:
#    print(f"Node: {node.id}\tDegree: {node.degree}\tCloseness: {node.closeness}\tBetweenness: {node.betweenness}")

json_string = json.dumps([ob.__dict__ for ob in node_list])

def retrieve_network(id):
    conn = sqlite3.connect("network_storage.db")
    cur = conn.cursor()
    cur.execute("SELECT network FROM networks WHERE id = ?", (id,))
    network_string = cur.fetchone()[0]
    return json.loads(network_string)

def save_network(network_data):
    network_json = json.loads(network_data)

    network_id = network_json["network_id"]
    network_string = network_json["network"][0]

    g = nx.node_link_graph(network_string)

    degree_dict = nx.degree_centrality(g)
    closeness_dict = nx.closeness_centrality(g)
    betweenness_dict = nx.betweenness_centrality(g)

    node_list = []

    for node in g.nodes:
        temp_node = Node(node)
        temp_node.degree = degree_dict[node]
        temp_node.closeness = closeness_dict[node]
        temp_node.betweenness = betweenness_dict[node]
        node_list.append(temp_node)

    node_list.sort(key=lambda x: x.id)
    network_string = json.dumps([ob.__dict__ for ob in node_list])
    conn = sqlite3.connect("network_storage.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO networks(id, network) VALUES (?, ?)", (network_id, network_string))
    conn.commit()

test_string ='{"network_id":2,"network":[{"directed":false,"multigraph":false,"graph":{},"nodes":[{"id":0},{"id":1},{"id":25},{"id":45},{"id":11},{"id":21},{"id":31},{"id":33},{"id":34},{"id":36},{"id":37},{"id":38},{"id":39},{"id":40},{"id":41},{"id":47},{"id":48},{"id":50},{"id":53},{"id":54},{"id":55},{"id":58},{"id":2},{"id":28},{"id":3},{"id":9},{"id":16},{"id":4},{"id":5},{"id":6},{"id":49},{"id":20},{"id":32},{"id":7},{"id":23},{"id":57},{"id":8},{"id":51},{"id":56},{"id":10},{"id":59},{"id":13},{"id":14},{"id":22},{"id":42},{"id":46},{"id":52},{"id":12},{"id":15},{"id":29},{"id":17},{"id":18},{"id":19},{"id":60},{"id":63},{"id":64},{"id":35},{"id":24},{"id":26},{"id":27},{"id":30},{"id":43},{"id":44},{"id":61},{"id":62}],"links":[{"source":0,"target":1},{"source":0,"target":25},{"source":0,"target":45},{"source":0,"target":4},{"source":1,"target":11},{"source":1,"target":21},{"source":1,"target":25},{"source":1,"target":31},{"source":1,"target":33},{"source":1,"target":34},{"source":1,"target":36},{"source":1,"target":37},{"source":1,"target":38},{"source":1,"target":39},{"source":1,"target":40},{"source":1,"target":41},{"source":1,"target":45},{"source":1,"target":47},{"source":1,"target":48},{"source":1,"target":50},{"source":1,"target":53},{"source":1,"target":54},{"source":1,"target":55},{"source":1,"target":58},{"source":1,"target":15},{"source":1,"target":56},{"source":25,"target":4},{"source":25,"target":8},{"source":25,"target":11},{"source":25,"target":45},{"source":25,"target":33},{"source":25,"target":34},{"source":25,"target":39},{"source":25,"target":48},{"source":25,"target":56},{"source":25,"target":59},{"source":25,"target":58},{"source":45,"target":3},{"source":45,"target":4},{"source":45,"target":7},{"source":45,"target":9},{"source":45,"target":11},{"source":45,"target":19},{"source":45,"target":20},{"source":45,"target":21},{"source":45,"target":22},{"source":45,"target":23},{"source":45,"target":27},{"source":45,"target":28},{"source":45,"target":31},{"source":45,"target":33},{"source":45,"target":34},{"source":45,"target":36},{"source":45,"target":39},{"source":45,"target":37},{"source":45,"target":38},{"source":45,"target":40},{"source":45,"target":41},{"source":45,"target":42},{"source":45,"target":43},{"source":45,"target":44},{"source":45,"target":47},{"source":45,"target":48},{"source":45,"target":51},{"source":45,"target":52},{"source":45,"target":53},{"source":45,"target":54},{"source":45,"target":55},{"source":45,"target":56},{"source":45,"target":58},{"source":11,"target":10},{"source":11,"target":13},{"source":11,"target":14},{"source":11,"target":21},{"source":11,"target":22},{"source":11,"target":31},{"source":11,"target":36},{"source":11,"target":37},{"source":11,"target":38},{"source":11,"target":39},{"source":11,"target":40},{"source":11,"target":41},{"source":11,"target":42},{"source":11,"target":46},{"source":11,"target":47},{"source":11,"target":49},{"source":11,"target":50},{"source":11,"target":51},{"source":11,"target":52},{"source":11,"target":53},{"source":11,"target":54},{"source":11,"target":55},{"source":11,"target":56},{"source":11,"target":57},{"source":11,"target":58},{"source":11,"target":15},{"source":11,"target":17},{"source":11,"target":18},{"source":11,"target":35},{"source":21,"target":2},{"source":21,"target":3},{"source":21,"target":5},{"source":21,"target":7},{"source":21,"target":8},{"source":21,"target":10},{"source":21,"target":16},{"source":21,"target":39},{"source":21,"target":58},{"source":21,"target":54},{"source":21,"target":56},{"source":21,"target":47},{"source":21,"target":29},{"source":21,"target":28},{"source":21,"target":38},{"source":21,"target":32},{"source":21,"target":15},{"source":21,"target":20},{"source":21,"target":22},{"source":21,"target":24},{"source":21,"target":36},{"source":21,"target":37},{"source":21,"target":42},{"source":21,"target":49},{"source":21,"target":50},{"source":21,"target":51},{"source":21,"target":52},{"source":21,"target":53},{"source":21,"target":55},{"source":21,"target":59},{"source":21,"target":60},{"source":21,"target":63},{"source":21,"target":64},{"source":31,"target":38},{"source":31,"target":40},{"source":31,"target":48},{"source":31,"target":39},{"source":31,"target":36},{"source":31,"target":53},{"source":31,"target":54},{"source":31,"target":55},{"source":31,"target":58},{"source":33,"target":4},{"source":33,"target":18},{"source":33,"target":32},{"source":33,"target":34},{"source":33,"target":39},{"source":33,"target":59},{"source":33,"target":50},{"source":33,"target":56},{"source":33,"target":58},{"source":34,"target":32},{"source":36,"target":7},{"source":36,"target":15},{"source":36,"target":22},{"source":36,"target":49},{"source":36,"target":39},{"source":36,"target":58},{"source":37,"target":7},{"source":37,"target":8},{"source":37,"target":39},{"source":37,"target":50},{"source":37,"target":56},{"source":37,"target":58},{"source":38,"target":4},{"source":38,"target":7},{"source":38,"target":15},{"source":38,"target":40},{"source":38,"target":41},{"source":38,"target":39},{"source":38,"target":53},{"source":38,"target":54},{"source":38,"target":55},{"source":38,"target":58},{"source":39,"target":3},{"source":39,"target":5},{"source":39,"target":7},{"source":39,"target":8},{"source":39,"target":9},{"source":39,"target":10},{"source":39,"target":12},{"source":39,"target":13},{"source":39,"target":14},{"source":39,"target":15},{"source":39,"target":16},{"source":39,"target":18},{"source":39,"target":20},{"source":39,"target":22},{"source":39,"target":24},{"source":39,"target":28},{"source":39,"target":29},{"source":39,"target":32},{"source":39,"target":41},{"source":39,"target":40},{"source":39,"target":42},{"source":39,"target":46},{"source":39,"target":47},{"source":39,"target":49},{"source":39,"target":50},{"source":39,"target":51},{"source":39,"target":52},{"source":39,"target":53},{"source":39,"target":54},{"source":39,"target":55},{"source":39,"target":56},{"source":39,"target":58},{"source":39,"target":59},{"source":39,"target":60},{"source":39,"target":61},{"source":39,"target":62},{"source":39,"target":63},{"source":39,"target":64},{"source":40,"target":15},{"source":40,"target":41},{"source":41,"target":13},{"source":41,"target":47},{"source":47,"target":4},{"source":47,"target":7},{"source":47,"target":15},{"source":47,"target":22},{"source":47,"target":53},{"source":47,"target":54},{"source":47,"target":55},{"source":47,"target":58},{"source":50,"target":18},{"source":50,"target":51},{"source":50,"target":52},{"source":50,"target":53},{"source":50,"target":54},{"source":50,"target":55},{"source":50,"target":57},{"source":50,"target":56},{"source":50,"target":58},{"source":53,"target":15},{"source":53,"target":51},{"source":53,"target":52},{"source":53,"target":54},{"source":53,"target":55},{"source":53,"target":56},{"source":53,"target":57},{"source":53,"target":58},{"source":54,"target":15},{"source":54,"target":51},{"source":54,"target":52},{"source":54,"target":55},{"source":54,"target":56},{"source":54,"target":57},{"source":54,"target":58},{"source":55,"target":8},{"source":55,"target":16},{"source":55,"target":51},{"source":55,"target":52},{"source":55,"target":56},{"source":55,"target":57},{"source":55,"target":58},{"source":58,"target":2},{"source":58,"target":3},{"source":58,"target":5},{"source":58,"target":8},{"source":58,"target":10},{"source":58,"target":16},{"source":58,"target":22},{"source":58,"target":28},{"source":58,"target":29},{"source":58,"target":32},{"source":58,"target":56},{"source":58,"target":57},{"source":58,"target":15},{"source":58,"target":20},{"source":58,"target":49},{"source":58,"target":51},{"source":58,"target":52},{"source":58,"target":59},{"source":58,"target":60},{"source":58,"target":63},{"source":58,"target":64},{"source":2,"target":28},{"source":2,"target":16},{"source":28,"target":3},{"source":28,"target":7},{"source":28,"target":8},{"source":28,"target":16},{"source":28,"target":22},{"source":28,"target":26},{"source":28,"target":27},{"source":28,"target":29},{"source":28,"target":32},{"source":3,"target":9},{"source":3,"target":16},{"source":9,"target":24},{"source":16,"target":29},{"source":4,"target":5},{"source":4,"target":6},{"source":4,"target":19},{"source":5,"target":49},{"source":5,"target":20},{"source":5,"target":32},{"source":6,"target":7},{"source":6,"target":23},{"source":6,"target":57},{"source":49,"target":15},{"source":49,"target":18},{"source":20,"target":19},{"source":20,"target":32},{"source":32,"target":59},{"source":23,"target":24},{"source":23,"target":35},{"source":57,"target":18},{"source":57,"target":51},{"source":57,"target":52},{"source":57,"target":56},{"source":8,"target":51},{"source":8,"target":56},{"source":8,"target":24},{"source":8,"target":35},{"source":51,"target":52},{"source":51,"target":56},{"source":56,"target":52},{"source":10,"target":59},{"source":13,"target":12},{"source":13,"target":14},{"source":14,"target":12},{"source":22,"target":15},{"source":22,"target":60},{"source":22,"target":63},{"source":22,"target":64},{"source":22,"target":35},{"source":29,"target":30},{"source":26,"target":27},{"source":43,"target":44}]}]}'

save_network(test_string)

#G = nx.parse_edgelist(Data, delimiter=',', create_using=Graphtype, nodetype=int, data=(('weight', float),))
