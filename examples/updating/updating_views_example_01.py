# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import networkx as nx

from py2cytoscape.data.cynetwork import CyNetwork
from py2cytoscape.data.cyrest_client import CyRestClient

if __name__ == "__main__":
    
    # Create a network with NetworkX.DiGraph object
    dg = nx.DiGraph()
    
    dg.add_node(0, {'activity': 1})
    dg.add_node(1, {'activity': 2})
    dg.add_node(2, {'activity': 3})
    dg.add_node(3, {'activity': 2})
    dg.add_node(4, {'activity': 4})
    dg.add_node(5, {'activity': 5})
    dg.add_node(6, {'activity': 2})
    dg.add_node(7, {'activity': 3})
    
    dg.add_edge(0, 1, {'sign': +1})
    dg.add_edge(1, 2, {'sign': +1})
    dg.add_edge(2, 3, {'sign': -1})
    dg.add_edge(2, 4, {'sign': -1})
    dg.add_edge(3, 5, {'sign': +1})
    dg.add_edge(4, 6, {'sign': -1})
    dg.add_edge(6, 1, {'sign': +1})
    dg.add_edge(6, 7, {'sign': +1})
    
    # Start cyREST session
    cy = CyRestClient()
    cy.session.delete()
    net = cy.network.create_from_networkx(dg)
   
    # Set layout option
    cy.layout.apply(name='kamada-kawai',
                    network=net)

    # Get CyNetworkView objects from CyNetwork
    view_id_list = net.get_views() 
    view = net.get_view(view_id_list[0], format='view')

    # View as DataFrame makes it easier to see
    # the names of visual properties.
    df_node_view = view.get_node_views_as_dataframe()
    df_edge_view = view.get_edge_views_as_dataframe() 
    
    print(df_node_view.columns)
    print(df_edge_view.columns)

    # Change the colors of nodes
    table_nodes = net.get_node_table()
    node_fill_colors = {}
    rand_G = np.random.randint(0, 255)
    rand_B = np.random.randint(0, 255)

    max_act = table_nodes.activity.max()    
    min_act = table_nodes.activity.min()    
    
    max_R = 255
    min_R = 150
    
    for id_node, row in table_nodes.iterrows():       
        # Determine a node color according to its 'activity' data
        # (Convert RGB color to hex code)
        val_R = int((row.activity-min_act)*(max_R-min_R) \
                     /(max_act-min_act)+min_R)
                
        xcolor = "#%02x%02x%02x" % (val_R,
                                    rand_G,
                                    rand_B)
                                    
        node_fill_colors[int(id_node)] = xcolor
    # end of for    
    
    # Update node color
    view.update_node_views(visual_property="NODE_FILL_COLOR",
                           values=node_fill_colors)
        
    # Change some visual propertis of nodes
    for id_node, row in df_node_view.iterrows():
        #row.NODE_WIDTH = np.random.randint(1, 3)  
        row.NODE_LABEL_COLOR = "#FFFFFF"
        row.NODE_LABEL_FONT_SIZE = 16
    # end of for
    
    # Update edge data using batch_update
    #view.batch_update_node_views(df_node_view)
    view.update_node_views(visual_property="NODE_LABEL_COLOR",
                           values=df_node_view.NODE_LABEL_COLOR)

        
    # It is convenient to use the edge table from CyNetwork object
    # for dealing with edge data such as signs of edges.
    # (The edge table is a Pandas.DataFrame object.)
    table_edges = net.get_edge_table() 
    
    
    # Select options for the shapes of target arrows
    # according to the sign of edge.
    target_arrow_shapes = {}
    for id_edge, row in table_edges.iterrows():
        id_edge = int(id_edge)
        if row.sign>0:
            target_arrow_shapes[id_edge] = "Delta"
        elif row.sign<0:
            target_arrow_shapes[id_edge] = "T"
        elif row.sign==0:
            pass # Do nothing for unexisting edges
        else:
            err_msg = "The value of sign for edge should be 0, 1, or -1."
            raise ValueError(err_msg)
        # end of if-else
    # end of for

    # Update target arrow shapes of the signed network
    view.update_edge_views(visual_property="EDGE_TARGET_ARROW_SHAPE",
                           values=target_arrow_shapes)
    
    # Change the widths and colors of edge stroke
    df_edge_view = view.get_edge_views_as_dataframe()
    for id_edge, row in df_edge_view.iterrows():
        row.EDGE_WIDTH = np.random.randint(1, 5)
        row.EDGE_STROKE_UNSELECTED_PAINT = '#33CC00'
    # end of for
    
    # Update edge data using batch_update
    view.batch_update_edge_views(df_edge_view) 
