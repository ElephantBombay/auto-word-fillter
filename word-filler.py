from docxtpl import DocxTemplate
import sys, os
import click
import csv
import datetime


def extract_from_csv(path_csv):
    with open(path_csv) as csvDataFile:
        data = [row for row in csv.reader(csvDataFile)]
        data.pop(0)
    return data

@click.command()
@click.option('--name', prompt='Your name', help='Name of the report creator')
@click.option('--last', prompt='Your last name', help='Last name of the report creator')
@click.option('--company', prompt='Your company', help='Name of the company')

def fill_doc(name, last, company):
    csv_data = extract_from_csv("test.csv")
    context = {
        "name": name,
        "last": last,
        "company": company,
        "created": datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
        "table" : csv_data,
    }

    # import pdb; pdb.set_trace()
    doc = DocxTemplate("templates/my-template.docx")
    doc.render(context)
    doc.save("output/generated_doc.docx")
    click.echo("Report complete!")

   
    
if __name__ == '__main__':
    fill_doc()