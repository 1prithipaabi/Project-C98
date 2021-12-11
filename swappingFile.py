def swapFileData():
    file1 = input("file 2")
    file2 = input("file 1")
    with open(file1, 'r') as a:
        data_a = a.read()
    with open(file1, 'w') as a:
        a.write(data_b)
    with open(file2, 'r') as a:
        data_b = b.read()
    with open(file2, 'w') as a:
        b.write(data_a)

swapFileData()