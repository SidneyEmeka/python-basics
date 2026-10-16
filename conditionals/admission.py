utmeScore = int (input ( 'Utme score '))
pUtmeScore = int(input ( 'Post Utme score '))
oLvl = (input( 'Enter Yes if your 0 level result is available or No if not '))
numberOlvC = int(input ('How many 0 level Credits '))
age = int (input ( 'How old are you '))
nOPAA = int (input ( 'How many times have you written JAMB '))


######### ADMISSION REQUIREMENT ###########

if utmeScore >= 180:
    if oLvl == "Yes" and numberOlvC >= 5:
        if (numberOlvC == 5 and utmeScore >= 220) or (numberOlvC >= 6):
            if (age >= 26 and age <= 27 and utmeScore >= 250) or (age <= 25):
                if (nOPAA >=3 and nOPAA < 4 and utmeScore >= 220) or (nOPAA <=2):
                    if utmeScore >= 180 and utmeScore <= 199:
                        print( 'Rejected: You are automatically rejected')
                    elif utmeScore >= 200 and utmeScore <= 219:
                        if pUtmeScore >= 60:
                            print ( 'Admitted')
                        else: print ( 'Waitlisted: Your Post-UTME is too low')
                    elif utmeScore >= 220 and utmeScore <= 279:
                        if pUtmeScore >= 50: 
                            print ( 'Admitted')
                        else: print('Waitlisted: Your Post-UTME is too low')
                    elif utmeScore >= 280: 
                        if pUtmeScore >= 45:
                            print ('Admitted')
                        else: print( 'Waitlisted: Your Post-UTME is too low')
                else: print( 'Rejected: You have exceeded the maximum number of trials')
            else: print( 'Rejected: Your Age is not eligible for admission' )
    else: print( 'Rejected: You must have an O-level with at least 5 credits')
else: print( 'Rejected: Your JAMB score is too low are not eligible for admission' )