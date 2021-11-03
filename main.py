def find_min_cover_sets(univSet, subSets, minSet):
    testSet=set()
    possibleSets=[]
    for setKey in subSets.keys():
        possibleSets.append([setKey])
    #back_track(univSet,subSets,minSet,testSet)
    answer=BFS(univSet,subSets,possibleSets)

    return answer

def BFS(univSet,subSets,possibleSets):
    newPossibleSets=[]
    for unionSetIndexs in possibleSets:
        unionSet=set()
        for i in unionSetIndexs:
            unionSet.update(subSets.get(i))
        if is_solution(univSet,unionSet):
            return unionSetIndexs
        if unionSetIndexs.__len__()==setsNum:
            return None
        if  unionSetIndexs[unionSetIndexs.__len__()-1]+1!=setsNum:
            for next in range(unionSetIndexs[unionSetIndexs.__len__()-1]+1,setsNum+1):
                newUnion=unionSetIndexs.copy()
                newUnion.append(next)
                newPossibleSets.append(newUnion)
    return BFS(univSet,subSets,newPossibleSets)

def back_track(univSet, subSets, minSet,testSet):
    minSetIndex=[]
    for s in range(subSets.keys().__len__()):
        minSetIndex.clear()
        for y in range(s,subSets.keys().__len__()):
            unionSet=testSet.union(subSets[s+1])
            minSetIndex.append(s+1)
            if is_solution(univSet, unionSet):
                if len(minSet) and len(minSetIndex) < len(minSet):
                    minSet = minSetIndex
                    back_track(univSet,subSets,minSet,testSet)


def is_solution(univ_set, test_set):
    return univ_set.__eq__(test_set)


# Driver Code
if __name__ == "__main__":
    count = 0
    setsNum = 0
    univSet = set()
    subSets = {}
    minSet = []
    filename = "testfiles/s-k-20-30.txt"
    with open(filename) as f:
        for line in f:  ## read file line by line
            if count == 0:  ## first line is the university set (1,2,3,..,n)
                univSet = set([x for x in range(1,int(line)+1)])
                count += 1
                continue
            if count == 1:
                setsNum = int(line)  ## second line is the number of subsets
                count += 1
                continue
            else:
                x = set(int(n) for n in line.split())
                subSets[count - 1] = x
                count += 1

    solution=find_min_cover_sets(univSet, subSets, minSet)
    print("Following are the minimum set cover in " + filename)
    print(solution)
    # if minSet:
    #     print("Following are the minimum set cover in " + filename)
    #     print(minSet)
    # else:
    #     print("Don't have set cover for this question")
