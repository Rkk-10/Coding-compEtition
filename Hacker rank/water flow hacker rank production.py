matrix_size=int(input())

terrain=[]

def di(x):
    a=[int(x),'.']
    return a

def pr_tr(terrain):
    for i in terrain:
        for j in i:
            print(j[1], end ="") 
        print('')

def simulate(terrain,matrix_size,wet_arr):
    water_level=terrain[mid_index][mid_index][0]
    while True:
        present_wet_area=len(wet_arr)
        temp_wet_arr=wet_arr.copy()
        for index in temp_wet_arr:
            i=index[0]
            j=index[1]
            if (i-1) >= 0 and  water_level>= terrain[i-1][j][0]:
                terrain[i-1][j][1]='W'
                wet_arr.add((i-1,j))
            if (i+1) < matrix_size and water_level >= terrain[i+1][j][0]:
                terrain[i+1][j][1]='W'
                wet_arr.add((i+1,j))
            if (j-1) >= 0 and water_level >= terrain[i][j-1][0]:
                terrain[i][j-1][1]='W'
                wet_arr.add((i,j-1))
            if (j+1) < matrix_size and water_level >= terrain[i][j+1][0]:
                terrain[i][j+1][1]='W'
                wet_arr.add((i,j+1))
                
        if len(wet_arr) == present_wet_area:
            water_level+=1
            
        for index in wet_arr:
            comp=list(index)
            if comp in boundary_index:
                return terrain



for i in range(matrix_size):
    terrain.append(list(map(di, input().split())))

mid_index=int((matrix_size-1)/2)

terrain[mid_index][mid_index][1]='W'

wet_arr={(mid_index,mid_index)}


        

boundary_index=[]
for i in range(0,matrix_size):
    boundary_index.append([i,(matrix_size-1)])
for j in range(0,matrix_size):
    boundary_index.append([(matrix_size-1),j])
for i in range(0,matrix_size):
    boundary_index.append([i,0])
for j in range(0,matrix_size):
    boundary_index.append([0,j])




result=simulate(terrain,matrix_size,wet_arr)
pr_tr(result)
