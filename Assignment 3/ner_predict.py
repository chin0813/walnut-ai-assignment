import spacy
import argparse
import re
import pprint
pp = pprint.PrettyPrinter(indent=4)

parser = argparse.ArgumentParser(description='NER Predictor')
parser.add_argument('sentence', type=str, help='Sentence to tag')

args = parser.parse_args()




sent = re.sub(r'[^\w\s]', '', args.sentence).lower()
ner = spacy.load(r"./output/model-last")
doc = ner(sent)
entities = {}
for ent in doc.ents:
    entities[ent.text] = ent.label_
pp.pprint(entities)