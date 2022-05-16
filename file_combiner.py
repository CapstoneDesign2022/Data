import csv

coin_name = "ZRX"

f = open(f'BINANCE_{coin_name}USDT_1m.csv','r',encoding= 'utf-8')
Bi = csv.reader(f)

f = open(f'UPBIT_{coin_name}KRW_1m.csv','r',encoding= 'utf-8')
Up = csv.reader(f)

f=open(f'combine_{coin_name}.csv','w',newline='')
wr=csv.writer(f)

B_data=[]
U_data=[]
for i in Bi:
    B_data.append(i)
for i in Up:
    U_data.append(i)

cnt = 0
for i in range(len(B_data)):
    B_current = B_data[i]
    U_current = U_data[cnt]
    if(B_current[0] == U_current[0]):
            wr.writerow([B_current[0], B_current[1], B_current[2], B_current[3], B_current[4], B_current[5],
                        U_current[0], U_current[1], U_current[2], U_current[3], U_current[4], U_current[5]])
            cnt+=1




f.close()


# f = open('USDT.csv','r',encoding = 'utf -8')
# USDT = csv.reader(f)