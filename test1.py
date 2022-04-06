import xlwt
def write_file():
    book = xlwt.Workbook(encoding='utf-8') #创建Workbook，相当于创建Excel

    # 创建sheet，Sheet1为表的名字，cell_overwrite_ok为是否覆盖单元格
    sheet1 = book.add_sheet(u'Sheet1', cell_overwrite_ok=True)

    data = {
            "ID1": [ 130, 120, 100],
            "ID2": [ 100, 110, 120],
            "ID3": [ 125, 135, 135]
           }

    r = 0
    sheet1.write(0, 1, 'n1')
    sheet1.write(0, 2, 'n2')
    sheet1.write(0, 3, 'n3')
    for i, j in data.items():   # i表示data中的key，j表示data中的value
        le = len(j)   # values返回的列表长度
        sheet1.write(r+1, 0, i)
        for c in range(1, le + 1):  #values列表中索引
                sheet1.write(r+1, c, j[c - 1])
        r += 1  # 行数
    book.save('D:\\write.xls')
write_file()