# case 1. (day-night)* (i)th + day >= top
# case 2. (day-night)* i th == top
import math

day, night, top = map(int, input().split())

print(math.ceil((((top-day)/(day-night))+1)))
