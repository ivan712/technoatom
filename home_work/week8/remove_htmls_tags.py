from pyquery import PyQuery
import requests
import re
# print the html o
def words(site):
    try:
        response = requests.get(site)
    except requests.exceptions.InvalidSchema:
        s="incorrect adress"
        return json.dumps(s)
    except :
        s = "cannot connect to website"
        return json.dumps(s)
    response.encoding = 'utf-8'
    text_response = response.text.lower()

    text_without_space = re.sub(r'\n+','//0000//',text_response)

    text_without_script = re.sub(r'<script.+?/script>','',text_without_space)

    text_without_style = re.sub(r'<style.+?/style>','',text_without_script)

    text_without_html_tags = re.sub(r'<[^>]+>','',text_without_style)
    structuring_text = re.sub(r'&quot|&nbsp','',re.sub(r'//0000//','\n',text_without_html_tags))
    return structuring_text
print(words('https://yandex.ru'))
