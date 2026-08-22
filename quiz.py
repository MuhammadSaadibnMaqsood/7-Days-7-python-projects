# QUIZ APP


def quiz():
    quiz_question = [
        {
            "question": "What is the capital of France?",
            "options": ["London", "Berlin", "Paris", "Madrid"],
            "answer": "Paris",
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Jupiter", "Saturn", "Mars"],
            "answer": "Jupiter",
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": ["Au", "Ag", "Fe", "Pb"],
            "answer": "Au",
        },
        {
            "question": "Which ocean is the largest on Earth?",
            "options": [
                "Atlantic Ocean",
                "Indian Ocean",
                "Arctic Ocean",
                "Pacific Ocean",
            ],
            "answer": "Pacific Ocean",
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": [
                "Vincent van Gogh",
                "Leonardo da Vinci",
                "Pablo Picasso",
                "Claude Monet",
            ],
            "answer": "Leonardo da Vinci",
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["Gold", "Iron", "Diamond", "Platinum"],
            "answer": "Diamond",
        },
        {
            "question": "Which programming language is known as the 'language of the web'?",
            "options": ["Python", "JavaScript", "C++", "Java"],
            "answer": "JavaScript",
        },
        {
            "question": "How many continents are there on Earth?",
            "options": ["5", "6", "7", "8"],
            "answer": "7",
        },
        {
            "question": "Which gas do plants absorb from the atmosphere for photosynthesis?",
            "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
            "answer": "Carbon Dioxide",
        },
        {
            "question": "In which year did the Titanic sink?",
            "options": ["1905", "1912", "1918", "1923"],
            "answer": "1912",
        },
    ]

    score = 0
    for question in quiz_question:
        print("\n", question["question"])
        print("Options:")
        for i, option in enumerate(question["options"], 1):
            print(f"{i} - {option}")
            
        user = int(input("Enter your answer (1-4)"))
        user_answer = question["options"][user-1]
        
        if(user_answer == question["answer"]):
            score +=1
            print("Correct answer")
            
        else:
            print("Wrong answer! correct answer is ", question["answer"])
            
    print("\nYour score is ", score, "out of 10")
    
quiz()
