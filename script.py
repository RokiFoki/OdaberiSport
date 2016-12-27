br_sportova = 31
br_pitanja = 21

with open("Sportovi.txt", "r") as f:
	lines = f.readlines()
	lines = filter(lambda x: len(x.strip()) > 0, lines)
	
	def fun(x):
		tmp = x.split()
		return tmp[0], " ".join(tmp[1:])
		
	sports = { x: y for x,y in map(fun, lines) }
	

with open("Vjerojatnosti_TMP.txt", "w") as f:
	for i in range(1, br_sportova+1):
		f.write("#{}\n".format(sports["("+str(i)+")"]))
		f.write("P({})=\n".format(i))
		for j in range(1, br_pitanja+1):
			f.write("P({}|{})=\n".format(j, i))
		f.write("\n")
		