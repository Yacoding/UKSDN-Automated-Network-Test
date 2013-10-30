import test_distribution as td

testing = True

list_of_connections = []

if testing:
	s = """[0, 1, 1, 1, 1, 1, 1, 1]
	[0, 0, 1, 1, 1, 1, 1, 1]
	[0, 0, 0, 1, 1, 1, 1, 1]
	[0, 0, 0, 0, 1, 1, 1, 1]
	[0, 0, 0, 0, 0, 1, 1, 1]
	[0, 0, 0, 0, 0, 0, 1, 1]
	[0, 0, 0, 0, 0, 0, 0, 1]
	[0, 0, 0, 0, 0, 0, 0, 0]
	""".replace(",","").replace(" ","").replace(
	"[","").replace("]","").replace("\t","")
	print s
	list_of_connections = []
	for a in s.split():
		list_of_connections.append([int(b) for b in a])
	for a in list_of_connections:
		print a
	hosts = td.list_of_hosts
else:
	hosts = td.list_of_hosts
	for a in xrange(len(hosts)):
		l = [] + [0]*a
		for b in xrange(a,len(hosts)):
			print a,b
			if a != b:
				x = td.test_connection(hosts[a],hosts[b])
				if x[0]:
					l.append(1)
				else:
					l.append(0)
			else:
				l.append(0)
		list_of_connections.append(l)


grouped = [0]*len(hosts)
groups = []
for a in xrange(len(hosts)):
	current_grouping = []
	if grouped[a] != 0:
		grouped[a] = 1
		current_grouping.append(a)
		index = 0
		while index < len(current_grouping):
			for b in xrange(len(hosts)):
				if grouped[b] == 0 and list_of_connections[a][b] == 1:
					grouped[b] = 1
					current_grouping.append(b)
			index += 1
	if current_grouping != []:
		groups.append(current_grouping)
print groups
for a in groups:
	print a
