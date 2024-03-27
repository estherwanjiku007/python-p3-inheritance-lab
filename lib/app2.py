#input -array
def solution2(arrtrans,arrdate):
    arrtrans2=[]
    arrdate2=[]
    deductions=0
    for a in range(0,len(arrtrans)):
        if arrtrans[a]<1:
            continue
        else:
            arrtrans2.append(arrtrans[a])
            arrdate2.append(arrdate[a])

       
print(solution2([100,100,100,-10],["2020-12-31","2020-11-13","2020-03-10","2020-03-04"]))

        

