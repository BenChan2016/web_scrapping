# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
from bs4 import BeautifulSoup
import string


lst = [];
list_of_integer = list(range(1,101));
code_name_pair = [[]];

page = requests.get("http://apps.who.int/classifications/icd10/browse/2010/en/GetConcept?ConceptId=A01")
soup  = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
string_count = 0;

for string_count in range(0,len(string.ascii_uppercase[:])):
    for num_count in range (0,len(list_of_integer)):
        lst.append(str(string.ascii_uppercase[string_count])+str(list_of_integer[num_count]).zfill(2))


for i in range(0,len(lst)):
    page = requests.get("http://apps.who.int/classifications/icd10/browse/2010/en/GetConcept?ConceptId="+str(lst[i]));
    soup = BeautifulSoup(page.content, 'html.parser');
    Label = soup.find_all('span', {'class':'label'});
    Code = soup.find_all('a',class_='code');
    for j in range (0,len(Label)):
        if any([Code[j].get_text(),Label[j].get_text()] == sublist for sublist in code_name_pair):
            continue;
        else:
            code_name_pair.append([Code[j].get_text(),Label[j].get_text()]);
            print(code_name_pair);
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
  

    


# =============================================================================
#     Category1 = soup.find_all('div', class_='Category1')
#     page = soup.find_all('div', class_='Category1')
# =============================================================================







