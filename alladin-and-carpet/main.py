magic = [3, 2, 5, 4]
dist =  [2, 3, 4, 2]

def starting(magic,dist,i,start, currMagic,count):
    # Perform rotation
    if(i>=len(magic)):
        i = 0
    # If completed then return True
    if(i == start and count == 1):
        print("REturning true")
        return True
    elif(i == start):
        count += 1

    
    # Collect magic
    currMagic +=magic[i]

    # Travel dist
    currMagic -= dist[i]

    print(f"i={i} start={start} count={count} currMagic={currMagic}")

    if(currMagic<0):
        return False

    return starting(magic,dist,i+1,start,currMagic,count)


def letsTravelBruteForce(magic,dist):
    for i in range(len(magic)):
        # This is a portal where it travels to i+1 after collecting magic at i
        if(starting(magic,dist,i,i,0,0)):
            print("We can start at",i)
            return i
        else:
            print("we cannot start at",i)

print("*"*8,letsTravelBruteForce(magic,dist))
        
    