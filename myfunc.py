"""
This arranges arithmetic problems vertically. 
It takes in a list of arithmetic operations as input (Ops) and an optional boolean argument (Add) to determine whether to include the results of the operations. 
The function processes the operations and formats them in a visually appealing way.

Here's a breakdown of how the code works:

It initializes some variables to store the intermediate results and lengths.

It performs several error checks, such as checking the number of problems, verifying that numbers contain only digits,
ensuring the operator is either '+' or '-', and checking that numbers are not more than four digits long.

It calculates the sum or difference of each operation and stores it in the third element of each operation vector.

It also swaps the operator with the second operand and removes the second operand from the vector.

It determines the maximum length of each column and stores it in lenvec.

It formats the elements of the matrix (mtx) by padding them with spaces or hyphens to align them properly.

It constructs the first, second, and third rows of the arranged problems by concatenating the respective elements from mtx.

If Add is set to True, it adds a fourth row to the arranged problems by concatenating the elements from mtx representing the result line.

It returns the arranged problems as a formatted string.

"""





def arithmetic_arranger(Ops,Add = False ):

  lenvec = []
  mtx = []
  sings = []

  if len(Ops) > 5:
    return 'Error: Too many problems.'

  for Operation in Ops:
    vector = Operation.split()
    try: 
      int(vector[0])
    except: return 'Error: Numbers must only contain digits.'

    if vector[1] != '+' and vector[1] != '-':
      return '''Error: Operator must be '+' or '-'.''' 

    try: 
      int(vector[2])
    except: return 'Error: Numbers must only contain digits.'

    if len(vector[0]) > 4 or len(vector[2]) > 4:
      return 'Error: Numbers cannot be more than four digits.' 
    
    #suma o resta
    if vector[1] == '+':
      vector.append(str(int(vector[0]) + int(vector[2])))
    else:
      vector.append(str(int(vector[0]) - int(vector[2])))
    sings.append(vector[1])
    vector[1] = vector[2]
    vector[2] = ''
    mtx.append(vector)

  for i in range(len(mtx)): #Creates a vector with value of the maximum lenght string from each column of the matrix
    lenvec.append(0)
    for j in range(2):
      if lenvec[i] < len(mtx[i][j]):
        lenvec[i] = len(mtx[i][j])


  #Formatting
  for i in range(len(mtx)):
    while len(mtx[i][0]) < lenvec[i]:
        mtx[i][0] = ' ' + mtx[i][0]

    while len(mtx[i][1]) < lenvec[i]:
        mtx[i][1] = ' ' + mtx[i][1]

    while len(mtx[i][2]) < lenvec[i]: #Creates the result line
        mtx[i][2] = '-' + mtx[i][2]

    while len(mtx[i][3]) < len(mtx[i][2]):
        mtx[i][3] = ' ' + mtx[i][3]
    

    mtx[i][0] = '  ' + mtx[i][0]
    mtx[i][1] = sings[i] + ' ' + mtx[i][1]#adds the sign to the second operand
    mtx[i][2] = '--' + mtx[i][2]

    while len(mtx[i][3]) < len(mtx[i][2]):
        mtx[i][3] = ' ' + mtx[i][3]


  #Arranges the first row of the string to be returned
  arranged_problems = ['','','','']
  for i in range(len(mtx)):
    arranged_problems[0] = arranged_problems[0] + mtx[i][0] + '    '

  #Second Row
  for i in range(len(mtx)):
    arranged_problems[1] = arranged_problems[1] + mtx[i][1] + '    '

  #Third Row
  for i in range(len(mtx)):
    arranged_problems[2] = arranged_problems[2] + mtx[i][2] + '    '


  #Optional when Add = True
  if Add != True:
      return arranged_problems[0].rstrip() + '\n' + arranged_problems[1].rstrip() + '\n' + arranged_problems[2].rstrip()
  else:
    for i in range(len(mtx)):
      arranged_problems[3] = arranged_problems[3] + mtx[i][3] + '    '
    return arranged_problems[0].rstrip() + '\n' + arranged_problems[1].rstrip() + '\n' + arranged_problems[2].rstrip() + '\n' + arranged_problems[3].rstrip()
