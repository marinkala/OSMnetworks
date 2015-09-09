reciprocity=[]
for e in HC.edges_iter():
    if HC.has_edge(e[1],e[0]):
        if HC[e[1]][e[0]]['weight']>5: # get the constant from a distribution?
            if HC[e[0]][e[1]]['weight']>=HC[e[1]][e[0]]['weight']:
                reciprocity.append(HC[e[0]][e[1]]['weight']/float(HC[e[1]][e[0]]['weight']))
