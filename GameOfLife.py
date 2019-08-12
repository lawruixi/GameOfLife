#First line of input: number of rows and columns, separated by spaces
#Next line contains single number n, number of generations.
#Next r lines contains c characters each,"." for unoccupied and "X" for occupied.
import copy;

def readLine():
    line = infile.readline().strip();
    while(line[0] == "#"):
        line = infile.readline().strip()
    return line;

def numberOfNeighbours(row, column, graph):
    neighbours = 0;
    if(row > 0 and column > 0 and graph[row - 1][column - 1] == 1):
        neighbours += 1;
    if(row > 0 and graph[row - 1][column] == 1):
        neighbours += 1;
    if(row > 0 and column < columns - 1 and graph[row - 1][column + 1] == 1):
        neighbours += 1;

    if(column > 0 and graph[row][column - 1] == 1):
        neighbours += 1;
    if(column < columns - 1 and graph[row][column + 1] == 1):
        neighbours += 1;

    if(row < rows - 1 and column > 0 and graph[row + 1][column - 1] == 1):
        neighbours += 1;
    if(row < rows - 1 and graph[row + 1][column] == 1):
        neighbours += 1;
    if(row < rows - 1 and column < columns - 1 and graph[row + 1][column + 1] == 1):
        neighbours += 1;
    return neighbours;
    
     
        
def printGraph(graph):
    for row in range(rows):
        for column in range(columns):
            if(graph[row][column] == 0):
                print(".", end="");
            elif(graph[row][column] == 1):
                print("x", end="")
        print()


infile = open("GameOfLife.txt", "r");

rows, columns = map(int, readLine().split());

generations = int(readLine().strip())

#0 = unoccupied
#1 = occupied
graph = [[-1 for i in range(columns)] for j in range(rows)];

for row in range(rows):
    line = readLine().strip();

    for column in range(columns):
        if line[column] == ".":
            graph[row][column] = 0;
        elif line[column].lower() == "x":
            graph[row][column] = 1;

newgraph = copy.deepcopy(graph);

for count in range(generations):
    for row in range(rows):
        for column in range(columns):
            if(numberOfNeighbours(row, column, graph) == 3) and graph[row][column] == 0:
                #Populated
                newgraph[row][column] = 1;
                continue
            elif(numberOfNeighbours(row, column, graph) < 2) and graph[row][column] == 1:
                #Dies of loneliness
                newgraph[row][column] = 0;
            elif(numberOfNeighbours(row, column, graph) > 3) and graph[row][column] == 1:
                #Dies of overpopulation
                newgraph[row][column] = 0;
    print("GENERATION " + str(count) + ":")
    printGraph(newgraph)

    graph = copy.deepcopy(newgraph);

infile.close();
