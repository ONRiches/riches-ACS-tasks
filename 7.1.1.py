Outlet1Sales = [10, 12,15,10]
Outlet2Sales = [5,8,3,6]
Outlet3Sales = [10,12,15,10]
total = [0,0,0,0]

for count in range (0,4):
    total[count] = Outlet1Sales[count] + total[count]
    total[count] = Outlet2Sales[count] + total[count]
    total[count] = Outlet3Sales[count] + total[count]
    print("The total sales for Q", count + 1, " is ", total[count])