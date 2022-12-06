import random


def shufflePassword(stringlength = 10):
  tempList = list(stringlength)
  random.shuffle(tempList)
  return ''.join(tempList)



number = str(random.randint(1,1000000000))
letter1=chr(random.randint(65,90)) #Generate a random Uppercase letter 
letter2=chr(random.randint(65,70)) #Generate a random Uppercase letter 
letter3=chr(random.randint(65,100))
letter4=chr(random.randint(65,90))
letter5=chr(random.randint(20,30))
letter6=chr(random.randint(65,990))
letter7=chr(random.randint(65,300))

password = letter1 + letter2 + number + number +letter3 +letter4+letter7
password = shufflePassword(password)


print('Generated password is ' +password)