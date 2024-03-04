import gzip
import sys
import re


def read_gzip_file(filepath):
    """ Reads and returns the content """
    with gzip.open(filepath, 'rt', encoding='utf-8') as file:
        content = file.read()
    return content


def remove_unwanted_text(text):
    """ Removes meta-information and headers """
    cleaned_text = re.sub(r'^.*?:.*\n', '', text, flags=re.MULTILINE)
    return cleaned_text


def split_into_sentences(text):
    """ Splits the text into sentences based on punctuation and newlines """
    parts = text.split('\n')
    sentences = []
    for part in parts:
        sub_sentences = re.split(r'(?<=[.!?])\s+', part)
        sentences.extend(sub_sentences)
    return sentences


def tokenize_sentences(sentences):
    """ Tokenizes sentences into words and punctuation,
    handling special cases """
    tokenized_sentences = []
    for sentence in sentences:
        tokens = re.findall(r"\w+'[\w]+|\w+|\d+|[.,!?;]|[-]|\"", sentence)
        tokenized_sentence = ' '.join(tokens)
        if tokenized_sentence.strip():
            tokenized_sentences.append(tokenized_sentence)
    return tokenized_sentences


def main(file_path):
    content = read_gzip_file(file_path)
    cleaned_content = remove_unwanted_text(content)
    sentences = split_into_sentences(cleaned_content)
    tokenized_sentences = tokenize_sentences(sentences)
    for line in tokenized_sentences:
        print(line)


if __name__ == '__main__':
    file_path = sys.argv[1]
    main(file_path)
