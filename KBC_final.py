
import time


def type_text(text, delay=0.03):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()


# ALL 10 QUESTIONS
questions = [
    {
        "intro": "Pehla prashan ₹1,000 ke liye!",
        "question": "India ke saath kaunsa desh land border share nahi karta?\nWhich country does not share a land border with India?",
        "options": {"A": "Bhutan", "B": "Bangladesh", "C": "Thailand", "D": "Myanmar"},
        "correct": "C",
        "fifty_fifty": ["B", "C"],
        "prize": 1000,
        "roast": "Bhai, pehla sawaal tha! Google bhi tujhe dekh ke apni services band kar de! 💀"
    },
    {
        "intro": "Dusra prashan ₹2,000 ke liye!",
        "question": "Periodic table mein W kis element ka chemical symbol hai?",
        "options": {"A": "Tungsten", "B": "Tin", "C": "Titanium", "D": "Tellurium"},
        "correct": "A",
        "fifty_fifty": ["A", "C"],
        "prize": 2000,
        "roast": "Aapka confidence dekh ke laga tha crorepati banenge, jawaab dekh ke lag raha hai admission form bhi kisi aur se bharwaya hoga!"
    },
    {
        "intro": "Teesra prashan ₹3,000 ke liye!",
        "question": "Solar system ka sabse bada grah kaunsa hai?",
        "options": {"A": "Jupiter", "B": "Saturn", "C": "Earth", "D": "Neptune"},
        "correct": "A",
        "fifty_fifty": ["A", "C"],
        "prize": 3000,
        "roast": "Bhai, grahon ka sawaal tha, aapne toh apni hi duniya basa li!"
    },
    {
        "intro": "Chautha prashan ₹5,000 ke liye!",
        "question": "Python programming language kisne banayi?",
        "options": {"A": "Dennis Ritchie", "B": "Guido van Rossum", "C": "James Gosling", "D": "Bjarne Stroustrup"},
        "correct": "B",
        "fifty_fifty": ["B", "D"],
        "prize": 5000,
        "roast": "Python seekh rahe ho aur uske creator ko hi bhool gaye? IDE bhi disappointed hai!"
    },
    {
        "intro": "Paanchva prashan ₹10,000 ke liye!",
        "question": "Binary number 1010 ka decimal value kya hai?",
        "options": {"A": "8", "B": "10", "C": "12", "D": "14"},
        "correct": "B",
        "fifty_fifty": ["B", "D"],
        "prize": 10000,
        "roast": "Binary ne aapko zero kar diya, bhai! Itna toh calculator bhi kar leta!"
    },
    {
        "intro": "Chhatha prashan ₹20,000 ke liye!",
        "question": "Kaunse planet ko Red Planet kaha jaata hai?",
        "options": {"A": "Venus", "B": "Jupiter", "C": "Mars", "D": "Mercury"},
        "correct": "C",
        "fifty_fifty": ["A", "C"],
        "prize": 20000,
        "roast": "Red Planet ka sawaal tha, lekin aapka jawaab dekh ke host ka chehra red ho gaya!"
    },
    {
        "intro": "Saatva prashan ₹50,000 ke liye!",
        "question": "HTML ka full form kya hai?",
        "options": {"A": "HyperText Markup Language", "B": "HighText Machine Language", "C": "Hyper Transfer Main Link", "D": "Home Tool Markup Language"},
        "correct": "A",
        "fifty_fifty": ["A", "D"],
        "prize": 50000,
        "roast": "Website banana chahte ho aur HTML ka full form nahi pata? Browser ne tab band kar diya!"
    },
    {
        "intro": "Aathva prashan ₹1,00,000 ke liye!",
        "question": "CPU ka full form kya hai?",
        "options": {"A": "Computer Personal Unit", "B": "Central Processing Unit", "C": "Central Program Utility", "D": "Control Processing User"},
        "correct": "B",
        "fifty_fifty": ["B", "C"],
        "prize": 100000,
        "roast": "CPU ka full form bhi nahi pata? Bhai, computer ko ab aapse technical support chahiye!"
    },
    {
        "intro": "Nauva prashan ₹10,00,000 ke liye!",
        "question": "144 ka square root kya hai?",
        "options": {"A": "10", "B": "11", "C": "14", "D": "12"},
        "correct": "D",
        "fifty_fifty": ["A", "D"],
        "prize": 1000000,
        "roast": "Bhai, 12 ka square 144 hota hai! Maths ne dhokha nahi diya, aapne diya!"
    },
    {
        "intro": "Aakhri prashan ₹1 CRORE ke liye!",
        "question": "Decimal number 5 ka binary representation kya hai?",
        "options": {"A": "100", "B": "110", "C": "101", "D": "111"},
        "correct": "C",
        "fifty_fifty": ["A", "C"],
        "prize": 10000000,
        "roast": "CROREPATI banne ka mauka tha, bhai! Binary mein 5 ko bhi aapne confuse kar diya!"
    }
]


