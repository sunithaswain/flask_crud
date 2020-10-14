import pandas as pd
from pandas import DataFrame
class Convert_excel_table():
    @staticmethod
    def exceldata():
        fidata=list()
        secdata=list()
        src="F:/pandas/excel/annual-enterprise-survey-2018-financial-year-provisional-csv - Copy.csv"
        src1="F:/pandas/excel/annual-enterprise-survey-2018-financial-year2-csv.csv"
        read=pd.read_csv(src,nrows=5)
        df=DataFrame(read)
        #print (type(df))
        products_list = df.values.tolist()
        read2=pd.read_csv(src1,nrows=5)
        return products_list
    @staticmethod
    def tableformat():
        finaldata=Convert_excel_table().exceldata()
        file = open("F:/pandas/excel/table.html", "w")
        file.write("<html>")
        file.write("<head>")
        file.write("<title>")
        file.write("Displaying table format")
        file.write("</title>")
        file.write("</head>")
        file.write("<body>")
        file.write('<center><table border="5" width = 1200>')
        file.write("<table border=10>")
        for i in finaldata:
           for k in i:
               print (k,"KKKKKKK")
               try:
                   file.write('<tr><th><b><font color="red">' + str(k) + '</font></th></tr>')
               except ValueError:
                   print ("this is done")
               #file.write('<tr><th><b><font color="blue">' + k + '</font></th></tr>')
               # if type(k)=="int":
               #     file.write('<tr><th><b><font color="blue">' + k + '</font></th></tr>')
               # elif type(k)=="str":
               #     for k1 in k:
               #         file.write('<tr><th><b><font color="red">' + k1 + '</font></th></tr>')
        file.write("</table>")
        file.write("</body>")
        file.write("</html>")
        file.close()
#print ("hello",finaldata)
Convert_excel_table.tableformat()
