quiz =[ 
    {
        "Question": "Con nhện có mấy chân?",
        "choices": ['3 chân', '2 chân', '4 chân', '8 chân'],
        "right_answer": 3
    },
    {
        "Question": "Con chó có mấy chân?",
        "choices": ['3 chân', '2 chân', '4 chân', '8 chân'],
        "right_answer": 2
    },
    {
        "Question": "Con gà có mấy chân?",
        "choices": ['3 chân', '2 chân', '4 chân', '8 chân'],
        "right_answer": 1
    }
]

point = 0

for question in quiz:
    choices = question['choices']
    print(question['Question'])
    for i in range(len(choices)):
        print(f"{i+1}. {choices[i]}")
    user_choice = int(input('Trả lời đê: ')) - 1
    if user_choice == question['right_answer']:
        point = point + 1
        print('Congrats!!!')
    else:
        print('Wrong!!!')
print("Điểm của bạn là: ",point/len(quiz)*100,"%")
    