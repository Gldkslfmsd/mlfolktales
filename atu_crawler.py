__author__ = 'Simon'
import requests
import re
import urllib.parse
from time import sleep
from corpus_classes import Story

def get_story(link, corpus_language):
    global num_matching_errors

    result = Story()

    text_re = re.compile(r'id=story>(?:<p.*?>)?(.*?)</div>')
    id_re = re.compile(r'id=([0-9]+)')
    title_re = re.compile(r'<TITLE>(.*?) - MFtD<')
    atu_re = re.compile(r'\(ATU.*?([0-9]+?[A-Z]?)\)')

    successful = False
    n = 1
    while(not successful and n <= 61):
        try:
            r = requests.get(link)
            successful = True
        except requests.exceptions.ConnectionError:
            sleep(n)
            n += 5
    if (not successful or r.status_code != 200):
        print('Could not access: '+link)
        return None

    try:
        r.encoding = 'utf-8'
        title = title_re.findall(r.text)[0]
        result.set_title(title)

        id = id_re.findall(link)[0]
        result.set_id(id)

        text = text_re.findall(r.text)[0]
        result.set_text(text)

        result.set_language(corpus_language)

        atu_candidate = atu_re.findall(r.text)
        if len(atu_candidate) > 1:
            #print("Error: Multiple possible ATU story types identified! Story: "+str(id)+", Candidate list: "+str(atu_candidate))
            atu_number = atu_candidate[0]
        elif len(atu_candidate) == 1:
            atu_number = atu_candidate[0]
        else:
            atu_number = 'UNKNOWN'
        result.set_atu_type(atu_number)
    except IndexError:
        num_matching_errors += 1
        return None
    return result

def get_corpus(link, language):
    global num_matching_errors

    corpus = []
    story_link_re = re.compile(r'href=\'(.*action=story.*?)\'>')
    next_page_link_re = re.compile(r'href=\'(.*?)\'>volgende')

    successful = False
    n = 1
    while(not successful and n <= 61):
        try:
            r = requests.get(link)
            successful = True
        except requests.exceptions.ConnectionError:
            sleep(n)
            n += 5
    if (not successful or r.status_code != 200):
        print('Could not access: '+link)
        return corpus

    story_links = story_link_re.findall(r.text)
    for rel_link in story_links:
        abs_link = urllib.parse.urljoin('http://www.mftd.org', rel_link)
        s = get_story(abs_link, language)
        if s != None:
            corpus.append(s)

    next_page_link = next_page_link_re.findall(r.text)
    assert(len(next_page_link) <= 1)
    if len(next_page_link) == 1:
        rel_np_link = next_page_link[0]
        abs_np_link = urllib.parse.urljoin('http://www.mftd.org', rel_np_link)
        corpus += get_corpus(abs_np_link, language)

    return corpus

if __name__ == '__main__':

    corpora = {}
    num_matching_errors = 0

    czech_link = 'http://www.mftd.org/index.php?action=browse&langname=Czech'
    danish_link = 'http://www.mftd.org/index.php?action=browse&langname=Danish'
    dutch_link = 'http://www.mftd.org/index.php?action=browse&langname=Dutch'
    english_link = 'http://www.mftd.org/index.php?action=browse&langname=English'
    french_link = 'http://www.mftd.org/index.php?action=browse&langname=French'
    german_link = 'http://www.mftd.org/index.php?action=browse&langname=German'
    hungarian_link = 'http://www.mftd.org/index.php?action=browse&langname=Hungarian'
    italian_link = 'http://www.mftd.org/index.php?action=browse&langname=Italian'
    polish_link = 'http://www.mftd.org/index.php?action=browse&langname=Polish'
    russian_link = 'http://www.mftd.org/index.php?action=browse&langname=Russian'
    spanish_link = 'http://www.mftd.org/index.php?action=browse&langname=Spanish'

    for link in [czech_link, danish_link, dutch_link, english_link, french_link, german_link, hungarian_link, italian_link, polish_link, russian_link, spanish_link]:
        language = link.split('=')[-1]
        print('Processing Folktales in: '+language+'...')
        corpora[language] = get_corpus(link, language)
        #print('Matching Errors: '+str(num_matching_errors))

    with open('corpora.txt', 'w+', encoding='utf-8') as outfile:
        outfile.write(str(corpora))