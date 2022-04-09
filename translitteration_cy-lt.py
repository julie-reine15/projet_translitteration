from collections import defaultdict, Counter, OrderedDict
from nltk import ngrams

RULES_TXT = list
NEW_FILE = str()
CHAR = list
DISTRI = OrderedDict()
FILE = str


class Translitteration:

    def __init__(self):

        global RULES_TXT
        RULES_TXT = open("regle_BGN.txt").readlines()
        rules = defaultdict(str)

        for line in RULES_TXT:
            for rule in line.split("\n"):
                if len(rule.split("\t")) > 1:
                    rules[rule.split("\t")[0]] = rule.split("\t")[1].strip("\n")

        self.dico = rules

    def translit_file_cy_lt(self, input_file, output_file=None, both=False):

        global FILE
        try:
            FILE = open(input_file).read()
        except FileNotFoundError:
            FILE = input_file

        global NEW_FILE

        global CHAR
        CHAR = list(ngrams(FILE, 1))

        i = 0

        if output_file is None:

            while i < len(CHAR):

                one = "".join(CHAR[i])
                try:
                    new_char = self.dico.get(one)
                except TypeError:
                    NEW_FILE += "".join(one)
                else:
                    NEW_FILE += "".join(new_char)
                finally:
                    i += 1
            return NEW_FILE

        else:
            output_file = open(output_file, "w", encoding="UTF-8")

            while i < len(CHAR):

                one = "".join(CHAR[i])
                try:
                    new_char = self.dico.get(one)
                except TypeError:
                    NEW_FILE += "".join(one)
                else:
                    NEW_FILE += "".join(new_char)
                finally:
                    i += 1

            if both:
                output_file.write(f"{FILE}")
                output_file.write("\n----------------------\n")
                output_file.write(f"{NEW_FILE}")

            else:
                output_file.write(f"Texte translittérer :\n{NEW_FILE}")

    def show_distribution(self, input_file, file_output_distri=None):

        global FILE
        global DISTRI

        try:
            FILE = open(input_file).read().split()
        except FileNotFoundError:
            FILE = input_file.split()
        finally:
            DISTRI = Counter([token for token in FILE if token.isalpha()])

        if file_output_distri is None:
            return DISTRI
        else:
            file_output_distri = open(file_output_distri, "w", encoding="UTF-8")
            for item in DISTRI.items():
                if item[0].isalpha():
                    file_output_distri.write(f"{item[0]}\t{item[1]}\n")


t = Translitteration()
# t.translit_file_cy_lt("tweet_test_transli.txt", output_file="output_test_translit.txt", both=False)
tr = t.translit_file_cy_lt("привет", output_file=None, both=False)
print(t.show_distribution(tr))
# print(t.show_distribution("output_test_translit.txt", is_file=True, file_output_distri="output_distri_transli.txt"))
