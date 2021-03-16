"""A collection of functions for doing my project."""
import sys 
user_information = []
yes_no = ["yes","no"]
possible_choices = ["A","B"]

def introduction():
    """Providers the user an introduction to the project and stores their name.
    
    Parameters
    ----------
    name : string
        
    Returns
    -------
    output_string : string
        Prints out a statement using their name.
    """ 
   
    name = input('Enter your name: ')
    print("Hello, it's nice to meet you",name)
    user_information.append(name)
    
    print ("\nI'm Lorraine and I'm the VP of Active Minds here at UCSD! I'm really excited to teach you about VAR.\n")
    
                   
def var_info():
    """To progress through the var information, user must provide inputs that in turn print out the next bits of information where the strings are dependent on their answer.
    
    Parameters
    ----------
    response : string
        either "yes" or "no"
        
    Returns
    -------
    output_string : string
        Depending on their answer, prints out a specific statement.
    """ 
    
    print ("VAR stands for Validate, Appreciate, and Refer.")
    print ("VAR is an ancronym you can use when navigating through tough conversations with someone in need of support. "
           "It can allow you to actively listen to someone you care about and help them cope.")
    print ("Conversations using VAR can take many forms, such as through the phone, in-person, text, etc. "
           "The method doesn't matter much but what does matter is the message that you care.")
    print ("A conversation such as this could help make all the difference and prevent a crisis from developing later on.")
         
    response = input ("\nLet's start going through each letter of VAR, are you ready?\nyes/no\n")
    if response == "yes":
        print ("Great! Let's start with the letter 'V' for Validate.")
        print ("In this part, the key is to validate someone's feelings.")
        print ("Let the person know that what they're feeling is okay and valid; "
               "that you're listening to and believing them.")
        print ("Some words of validation can include:")
        print ("\n That sounds difficult"
               "\n I'm so sorry to hear that you're strugging right now"
               "\n It sounds like you're having a really hard time right now")
        
        response = input ("\nAre you ready to move onto the letter 'A'? \nyes/no\n")
        if response == "yes":
            print ("With 'A' standing for Appreciate, it's all about appreciating someone's courage for speaking up.")
            print ("Let the person know that while speaking up is difficult, they're doing the right thing; "
                   "voicing their feelings is important and you're there to support them.")
            print ("Some words of appreciation can include:")
            print ("\n Thank you for sharing"
                   "\n I'm here for you if you want to talk or need anything"
                   "\n We all need support sometimes")
            
            response = input ("\nAre you ready to move onto the final letter, 'R'? \nyes/no\n")
            if response == "yes":
                print ("'R' stands for Refer and you're refering someone to skills and support.")
                print ("Let the person know that help is available and refer them to the appropriate resources.")
                print ("You can discuss what kind of skills and support helped you when you were in a similar situation.")
                print ("Some words of refering someone can include:")
                print ("\n It might be a good idea to make an appointment with CAPS. " 
                       "If you want I can be by your side while you give them a call. "
                       "\n We can plan to study sometime at the library"
                       "\n I've been using this meditation app and it's really helped slow down my thoughts.")
                
            elif response == "no":
                print ("It's okay, that was a lot of information to learn, take your time, we're almost done learning about VAR!")
            else: 
                print ("Sorry but I don't quite understand.")
        elif response == "no": 
            print ("It's okay, that was a lot of information to learn, take your time!")
        else: 
            print ("Sorry but I don't quite understand.")
        
    elif response == "no":
        print ("It's okay, take your time!")
        
    else:
        print ("Sorry but I don't quite understand.")


