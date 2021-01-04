#Defines a function for the tutor to set up the voting system with the details of the form
def tutorSetUp():
  global tutorGroupNumPupils, nameCandidates, numOfCandidates, votesCandidates, tutorGroup, abstainStudentVotes

  abstainStudentVotes = 0
  #Defines an array with the possible names of the forms
  tutorGroupOptions = ['7A', '7B', '7C', '7D', '7E', '7F', '8A', '8B', '8C', '8D', '8E', '8F', '9A', '9B', '9C', '9D', '9E', '9F', '10A', '10B', '10C', '10D', '10E', '10F', '11A', '11B', '11C', '11D', '11E', '11F']
  #Asks and validates the entry of the name of the tutor group
  tutorGroup = str(input('Enter the name of the tutor group: ')).upper()
  while tutorGroup not in tutorGroupOptions:
    tutorGroup = str(input('INVALID. Enter the name of the tutor group: ')).upper()

  #Asks and validates the entry of the number of pupils in the tutor group
  tutorGroupNumPupils = int(input("Enter the number of students in the tutor group: "))
  while tutorGroupNumPupils > 35 or tutorGroupNumPupils < 28:
    tutorGroupNumPupils = int(input("INVALID. Enter the number of students in the tutor group: "))
  
  #Asks and validates the entry of the number of pupils running in the election
  numOfCandidates = int(input("How many candidates are running in the election: "))
  while numOfCandidates > 4 or numOfCandidates < 2:
    numOfCandidates = int(input("INVALID. Minimum of 2, Maximum of 4. How many candidates are running in the election: "))
  
  #Asks and Validates the entry of the names of the pupils running in the election
  nameCandidates = [''] * (numOfCandidates)
  votesCandidates = [0] * (numOfCandidates)

  for student in range(len(nameCandidates)):
    name = str(input("\nEnter the name of the student: ")).title()
    nameCandidates[student] = name

#Defines a function for each student to cast their vote
def studentVoting():
  global abstainStudentVotes
  
  #For loop to iterate through every student in the form
  for student in range(tutorGroupNumPupils):
    print("\nCandidates in the election:: ")

    #For loop to print out the options to vote for each of the candidates
    for name in range(len(nameCandidates)):
      print (str(name + 1) + '.', nameCandidates[name])
    print (str(len(nameCandidates) + 1) + '. Abstain')

    studentVote = int(input("\nWho would you like to vote for: "))
    while studentVote > numOfCandidates + 1 or studentVote < 1:
      studentVote = int(input("INVALID. Please enter a number listed. Who would you like to vote for: "))
    
    if studentVote <= len(votesCandidates):
      votesCandidates[studentVote-1] += 1
    else:
      abstainStudentVotes += 1

def outputWinner():
  winner = ''
  winnerVotes = 0
  #Outputs the tutor tutor group details
  print ('\nForm:' + tutorGroup)
  
  #Outputs the number of votes for each candidate
  for candidate in nameCandidates:
    print (candidate, 'recived', str(votesCandidates[nameCandidates.index(candidate)]), 'votes')


  #Checks who won the election
  for vote in range(len(votesCandidates)):
    if votesCandidates[vote] > winnerVotes:
      winnerVotes = votesCandidates[vote]
      winner = nameCandidates[vote]

  #Outputs the winner of the election
  print ('The winner of the election was', winner)