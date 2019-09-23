from mcq_ques import MCQ

question_prompt = [
    "1. What is the colour of a rose? \n(a) Red \n(b) Blue \n(c) Green\n",
    "2. What is the colour of a lemon? \n(a) Orange \n(b) Green \n(c) Yellow\n"
]

questions = [
    MCQ(question_prompt[0], 'a'),
    MCQ(question_prompt[1], 'c')
]

def run_test(questions):
    score = 0
    for ques in questions:
        answer = input(ques.prompt)
        if answer == ques.answer:
            score += 1
    print("Your got " + str(score) + "/" + str(len(questions)) + " correct!")

print(run_test(questions))   
    



