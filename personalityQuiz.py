#########################################################
#   This is peronality quiz using the Myers Test model  #
#   to determine where the individual is                #
#   Introvert or Extrovert                              #
#   Sensing or Intuitive                                #
#   Judging or Perceiving                               #
#   Thinking or Feeling                                 #
#########################################################

def displayPersonalty(code):
    if code == "ISTJ":
        print("Your personailty is defined as   The Inspector")
        print("Reserved and practical, they tend to be loyal, orderly, and traditional.")
    elif code == "ISTP":
        print("Your personailty is defined as   The Crafter")
        print("Highly independent, they enjoy new experiences that provide first-hand learning.")
    elif code == "ISFJ":
        print("Your personailty is defined as   The Protector")
        print("Warm-hearted and dedicated, they are always ready to protect the people they care about.")
    elif code == "ISFP":
        print("Your personailty is defined as   The Artist")
        print("Easy-going and flexible, they tend to be reserved and artistic.")
    elif code == "INFJ":
        print("Your personailty is defined as   The Advocate")
        print("Creative and analytical, they are considered one of the rarest Myers-Briggs types.")
    elif code == "INFP":
        print("Your personailty is defined as   The Mediator")
        print("Idealistic with high values, they strive to make the world a better place.")
    elif code == "INTJ":
        print("Your personailty is defined as   The Architect")
        print("High logical, they are both very creative and analytical.")
    elif code == "INTP":
        print("Your personailty is defined as   The Thinker")
        print("Quiet and introverted, they are known for having a rich inner world.")
    elif code == "ESTP":
        print("Your personailty is defined as   The Persuader")
        print("Out-going and dramatic, they enjoy spending time with others and focusing on the here-and-now.")
    elif code == "ESTJ":
        print("Your personailty is defined as   The Director")
        print("Assertive and rule-oriented, they have high principles and a tendency to take charge.")
    elif code == "ESFP":
        print("Your personailty is defined as   The Performer")
        print("Outgoing and spontaneous, they enjoy taking center stage.")
    elif code == "ESFJ":
        print("Your personailty is defined as   The Caregiver")
        print("Soft-hearted and outgoing, they tend to believe the best about other people.")
    elif code == "ENFP":
        print("Your personailty is defined as   The Champion")
        print("Charismatic and energetic, they enjoy situations where they can put their creativity to work.")
    elif code == "ENFJ":
        print("Your personailty is defined as   The Giver")
        print("Loyal and sensitive, they are known for being understanding and generous.")
    elif code == "ENTP":
        print("Your personailty is defined as   The Debator")
        print("Highly inventive, they love being surrounded by ideas and tend to start many projects (but may struggle to finish them).")
    elif code == "ENTJ":
        print("Your personailty is defined as   The Commandor")
        print("Outspoken and confident, they are great at making plans and organizing projects.")
    else:
        print("Opps looks like your personaltiy key was not found.")
    print("To learn more about your personaltiy you can visit the following link.")
    print("https://eu.themyersbriggs.com/en/tools/MBTI/MBTI-personality-Types#:~:text=Where%20you%20focus%20your%20attention,J)%20or%20Perceiving%20(P)")

def calcPersonalityCode(questions):
    totalAnswered = 0
    aCount = 0
    bCount = 0
    code = ""
    for question in questions:
        totalAnswered += 1
        print(question)
        letter =  input("A or B: ")
        while not (letter == 'A' or letter == 'B'):
            print("Invalid input, try again.")
            print(question)
            letter =  input("A or B: ")
        if letter == 'A':
            aCount += 1
        else:
            bCount += 1
    
        if totalAnswered == 5:
            if aCount > bCount:
                code = code + 'E'
            else:
                code = code + 'I'
        elif totalAnswered == 10:
            if aCount > bCount:
                code = code + 'S'
            else:
                code = code + 'N'
        elif totalAnswered == 15:
            if aCount > bCount:
                code = code + 'T'
            else:
                code = code + 'F'
        elif totalAnswered == 20:
            if aCount > bCount:
                code = code + 'J'
            else:
                code = code + 'P'
    return code
def main():
    questions = ["Q1 - Do you prefer spending time, A: one-on-one or B: In groups ", 
    "Q2 - Would you consider yourself more A: outgoing or B: Reserved ", 
    "Q3 - Do you seek out more of A: Public activities or B: solitary activities ", 
    "Q4 - Are you more of a A: Talker or B: Listener ",
    "Q5 - Which words describe you better A: Active, Initiate or B: Reflective, Deliberate ",
    
    "Q6 - How would you interpret something A: Literally or B: Look for meaning and possibilities ",
    "Q7 - Are you more A: Practical, realistic, experiential or B: Imaginative, innovative, theoretical ",
    "Q8 - How do you prefer things A: Standard, usual, conventional or B: Different, novel, unique ",
    "Q9 - Do you tend to A: focus on here-and-now or B: look to the future, global perspective, (big picture) ",
    "Q10 - Do you think more in terms of A: Solid facts or B: ideas, dreams, philosophical ",
    
    "Q11 - Would you consider yourself more A: logical, thinking, questioning or B: empathetic, feeling, accommodating ",
    "Q12 - When interacting with others are you more A: candid, straight forward, frank or B: tactful, kind, encouraging ",
    "Q13 - When reflecting or evaulating do you tend to be more A: firm, tend to criticize, hold the line or B: gentle, tend to appreciate, conciliate ",
    "Q14 - When someone does something wrong are you more A: tough-minded, just or B: tender-hearted, merciful ",
    "Q15 - Are you more A: matter of fact, issue-oriented or B: sensitive, people-oriented, compassionate ",
    
    "Q16 - Do do you prefer to work A: organized, orderly or B: flexible, adaptable ",
    "Q17 - Do you like to live me A: plan, schedule or B: unplanned, spontaneous ",
    "Q18 - How would you describe yourself A: regulated, structured or B: easygoing, live and let live ",
    "Q19 - Do you prefer to A: preparation, plan ahead or B: go with the flow, adapt as you go ",
    "Q20 - Do you like A: control, govern or B: latitude, freedom"]
    displayPersonalty(calcPersonalityCode(questions))
   # code = input("Enter the code to learn about your personality: ")
   # displayPersonalty(code)

main()
    
    
    
        
    
