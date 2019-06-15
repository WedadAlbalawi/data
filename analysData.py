

print "Wrote By Wedad Albalawi"
print "Saturday 15th Jun 2019"
print "Pre-Interview Question from SCFHS"
print "Question : A friend once told me some in the Muslim community think people tend to die more (often) in the month of Shaban.As a data scientist, what do you think?" +"\n"

print "-------------------------Approach-------------------------" + "\n"

#Please make use of (but not limited to) the data by the Medina Municipality

#Structure your analysis with the following components:

print "1)objective"
print "     Scientifically, assay how many people died from Rajab to Ramadan in 1440 years Hijri, and what the highest death month is base on  Medina Municipality website"

print "2)Collect the data (save the data in the directory data/)"
#Data was extract from https://webscraper.io/ and save as Excel sheet as DataSetMeadinaDeathExcel.xlsx in data/ directory.However, there was issue when I extracted big data and website did not allowed to extract.

print "3+4)Data Exploration,Data Cleaning, and modling By python , I wrote code to explora and clean data"
print "5)print the result"+"\n"


import xlrd
import pandas as pd


FileName ="DataSetMeadinaDeathExcel.xlsx"

workbook = xlrd.open_workbook(FileName)
worksheet = workbook.sheet_by_name("DataSet") # We need to read the data
#from the Excel sheet named "Sheet1"
#print "".join("This Excel Sheet has " + str(worksheet.nrows) + " rows and " + str(worksheet.ncols) + " colums")
print "---------------------------Steps---------------------" + "\n"
print "The First step, pulls the Excelfile-DataSet Sheet as Dataframe"+ "\n"
sheetXl = pd.ExcelFile(FileName)
DataFrame  = sheetXl.parse("DataSet")   #-----> parse  read the DataSet as dataframe.

print "The Second step, read the dataFrame by .read_excel"+ "\n"
Data_read = pd.read_excel(FileName,delimiter='/t',name =['Name','Gender','Nationality','Age_Num','AgeDescripe','Yesr','Month','Day'])

print "The third step, Read lines and count how many people died from Rajab to Ramdan in 1440 year,Hijri " + "\n"

Num_Death_Rajab = []
Num_Death_Shaban =[]
Num_Death_Ramadan = []

for line in Data_read["Month"]:
    #print line
    if line == 7:
        Num_Death_Rajab.insert(0,line)
        #print "Yes"
    elif line == 8:
        Num_Death_Shaban.insert(0, line)
    elif line == 9:
        Num_Death_Ramadan.insert(0,line)
    else:
        print "No"

print "Finally, compare the results and find out which month  most people died  through the 1440 year in Madina comunity" + "\n"

Highestmonth_dic = {"Rajab":len(Num_Death_Rajab),"Shaban":len(Num_Death_Shaban),"Ramadan":len(Num_Death_Ramadan)}

def HighestDeathMonth(Highestmonth_dic):
    value = list(Highestmonth_dic.values())
    key = list(Highestmonth_dic.keys())
    return key[value.index(max(value))],Highestmonth_dic[key[value.index(max(value))]]



print "--------------------------Results---------------------------"+ "\n"

Totalline = len(Num_Death_Rajab) + len(Num_Death_Shaban) +len(Num_Death_Ramadan)
print "".join("The total number of people died from Rajab to Ramdan in 1440 Hijri base on Medina Municipality  is " + str(Totalline) + ", and it must be equil to the length of data  " + str(len(Data_read)) + " to avoid missing value") + "\n"
print "".join("The number of people died in Rajab, 1440 Hijri , Madina Community,Saudi Arabia  " + str(len(Num_Death_Rajab)))+ "\n"
print "".join("The number of people died in Shaban, 1440 Hijri , Madina Community,Saudi Arabia  " + str(len(Num_Death_Shaban)))+ "\n"
print "".join("The number of people died in Ramadan, 1440 Hijri , Madina Community,Saudi Arabia  " + str(len(Num_Death_Ramadan)))+ "\n"
print "Scientifically, the Highest Month death from Rajab to Ramadan in 1440 year-Hijri  is " + HighestDeathMonth(Highestmonth_dic)[0] +"\n"


print "--------------------------End----------------------------------"+ "\n"



