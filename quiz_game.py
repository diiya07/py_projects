# List of quiz questions. Each question is a dictionary.
questions = [
    {
        'prompt' : 'king of fruits?',
        'options' : ['a. mango', 'b. apple'],
        'answer' : 'a'
    },
    {
        'prompt' : 'king of veg?',
        'options' : ['a. gaurd', 'b. pumpkin'],
        'answer' : 'b'
    }
]


def run_quiz(questions):
    score = 0
    for question in questions:
        print('\n')
        print(question['prompt'])
        
        for option in question['options']:
            print(option)
        

        ans = input('enter a / b: ')
    
        if ans == question['answer']:
            print('yayy! correct')
            score+=1
        else:
            print('ohhNo the correct answer is', question['answer'], '\n')
        
        print('\n')
        
    print(f"Done! that's the end of quiz \nyou got {score} correct out of {len(questions)}")


#run the quiz (function call)
run_quiz(questions)