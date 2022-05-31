import matplotlib.pyplot as plt


nodes = ["Arad",
"Oradea",
"Zerind",
"Sibiu",
"Timisoara",
"Lugoj",
"Mehadia",
"Drobeta",
"Cralova",
"Pitesti",
"Rimnicu",
"Bucharest",
"Giurgiu",
"Urziceni",
"Hirsova",
"Eforie",
"Vaslui",
"Iasi",
"Neamt",
"Fagaras"
]
degre = [ 
 0,
 4,
 54,
 34,
 10,
 8,
 16,
 25,
 35,
 56,
 0,
 80,
 90,
 0,
 76,
 18,
 0,
 34,
 18,
 0
]

plt.plot(nodes, degre, 'o-c', ms=15, mec='g', mfc='g')
plt.xticks(rotation='vertical')
plt.ylabel(' betweeness Centrality')
plt.xlabel('Nodes')
plt.title("Betweeness Centrality")

plt.show()