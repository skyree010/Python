import os,sys

directoryname = sys.argv[1]
print("NAZWA FOLDERU: ", directoryname)

current = os.getcwd()
dirloc = os.path.join(current,directoryname)

xd = os.listdir(directoryname)

duplicatesbycontain = list()
duplicates=dict()

for values in xd:
    path = os.path.join(dirloc,values)
    if os.path.isdir(path):
        continue
    else:
        filesize = os.stat(path).st_size
        file_contain = open(path,errors='ignore').read()
        zmienna = [values,filesize,file_contain]
        duplicatesbycontain.append(zmienna)

for entries in duplicatesbycontain:
    print(entries[0])
    print(entries[1])
    print("________________________")
    zmienna=os.path.join(str(entries[1]),entries[2])
    if duplicates.__contains__(zmienna):
            duplicates[zmienna].append(entries[0])
    else:
        duplicates[zmienna]=list()
        duplicates[zmienna].append(entries[0])


for entry in duplicates:
    tocut = entry
    cut = tocut.split("\\",1)
    size = cut[0]
    if len(duplicates[entry])>1:
        print("Duplicated: ",size,"b")
        for items in duplicates[entry]:
            print(items)
        print("----------")
