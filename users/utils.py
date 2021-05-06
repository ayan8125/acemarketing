import xlsxwriter
from io import BytesIO
from django.utils.translation import ugettext


def WriteToExcel(data, camp_name):
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet("Leads")

    title = workbook.add_format({
        'bold': True,
        'font_size': 14,
        'align': 'center',
        'valign': 'vcenter'
    })
    header = workbook.add_format({
        'bg_color': '#F7F7F7',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
    })

    cell_center = workbook.add_format({
        'bg_color': '#F7F7F7',
        'color': 'black',
        'align': 'center',
        'valign': 'top',
        'border': 1
    })
    cell = workbook.add_format({
        'bg_color': '#F7F7F7',
        'color': 'black',
        'valign': 'top',
        'border': 1
    })

    # addding title to excel file
    title_text = u"{0} {1}".format(
        ugettext("Leads of "), camp_name)
    worksheet.merge_range('B2:H2', title_text, title)

    worksheet.set_column('A:A', 5)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 25)
    worksheet.set_column('E:E', 25)

    worksheet.write(4, 0, ugettext("No"), header)
    worksheet.write(4, 1, ugettext("First Name"), header)
    worksheet.write(4, 2, ugettext("Last Name"), header)
    worksheet.write(4, 3, ugettext("Email"), header)
    worksheet.write(4, 4, ugettext("Phone Number"), header)

    for idx, data in enumerate(data):
        row = 5 + idx
        worksheet.write_number(row, 0, idx + 1, cell_center)
        worksheet.write_string(row, 1, data.first_name, cell)
        worksheet.write_string(row, 2, data.last_name, cell)
        worksheet.write_string(row, 3, ugettext(data.email), cell)
        worksheet.write_string(row, 4, ugettext(str(data.phone_number)), cell)
        # the rest of the data

    workbook.close()
    xlsx_data = output.getvalue()
    # xlsx_data contains the Excel file
    return xlsx_data
