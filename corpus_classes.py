__author__ = 'Simon'
from collections import defaultdict
import os, re, html

class Corpus():
    def __init__(self, story_collection):
        stories = []
        if isinstance(story_collection, dict):
            for story_list in story_collection.values():
                stories += story_list
        if isinstance(story_collection, list):
            stories = story_collection

        if not isinstance(stories[0], Story):
            assert (isinstance(stories[0], tuple))
            proper_stories = [Story.from_Representation(x) for x in stories]
            stories = proper_stories
        self.all_stories = sorted(stories, key=lambda x: x.get_id())

        self.language_corpora = defaultdict(list)
        self.atu_corpora_level_1 = defaultdict(list)
        self.atu_corpora_level_2 = defaultdict(list)
        self.initialize_specific_corpora()
        self.clean()

    def initialize_specific_corpora(self):
        for story in self.all_stories:
            self.language_corpora[story.get_language()].append(story)
            self.atu_corpora_level_1[story.get_atu_level_1()].append(story)
            self.atu_corpora_level_2[story.get_atu_level_2()].append(story)

    def get_corpora_by_language(self):
        return self.language_corpora

    def get_corpora_by_atu_level_1(self):
        return self.atu_corpora_level_1

    def get_corpora_by_atu_level_2(self):
        return self.atu_corpora_level_2

    def write_specific(self, specific_corpus, filename):
        with open(filename, 'w+', encoding='utf-8') as f:
            f.write(str(specific_corpus))

    def pretty_write(self):

        for story in self.all_stories:
            if story.get_atu_level_1() == 'UNKNOWN':
                path = os.path.join('Fairytale Corpus', story.get_language(), story.get_atu_level_1(), '')
            else:
                path = os.path.join('Fairytale Corpus', story.get_language(), story.get_atu_level_1(), story.get_atu_level_2(), '')
                
            # this is horrible, never repeat the same code!!! and never don't catch Exception, but PathNotFoundException or 
            # something like this...
            try:
                with open(os.path.join(path, re.sub(r'[\\/:*?"<>|\t]', '', str(story.get_title()))+'.txt'), 'w+', encoding='utf-8') as f:
                    out_string = 'Story Title: '+str(story.get_title())+'\n'
                    out_string += 'Story ID (from ATU-website): '+str(story.get_id())+'\n'
                    out_string += 'ATU Classification Number: '+str(story.get_atu_integer())+'\n\n'
                    out_string += story.get_text()
                    f.write(out_string)
            except Exception:
                os.makedirs(path, exist_ok = True)
                with open(os.path.join(path, re.sub(r'[\\/:*?"<>|\t]', '', str(story.get_title()))+'.txt'), 'w+', encoding='utf-8') as f:
                    out_string = 'Story Title: '+str(story.get_title())+'\n'
                    out_string += 'Story ID (from ATU-website): '+str(story.get_id())+'\n'
                    out_string += 'ATU Classification Number: '+str(story.get_atu_integer())+'\n\n'
                    out_string += story.get_text()
                    f.write(out_string)

    def clean(self):
        for story in self.all_stories:
            story.clean()


from dict2xml import dict2xml as xmlify
import pandas as pd

class AbstractFlatCorpus(Corpus):
    DIR = None
    FILE_SUFFIX = None
    
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        
    def story_to_dict(self, story):
        return {
            "language" : story.get_language(),
            "level_1" : story.get_atu_level_1(),
            "level_2" : story.get_atu_level_2(),
            "title" : story.get_title(),
            "id" : story.get_id(),
            "atu" : story.get_atu_integer(),
            "text" : story.get_text(),
        }
    
    def story_to_path(self, story):
        p = (self.DIR, "%s.%s" % (story.get_id(), self.FILE_SUFFIX))
        return os.path.join(*p)
    
    def pretty_write(self):
        os.makedirs(self.DIR, exist_ok = True)
        stories = []
        for story in self.all_stories:
            self.story_to_file(story)
            d = self.story_to_dict(story)
            del d["text"]
            stories.append(d)
        df = pd.DataFrame.from_dict(stories)
        df.to_csv("stories.csv")
        
    def story_to_file(self, story):
        raise NotImplemented()
    
class XmlFlatCorpus(AbstractFlatCorpus):
    DIR = "corpus_xml"
    FILE_SUFFIX = "xml"
    
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
    
    def story_to_file(self, story):
        d = self.story_to_dict(story)
        xml = xmlify(d)
        path = self.story_to_path(story)
        with open(path, "w", encoding="utf-8") as f:
            f.write(xml)
            print("writing ", d["id"], d["title"])

class TxtFlatCorpus(AbstractFlatCorpus):
    DIR = "corpus_txt"
    FILE_SUFFIX = "txt"
    
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
    
    def story_to_file(self, story):
        path = self.story_to_path(story)
        with open(path, "w", encoding="utf-8") as f:
            f.write(story.get_text())
            print("writing ", story.get_id(), story.get_title())

        
        


