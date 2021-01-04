from docxtpl import DocxTemplate
import sys, os
import click
import csv
import datetime


def extract_from_csv(path_csv):
    
    with open(path_csv) as csvDataFile:
        data = [row for row in csv.reader(csvDataFile)]
        import pdb; pdb.set_trace()
        date = data[1][0]
        order = data[1][1]
        volume = data[1][2]
        price = data[1][3]

    return date, order, volume, price



@click.command()
@click.option('--name', prompt='Your name', help='Name of the report creator')
@click.option('--last', prompt='Your last name', help='Last name of the report creator')
@click.option('--company', prompt='Your company', help='Name of the company')

def fill_doc(name, last, company):
    csv_data = extract_from_csv("test.csv")
    # import pdb; pdb.set_trace()
    data = {
        "name": name,
        "last": last,
        "company": company,
        "created": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        "order": csv_data[1],
        "date": csv_data[0],
        "volume": csv_data[2], 
        "price": csv_data[3]
    }
    # fill_doc("templates/my-template.docx", {"created": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),"name": name, "last": last, "company": company,})
    # fill_doc("templates/my-template.docx", context)

    doc = DocxTemplate("templates/my-template.docx")
    context = data
    doc.render(context)
    doc.save("output/generated_doc.docx")
        # "company": company,
        # "date": csv_data[0],
        # "volume": csv_data[1], 
        # "price": csv_data[2]
   
    
if __name__ == '__main__':
    fill_doc()