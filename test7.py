import matplotlib.pyplot as plt  #画图用
import numpy as np
import matplotlib
import xlrd  				#读Excel数据用
import xlwt
import xlsxwriter as xw     #写Excel数据用
file_all=['30cm.xls','50cm.xls','70cm.xls','90cm.xls','110cm.xls','130cm.xls','150cm.xls','170cm.xls','200cm.xls','250cm.xls','300cm.xls','350cm.xls','400cm.xls']
file1 = "D:\\数据\\"
file_name1 = "D:\\数据\\date2\\"
for z in range(len(file_all)):
    file = file1 + file_all[z]
    file_name = file_name1 + file_all[z]
    print(file,file_name)
    data = xlrd.open_workbook(file)
    sheet = data.sheet_by_index(0)

    book = xlwt.Workbook(encoding='utf-8') #创建Workbook，相当于创建Excel
    worksheet1 = book.add_sheet(u'Sheet1', cell_overwrite_ok=True)

    title = ['x_now', 'aera_max', 'aera_min','angle_max', 'angle_min','aera_aver','angle_aver']  # 设置表头
    for i in range (len(title)):
        worksheet1.write(0, i, title[i])
    j = 1  # 从第二行开始写入数据

    #print(sheet.cell_value(0,0))
    row = sheet.nrows
    col = sheet.ncols
    x_now=0
    flag=0
    for i in range(1,row-2):
        if(not flag):
            flag = 1
            x_now = sheet.cell_value(i,1)
            angle_max = sheet.cell_value(i, 3)
            angle_min = sheet.cell_value(i, 3)
            angle_aver = sheet.cell_value(i, 3)
            aera_max = sheet.cell_value(i, 4)
            aera_min = sheet.cell_value(i, 4)
            aera_aver = sheet.cell_value(i, 4)
            x_all = 1
        else:
            if((sheet.cell_value(i,1)) !=x_now):
                aera_aver = aera_aver/ x_all
                angle_aver = angle_aver/x_all
                #写入数据 title = ['x_now', 'aera_max', 'aera_min','angle_max', 'angle_min','aera_aver','angle_aver']  # 设置表头
                worksheet1.write(j, 0, x_now)
                worksheet1.write(j, 1, aera_max)
                worksheet1.write(j, 2, aera_min)
                worksheet1.write(j, 3, angle_max)
                worksheet1.write(j, 4, angle_min)
                worksheet1.write(j, 5, aera_aver)
                worksheet1.write(j, 6, angle_aver)

                angle_max = sheet.cell_value(i, 3)
                angle_min = sheet.cell_value(i, 3)
                aera_max = sheet.cell_value(i,4)
                aera_min = sheet.cell_value(i,4)
                x_now = sheet.cell_value(i,1)
                aera_aver = sheet.cell_value(i,4)
                angle_aver = sheet.cell_value(i, 3)
                x_all = 1
                j +=1
            else:
                if(aera_max<(sheet.cell_value(i,4))):
                    aera_max = sheet.cell_value(i,4)
                if(aera_min>(sheet.cell_value(i,4))):
                    aera_min = sheet.cell_value(i, 4)

                if (angle_max < (sheet.cell_value(i, 3))):
                    angle_max = sheet.cell_value(i, 3)
                if (angle_min > (sheet.cell_value(i, 3))):
                    angle_min = sheet.cell_value(i, 3)
                x_all +=1
                aera_aver += sheet.cell_value(i,4)
                angle_aver += sheet.cell_value(i,3)
    book.save(file_name)