def var_scenario():
    """To progress throughout the scenario the user must provide inputs that are responses to the scenario that then print out statements that are dependent on their answer.
    
    Parameters
    ----------
    response : string
        either "yes" or "no" or "A" or "B"
        
    Returns
    -------
    output_string : string
        Depending on their answer, prints out a specific statement.
    """ 
    
    print ("\nI know that was a lot of information to learn, but let's try putting that knowledge into practice!\n")
    response = input ("Are you ready to try a scenario?\nyes/no\n")
    
    if response == "yes":
        print ("Perfect, let's get started!")
        print ("This scenario focuses on your friend coming to you for support because they're lacking motivation")
        print ("friend: Hey, can I be honest with you? Maybe you've been experiencing the same thing with remote learning.") 
        print ("\n A. Of course! what's up?"
               "\n B. Yeah, sure thing, I'm all ears.")
        
        response = input ("\nPlease pick A or B\n")
        if response == "A" or "B":
            print ("friend: Well, I've been having a hard time getting out of bed everyday. "
                   "I've been missing classes and I've hardly done any of my assignments. "
                   "I just can't get myself motivated.")
            print ("\n A. Oh man, I'm so sorry to hear that you're struggling with all of this right now. "
                   "I definitely resonate with how you're feeling as I've felt that way sometimes too "
                   "and I understand how hard it is."
                   "\n B. Oh wow, uhm, that sounds really tough but unfortunately I can't really relate.")
            
            response = input ("\nPlease pick A or B\n")
            if response == "A":
                print ("friend: R-really?! Oh wow, it's reassuring to know that I'm not the only one feeling like this, "
                       "y'know it sometimes feels like everyone at the school knows what they're doing "
                       "and has everything under control. I thought I was just dumb.")
                print ("\n A. Yeah, I agree! You're definitely not the only one who feels that way sometimes. "
                       "We all struggle at times! I just want you to know that I appreciate you opening up to me "
                       "about this sort of thing, I bet it must've been pretty hard to do."
                       "\n B. Yeah, it's like that sometimes. I don't know why you decided to open up to me, "
                       "I'm not the best at this type of thing.")
                
                response = input ("\nPlease pick A or B\n")
                if response == "A":
                    print ("friend: Thanks, it really means a lot to me knowing that I can talk to you about this stuff. "
                           "I didn't know who to turn to or what to do.")
                    print ("\n A. Don't worry, I'll be here to support you and if you need anything at all, please let me know. "
                           "I know alot of resources or tricks that could be helpful!"
                           "\n B. Maybe you should've gone to CAPS or something? I don't know, I heard that people find them useful.")
                    response = input ("\nPlease pick A or B\n")
                    
                    if response == "A":
                        print ("friend: You do? That's great! I haven't really put much thought into it, "
                               "so any help is very much appreciated. What sort of ideas did you have in mind?")
                        print ("\n A. Oh yeah, sure thing! How about this, I send you reminder texts right before class "
                               "so you remember or at least have a reminder to go? I can also text you every now "
                               "and then to check up on you and see how things are! Getting reminders from my friends "
                               "has usually worked wonders for me, so hopefully it does for you too!"
                           "\n B. Uhm, there's way too many, it might just be better for you to "
                               "just go online and research something yourself.")
                        
                        response = input ("\nPlease pick A or B\n")
                        if response == "A":
                            print ("friend: That's a great idea actually! I'd really appreciate it. "
                                   "Those reminders seem like they'd be a huge help.")
                            
                        elif response == "B":
                            print ("Hmm, that doesn't really seem like an appropriate response. Remember to use VAR!")
                        else:
                            print ("Sorry but I don't quite understand.")
                    elif response == "B":
                        print ("Hmm, that doesn't really seem like an appropriate response. Remember to use VAR!")
                    else:
                        print ("Sorry but I don't quite understand.")
                elif response == "B":
                    print ("Hmm, that doesn't really seem like an appropriate response. Remember to use VAR!")
                else:
                    print ("Sorry but I don't quite understand.")
            elif response == "B":
                print ("Hmm, that doesn't really seem like an appropriate response. Remember to use VAR!")
            else:
                print ("Sorry but I don't quite understand.")
        
    elif response == "no":
        print ("No worries, take your time! It can be a lot of information at once. Let me know when you're ready")
        
    else:
        print ("Sorry but I don't quite understand.")


def active_minds_plug():
    """User must provide an input that in return prints a statement dependent on their answer, either giving them Active Minds information or saying Goodbye.
    
    Parameters
    ----------
    learn_more : string
       "A" or "B"
        
    Returns
    -------
    output_string : string
        Depending on their answer, prints out a specific statement.
    """ 
    
    print ("\nThank you so much for participating in my workshop! "
           "I hope you enjoyed learning about practicing VAR. "
           "Please let me know if you want to learn more about Active Minds.\n")
    
    print ("\n A. What is Active Minds and how can I stay up to date with events?"
           "\n B. I'm all good, thank you!")
           
    learn_more = input ("\nPlease type in A or B\n")
    
    if learn_more == "A":
        print ("The mission of Active Minds is to change the conversation about mental health. "
               "Active Minds at UCSD is a student-run organization dedicated to mental health advoacy and "
               "the destigmatization of mental illnesses both on campus and in the local community. "
               "We host volunteer events, administer workshops, and feature speakers to educate on mental health.")
        print ("If you follow us on Facebook using @activemindsatucsd or Instagram with @activemindsucsd you can keep track of events. "
               "You can also check out our website 'https://activemindsucsd.wordpress.com' to learn more about us!")
        print ("Thanks and have a great rest of your day!")
    elif learn_more == "B": 
        print ("Of course! Have a great rest of your day!")
    else:
        print ("Sorry but I don't quite understand.")