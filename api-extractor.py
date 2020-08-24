#!/usr/bin/python
#coding=utf-8
import csv
import sys
import requests
import bs4
import subprocess
import re
import string

contains_response_doc = False
contains_results_embedded_doc = False

def path_param_checker(soup):
    #Request Path Param
    path_param_code = soup.select('#'+'request-path-parameters')
    
    if(path_param_code):
        path_param_soup = bs4.BeautifulSoup(str(path_param_code[0]), 'lxml')
        if(path_param_soup.find_all('tbody')):
            # with open(sys.argv[1], 'a') as output:
            #     writer = csv.writer(output)
            #     writer.writerow(["Request Path Parameters"])
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
            # with open(sys.argv[1], 'a') as output:
            #     writer = csv.writer(output)
            #     writer.writerow(["Request Query Parameters"])
            return True
        else:
            return False
    return False


def body_param_checker(soup):
    body_param_code = soup.select('#'+'request-body-parameters')
    if(body_param_code):
        body_param_soup = bs4.BeautifulSoup(str(body_param_code[0]), 'lxml')
        if(body_param_soup.find_all('tbody')):
            # with open(sys.argv[1], 'a') as output:
            #     writer = csv.writer(output)
            #     writer.writerow(["Request Body Parameters"])
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
                # with open(sys.argv[1], 'a') as output:
                #     writer = csv.writer(output)
                #     writer.writerow(["Response Elements"])
                    
                if(response_elems_soup.select('#'+'response-document')):
                  contains_response_doc = True
                  # writer.writerow(["Response Document"])

                return True
            else:
                return False
        else:
            response_elems_soup_2 = bs4.BeautifulSoup(str(response_elements_code_2[0]), 'lxml')
            if(response_elems_soup_2.find_all('tbody')):
                # with open(sys.argv[1], 'a') as output:
                    # writer = csv.writer(output)
                    # writer.writerow(["Response Elements"])

                if(response_elems_soup_2.select('#'+'response-document')):
                  contains_response_doc = True
                  # writer.writerow(["Response Document"])

                return True
            else:
                return False
    return False

def path_param_writer(body):

  path_param_row = [app,title,collection,file_name,method,base_url,resource_path,'Path Param','','','','','']
  printable = set(string.printable)
  path_param_row[1] = ''.join(filter(lambda x: x in printable, path_param_row[1]))
  for row in body:
    if len(row) == 3:
      path_param_row[8] = ''.join(filter(lambda x: x in printable, row[0]))
      path_param_row[9] = ''.join(filter(lambda x: x in printable, row[1]))
      path_param_row[11] = ''.join(filter(lambda x: x in printable, row[2]))
      with open(sys.argv[1], 'a') as output:
        writer = csv.writer(output)
        writer.writerow(path_param_row)
    else: print(len(row))
  remove_temp = subprocess.check_output(['rm', 'temp.csv'])

def query_param_writer(body):

  query_param_row = [app,title,collection,file_name,method,base_url,resource_path,'Query Param','','','','','']
  printable = set(string.printable)
  query_param_row[1] = ''.join(filter(lambda x: x in printable, query_param_row[1]))
  for row in body:
    if len(row) == 4:
      query_param_row[8] = ''.join(filter(lambda x: x in printable, row[0]))
      query_param_row[9] = ''.join(filter(lambda x: x in printable, row[1]))
      query_param_row[11] = ''.join(filter(lambda x: x in printable, row[2]))
      query_param_row[12] = ''.join(filter(lambda x: x in printable, row[3]))
      with open(sys.argv[1], 'a') as output:
        writer = csv.writer(output)
        writer.writerow(query_param_row)
    else: print(len(row))
  remove_temp = subprocess.check_output(['rm', 'temp.csv'])

