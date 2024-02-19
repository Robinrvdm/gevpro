import xml.etree.ElementTree as ET
import sys

def get_adjectives(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    adjectives = set()
    for cid in root.findall('.//cid'):
        pos = cid.get('pos')
        if pos == 'ADJ':
            form = cid.get('form')
            if form:
                adjectives.add(form.strip()) 
    return sorted(adjectives)

def main():
    xml_file = sys.argv[1]
    adjectives = get_adjectives(xml_file)
    for adj in adjectives:
        print(adj)

if __name__ == "__main__":
    main()
