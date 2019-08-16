#!/usr/bin/python
#coding=utf-8
import csv
import sys
import requests
import bs4
import subprocess
import re


contains_response_doc = False
contains_results_embedded_doc = False

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
    global contains_response_doc 

    response_elements_code_1 = soup.select('#'+'response-elements')
    response_elements_code_2 = soup.select('#'+'response')

    if(response_elements_code_1 or response_elements_code_2):
        if(response_elements_code_1):
            response_elems_soup = bs4.BeautifulSoup(str(response_elements_code_1[0]), 'lxml')
            if(response_elems_soup.find_all('tbody')):
                with open(sys.argv[1], 'a') as output:
                    writer = csv.writer(output)
                    writer.writerow(["Response Elements"])
                    
                    if(response_elems_soup.select('#'+'response-document')):
                        contains_response_doc = True
                        writer.writerow(["Response Document"])

                return True
            else:
                return False
        else:
            response_elems_soup_2 = bs4.BeautifulSoup(str(response_elements_code_2[0]), 'lxml')
            if(response_elems_soup_2.find_all('tbody')):
                with open(sys.argv[1], 'a') as output:
                    writer = csv.writer(output)
                    writer.writerow(["Response Elements"])

                    if(response_elems_soup_2.select('#'+'response-document')):
                        contains_response_doc = True
                        writer.writerow(["Response Document"])

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
    title = soup.select('h1')[0].getText()[:-2]
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

    #tags_list = ['h2+p+div+table.docutils', 'h2+p+table.docutils', 'h2+div+table.docutils', 'h2+table.docutils', 'h2+table.docutils', 'h3+p+p+table.docutils',
    #'h3+p+table.docutils', 'div#response-elements+h3+p+table.docutils', 'div#response+h3+p+table.docutils']
    
    tags_list = ["(//div[@id='response-elements']//table)[1]/tbody/tr", "(//div[@id='response']//table)[1]/tbody/tr"]
    tags_list_2 = ["(//div[@id='response-elements']//table)[2]/tbody/tr", "(//div[@id='response']//table)[2]/tbody/tr"]
    #Request Path Param

    if(path_param_checker(soup)):
        path = subprocess.check_output(['htmltab',url, sys.argv[1]])

        #Request Query Param
        if(query_param_checker(soup)):        
            query = subprocess.check_output(['htmltab', '--select', '2', url, sys.argv[1]])

            if(body_param_checker(soup)):
                body = subprocess.check_output(['htmltab', '--select', '3', url, sys.argv[1]])

                if(response_elems_checker(soup)):
                    for tags in tags_list:
                        try:
                            reponse = subprocess.check_output(['htmltab', '--select', tags, url, sys.argv[1]])
                        except subprocess.CalledProcessError as e:
                            continue
                    if(contains_response_doc):
                        with open(sys.argv[1], 'a') as output:
                            writer = csv.writer(output)
                            writer.writerow(["results Embedded Document"])

                        for tags in tags_list_2:
                            try:
                                reponse = subprocess.check_output(['htmltab', '--select', tags, url, sys.argv[1]])
                            except subprocess.CalledProcessError as e:
                                continue


            else:
                if(response_elems_checker(soup)):
                    for tags in tags_list:
                        try:
                            reponse = subprocess.check_output(['htmltab', '--select', tags, url, sys.argv[1]])
                        except subprocess.CalledProcessError as e:
                            continue
                    if(contains_response_doc):
                        with open(sys.argv[1], 'a') as output:
                            writer = csv.writer(output)
                            writer.writerow(["results Embedded Document"])
                        for tags in tags_list_2:
                            try:
                                reponse = subprocess.check_output(['htmltab', '--select', tags, url, sys.argv[1]])
                            except subprocess.CalledProcessError as e:
                                continue

        
        elif(body_param_checker(soup)):
            body = subprocess.check_output(['htmltab', '--select', '2', url, sys.argv[1]])

            #Response Elements
            if(response_elems_checker(soup)):
                for tags in tags_list:
                    try:
                        reponse = subprocess.check_output(['htmltab', '--select', tags, url, sys.argv[1]])
                    except subprocess.CalledProcessError as e:
                        continue
                if(contains_response_doc):
                    with open(sys.argv[1], 'a') as output:
                        writer = csv.writer(output)
                        writer.writerow(["results Embedded Document"])
                    for tags in tags_list_2:
                        try:
                            reponse = subprocess.check_output(['htmltab', '--select', tags, url, sys.argv[1]])
                        except subprocess.CalledProcessError as e:
                            continue


        else:
            #Response Elements
            if(response_elems_checker(soup)):
                for tags in tags_list:
                    try:
                        reponse = subprocess.check_output(['htmltab', '--select', tags, url, sys.argv[1]])
                    except subprocess.CalledProcessError as e:
                        continue
                if(contains_response_doc):
                    with open(sys.argv[1], 'a') as output:
                        writer = csv.writer(output)
                        writer.writerow(["results Embedded Document"])
                    for tags in tags_list_2:
                        try:
                            reponse = subprocess.check_output(['htmltab', '--select', tags, url, sys.argv[1]])
                        except subprocess.CalledProcessError as e:
                            continue

    elif(query_param_checker(soup)):
        #Request Query Param
        query = subprocess.check_output(['htmltab', '--select', '1', url, sys.argv[1]])

        if(body_param_checker(soup)):
            body = subprocess.check_output(['htmltab', '--select', '2', url, sys.argv[1]])

            if(response_elems_checker(soup)):
                for tags in tags_list:
                    try:
                        reponse = subprocess.check_output(['htmltab', '--select', tags, url, sys.argv[1]])
                    except subprocess.CalledProcessError as e:
                        continue

                if(contains_response_doc):
                    
                    with open(sys.argv[1], 'a') as output:
                        writer = csv.writer(output)
                        writer.writerow(["results Embedded Document"])
                    for tags in tags_list_2:
                        try:
                            reponse = subprocess.check_output(['htmltab', '--select', tags, url, sys.argv[1]])
                        except subprocess.CalledProcessError as e:
                            continue

        else:
            if(response_elems_checker(soup)):
                for tags in tags_list:
                    try:
                        reponse = subprocess.check_output(['htmltab', '--select', tags, url, sys.argv[1]])
                    except subprocess.CalledProcessError as e:
                        continue
                if(contains_response_doc):

                    for tags in tags_list_2:
                        try:
                            reponse = subprocess.check_output(['htmltab', '--select', tags, url, sys.argv[1]])
                        except subprocess.CalledProcessError as e:
                            continue

    elif(body_param_checker(soup)):
        body = subprocess.check_output(['htmltab', '--select', '1', url, sys.argv[1]])

        if(response_elems_checker(soup)):
            for tags in tags_list:
                try:
                    reponse = subprocess.check_output(['htmltab', '--select', tags, url, sys.argv[1]])
                except subprocess.CalledProcessError as e:
                    continue
            if(contains_response_doc):
                for tags in tags_list_2:
                    try:
                        reponse = subprocess.check_output(['htmltab', '--select', tags, url, sys.argv[1]])
                    except subprocess.CalledProcessError as e:
                        continue
    else:
        if(response_elems_checker(soup)):
            reponse = subprocess.check_output(['htmltab', '--select', '1', url, sys.argv[1]])


    with open(sys.argv[1], 'a') as output:
        writer = csv.writer(output)
        writer.writerow(["~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"])
        writer.writerow("")
if __name__ == "__main__":
	main()



