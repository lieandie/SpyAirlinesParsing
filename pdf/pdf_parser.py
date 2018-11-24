import PyPDF2
import re
import csv

if __name__ == '__main__':
    cell_delimiter = ';'

    input_file_path = '../assets/Skyteam_Timetable.pdf'
    output_file_path = '../assets/Skyteam_Timetable.csv'

    table_row_regex = ur"(\d{2}\s\w{3})\s{2}-\s{2}(\d{2}\s\w{3})([1-7 ]*)(\d{2}:\d{2})(\d{2}:\d{2}(\+1)?)(\w{2}\d*\*?)(.{3})(\d{1,2}H\d{1,2}M)"

    start_page_num = 4
    end_page_num = 27514

    nested_regex_group_numbers = {6}
    header = ["validity_from", "validity_to", "days", "dep_time", "arr_time", "flight", "aircraft", "travel_time"]

    input_file = open(input_file_path, 'rb')
    output_file = open(output_file_path, 'wb')
    output_file_writer = csv.writer(output_file, delimiter=cell_delimiter)
    print 'Files ready'

    PDF_report = PyPDF2.PdfFileReader(input_file)
    print 'PDF opened'

    output_file_writer.writerow(header)
    print 'Header writen'

    print 'Processing'
    for current_page_num in range(start_page_num, end_page_num):
        print str(current_page_num) + ' of ' + str(end_page_num)
        page = PDF_report.getPage(current_page_num)
        matches = re.finditer(table_row_regex, page.extractText(), re.MULTILINE)
        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1
            row = []
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                if groupNum not in nested_regex_group_numbers:
                    groupString = match.group(groupNum)
                    if groupString:
                        row.append(match.group(groupNum))
            output_file_writer.writerow(row)
    output_file.close()
    input_file.close()
