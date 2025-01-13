while True:
  palindrome = (input("\nEnter a word to see if it is a palindrome: "))
  ori_pal = palindrome #allows us to show user the original word(s)
  palindrome = "".join( ign for ign in palindrome if ign.isalnum()) #removes white space AND also ignores any other characters that are not str type (or letters)
  '''
  The "" replaces white space with anything that's within the double quotes
  since it is empty, it replaces white spaces with no space at all
  
  the <.join> removes all whitespace
  
  <for> is a loop, allows us to go throughout the palindrome
  and remove any that isn't considered as a string or letter via the
  <isalnum()> syntax

  the ign variable stores the data after getting rid of white spaces and punctuation marks
  then adds it back into palindrome via declaring palindrome again.
  ''' 
  
  palindrome = palindrome.lower() #makes letters all lowercase
  palin_rev = palindrome[::-1] #reverse the strings

  while palin_rev == palindrome:
    success = ("\n" + input("\n< " + ori_pal+ " >" + ", is a palindrome! Do you want to try again? (yes or no): ")).lower().strip()
    if success == "yes":
      break
    if success == "no":
      print("\nThank you for using my program!")
      quit()
    else:
      print("\nThe answer you submitted was not clear")
      success = (input("\ntype 'yes' if you still want to continue, type 'no' if you want to quit: ")).lower().strip()
    if success == "yes":
      break
    if success == "no":
      print("\nThank you for using my program!")
      quit()
      
  while palin_rev != palindrome:
    wrong = (input("\n" + "< " + ori_pal+ " >" + "," + "is not a palindrome. Do you want to try again? (yes or no): ")).lower().strip()
    if wrong == "yes":
      break
    if wrong == "no":
      print("\nThank you for using my program!")
      quit()
    else:
      print("\nThe answer you submitted was not clear")
      wrong = (input("\ntype 'yes' if you still want to continue, type 'no' if you want to quit: ")).lower().strip()
    if wrong == "yes":
      break
    if wrong == "no":
      print("\nThank you for using my program!")
      quit();