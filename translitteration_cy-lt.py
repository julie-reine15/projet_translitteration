from collections import defaultdict
from nltk import ngrams


class Translitteration:

    def rule_cy_lt(self):

        file = open("regle_BGN.txt").readlines()
        rules = defaultdict(str)

        for line in file:
            for rule in line.split("\n"):
                if len(rule.split("\t")) > 1:
                    rules[rule.split("\t")[0]] = rule.split("\t")[1].strip("\n")
        return rules

    def translit_file_cy_lt(self, input_file, output_file=None, both=False):

        input_file = open(input_file).read()
        new_file = ""
        rules = self.rule_cy_lt()
        char = list(ngrams(input_file, 1))
        i = 0

        if output_file is None:

            while i < len(char)-3:

                three = "".join(char[i]+char[i+1]+char[i+2])
                # print(three)
                two = "".join(char[i]+char[i+1])
                # print(two)
                one = "".join(char[i])

                if three in rules.keys():
                    new_char = rules.get(three)
                    # print("3. ok")
                    new_file += "".join(new_char)
                    # print(new_file)
                    i += 3
                elif two in rules.keys():
                    new_char = rules.get(two)
                    # print("2. ok")
                    new_file += "".join(new_char)
                    # print(new_file)
                    i += 2
                elif one in rules.keys():
                    new_char = rules.get(one)
                    # print("1. ok")
                    new_file += "".join(new_char)
                    # print(new_file)
                    i += 1
                else:
                    new_file += "".join(one)
                    # print("4. pas ok")
                    i += 1
            # print(i)
            two = "".join(char[i]+char[i+1])
            if two in rules.keys():
                new_file += "".join(rules.get(two))
            elif char[i] and char[i+1] in rules.keys():
                new_file += "".join(rules.get(char[i]))
                new_file += "".join(rules.get(char[i+1]))
            else:
                new_file += "".join(two)

        else:
            output_file = open(output_file, "w")

            while i < len(char) - 3:

                three = "".join(char[i] + char[i + 1] + char[i + 2])
                # print(three)
                two = "".join(char[i] + char[i + 1])
                # print(two)
                one = "".join(char[i])

                if three in rules.keys():
                    new_char = rules.get(three)
                    # print("3. ok")
                    new_file += "".join(new_char)
                    # print(new_file)
                    i += 3
                elif two in rules.keys():
                    new_char = rules.get(two)
                    # print("2. ok")
                    new_file += "".join(new_char)
                    # print(new_file)
                    i += 2
                elif one in rules.keys():
                    new_char = rules.get(one)
                    # print("1. ok")
                    new_file += "".join(new_char)
                    # print(new_file)
                    i += 1
                else:
                    new_file += "".join(one)
                    # print("4. pas ok")
                    i += 1
            # print(i)
            two = "".join(char[i] + char[i + 1])
            if two in rules.keys():
                new_file += "".join(rules.get(two))
            elif char[i] and char[i + 1] in rules.keys():
                new_file += "".join(rules.get(char[i]))
                new_file += "".join(rules.get(char[i + 1]))
            else:
                new_file += "".join(two)

            if both:
                output_file.write(f"Texte original :\n{input_file}")
                output_file.write("\n----------------------\n")
                output_file.write(f"Texte translittérer :\n{new_file}")

            else:
                output_file.write(f"Texte translittérer :\n{new_file}")


t = Translitteration()
t.translit_file_cy_lt("tweet_test_transli.txt", output_file="output_test_translit.txt", both=True)