# FUNCTION TO ASK ONE QUESTION
def ask_question(q, prize_money, lifeline_used):
    type_text("\n" + q["intro"])
    time.sleep(1)

    type_text("Dhyaan se suniye sawaal...")
    type_text(q["question"])

    allowed_options = ["A", "B", "C", "D"]

    if not lifeline_used:
        type_text(
            "Kya aap apni lifeline use karna chaahenge? "
            "Isse do galat vikalp hata diye jaayenge!"
        )

        lifeline_choice = input("Yes or No: ").strip().lower()

        while lifeline_choice not in ["yes", "no"]:
            lifeline_choice = input("Bhai, Yes ya No bolo: ").strip().lower()

        if lifeline_choice == "yes":
            lifeline_used = True
            allowed_options = q["fifty_fifty"]
            type_text("Computer Ji, do galat vikalp hata dijiye!")

    type_text("Ye rahe aapke options:")

    for option in allowed_options:
        type_text(f"{option}. {q['options'][option]}")

    answer = input("Apna jawaab chuniye: ").strip().upper()

    while answer not in allowed_options:
        type_text("Bhai, available options mein se jawaab do!")
        answer = input("Apna jawaab chuniye: ").strip().upper()

    time.sleep(1)
    type_text(f"Computer Ji, option {answer} lock kiya jaaye!")
    time.sleep(1)
    type_text("..............", 0.09)

    if answer == q["correct"]:
        prize_money = q["prize"]
        type_text(
            f"Mubarak ho! Aap jeet gaye hain "
            f"₹{prize_money:,} ki dhanraashi!"
        )
        return prize_money, lifeline_used, True

    type_text(q["roast"])
    type_text("Chaliye koi nahi, aap haar gaye hain KBC!")
    type_text(f"Aap apne ghar ₹{prize_money:,} lekar jaa rahe hain!")

    return prize_money, lifeline_used, False


# ONE COMPLETE ROUND OF KBC
def play_game():
    # Reset everything for a fresh game
    prize_money = 0
    lifeline_used = False

    type_text(
        "\n🎙️ SWAGAT HAI AAPKA KAUN BANEGA CROREPATI MEIN! 🎉\n"
        "Taiyaar ho apne dimaag ke taar hilaane ke liye?\n"
    )

    type_text(
        "Rules:\n"
        "1. Total 10 sawaal honge.\n"
        "2. Galat jawaab diya toh GAME OVER!\n"
        "3. Har sahi jawaab ke baad aap quit kar sakte hain.\n"
        "4. Ek 50:50 lifeline milegi.\n"
        "5. Galat jawaab par FREE ROASTING SERVICE! 🔥\n"
    )

    ready = input("Kya aap taiyaar hain? Yes or No: ").strip().lower()

    if ready != "yes":
        type_text("Taiyaar ho ya nahi, KBC toh shuru hoga! 😂")

    for index, q in enumerate(questions):
        prize_money, lifeline_used, correct = ask_question(
            q, prize_money, lifeline_used
        )

        if not correct:
            return

        # Check if the player has won the final question
        if index == len(questions) - 1:
            type_text("\n🎉 DEVIYO AUR SAJJANNO, HUMARE NAYE CROREPATI!")
            type_text("Aapne saare 10 sawaalon ke sahi jawaab diye!")
            type_text("₹1 CRORE AAPKE HUE! 🏆🔥")
            return

        # Offer the option to quit
        choice = input(
            "Kya aap agla sawaal khelna chahenge? Yes or No: "
        ).strip().lower()

        while choice not in ["yes", "no"]:
            choice = input("Bhai, Yes ya No bolo: ").strip().lower()

        if choice == "no":
            type_text(
                f"Shukriya khelne ke liye! Aap ₹{prize_money:,} "
                "lekar ghar jaa rahe hain!"
            )
            return


# PLAY AGAIN LOOP
while True:
    play_game()

    play_again = input(
        "\nKya aap dobara KBC khelna chahenge? Yes or No: "
    ).strip().lower()

    while play_again not in ["yes", "no"]:
        play_again = input(
            "Bhai, Yes ya No bolo: "
        ).strip().lower()

    if play_again == "no":
        type_text("Shukriya khelne ke liye! Alvida! 🎙️")
        break

    type_text("\n🔥 NAYA GAME SHURU! ISS BAAR CROREPATI BANKE DIKHAO! 🔥")