def body_param_writer(body):

  body_param_row = [app,title,collection,file_name,method,base_url,resource_path,'Body Param','','','','','']
  printable = set(string.printable)
  body_param_row[1] = ''.join(filter(lambda x: x in printable, body_param_row[1]))
  for row in body:
    if len(row) == 4:
      body_param_row[8] = ''.join(filter(lambda x: x in printable, row[0]))
      body_param_row[9] = ''.join(filter(lambda x: x in printable, row[1]))
      body_param_row[10] = ''.join(filter(lambda x: x in printable, row[2]))
      body_param_row[11] = ''.join(filter(lambda x: x in printable, row[3]))
      with open(sys.argv[1], 'a') as output:
        writer = csv.writer(output)
        writer.writerow(body_param_row)
    elif len(row) == 3:
      body_param_row[8] = ''.join(filter(lambda x: x in printable, row[0]))
      body_param_row[9] = ''.join(filter(lambda x: x in printable, row[1]))
      body_param_row[10] = ''
      body_param_row[11] = ''.join(filter(lambda x: x in printable, row[2]))
      with open(sys.argv[1], 'a') as output:
        writer = csv.writer(output)
        writer.writerow(body_param_row)
    else: print(len(row))
  remove_temp = subprocess.check_output(['rm', 'temp.csv'])

def response_writer(body):

  response_row = [app,title,collection,file_name,method,base_url,resource_path,'Response Element','','','','','']
  printable = set(string.printable)
  response_row[1] = ''.join(filter(lambda x: x in printable, response_row[1]))
  for row in body:
    if len(row) == 3:
      response_row[8] = ''.join(filter(lambda x: x in printable, row[0]))
      response_row[9] = ''.join(filter(lambda x: x in printable, row[1]))
      response_row[11] = ''.join(filter(lambda x: x in printable, row[2]))
      with open(sys.argv[1], 'a') as output:
        writer = csv.writer(output)
        writer.writerow(response_row)
    else: print(len(row))
  remove_temp = subprocess.check_output(['rm', 'temp.csv'])

def response_doc_writer(body):

  response_doc_row = [app,title,collection,file_name,method,base_url,resource_path,'Response Document Fields','','','','','']
  printable = set(string.printable)
  response_doc_row[1] = ''.join(filter(lambda x: x in printable, response_doc_row[1]))
  for row in body:
    if len(row) == 3:
      response_doc_row[8] = ''.join(filter(lambda x: x in printable, row[0]))
      response_doc_row[9] = ''.join(filter(lambda x: x in printable, row[1]))
      response_doc_row[11] = ''.join(filter(lambda x: x in printable, row[2]))
      with open(sys.argv[1], 'a') as output:
        writer = csv.writer(output)
        writer.writerow(response_doc_row)
    else: print(len(row))
  remove_temp = subprocess.check_output(['rm', 'temp.csv'])

