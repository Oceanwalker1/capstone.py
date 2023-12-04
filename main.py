import time
# keepRunning variable to put the entire generator in a loop until set to false
keepRunning = True
# Givenroot is the user-input root note as a numerical value
givenRoot = 0

# The entire code is in a loop to keep running and generate multiple chord notes
while keepRunning:
  # Assigns a numerical value to givenRoot based off of the given root note (only for sharps and naturals)
  def rootNoteWithSharps(x):
    global givenRoot
    if x == "C":
      givenRoot = 1
    elif x == "C#":
      givenRoot = 2
    elif x == "D":
      givenRoot = 3
    elif x == "D#":
      givenRoot = 4
    elif x == "E":
      givenRoot = 5
    elif x == "F":
      givenRoot = 6
    elif x == "F#":
      givenRoot = 7
    elif x == "G":
      givenRoot = 8
    elif x == "G#":
      givenRoot= 9
    elif x == "A":
      givenRoot = 10
    elif x == "A#":
      givenRoot = 11
    elif x == "B":
      givenRoot = 12
    else:
      return 0
    return givenRoot
  
  # Assigns a numerical value to givenRoot based off of the given root note (only for flats and naturals)
  def rootNoteWithFlats(x):
    global givenRoot
    if x == "C":
      givenRoot = 1
    elif x == "DB":
      givenRoot = 2
    elif x == "D":
      givenRoot = 3
    elif x == "EB":
      givenRoot = 4
    elif x == "E":
      givenRoot = 5
    elif x == "F":
      givenRoot = 6
    elif x == "GB":
      givenRoot = 7
    elif x == "G":
      givenRoot = 8
    elif x == "AB":
      givenRoot = 9
    elif x == "A":
      givenRoot = 10
    elif x == "BB":
      givenRoot = 11
    elif x == "B":
      givenRoot = 12
    else:
      return 0
    return givenRoot
  
  # Combines rootNoteWithFlats and rootNoteWith Sharps
  def allPossibleRoots(x):
    rootNoteWithSharps(x)
    rootNoteWithFlats(x)
    return givenRoot
  
  # Because I made rootInput (line 111) convert to all uppercase, this function will put it in the proper capitalization to be repeated to the user in line 119
  def correctRootCapitalization(x):
    global rootInput2
    if x == "C":
      return "C"
    elif x == "C#":
      return "C#"
    elif x == "DB":
      return "Db"
    elif x == "D":
      return "D"
    elif x == "D#":
      return "D#"
    elif x == "EB":
      return "Eb"
    elif x == "E":
      return"E"
    elif x == "F":
      return "F"
    elif x == "F#":
      return "F#"
    elif x == "GB":
      return "Gb"
    elif x == "G":
      return "G"
    elif x == "G#":
      return "G#"
    elif x == "AB":
      return "Ab"
    elif x == "A":
      return "A"
    elif x == "A#":
      return "A#"
    elif x == "BB":
      return "Bb"
    elif x == "B":
      return "B"
      rootInput2 = "B"

  # 
  while givenRoot == 0:
    rootInput = input("Enter a root note: ")
    rootInput = rootInput.upper()
    # rootInput2 is used to read the root to the user
    rootInput2 = rootInput
    #rootInput2 = correctRootCapitalization(rootInput2)
    allPossibleRoots(rootInput)
    if givenRoot == 0:
      print("Invalid root note.")
    if givenRoot > 0:
      time.sleep(0.5)
      print("You chose", correctRootCapitalization(rootInput2), "as your root note.")
      break
  
  # List of notes as numerical values
  givenIntervals = []
  
  # New variable qual that sets to "maj", "min", "dom" etc. based off of the quality given by user
  qual = ""
  
  # Adds to givenIntervals list with numbers that are going to correlate with the given notes
  def allPossibleQualities(x):
    global givenIntervals
    global qual
    if x == "major" or x == "maj":
      qual = "maj"
      givenIntervals.append(givenRoot)
      givenIntervals.append(givenRoot + 4)
      givenIntervals.append(givenRoot + 7)
    elif x == "major 7" or x == "maj7" or x == "maj 7":
      qual = "maj"
      givenIntervals.append(givenRoot)
      givenIntervals.append(givenRoot + 4)
      givenIntervals.append(givenRoot + 7)
      givenIntervals.append(givenRoot + 11)
    elif x == "minor" or x == "min":
      qual = "min"
      givenIntervals.append(givenRoot)
      givenIntervals.append(givenRoot + 3)
      givenIntervals.append(givenRoot + 7)
    elif x == "minor 7" or x == "min7" or x == "min 7":
      qual = "min"
      givenIntervals.append(givenRoot)
      givenIntervals.append(givenRoot + 3)
      givenIntervals.append(givenRoot + 7)
      givenIntervals.append(givenRoot + 10)
    elif x == "dominant 7" or x == "dominant" or x == "dom" or x == "dom7":
      qual = "dom"
      givenIntervals.append(givenRoot)
      givenIntervals.append(givenRoot + 4)
      givenIntervals.append(givenRoot + 7)
      givenIntervals.append(givenRoot + 10)
  
  while qual == "":
    qualityInput = (input("Enter a quality: "))
    qualityInput = qualityInput.lower()
    allPossibleQualities(qualityInput)
    if qual == "":
      print("Please provide a valid quality")
    if qual != "":
      break
  
  # List for numbers2Notes to add to that will give the notes as strings
  notes = []
  
  # Converts the number values in givenIntervals to note names and adds them to the notes list with sharp accidentals
  def numbers2NotesSharps(x):
    global notes
    global givenIntervals
    if 1 in givenIntervals:
      notes.append("C")
    if 2 in givenIntervals:
      notes.append("C#")
    if 3 in givenIntervals:
      notes.append("D")
    if 4 in givenIntervals:
      notes.append("D#")
    if 5 in givenIntervals:
      notes.append("E")
    if 6 in givenIntervals:
      notes.append("F")
    if 7 in givenIntervals:
      notes.append("F#")
    if 8 in givenIntervals:
      notes.append("G")
    if 9 in givenIntervals:
      notes.append("G#")
    if 10 in givenIntervals:
      notes.append("A")
    if 11 in givenIntervals:
      notes.append("A#")
    if 12 in givenIntervals:
      notes.append("B")
    if 13 in givenIntervals:
      notes.append("C")
    if 14 in givenIntervals:
      notes.append("C#")
    if 15 in givenIntervals:
      notes.append("D")
    if 16 in givenIntervals:
      notes.append("D#")
    if 17 in givenIntervals:
      notes.append("E")
    if 18 in givenIntervals:
      notes.append("F")
    if 19 in givenIntervals:
      notes.append("F#")
    if 20 in givenIntervals:
      notes.append("G")
    if 21 in givenIntervals:
      notes.append("G#")
    if 22 in givenIntervals:
      notes.append("A")
    if 23 in givenIntervals:
      notes.append("A#")
    if 24 in givenIntervals:
      notes.append("B")
  
  # Converts the number values in givenIntervals to note names and adds them to the notes list with flat accidentals
  def numbers2NotesFlats(x):
    global notes
    global givenIntervals
    if 1 in givenIntervals:
      notes.append("C")
    if 2 in givenIntervals:
      notes.append("Db")
    if 3 in givenIntervals:
      notes.append("D")
    if 4 in givenIntervals:
      notes.append("Eb")
    if 5 in givenIntervals:
      notes.append("E")
    if 6 in givenIntervals:
      notes.append("F")
    if 7 in givenIntervals:
      notes.append("Gb")
    if 8 in givenIntervals:
      notes.append("G")
    if 9 in givenIntervals:
      notes.append("Ab")
    if 10 in givenIntervals:
      notes.append("A")
    if 11 in givenIntervals:
      notes.append("Bb")
    if 12 in givenIntervals:
      notes.append("B")
    if 13 in givenIntervals:
      notes.append("C")
    if 14 in givenIntervals:
      notes.append("Db")
    if 15 in givenIntervals:
      notes.append("D")
    if 16 in givenIntervals:
      notes.append("Eb")
    if 17 in givenIntervals:
      notes.append("E")
    if 18 in givenIntervals:
      notes.append("F")
    if 19 in givenIntervals:
      notes.append("Gb")
    if 20 in givenIntervals:
      notes.append("G")
    if 21 in givenIntervals:
      notes.append("Ab")
    if 22 in givenIntervals:
      notes.append("A")
    if 23 in givenIntervals:
      notes.append("Bb")
    if 24 in givenIntervals:
      notes.append("B")
  
  # Checks rootInput so that the correct accidentals are used
  if rootInput == "DB" or rootInput == "EB" or rootInput == "GB" or rootInput == "AB" or rootInput == "BB":
    numbers2NotesFlats(rootInput)
  else:
    numbers2NotesSharps(rootInput)
  
  # New variable qualStr that checks if the qual variable is maj, min, or dom and represents it as a string to use in print function
  qualStr = ""
  if qual == "maj":
    qualStr = "major"
  elif qual == "min":
    qualStr = "minor"
  elif qual == "dom":
    qualStr = "dominant 7"
  
  # "[root note] contains the notes [notes list]"
  time.sleep(0.5)
  print(notes[0], qualStr, "contains the notes", ", ".join(notes))
  
  # keepAsking variable is used to create a while loop that asks the user if they'd like to generate more chords
  keepAsking = True
  while keepAsking:
    tryAgain = input("Would you like to find another chord? \n")
    tryAgain = tryAgain.lower()
    if tryAgain == "yes" or tryAgain == "y":
      givenRoot = 0
      keepAsking = False
      time.sleep(0.5)
    elif tryAgain == "no" or tryAgain == "n":
      time.sleep(0.5)
      print("Thanks for using the chord finder!")
      keepAsking = False
      keepRunning = False
    else:
      time.sleep(0.5)
      print("Please enter either yes or no.")
