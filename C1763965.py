# Exercise 1
def freeFall(val,isD):
    #Define rate of acceleration due to gravity
    g = 9.81
    if isD == True:
        # D is true therefore using distance to find time
        return(round(((2*float(val)/g)**0.5),2))
    else:
        # D is false therefore using time to find distance
        return(round((0.5*g*(float(val)**2)),2))
    

# Exercise 2
def RPS(s):
    # create variable to store results
    res = ""
    # ensure all input is capitalised
    s = s.upper()
    #Loop through for each character in string to add the winning solution
    for c in s:
        if c=="R":
            res+="P"
        elif c == "P":
            res+="S"
        else:
            res+="R"
    return(res)
    


# Exercise 3
def list2str(l):
    #create variable starting with [
    res = "["
    #iterate through l adding individual elements to string
    for element in l:
        if type(element) == list:
            res += list2str(element)
        else:
            res += element
    res += "]"
    return(res)
    


# Exercise 4
def textPreprocessing(text):
    #remove punctuation
    text = text.strip('.?!,:;-[]{}()"')
    #remove commas
    text = text.replace(',','')
    #convert to lower case
    text = text.lower()
    #convert text to list at spaces
    text = text.split()
    stopwords = ['i','a','about','am','an','are','as','at','be','by','for','from','how','in','is','it','of','on','or','that','the','this','to','was','what','when','where','who','will','with']
    #iterate through text and if any match with any in stopwords, remove them
    text = [word for word in text if word not in stopwords]
    #remove specifide suffixes
    text = [word.replace('ed','').replace('ing','').replace('s','') for word in text]
    return(text)
    


# Exercise 5
def isGreaterThan(dict1,dict2):
    #find if any variables are in dict2 and not in dict1. if true set to false
    for key in dict2:
        if key not in dict1:
            GreaterThan = False
        else:
            #iterate through dict1 comparing to matching key to find if >=
            for key in dict1:
                if key in dict2:
                    if dict1.get(key) >= dict2.get(key):
                        GreaterThan = True
                    else:
                        GreaterThan = False
                        break
                else:
                    GreaterThan = True
    #return false if dict1 and dict2 are the same
    if dict1 == dict2:
        GreaterThan = False
    return(GreaterThan)
    


# Exercise 6
def CSVsum(filename):
    #create variable from open csv
    Table = open(filename)
    #create open list variable
    sums = []
    #iterate through table items converting into list
    for row in Table:
        row = row.split(',')
        try:
            #convert list items into floats and add list to sums
            row = [float(value) for value in row]
            sums.append(row)
        except:
            continue
#add the coloumn figures together
# code to sum lists in a list
#taken from Stack Overflow post by E-A 8-10-2020
#accessed 26/12/21
#https://stackoverflow.com/questions/64264392/adding-numbers-in-the-same-indices-in-list-of-lists
    sums = list(map(sum,zip(*sums)))
#end of referenced code
    return(sums)
    
# Exercise 7
def str2list(s):
    #create empty list
    res = []
    #start counter
    i = 0
    #remove first and last character of string which will always be []
    s = s[1:-1]
    #iterate through string adding to list and adding brackets 
    while i < len(s):
        if s[i] == '[':
            substr = s[i+1:s.find(']')]
            removing = s[i:s.find(']')+1]
            res.append(list(substr))
            s = s.replace(removing,' ')
        else:
            res.append(s[i])
        #increase counter
        i+=1
    print(res)
    

# Exercise 8
def spacemonSim(roster1,roster2):
    #A round of battle where typeFight is used untill one mon hits 0 energy
    def battle(mon1,mon2):
        #determining the attack strength and recording dmg on mon
        def typeFight(AttName, AttPower, DefName, DefEnergy):
        #find name of att mon then compare with def mon to find right eqn
            if AttName == 'Mercury':
                if DefName == 'Mercury':
                    DefEnergy -= AttPower
                elif DefEnergy == 'Earth':
                    DefEnergy -= AttPower
                elif DefName == 'Venus':
                    DefEnergy -= AttPower * 2
                elif DefName == 'Mars':
                    DefEnergy -= AttPower * 0.5
            elif AttName == 'Venus':
                if DefName == 'Venus':
                    DefEnergy -= AttPower
                elif DefName =='Mars':
                    DefEnergy -= AttPower
                elif DefName == 'Earth':
                    DefEnergy -= AttPower * 2
                elif DefName == 'Mercury':
                    DefEnergy -= AttPower * 0.5
            elif AttName == 'Earth':
                if DefName == 'Mercury':
                    DefEnergy -= AttPower
                elif DefName == 'Earth':
                    DefEnergy -= AttPower
                elif DefName == 'Mars':
                    DefEnergy -= AttPower * 2
                elif DefName == 'Venus':
                    DefEnergy = DefEnergy - (AttPower * 0.5)
            else:
                if DefName == 'Venus':
                    DefEnergy -= AttPower
                elif DefName =='Mars':
                    DefEnergy -= AttPower
                elif DefName == 'Mercury':
                    DefEnergy -= AttPower * 2
                elif DefName == 'Earth':
                    DefEnergy -= AttPower * 0.5
            #return the defmon energy
            return(DefEnergy)
        #make energy variables therfore adjustable
        mon1Energy = mon1[1]
        mon2Energy = mon2[1]
        #start loop
        while mon1Energy and mon2Energy >= 0:
            mon2Energy = typeFight(mon1[0],mon1[2],mon2[0],mon2Energy)
            if mon2Energy <= 0:
                return(mon1Energy, mon2Energy)
            mon1Energy = typeFight(mon2[0],mon2[2],mon1[0],mon1Energy)
            if mon1Energy <= 0:
                return(mon1Energy, mon2Energy)
    #battles both mon
    while len(roster1) != 0 and len(roster2) != 0:
        Battlemon1 = roster1[0]
        Battlemon2 = roster2[0]
        joust = battle(Battlemon1,Battlemon2)
        mon1Energy, mon2Energy = joust
        if mon1Energy <= 0:
            roster1.pop(0)
            healthChange = list(roster2[0])
            healthChange[1] = mon2Energy
            roster2[0] = tuple(healthChange)
        elif mon2Energy <= 0:
            roster2.pop(0)
            healthChange = list(roster1[0])
            healthChange[1] = mon1Energy
            roster1[0] = tuple(healthChange)
    if len(roster1) == 0:
        return(False)
    elif len(roster2) == 0:
        return(True)


# Exercise 9
def rewardShortPath(env):
    return None


# Exercise 10
def cliqueCounter(network):
    return None