def main():

    if len(sys.argv) < 2:
        print ('Usage: %s <output-file> <url>' % sys.argv[0])
        sys.exit(1)

    url = sys.argv[2]
    res = requests.get(url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    #Application
    global app 
    app = soup.select('title')[0].getText()[-13:]

    #title
    global title 
    title = soup.select('h1')[0].getText()[:-2]

    #file name 
    global file_name 
    file_name = url

    #base url and resource path
    global base_url
    pattern = re.compile(r'Base URL')
    global resource_path

    #handle exception
    try:
      base_url = soup.find_all(text=re.compile("^https?://[^/]+/([^/]+)/.*$"))[0]
    except:
      base_url = '/'

    resource_block = soup.select_one(".highlight")
    resource = str(resource_block)
    #handle exception for root resource
    try:
       resource_path = re.search("<\/span>.+?(\/.+)", resource).group(1)
       if resource_path[:15] == "/api/atlas/v1.0":
          resource_path = resource_path[15:]
       if re.search("v1.0(.+)",base_url):
         resource_path = re.search("v1.0(.+)",base_url).group(1) + resource_path
    except: resource_path = '/'

    global method
    try:
      method = re.search("<\/span>(.+?\s)\/.+", resource).group(1)
      print(method)
    except:
      method = "none"
      print(method)

    # Write to the output file 
    # with open(sys.argv[1], 'a+') as output:
        # writer = csv.writer(output)
        # writer.writerow(values_list)

    global collection
    collection_select = str(soup.select_one(".bc"))
    collection_matches = re.findall("<li><a.+?\">(.+?)<",collection_select)
    collection = collection_matches[-1]
    if collection == "Public API Resources": collection = "Root"

    #tags_list = ['h2+p+div+table.docutils', 'h2+p+table.docutils', 'h2+div+table.docutils', 'h2+table.docutils', 'h2+table.docutils', 'h3+p+p+table.docutils',
    #'h3+p+table.docutils', 'div#response-elements+h3+p+table.docutils', 'div#response+h3+p+table.docutils']


    tag_path = "(//div[@id='request-path-parameters']//table)[1]/tbody/tr"
    tag_query = "(//div[@id='request-query-parameters']//table)[1]/tbody/tr"
    tag_body = "(//div[@id='request-body-parameters']//table)[1]/tbody/tr"
    tags_list = ["(//div[@id='response-elements']//table)[1]/tbody/tr", "(//div[@id='response']//table)[1]/tbody/tr"]
    tags_list_2 = ["(//div[@id='response-elements']//table)[2]/tbody/tr", "(//div[@id='response']//table)[2]/tbody/tr"]
    #Request Path Param

    if(path_param_checker(soup)):
      body = subprocess.check_output(['htmltab', '--select', tag_path, url, "temp.csv"])
      with open('temp.csv', 'r') as file:
        reader = csv.reader(file)
        path_param_writer(reader)

        #Request Query Param
        if(query_param_checker(soup)):        
          body = subprocess.check_output(['htmltab', '--select', tag_query, url, "temp.csv"])
          with open('temp.csv', 'r') as file:
            reader = csv.reader(file)
            query_param_writer(reader)

            if(body_param_checker(soup)):
                body = subprocess.check_output(['htmltab', '--select', tag_body, url, "temp.csv"])
                with open('temp.csv', 'r') as file:
                  reader = csv.reader(file)
                  body_param_writer(reader)

                if(response_elems_checker(soup)):
                    for tags in tags_list:
                        try:
                            reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                            with open('temp.csv', 'r') as file:
                              reader = csv.reader(file)
                              response_writer(reader)
                        except subprocess.CalledProcessError as e:
                            continue
                    if(contains_response_doc):
                      reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                      with open('temp.csv', 'r') as file:
                        reader = csv.reader(file)
                        response_doc_writer(reader)
                        # with open(sys.argv[1], 'a') as output:
                        #     writer = csv.writer(output)
                        #     writer.writerow(["results Embedded Document"])

                        for tags in tags_list_2:
                            try:
                              reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                              with open('temp.csv', 'r') as file:
                                reader = csv.reader(file)
                                response_doc_writer(reader)
                            except subprocess.CalledProcessError as e:
                                continue

            else:
                if(response_elems_checker(soup)):
                    for tags in tags_list:
                        try:
                            reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                            with open('temp.csv', 'r') as file:
                              reader = csv.reader(file)
                              response_writer(reader)
                        except subprocess.CalledProcessError as e:
                            continue
                    if(contains_response_doc):
                      reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                      with open('temp.csv', 'r') as file:
                        reader = csv.reader(file)
                        response_doc_writer(reader)
                        for tags in tags_list_2:
                            try:
                              reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                              with open('temp.csv', 'r') as file:
                                reader = csv.reader(file)
                                response_doc_writer(reader)
                            except subprocess.CalledProcessError as e:
                                continue

        
        elif(body_param_checker(soup)):
          body = subprocess.check_output(['htmltab', '--select', tag_body, url, "temp.csv"])
          with open('temp.csv', 'r') as file:
            reader = csv.reader(file)
            body_param_writer(reader)

            #Response Elements
            if(response_elems_checker(soup)):
                for tags in tags_list:
                    try:
                      reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                      with open('temp.csv', 'r') as file:
                        reader = csv.reader(file)
                        response_writer(reader)
                    except subprocess.CalledProcessError as e:
                        continue
                if(contains_response_doc):
                  reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                  with open('temp.csv', 'r') as file:
                    reader = csv.reader(file)
                    response_doc_writer(reader)
                    for tags in tags_list_2:
                        try:
                          reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                          with open('temp.csv', 'r') as file:
                            reader = csv.reader(file)
                            response_doc_writer(reader)
                        except subprocess.CalledProcessError as e:
                            continue


        else:
            #Response Elements
            if(response_elems_checker(soup)):
                for tags in tags_list:
                    try:
                      reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                      with open('temp.csv', 'r') as file:
                        reader = csv.reader(file)
                        response_writer(reader)
                    except subprocess.CalledProcessError as e:
                        continue
                if(contains_response_doc):
                  reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                  with open('temp.csv', 'r') as file:
                    reader = csv.reader(file)
                    response_doc_writer(reader)
                    for tags in tags_list_2:
                        try:
                          reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                          with open('temp.csv', 'r') as file:
                            reader = csv.reader(file)
                            response_doc_writer(reader)
                        except subprocess.CalledProcessError as e:
                            continue

    elif(query_param_checker(soup)):
      body = subprocess.check_output(['htmltab', '--select', tag_query, url, "temp.csv"])
      with open('temp.csv', 'r') as file:
        reader = csv.reader(file)
        query_param_writer(reader)

        if(body_param_checker(soup)):
          body = subprocess.check_output(['htmltab', '--select', tag_body, url, "temp.csv"])
          with open('temp.csv', 'r') as file:
            reader = csv.reader(file)
            body_param_writer(reader)

            if(response_elems_checker(soup)):
                for tags in tags_list:
                    try:
                      reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                      with open('temp.csv', 'r') as file:
                        reader = csv.reader(file)
                        response_doc_writer(reader)
                    except subprocess.CalledProcessError as e:
                        continue

                if(contains_response_doc):
                    
                  reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                  with open('temp.csv', 'r') as file:
                    reader = csv.reader(file)
                    response_doc_writer(reader)
                    for tags in tags_list_2:
                        try:
                          reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                          with open('temp.csv', 'r') as file:
                            reader = csv.reader(file)
                            response_doc_writer(reader)
                        except subprocess.CalledProcessError as e:
                            continue

        else:
            if(response_elems_checker(soup)):
                for tags in tags_list:
                    try:
                      reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                      with open('temp.csv', 'r') as file:
                        reader = csv.reader(file)
                        response_doc_writer(reader)
                    except subprocess.CalledProcessError as e:
                        continue
                if(contains_response_doc):
                    for tags in tags_list_2:
                        try:
                          reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                          with open('temp.csv', 'r') as file:
                            reader = csv.reader(file)
                            response_doc_writer(reader)
                        except subprocess.CalledProcessError as e:
                            continue

    elif(body_param_checker(soup)):
      body = subprocess.check_output(['htmltab', '--select', tag_body, url, "temp.csv"])
      with open('temp.csv', 'r') as file:
        reader = csv.reader(file)
        body_param_writer(reader)

        if(response_elems_checker(soup)):
            for tags in tags_list:
                try:
                  reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                  with open('temp.csv', 'r') as file:
                    reader = csv.reader(file)
                    response_doc_writer(reader)
                except subprocess.CalledProcessError as e:
                    continue
            if(contains_response_doc):
                for tags in tags_list_2:
                    try:
                      reponse = subprocess.check_output(['htmltab', '--select', tags, url, "temp.csv"])
                      with open('temp.csv', 'r') as file:
                        reader = csv.reader(file)
                        response_doc_writer(reader)
                    except subprocess.CalledProcessError as e:
                        continue
    else:
        if(response_elems_checker(soup)):
                      reponse = subprocess.check_output(['htmltab', '--select', '1', url, "temp.csv"])
                      with open('temp.csv', 'r') as file:
                        reader = csv.reader(file)
                        response_doc_writer(reader)


    # with open(sys.argv[1], 'a') as output:
    #     writer = csv.writer(output)
    #     writer.writerow(["~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"])
    #     writer.writerow("")
if __name__ == "__main__":
	main()



