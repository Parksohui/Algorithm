if __name__=='__main__' :
    n=int(input())

    name=[]
    year=[]
    month=[]
    day=[]

    for i in range(n):
        temp=list(input().split())
        name.append(temp[0])
        year.append(int(temp[3]))
        month.append(int(temp[2]))
        day.append(int(temp[1]))

    maxyear=min(year) #나이 많은 사람
    minyear=max(year) #나이 적은 사람

    resultmax=""#나이 적은 사람
    if year.count(minyear)==1: #year
        resultmax=name[year.index(minyear)]
    else:
        tempyear=[]
        for i in range(n):
            if year[i]==minyear:
                tempyear.append(i) #year index save
        tempmonth=[]
        for i in tempyear: #month
           tempmonth.append(month[i])
        maxmonth=max(tempmonth)
        if tempmonth.count(maxmonth)==1:
            resultmax=name[tempyear[tempmonth.index(maxmonth)]]
        else:
            tempday=[]
            for i in range(n): #day
                if month[i]==maxmonth:
                    tempday.append(day[i])
            maxday=max(tempday)
            resultmax=name[day.index(maxday)]

    resultmin=""#나이 많은 사람
    if year.count(maxyear)==1:
        resultmin=name[year.index(maxyear)]
    else:
        tempyear=[]
        for i in range(n): #year
            if year[i]==maxyear:
                tempyear.append(i) #year index save
        tempmonth=[]
        for i in tempyear: #month
           tempmonth.append(month[i])
        minmonth=min(tempmonth)
        if tempmonth.count(minmonth)==1:
            resultmin=name[tempyear[tempmonth.index(minmonth)]]
        else:
            tempday=[]
            for i in range(n): #day
                if month[i]==minmonth:
                    tempday.append(day[i])
            minday=min(tempday)
            resultmin=name[day.index(minday)]

    print(resultmax) #나이 적은 사람
    print(resultmin) #나이 많은 사람

