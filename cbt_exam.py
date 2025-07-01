cbt_questions = {
    "What is 2 + 2?": {
"a": 3,
"b": 4,
"c": 5,
"d": 6,
"answer": "b"
},
    "What color is the sky on a clear day?": {
"a": "Red",
"b": "Blue",
"c": "Green",
"d": "Yellow",
"answer": "b"
},
    "How many legs does a spider have?": {
"a": 6,
"b": 7,
"c": 8,
"d": 9,
"answer": "c"
},
    "What sound does a cow make?": {
"a": "Meow",
"b": "Bark",
"c": "Moo",
"d": "Quack",
"answer": "c"
},
    "What is the opposite of 'hot'?": {
"a": "Warm",
"b": "Cold",
"c": "Cool",
"d": "Boiling",
"answer": "b"
},
}

def cbt(cbt_questions):
    score = 0
    for question, options in cbt_questions.items():
        print(question)
        for option, value in options.items():
            if option != "answer":
                print(f"{option}:{value}")
        answer = input("choose an answer (a,b,c,d):")
        if answer.lower() == options["answer"]:
        #     correct_answer = options.get("answer")
        # if answer.lower() == correct_answer.lower():
            print("Your answer is correct")
            score += 1
        else:
            print( f"Your answer is incorrect, {options["answer"]} is the correct answer.")
    print( f"All questions have been answered, your total score is {score}/{len(cbt_questions)}")


print("Welcome to the CBT Exam Program, Best of luck")
cbt(cbt_questions)