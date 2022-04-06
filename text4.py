import xlwt

def read_file(file1,file2):
    fp = open(file1,'r+')
    l=[]
    data = fp.readlines()
    r = 0
    book = xlwt.Workbook(encoding='utf-8')  # 创建Workbook，相当于创建Excel
    sheet1 = book.add_sheet(u'Sheet1', cell_overwrite_ok=True)
    sheet1.write(0, 1, 'x')
    sheet1.write(0, 2, 'y')
    sheet1.write(0, 3, '角度')
    sheet1.write(0, 4, '面积')
    sheet1.write(1, 0, '数据1')
    for i in range(len(data)):  #len(data)为数据行数
        for j in range(len(list(data[0].split()))):   #len(list(data[0].split()))为数据列数
            l.append(data[i].split(' ')[j])
    #print(l)
    m=0
    n=0
    for x in range(len(l)):
        sheet1.write(m + 1, n + 1, l[x])
        look = l[x].replace('.','')
        look = look.replace('-', '')
        #print(look)
        if(not look.isdigit()):
            n=0
            sheet1.write(m+2, n, '数据'+str(m+2))
            m+=1
        else:
            n+=1
    book.save(file2)

file1 = 'D:\\数据\\13.txt'
file2 ='D:\\数据\\400cm.xls'
read_file(file1,file2)