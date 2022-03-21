from collections import defaultdict


class Translitteration():

    # def __init__(self, translit=None):
    #     self.translit = translit

    def rule_cy_lt(self):

        file = open("regle_BGN.txt").readlines()
        rules = defaultdict(str)

        for line in file:
            for rule in line.split("\n"):
                if len(rule.split("\t")) > 1:
                    rules[rule.split("\t")[0]] = rule.split("\t")[1].strip()
        return rules

    def translit_cy_lt(self, input_file, output_file=None, both=False):

        input_file = open(input_file).read()
        new_file = ""
        rules = self.rule_cy_lt()

        if output_file is None:
            for char in input_file:
                if char in rules.keys():
                    new_char = rules.get(char)
                    # print(new_char)
                    new_file += "".join(new_char)
                    # print(new_file)
                else:
                    new_file += "".join(char)

            return new_file
        else:
            output_file = open(output_file, "w")

            for char in input_file:
                if char in rules.keys():
                    new_char = rules.get(char)
                    new_file += "".join(new_char)
                else:
                    new_file += "".join(char)

            if both:
                output_file.write(f"Texte original :\n{input_file}")
                output_file.write("\n----------------------\n")
                output_file.write(f"Texte translittérer :\n{new_file}")
            else:
                output_file.write(f"Texte translittérer :\n{new_file}")



t = Translitteration()
t.translit_cy_lt("tweet_test_transli.txt", "output_test_translit.txt", both=True)
