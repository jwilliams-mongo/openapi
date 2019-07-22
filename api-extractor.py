#!/usr/bin/python
#coding=utf-8
import csv
import sys
import requests
import bs4
import subprocess
import re

def path_param_checker(soup):
    #Request Path Param
    path_param_code = soup.select('#'+'request-path-parameters')
    
    if(path_param_code):
        path_param_soup = bs4.BeautifulSoup(str(path_param_code[0]), 'lxml')
        if(path_param_soup.find_all('tbody')):
            with open(sys.argv[1], 'a') as output:
                writer = csv.writer(output)
                writer.writerow(["Request Path Parameters"])
            return True
        else: 
            return False
    return False


def query_param_checker(soup):
    #Request Query Param
    query_param_code = soup.select('#'+'request-query-parameters')
    if(query_param_code):
        query_param_soup = bs4.BeautifulSoup(str(query_param_code[0]), 'lxml')
        if(query_param_soup.find_all('tbody')):
            with open(sys.argv[1], 'a') as output:
                writer = csv.writer(output)
                writer.writerow(["Request Query Parameters"])
            return True
        else:
            return False
    return False


def body_param_checker(soup):
    body_param_code = soup.select('#'+'request-body-parameters')
    if(body_param_code):
        body_param_soup = bs4.BeautifulSoup(str(body_param_code[0]), 'lxml')
        if(body_param_soup.find_all('tbody')):
            with open(sys.argv[1], 'a') as output:
                writer = csv.writer(output)
                writer.writerow(["Request Body Parameters"])
            return True
        else:
            return False
    return False

def response_elems_checker(soup):
    response_elements_code_1 = soup.select('#'+'response-elements')
    response_elements_code_2 = soup.select('#'+'response')
    if(response_elements_code_1 or response_elements_code_2):
        if(response_elements_code_1):
            response_elems_soup = bs4.BeautifulSoup(str(response_elements_code_1[0]), 'lxml')
            if(response_elems_soup.find_all('tbody')):
                with open(sys.argv[1], 'a') as output:
                    writer = csv.writer(output)
                    writer.writerow(["Response Elements"])
                return True
            else:
                return False
        else:
            response_elems_soup_2 = bs4.BeautifulSoup(str(response_elements_code_2[0]), 'lxml')
            if(response_elems_soup_2.find_all('tbody')):
                with open(sys.argv[1], 'a') as output:
                    writer = csv.writer(output)
                    writer.writerow(["Response Elements"])
                return True
            else:
                return False
    return False



def main():

    if len(sys.argv) < 2:
        print ('Usage: %s <output-file> <url>' % sys.argv[0])
        sys.exit(1)

   
    fields = ["Application", "Title", "Filename", "Base URL"]

    values_list = []


    url = sys.argv[2]
    res = requests.get(url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    #Application
    app = soup.select('title')[0].getText()[-13:]
    values_list.append(app)

    #title
    title = soup.select('title')[0].getText()[:-19]
    values_list.append(title)

    #file name 
    file_name = url.split('/')[-1]
    values_list.append(file_name)

    #base url
    pattern = re.compile(r'Base URL')
    base_url = soup.find_all(text=re.compile("^https?://[^/]+/([^/]+)/.*$"))[0]
    values_list.append(base_url)

    # Write to the output file 
    with open(sys.argv[1], 'a') as output:
        writer = csv.writer(output)
        writer.writerow(fields)
        writer.writerow(values_list)
    
    #Request Path Param
    #path_param = path_param_checker()

    if(path_param_checker(soup)):
        path = subprocess.check_output(['htmltab',url, sys.argv[1]])

        #Request Query Param
        if(query_param_checker(soup)):        
            query = subprocess.check_output(['htmltab', '--select', '2', url, sys.argv[1]])

            if(body_param_checker(soup)):
                body = subprocess.check_output(['htmltab', '--select', '3', url, sys.argv[1]])

                if(response_elems_checker(soup)):
                    reponse = subprocess.check_output(['htmltab', '--select', '4', url, sys.argv[1]])
            else:

                if(response_elems_checker(soup)):
                    reponse = subprocess.check_output(['htmltab', '--select', '3', url, sys.argv[1]])
        
        elif(body_param_checker(soup)):
            body = subprocess.check_output(['htmltab', '--select', '2', url, sys.argv[1]])

            #Response Elements
            if(response_elems_checker(soup)):
                reponse = subprocess.check_output(['htmltab', '--select', '3', url, sys.argv[1]])
        else:
            #Response Elements
            if(response_elems_checker(soup)):
                reponse = subprocess.check_output(['htmltab', '--select', '2', url, sys.argv[1]])

    elif(query_param_checker(soup)):
        #Request Query Param
        query = subprocess.check_output(['htmltab', '--select', '1', url, sys.argv[1]])

        if(body_param_checker(soup)):
            body = subprocess.check_output(['htmltab', '--select', '2', url, sys.argv[1]])

            if(response_elems_checker(soup)):
                reponse = subprocess.check_output(['htmltab', '--select', '3', url, sys.argv[1]])
        else:
            if(response_elems_checker(soup)):
                reponse = subprocess.check_output(['htmltab', '--select', '2', url, sys.argv[1]])

    elif(body_param_checker(soup)):
        body = subprocess.check_output(['htmltab', '--select', '1', url, sys.argv[1]])

        if(response_elems_checker(soup)):
            reponse = subprocess.check_output(['htmltab', '--select', '2', url, sys.argv[1]])
    else:
        if(response_elems_checker(soup)):
            reponse = subprocess.check_output(['htmltab', '--select', '1', url, sys.argv[1]])


    with open(sys.argv[1], 'a') as output:
        writer = csv.writer(output)
        writer.writerow(["~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"])
       
if __name__ == "__main__":
	main()



