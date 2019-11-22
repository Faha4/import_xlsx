# -*- coding: utf-8 -*-

from odoo import models, fields, api
import xlrd
import base64
import os
import pandas as pd 
import csv
from xlsxwriter.workbook import Workbook
# import glob

class DataLinkedin(models.TransientModel):
    _name = 'data.linkedin'
    # csv_file = fields.Binary(string='CSV File to convert')
    xls_file_info_company = fields.Binary("Importation des infos de l'entreprise")


#     def import_csv(self):
        
#         filename_chem = open('./input/example_Na/example_Na.chem', 'r').read()
#         input_file_chem = filename_chem.format(albeitSSA=albeitSSA)
#         with open('./input/example_Na/example_Na.chem', 'w') as fid:
#             fid.write(input_file_chem)

#         fname = self.csv_file
#         # reader = csv.DictReader(base64.b64decode(fname))
#         input_file_chem = fname.format(albeitSSA=albeitSSA)
#         with open(fname, "rb") as f:
#             fichier = f.read()
#             self.file = base64.b64encode(fichier)
#             read_file = pd.read_csv(self.file, encoding= 'UTF-8')
#             read_file.to_excel ('/home/dev/Téléchargements/encode.xlsx', index = None, header=True)

# #path_to_directory = min(glob.iglob('/home/dev/Téléchargements/*.xls'), key=os.path.getctime)

    def import_info_company(self):
        infoc = xlrd.open_workbook(file_contents=base64.decodestring(self.xls_file_info_company))
        for sheet in infoc.sheets():
            for row in range(sheet.nrows):
                array = []
                for col in range(sheet.ncols):
                    array.append(sheet.cell(row,col).value)  
                if array:
                    leads = self.env['crm.lead'].search([('name','ilike',array[0].encode('utf-8'))])
                    if leads:
                        leads.update({'contact_description':array[2], 'contact_website':array[4], 'contact_secteur':array[7], 'contact_employee_quantity':array[8], 'city':array[9], 'contact_type_company':array[10], 
                            'contact_linkedin':array[26], 'street':array[37]})   

    




        #Pour l'importation CSV(erreur : nom de fichier trop long)
    # with open(fname) as csvfile:
    #     reader = csv.DictReader(base64.b64decode(csvfile).split('\n'))
    #     for row in reader:
    #         if row['linkedinUrl']:
    #             leads = self.env['crm.lead'].search([('name','=','efe')])
    #             if leads:
    #                 leads.update({'contact_birthplace':row['linkedinUrl']})
    

    # def convert_csv_to_xls(self):
    #     for self.csv_file_info_company in glob.glob(os.path.join('.', '*.csv')):
    #         workbook = Workbook(self.csv_file_info_company[:-4] + '.xlsx')
    #         worksheet = workbook.add_worksheet()
    #         with open(self.csv_file_info_company, 'rt', encoding='utf8') as f:
    #             reader = csv.reader(f)
    #             for r, row in enumerate(reader):
    #                 for c, col in enumerate(row):
    #                     worksheet.write(r, c, col)
    #         workbook.close()