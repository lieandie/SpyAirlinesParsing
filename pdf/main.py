import PyPDF2
import re

if __name__ == '__main__':
    regex = ur"(\d{2}\s\w{3})\s{2}-\s{2}(\d{2}\s\w{3})([1-7 ]*)(\d{2}:\d{2})(\d{2}:\d{2}(\+1)?)(\w{2}\d*\*?)(.{3})(\d{1,2}H\d{1,2}M)"
    start_page_num = 4
    end_page_num = 27514
    cell_delimiter = '\t'
    row_delimiter = '\n'
    nested_regex_group_numbers = {6}

    input_file = open('assets/Skyteam_Timetable.pdf', 'rb')
    output_file = open('assets/Skyteam_Timetable.txt', 'w+')
    print 'Files ready'

    PDF_report = PyPDF2.PdfFileReader(input_file)
    print 'PDF opened'

    print 'Processing'
    for current_page_num in range(start_page_num, end_page_num):
        print str(current_page_num) + ' of ' + str(end_page_num)
        page = PDF_report.getPage(current_page_num)
        matches = re.finditer(regex, page.extractText(), re.MULTILINE)
        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                if groupNum not in nested_regex_group_numbers:
                    groupString = match.group(groupNum)
                    if groupString:
                        output_file.write(match.group(groupNum) + cell_delimiter)
            output_file.write(row_delimiter)
