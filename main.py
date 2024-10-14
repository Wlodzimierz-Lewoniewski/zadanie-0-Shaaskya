import string
from collections import defaultdict

# Funkcja do usunięcia interpunkcji i podzielenia na słowa
def process_document(doc):
    replacements = string.punctuation
    my_str = doc.lower()
    for r in replacements:
        my_str = my_str.replace(r, ' ')
    words = my_str.split()
    return words

def search_documents(documents, queries):
    # Lista do przechowywania słowników częstotliwości słów dla każdego dokumentu
    document_word_count = []

    # Przetwarzanie każdego dokumentu
    for doc in documents:
        words = process_document(doc)
        frequency = defaultdict(int)
        # Zliczanie wystąpień słów w dokumencie
        for word in words:
            frequency[word] += 1
        document_word_count.append(frequency)

    # Wyniki dla każdego zapytania
    results = []
    for query in queries:
        query = query.lower()
        
        results.append(sorted([i for i, doc_freq in enumerate(document_word_count) if doc_freq[query] > 0], key=lambda x: document_word_count[x][query], reverse=True))

    return results


n = int(input())  # liczba dokumentów
documents = [input().strip() for _ in range(n)] 
m = int(input())  # liczba zapytań
queries = [input().strip() for _ in range(m)] 

results = search_documents(documents, queries)

for result in results:
    print(result)
