# List


# Print,
# ['ka','kr','mh','dl']
# kr
# mh
state=["ka","kr","mh","dl"]
print(state)
print(state[1])
print(state[-2])


# To change kr into hy,
# Print,
# ['ka','hy','mh','dl']
state=["ka","kr","mh","dl"]
state[1]="hy"
print(state)


# append,
# Print,
# ['ka','hy','mh','dl','kr']
state=["ka","hy","mh","dl"]
state.append("kr")
print(state)


# extend,
# Print,
# ['ka','hy','mh','dl', 'mh', 'ch']
state=["ka","hy","mh","dl"]
state.extend(["mh","ch"])
print(state)
