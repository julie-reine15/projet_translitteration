from collections import defaultdict, Counter, OrderedDict
from nltk import ngrams, RegexpTokenizer

RULES_TXT = list
NEW_FILE = ""
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
        FILE = open(input_file).read()

        global NEW_FILE

        global CHAR
        CHAR = list(ngrams(FILE, 1))
        i = 0
        # print(FILE)

        if output_file is None:

            while i < len(CHAR)-3:

                three = "".join(CHAR[i] + CHAR[i + 1] + CHAR[i + 2])
                # print(three)
                two = "".join(CHAR[i] + CHAR[i + 1])
                # print(two)
                one = "".join(CHAR[i])

                if three in self.dico.keys():
                    new_char = self.dico.get(three)
                    # print("3. ok")
                    NEW_FILE += "".join(new_char)
                    # print(new_file)
                    i += 3
                elif two in self.dico.keys():
                    new_char = self.dico.get(two)
                    # print("2. ok")
                    NEW_FILE += "".join(new_char)
                    # print(new_file)
                    i += 2
                elif one in self.dico.keys():
                    new_char = self.dico.get(one)
                    # print("1. ok")
                    NEW_FILE += "".join(new_char)
                    # print(new_file)
                    i += 1
                else:
                    NEW_FILE += "".join(one)
                    # print("4. pas ok")
                    i += 1

            if "".join(CHAR[i] + CHAR[i + 1] + CHAR[i + 2]) in self.dico.keys():
                three = "".join(CHAR[i] + CHAR[i + 1] + CHAR[i + 2])
                new_char = self.dico.get(three)
                NEW_FILE += "".join(new_char)

            elif "".join(CHAR[i] + CHAR[i + 1]) in self.dico.keys():
                two = "".join(CHAR[i] + CHAR[i + 1])
                new_char = self.dico.get(two)
                NEW_FILE += "".join(new_char)

            else:
                for car in [CHAR[i], CHAR[i + 1], CHAR[i + 2]]:
                    new_char = self.dico.get("".join(car))
                    NEW_FILE += "".join(new_char)

            return NEW_FILE

        else:
            output_file = open(output_file, "w", encoding="UTF-8")

            while i < len(CHAR) - 3:

                three = "".join(CHAR[i] + CHAR[i + 1] + CHAR[i + 2])
                # print(three)
                two = "".join(CHAR[i] + CHAR[i + 1])
                # print(two)
                one = "".join(CHAR[i])

                if three in self.dico.keys():
                    new_char = self.dico.get(three)
                    # print("3. ok")
                    NEW_FILE += "".join(new_char)
                    # print(new_file)
                    i += 3
                elif two in self.dico.keys():
                    new_char = self.dico.get(two)
                    # print("2. ok")
                    NEW_FILE += "".join(new_char)
                    # print(new_file)
                    i += 2
                elif one in self.dico.keys():
                    new_char = self.dico.get(one)
                    # print("1. ok")
                    NEW_FILE += "".join(new_char)
                    # print(new_file)
                    i += 1
                else:
                    NEW_FILE += "".join(one)
                    # print("4. pas ok")
                    i += 1

            if "".join(CHAR[i] + CHAR[i + 1] + CHAR[i + 2]) in self.dico.keys():
                three = "".join(CHAR[i] + CHAR[i + 1] + CHAR[i + 2])
                new_char = self.dico.get(three)
                NEW_FILE += "".join(new_char)

            elif "".join(CHAR[i] + CHAR[i + 1]) in self.dico.keys():
                two = "".join(CHAR[i] + CHAR[i + 1])
                new_char = self.dico.get(two)
                NEW_FILE += "".join(new_char)

            else:
                for car in [CHAR[i], CHAR[i + 1], CHAR[i + 2]]:
                    new_char = self.dico.get("".join(car))
                    NEW_FILE += "".join(new_char)

            if both:
                output_file.write(f"Texte original :\n{FILE}")
                output_file.write("\n----------------------\n")
                output_file.write(f"Texte translittérer :\n{NEW_FILE}")

            elif not both:
                output_file.write(f"Texte translittérer :\n{NEW_FILE}")

    def show_distribution(self, input_file, is_file=True, file_output_distri=None):

        global FILE
        global DISTRI

        if is_file:
            FILE = open(input_file).read().split()
            DISTRI = Counter(FILE)

            if file_output_distri is None:
                return DISTRI
            else:
                file_output_distri = open(file_output_distri, "w", encoding="UTF-8")
                list_item = list(DISTRI.items())
                for item in list_item[3:]:
                    file_output_distri.write(f"{item[0]}\t{item[1]}\n")
        else:
            FILE = str(input_file).split()
            DISTRI = Counter(FILE)
            if file_output_distri is None:
                return DISTRI
            else:
                file_output_distri = open(file_output_distri, "w", encoding="UTF-8")
                list_item = list(DISTRI.items())
                for item in list_item[3:]:
                    file_output_distri.write(f"{item[0]}\t{item[1]}\n")


t = Translitteration()
t.translit_file_cy_lt("tweet_test_transli.txt", output_file="output_test_translit.txt", both=False)
# tr = t.translit_file_cy_lt("tweet_test_transli.txt", output_file=None, both=False)
# print(t.show_distribution(tr, is_file=True))
print(t.show_distribution("output_test_translit.txt", is_file=True, file_output_distri="output_distri_transli.txt"))
