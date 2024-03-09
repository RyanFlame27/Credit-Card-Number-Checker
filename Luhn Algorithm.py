def LuhnChecker(number):
  revNumber=number[::-1]
  doubleNos=revNumber[1::2]
  otherNos=revNumber[::2]
  CheckSum=0
  for i in otherNos:
    CheckSum+=int(i)
  for i in range(len(doubleNos)):
    doubleNos[i]=str(2*int(doubleNos[i]))
    if int(doubleNos[i])<10:
      CheckSum+=int(doubleNos[i])
    else:
      tempL=list(doubleNos[i])
      tempsum=0
      for i in tempL:
        tempsum+=int(i)
      CheckSum+=tempsum
  if CheckSum%10==0:
    return True
  else:
    return False

cardNo=input("Enter Card number: ")
numberformatter=str.maketrans({"-":""," ":""})
cardNo=cardNo.translate(numberformatter)
cardNo_List=list(cardNo)
if LuhnChecker(cardNo_List):
  print("VALID NUMBER")
else:
  print("INVALID NUMBER")