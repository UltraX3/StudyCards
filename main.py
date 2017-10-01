#!/usr/bin/env python3
"""
First argument is variables.txt
Second argument is questions.txt

"""
import sys
import random

blue = "\033[0;34m"
green="\033[0;32m"
purple="\033[0;35m"
reset="\033[0m"
yellow="\033[0;33m"

variables = {}
questions = []
if __name__ == "__main__":
    variables_file_name = sys.argv[1]
    with open(variables_file_name) as file:
        for line in file:
            terms = line.replace('\n','').split("\t")
            values = terms[1].split(",")
            random.shuffle(values)
            variables[terms[0]] = values
    questions_file_name = sys.argv[2]
    with open(questions_file_name) as file:
        for i,line in enumerate(file):
            terms = line.replace('\n','').split("\t")
            if(len(terms) < 2):
                print("Error for "+terms[0]+", line:"+str(i+1)+"file: "+questions_file_name+", length: "+str(len(terms)))
            questions.append({'ask': terms[0], 'answer': terms[1]})
    random.shuffle(questions)
    length = str(len(questions))
    for i,question in enumerate(questions):
        print(reset + "===== QUESTION: "+str(i+1)+"/"+length+" =====")
        ask = question['ask']
        possible_answers = []
        answer = question['answer']
        for variable in variables:
            if variable in ask:
                ask = ask.replace('%' + variable + "%", '________')
                possible_answers.append(variables[variable])
        print("Word Bank: "+str(possible_answers))
        print(blue+"Question: "+ask)
        person = input(reset+'Your answer: ')
        print(green+"Answer: "+answer)
        print("")
