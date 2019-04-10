import re

text_path = 'text'
stopwords_path = 'stopwords'


def read_tokens(path):
    tokens = []
    with open(path) as file:
        for line in file:
            for word in re.split('\s+|[,;.-]\s*', line):
                if word:
                    tokens.append(word.lower())
    return tokens


def agregate(tokens, stopwords, limit=10):
    results = {}
    for token in tokens:
        if token not in stopwords:
            if token in results:
                results[token] += 1
            else:
                results[token] = 1
    return sorted(results.items(), key=lambda x: x[1], reverse=True)[:limit]


def print_result(results):
    for tup in results:
        print("Token: {0} - Times: {1}".format(tup[0], tup[1]))


def run_unit_test(text_path, stopwords_path):
    expected_results = {"andriana": 3,
                        "girl": 3}
    tokens = read_tokens(text_path)
    stopwords = read_tokens(stopwords_path)
    results = agregate(tokens, stopwords, 2)
    results = dict(results)
    print("Tests started")
    for expected_key in expected_results:
        count = results[expected_key]
        expected_count = expected_results[expected_key]
        print("For value: {0} real: {1} - expected: {2}".format(expected_key, count, expected_count))
        if not (count == expected_count):
            raise Exception("Test failed")
    print("All tests passed")
    print()


run_unit_test('text', 'stopwords')
tokens = read_tokens(text_path)
stopwords = read_tokens(stopwords_path)
results = agregate(tokens, stopwords)
print_result(results)
