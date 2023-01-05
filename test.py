from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-vietnamese-diacritics-uncased")
sentence = "cong chung khong co ban goc"
print(tokenizer(sentence))