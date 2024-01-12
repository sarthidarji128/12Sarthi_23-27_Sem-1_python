def cube_range(a,b):
    cubes= {} 
    for num in range(a,b+1):
        if num%2!=0: 
            cubes[num] = num**3 
    return cubes
cubes = cube_range(1,5)
print(cubes)  
