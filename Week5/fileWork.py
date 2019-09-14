fr = open('hnr.abc','r')

s = 0
for line in fr:
    #print(line)
    if 'X:' in line:
        print(line.replace("X:",""))

    if 'T:' in line:
        print(line)
        s+1
        if s >0:
            break

#print(fr.readline(1))
#fr.close()
