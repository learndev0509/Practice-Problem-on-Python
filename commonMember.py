

def common(l1,l2):
    result=False
    for i in l1:
        for j in l2:
            if i==j:
                result=True
                return result

print(common([1,4,3],[3,8,7]))


