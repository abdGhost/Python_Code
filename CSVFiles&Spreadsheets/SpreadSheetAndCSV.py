# import csv

# Open the file
# data = open('example.csv', encoding='utf-8')

# csv.reader
# csv_data = csv.reader(data)

# reformat it into a python object list of lists
# data_lines = list(csv_data)

# print(data_lines[0])

# for line in data_lines[:5]:
#     print(line)


# all_emails = []
#
# for line in data_lines[1:]:
#     all_emails.append(line[3])
#
# print(all_emails)

# full_name = []
#
# for line in data_lines[1:]:
#     full_name.append(line[1] +" "+ line[2])
#
# print(full_name)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$ Write in CSV FILE $$$$$$$$$$$$$$$$$$$$$$$$

# file_to_output = open('to_save_file.csv', mode='w',newline='')
# csv_writer = csv.writer(file_to_output, delimiter=',')
# csv_writer.writerow(['a', 'b', 'c'])
#
# csv_writer.writerows([['1','2','3'],['3','4','5']])
# file_to_output.close()

# $$$$$$$$$$$$$ ERROR OPENING CSV FILE $$$$$$$$$$$$$$$

# f = open('to_save_file.csv', mode='a', newline='')
# csv_writer = csv.writer(f, delimiter=',')
# csv_writer = csv_writer(f)
# csv_writer.writerow(['1','2','3'])

# import PyPDF2
#
# f = open('Working_Business_Proposal.pdf','rb')
# pdf_reader = PyPDF2.PdfFileReader(f)
#
# print(pdf_reader.numPages)
#
# page_one = pdf_reader.getPage(0)
#
# page_one_text = page_one.extractText()
# # print(page_one_text)
#
# f.close()
#
# f = open("Working_Business_Proposal.pdf", "rb")
# pdf_reader = PyPDF2.PdfFileReader(f)
#
# first_page = pdf_reader.getPage(0)
#
# pdf_writer = PyPDF2.PdfFileWriter()
#
# pdf_writer.addPage(first_page)
# pdf_output = open('Some_BrandNew_doc.pdf', 'wb')
#
# f.close()
# pdf_output.close()
#
# f = open("Working_Business_Proposal.pdf", 'rb')
#
# pdf_text = []
# pdf_reader = PyPDF2.PdfFileReader(f)
#
# for num in range(pdf_reader.numPages):
#
#     page = pdf_reader.getPage(num)
#     pdf_text.append(page.extractText())
#
# print(pdf_text[:1])

import csv

data = open('Exercise_Files/find_the_link.csv', encoding='utf-8')
csv_data = csv.reader(data)

data_lines = list(csv_data)
# print(data_lines)

link_str = ''

for row_num, data in enumerate(data_lines):

    link_str += data[row_num]

print(link_str)

import PyPDF2

f = open('Exercise_Files/Find_the_phone_number.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(f)
# print(pdf.numPages)

import re

pattern = r'\d{3}.\d{3}.\d{4}'

all_text = ''

for n in range(pdf.numPages):

    page = pdf.getPage(n)
    page_text = page.extractText()

    all_text = all_text +' '+page_text

# print(all_text)

for match in re.finditer(pattern,all_text):
    print(match)


























