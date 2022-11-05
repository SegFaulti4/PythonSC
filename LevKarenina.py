from sys import stdin
from collections import defaultdict

p, b, g, e = input().strip()
sentence_count = 0
first_criteria_words = defaultdict(int)
first_criteria_appearances = dict()
second_criteria_words = defaultdict(int)
second_criteria_appearances = dict()


def process_sentence(sentence, prev_mark, sentence_count):
    words = sentence.split()
    if not words:
        return
    '''print()
    print("first word: |" + words[0] + "|")
    print("last_word: |" + words[-1] + "|")
    print("prev_mark: |" + prev_mark + "|")
    print()'''

    if words[0][0] == b and prev_mark == p:
        first_criteria_words[words[0]] += 1
        if words[0] not in first_criteria_appearances:
            first_criteria_appearances[words[0]] = sentence_count

    if words[-1][0] == g and words[-1][-1] == e:
        second_criteria_words[words[-1]] += 1
        if words[-1] not in second_criteria_appearances:
            second_criteria_appearances[words[-1]] = sentence_count


leftover = ""
prev_mark = ''
for line in stdin:
    if line == "" or line == "\n":
        break

    p_pos = line.find(p)
    e_pos = line.find(e)
    while p_pos != -1 or e_pos != -1:
        if p_pos == -1:
            pos = e_pos
        elif e_pos == -1:
            pos = p_pos
        else:
            pos = min(e_pos, p_pos)

        sentence = leftover + line[:pos + 1]
        new_prev_mark = sentence[-1]

        process_sentence(sentence, prev_mark, sentence_count)
        sentence_count += 1

        leftover = ""
        prev_mark = new_prev_mark
        line = line[pos + 1:]
        p_pos = line.find(p)
        e_pos = line.find(e)

    leftover += line

process_sentence(leftover, prev_mark, sentence_count)


def criteria_res(criteria_words, criteria_appearances):
    if criteria_words:
        max_count = max(criteria_words.values())
        candidates = [word for word in criteria_words if criteria_words[word] == max_count]
        min_appearance = min(criteria_appearances[word] for word in candidates)
        for word in candidates:
            if criteria_appearances[word] == min_appearance:
                return word + " " + str(criteria_words[word])
    return "... 0"


res = criteria_res(first_criteria_words, first_criteria_appearances) + " - " + \
      criteria_res(second_criteria_words, second_criteria_appearances)
print(res)
