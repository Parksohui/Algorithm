import sys

def main():
    n,m=map(int, sys.stdin.readline().split()) # 세로, 가로

    arr=[]
    for i in range(n):
        arr.append(list(map(int,sys.stdin.readline().split())))

    result=0

    Fig_1_x=[0,1,2,3]
    Fig_1_y=[0,0,0,0]

    for i in range(n):
        for j in range(m):
            flag_a=True;flag_b=True;temp_a=0;temp_b=0
            for k in range(4):
                x_1=i+Fig_1_x[k]
                y_1=j+Fig_1_y[k]
                if 0<=x_1<n and 0<=y_1<m:
                    temp_a+=arr[x_1][y_1]
                else:
                    flag_a=False
                x_2=i+Fig_1_y[k]
                y_2=j+Fig_1_x[k]
                if 0<=x_2<n and 0<=y_2<m:
                    temp_b+=arr[x_2][y_2]
                else:
                    flag_b=False
            if flag_a==True and result<temp_a:
                result=temp_a
            if flag_b==True and result<temp_b:
                result=temp_b

    Fig_2_x=[0,0,1,1]
    Fig_2_y=[0,1,0,1]

    for i in range(n):
        for j in range(m):
            temp=0; flag=True
            for k in range(4):
                x=i+Fig_2_x[k]
                y=j+Fig_2_y[k]
                if 0<=x<n and 0<=y<m:
                    temp+=arr[x][y]
                else:
                    flag=False
                    break
            if flag==True and result<temp:
                result=temp

    Fig_3_x=[[0,1,2,2],[0,1,2,2],[0,0,1,2],[0,0,1,2]]
    Fig_3_y=[[0,0,0,1],[0,0,0,-1],[0,-1,-1,-1],[0,1,1,1]]

    for i in range(n):
        for j in range(m):
            for k in range(4):
                cnt_a = 0;cnt_b = 0;temp_a = 0;temp_b = 0
                for v in range(4):
                    x_1=i+Fig_3_x[k][v]
                    y_1=j+Fig_3_y[k][v]
                    if 0<=x_1<n and 0<=y_1<m:
                        cnt_a+=1
                        temp_a+=arr[x_1][y_1]
                    x_2=i+Fig_3_y[k][v]
                    y_2=j+Fig_3_x[k][v]
                    if 0<=x_2<n and 0<=y_2<m:
                        cnt_b+=1
                        temp_b+=arr[x_2][y_2]
                if cnt_a==4 and result<temp_a:
                    result=temp_a
                if cnt_b==4 and result<temp_b:
                    result=temp_b

    
    Fig_4_x=[[0,0,1,0],[0,0,-1,0],[0,0,-1,1],[0,0,-1,1]]
    Fig_4_y=[[0,1,1,2],[0,1,1,2],[0,1,1,1],[0,-1,-1,-1]]

    for i in range(n):
        for j in range(m):
            for k in range(4):
                cnt_a = 0;temp_a = 0
                for v in range(4):
                    x_1=i+Fig_4_x[k][v]
                    y_1=j+Fig_4_y[k][v]
                    if 0<=x_1<n and 0<=y_1<m:
                        cnt_a+=1
                        temp_a+=arr[x_1][y_1]
                if cnt_a==4 and result<temp_a:
                    result=temp_a

    Fig_5_x=[[0,1,1,2],[0,1,1,2]]
    Fig_5_y=[[0,0,1,1],[0,0,-1,-1]]

    for i in range(n):
        for j in range(m):
            for k in range(2):
                cnt_a = 0;cnt_b = 0;temp_a = 0;temp_b = 0
                for v in range(4):
                    x_1=i+Fig_5_x[k][v]
                    y_1=j+Fig_5_y[k][v]
                    if 0<=x_1<n and 0<=y_1<m:
                        cnt_a+=1
                        temp_a+=arr[x_1][y_1]
                    x_2=i+Fig_5_y[k][v]
                    y_2=j+Fig_5_x[k][v]
                    if 0<=x_2<n and 0<=y_2<m:
                        cnt_b+=1
                        temp_b+=arr[x_2][y_2]
                if cnt_a==4 and result<temp_a:
                    result=temp_a
                if cnt_b==4 and result<temp_b:
                    result=temp_b
    print(result)

if __name__=='__main__':
    main()