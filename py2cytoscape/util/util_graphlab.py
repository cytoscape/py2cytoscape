def from_sgraph(sgraph):
    new_graph = {}
    elements = {}
    nodes = []
    edges = []

    nodes_original = sgraph.vertices
    el = sgraph.edges

    node_attr = nodes_original[0].keys()

    for node in nodes_original:
        new_node = {}
        data = {}
        data['id'] = node['__id']
        data['name'] = node['__id']
        for key in node_attr:
            data[key] = node[key]
        new_node['data'] = data
        nodes.append(new_node)

    for edge in el:
        new_edge = {}
        data = {}
        data['source'] = str(edge['__src_id'])
        data['target'] = str(edge['__dst_id'])
        new_edge['data'] = data
        edges.append(new_edge)

    elements['nodes'] = nodes
    elements['edges'] = edges
    new_graph['elements'] = elements

    return new_graph

