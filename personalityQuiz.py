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

def main():
    code = input("Enter the code to learn about your personality: ")
    displayPersonalty(code)

main()
    
    
    
        
    
