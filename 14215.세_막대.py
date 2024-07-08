tri = list(map(int,input().split()))
tri.sort()

if tri[0] + tri[1] <= tri[2]:
    tri[2] = tri[0]+tri[1]-1

print(tri[0]+tri[1]+tri[2])