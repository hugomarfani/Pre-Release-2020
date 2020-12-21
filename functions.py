def tutorSetUp():
  tutorGroupOptions = ['7A', '7B', '7C', '7D', '7E', '7F', '8A', '8B', '8C', '8D', '8E', '8F', '9A', '9B', '9C', '9D', '9E', '9F', '10A', '10B', '10C', '10D', '10E', '10F', '11A', '11B', '11C', '11D', '11E', '11F']
  tutorGroup = str(input('Enter the name of the tutor group: ')).upper()
  while tutorGroup not in tutorGroupOptions:
    tutorGroup = str(input('INVALID. Enter the name of the tutor group: ')).upper()