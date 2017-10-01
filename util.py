from adjmat import AdjTypeMat

def get_inputs_data():
	adj_obj = AdjTypeMat()
	features = []
	with open('caselist.txt', 'r') as f:
		for file in f.readlines():
			adj.readin(file)
			adj_mat = adj.buildAdjTypeMat()
			features.append(adj_mat)

	labels = []
	with open('labellist.txt', 'r') as f:
		for line in f.readlines():
			if line == '1':
				labels.append(1)
			else:
				labels.append(0)
	return features, labels