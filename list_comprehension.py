if __name__ == '__main__':
    try:
        x = int(raw_input())
        y = int(raw_input())
        z = int(raw_input())
        n = int(raw_input())
    except EOFError:
        print()
    print([[i,j,k]] for x in range(x+1) for j in range(y+1) for k in range(z+1) if ((x+y+z)) != n)