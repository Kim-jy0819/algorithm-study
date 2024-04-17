coord_dict = {'x':dict(), 'y':dict()}
for _ in range(3):
    x, y = map(int, input().split())
    coord_dict['x'][x] = coord_dict['x'].get(x, 0) + 1
    coord_dict['y'][y] = coord_dict['y'].get(y, 0) + 1

print(sorted(coord_dict['x'].items(), key=lambda x:x[1])[0][0], sorted(coord_dict['y'].items(), key=lambda x:x[1])[0][0])