class Story():
    def __init__(self, id=None, title=None, language=None, atu_type=None, text=None):
        self.id = id
        if id != None:
            self.id = int(id)
        self.title = title
        self.language = language
        self.atu_type = atu_type
        self.text = text
    @classmethod
    def from_Representation(cls, story):
        (title, id, atu_type, language, text) = story
        return cls(id=id, title=title, language=language, atu_type=atu_type, text=text)
    def set_text(self, text):
        self.text = text
    def set_id(self, id):
        self.id = int(id)
    def set_language(self, language):
        self.language = language
    def set_title(self, title):
        self.title = title
    def set_atu_type(self, type):
        self.atu_type = type
    def get_text(self):
        return self.text
    def get_id(self):
        return self.id
    def get_language(self):
        return self.language
    def get_title(self):
        return self.title
    def get_atu_type(self):
        return self.atu_type
    def get_atu_integer(self):
        atu_number_str = self.atu_type

        if atu_number_str == 'UNKNOWN':
            return atu_number_str

        if not atu_number_str[-1].isdigit():
            atu_number_str = atu_number_str[:-1]
        return int(atu_number_str)

    def get_atu_level_1(self):

        atu_number = self.get_atu_integer()
        if not isinstance(atu_number, int):
            return 'UNKNOWN'

        if atu_number <= 299:
            return 'Animal Tales'
        elif atu_number <= 749:
            return 'Tales of Magic'
        elif atu_number <= 849:
            return 'Religious Tales'
        elif atu_number <= 999:
            return 'Realistic Tales'
        elif atu_number <= 1199:
            return 'Tales of the Stupid Ogre'
        elif atu_number <= 1999:
            return 'Anecdotes and Jokes'
        elif atu_number <= 2399:
            return 'Formula Tales'
        else:
            return 'NON VALID ATU'

    def get_atu_level_2(self):

        atu_number = self.get_atu_integer()
        if not isinstance(atu_number, int):
            return 'UNKNOWN'

        if atu_number <= 299:
            if atu_number <= 99:
                return 'Wild Animals'
            elif atu_number <= 149:
                return 'Wild Animals and Domestic Animals'
            elif atu_number <= 199:
                return 'Wild Animals and Humans'
            elif atu_number <= 219:
                return 'Domestic Animals'
            elif atu_number <= 299:
                return 'Other Animals and Objects'
        elif atu_number <= 749:
            if atu_number <= 399:
                return 'Supernatural Adversaries'
            elif atu_number <= 459:
                return 'Supernatural or Enchanted Wife (Husband) or Other Relative'
            elif atu_number <= 499:
                return 'Supernatural Tasks'
            elif atu_number <= 559:
                return 'Supernatural Helpers'
            elif atu_number <= 649:
                return 'Magic Objects'
            if atu_number <= 699:
                return 'Supernatural Power or Knowledge'
            elif atu_number <= 749:
                return 'Other Tales of the Supernatural'
        elif atu_number <= 849:
            if atu_number <= 779:
                return 'God Rewards and Punishes'
            elif atu_number <= 799:
                return 'The Truth Comes to Light'
            elif atu_number <= 809:
                return 'Heaven'
            elif atu_number <= 826:
                return 'The Devil'
            elif atu_number <= 849:
                return 'Other Religious Tales'
        elif atu_number <= 999:
            if atu_number <= 869:
                return 'The Man Marries the Princess'
            elif atu_number <= 879:
                return 'The Woman Marries the Prince'
            elif atu_number <= 899:
                return 'Proofs of Fidelity and Innocence'
            elif atu_number <= 909:
                return 'The Obstinate Wife Learns to Obey'
            elif atu_number <= 919:
                return 'Good Precepts'
            if atu_number <= 929:
                return 'Clever Acts and Words'
            elif atu_number <= 949:
                return 'Tales of Fate'
            elif atu_number <= 969:
                return 'Robbers and Murderers'
            elif atu_number <= 999:
                return 'Other Realistic Tales'
        elif atu_number <= 1199:
            if atu_number <= 1029:
                return 'Labor Contract'
            elif atu_number <= 1059:
                return 'Partnership between Man and Ogre'
            elif atu_number <= 1114:
                return 'Contest between Man and Ogre'
            elif atu_number <= 1144:
                return 'Man Kills (Injures) Ogre'
            elif atu_number <= 1154:
                return 'Ogre Frightened by Man'
            if atu_number <= 1169:
                return 'Man Outwits the Devil'
            elif atu_number <= 1199:
                return 'Souls Saved from the Devil'
        elif atu_number <= 1999:
            if atu_number <= 1349:
                return 'Stories about a Fool'
            elif atu_number <= 1439:
                return 'Stories about Married Couples'
            elif atu_number <= 1524:
                return 'Stories about a Woman'
            elif atu_number <= 1724:
                return 'Stories about a Man'
            elif atu_number <= 1849:
                return 'Jokes about Clergymen and Religious Figures'
            if atu_number <= 1874:
                return 'Anecdotes about Other Groups of People'
            elif atu_number <= 1999:
                return 'Tall Tales'
        elif atu_number <= 2399:
            if atu_number <= 2100:
                return 'Cumulative Tales'
            elif atu_number <= 2299:
                return 'Catch Tales'
            elif atu_number <= 2399:
                return 'Other Formula Tales'
        else:
            return 'NON VALID ATU'

    def clean(self):
        markup_re = re.compile(r'<.*?>')
        cleaned_text = re.sub(markup_re, '', self.text)
        cleaned_text = html.unescape(cleaned_text)
        cleaned_title = html.unescape(self.title)
        self.text = cleaned_text
        self.title = cleaned_title

    def __str__(self):
        res = 'Story: '+str(self.title)+'\n'
        res += 'ID: '+str(self.id)+'\n'
        res += 'ATU-type: '+str(self.atu_type)+'\n'
        res += 'Language: '+str(self.language)+'\n'
        res += 'Text: '+str(self.text)
        return res

    def __repr__(self):
        return str((self.title, self.id, self.atu_type, self.language, self.text))