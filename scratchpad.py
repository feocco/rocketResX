s = open('config.txt', 'r')

print(s.readlines()[0][8:-1])

s.close()
