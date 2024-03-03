import MeCab
import unidic
import markovify

text = open('wiki_text.txt' ,mode='r')
markov_text = text.read()

mecab = MeCab.Tagger('-Owakati')

result = mecab.parse(markov_text)
result_replace = result.replace('。', '。\n')

text_model = markovify.NewlineText(result_replace, well_formed=True, reject_reg="[〜・？！：；／＠％（）〔〕［］｛｝〈〉《》「」『』【】]", state_size=2)
for i in range(15):
    print(text_model.make_short_sentence(280, tries=50).replace(' ', '')) 
