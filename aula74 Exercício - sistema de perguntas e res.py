# Exercício - sistema de perguntas e respostas


questions = [
    {
        'Question' : 'How much is 2 + 2?',
        'Options' : ['1','2','3','4'],
        'Answer' : '4',
    },
    {
        'Question' : 'How much is 5 * 5?',
        'Options' : ['25','55','10','51'],
        'Answer' : '25',
    },
    {
        'Question' : 'How much is 10 / 2?',
        'Options' : ['4','5','2','1'],
        'Answer' : '5',
    },
]


index = 0


total_questions = len(questions)

while index < total_questions:
    
    
    print(questions[index]['Question'])

    for i, option in enumerate(questions[index]['Options']):
        print(f'{i})',option)

    user_input = input("Enter the answer: ")
    if user_input == questions[index]['Answer']:
        print("Correct Answer")
        print("*" * 20)
        index += 1 
    else:
        print("Missed")

       