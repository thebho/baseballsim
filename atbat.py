import math,random
import pylab
PITCH_SKILL,PITCH_FREQ=0,1
PITCH_DICT ={'Fastball':[0.97,'r'],'ChangeUp':[0.95,'b']}
STRIKE_WIDTH=(-1.0,1.0)
STRIKE_HEIGHT=(-4.0,3.0)
STRIKE_ZONE=(-0.85,0.85,-2.0,1.5)



    ### Temporary classes ###
class Player(object):
    """
    Creates a MLB player
    """
    def __init__(self, firstName, lastName, throwingHand, battingHand, jerseyNumber=0, position="", team="", status="Active"):
        """
        battingHand='Left','Right','Switch'
        throwingHand='Left','Right'
        position: Player's position (e.g., 'Pitcher', 'Catcher', 'Outfield')
        team: Team name
        status: 'Active' or 'Injured'
        """
        self.name = str(firstName) + str(lastName)
        self.firstName = firstName
        self.lastName = lastName
        self.throwingHand = throwingHand
        self.battingHand = battingHand
        self.jerseyNumber = jerseyNumber
        self.position = position
        self.team = team
        self.status = status
    
class Pitcher(Player):
    """
    A MLB pitcher. Subclass of Player
    """
    def __init__(self, firstName, lastName, age, throwingHand, battingHand, pitcherRating,
                 jerseyNumber=0, team="", status="Active"):
        """
        Creates a Pitcher Instance.
        Rating=an Integer 1-99
        """
        Player.__init__(self, firstName, lastName, throwingHand, battingHand, jerseyNumber, "Pitcher", team, status)
        self.age = age
        self.pitchDict = PITCH_DICT.copy()
        self.energy = 100
        self.rating = pitcherRating

    def getRating(self):
        return self.rating

class Batter(Player):
    """
    A MLB batter. Subclass of Player
    """
    def __init__(self, firstName, lastName, age, throwingHand, battingHand, contact,
                 jerseyNumber=0, position="", team="", status="Active"):
        """
        Creates a Batter Instance.
        Contact= An integer 1-99
        """
        Player.__init__(self, firstName, lastName, throwingHand, battingHand, jerseyNumber, position, team, status)
        self.age = age
        self.contact = contact

    def getRating(self):
        """
        Returns a batter's rating
        """
        return self.contact

   ### Temporary classes ###

class PlayerManager(object):
    """
    Manages storage and retrieval of players in memory
    """
    def __init__(self):
        """
        Initializes the PlayerManager with empty player storage
        """
        self.players = {}
    
    def addPitcher(self, firstName, lastName, age, throwingHand, battingHand, pitcherRating,
                   jerseyNumber=0, team="", status="Active"):
        """
        Adds a new pitcher to the player storage
        
        Args:
            firstName: Pitcher's first name
            lastName: Pitcher's last name
            age: Pitcher's age
            throwingHand: 'Left' or 'Right'
            battingHand: 'Left', 'Right', or 'Switch'
            pitcherRating: Integer 1-99
            jerseyNumber: Jersey number
            team: Team name
            status: 'Active' or 'Injured'
        
        Returns:
            The created Pitcher object
        """
        pitcher = Pitcher(firstName, lastName, age, throwingHand, battingHand, pitcherRating,
                         jerseyNumber, team, status)
        playerKey = pitcher.name
        self.players[playerKey] = pitcher
        print("Added pitcher: %s" % playerKey)
        return pitcher
    
    def addBatter(self, firstName, lastName, age, throwingHand, battingHand, contact,
                  jerseyNumber=0, position="", team="", status="Active"):
        """
        Adds a new batter to the player storage
        
        Args:
            firstName: Batter's first name
            lastName: Batter's last name
            age: Batter's age
            throwingHand: 'Left' or 'Right'
            battingHand: 'Left', 'Right', or 'Switch'
            contact: Integer 1-99
            jerseyNumber: Jersey number
            position: Player position
            team: Team name
            status: 'Active' or 'Injured'
        
        Returns:
            The created Batter object
        """
        batter = Batter(firstName, lastName, age, throwingHand, battingHand, contact,
                       jerseyNumber, position, team, status)
        playerKey = batter.name
        self.players[playerKey] = batter
        print("Added batter: %s" % playerKey)
        return batter
    
    def getPlayer(self, firstName, lastName):
        """
        Retrieves a player by first and last name
        
        Args:
            firstName: Player's first name
            lastName: Player's last name
        
        Returns:
            The Player object if found, None otherwise
        """
        playerKey = str(firstName) + str(lastName)
        return self.players.get(playerKey, None)
    
    def getAllPlayers(self):
        """
        Returns all stored players
        
        Returns:
            Dictionary of all players
        """
        return self.players
    
    def listPlayers(self):
        """
        Prints all stored players
        """
        if not self.players:
            print("No players stored")
            return
        print("Stored Players:")
        for playerName, player in self.players.items():
            playerType = "Pitcher" if isinstance(player, Pitcher) else "Batter"
            print("  - %s (%s)" % (playerName, playerType))
    
    def removePlayer(self, firstName, lastName):
        """
        Removes a player from storage
        
        Args:
            firstName: Player's first name
            lastName: Player's last name
        
        Returns:
            True if player was removed, False if not found
        """
        playerKey = str(firstName) + str(lastName)
        if playerKey in self.players:
            del self.players[playerKey]
            print("Removed player: %s" % playerKey)
            return True
        else:
            print("Player not found: %s" % playerKey)
            return False

class Pitch(object):
    """
    Chooses a pitch from a weighted list, chooses a location relative to
    the center of the strike zone, and exectues the pitch based on a pitcher's
    skill and energy.
    """
    def __init__(self,pitcher):
        """
        Initializes a single pitch.

        pitcher=A Pitcher object
        """
        self.pitcher=pitcher
        self.location=random.uniform(STRIKE_WIDTH[0],STRIKE_WIDTH[1]),random.uniform(STRIKE_HEIGHT[0],STRIKE_HEIGHT[1])
        self.pitch=random.choice(list(self.pitcher.pitchDict.keys()))
        self.pitchQuality=100-(10*random.random())
        print(self.pitch)
    
    def getPitch(self):
        """
        Returns current pitch
        """
        return self.pitch

    def getLocation(self):

        return self.location

    def getPitchQuality(self):
        """
        Chooses a pitch and location, and returns the pitch type, location, quality)
        """
        return self.pitchQuality

    def isStrike(self):
        """
        Returns True if a pitch taken is within the STRIKE_ZONE
        """
        if STRIKE_ZONE[0]<self.location[0]<STRIKE_ZONE[1] and STRIKE_ZONE[2]<self.location[1]<STRIKE_ZONE[3]:
            return True
        else: return False

class Swing(object):
    """
    Takes a Pitch object and a batter and decides whether to take a pitch,
    swing and miss, or swing and hit)
    """
    def __init__(self,pitcher,pitch,batter):
        """
        Initializes a single pitch.

        pitcher=A Pitcher object
        """
        self.currentPitch=pitch
        self.batter=batter
        self.pitcher=pitcher
        self.pitchQuality=pitch.getPitchQuality()

    def swingOrTake(self,balls,strikes):
        """
        Takes a pitch object and returns True if the batter swings,
        and False if they take the pitch
        """
        if balls==0 and strikes==0:takePer=80
        elif balls==3 and strikes==0:takePer=90
        elif strikes==2:takePer=10
        else:takePer=50
        randomTake=100-100*random.random()
        x,y = Pitch.getLocation(self.currentPitch)
        if -0.4<x<0.4 and -1.0<y<0.5:
            print('Swung at strike')
            return True
        elif -0.9<x<0.9 and -2.0<y<2.0 and takePer<randomTake:
            if random.random()>0.5:
                print('Swung at borderline pitch')
                return True
            else:
                print('Didnt swing at borderline pitch')
                return False
        else: return False

    def swingContact(self):
        """
        Takes a pitch,pitcher rating and batter rating and returns True
        if the batter makes contact, False for a swing and miss
        pitch=a pitch object
        """
        x,y=Pitch.getLocation(self.currentPitch)
        if -0.6<x<0.6 and -2.0<y<1.5:
            print('Made contact down the middle')
            return True
        batterRating=self.batter.getRating()
        pitcherAdvantage=self.pitchQuality-batterRating
        randomS=random.random()
##        print randomS
        if pitcherAdvantage>10:
            if randomS>.95:return True
            else: return False
        elif pitcherAdvantage>0:
            if randomS>0.5:return False
            else: return True
        elif pitcherAdvantage>-10:
            if randomS>0.3:return True
            else: return False
        else: return True

##def plotPitches(pitcher,pitch,result,pitchCount):
##
##    x,y=pitch.getLocation()
##    color=pitch.getPitch()[1]
##    pylab.plot([x],[y])
##    pylab.text(x,y,str(pitchCount))
##    pylab.show


def atBat(pitcher,batter):
    """
    Runs an atBat sequence
    pitcher,batter=pitcher object and batter object   
    """
    balls=0
    strikes=0
    pitchCount=0
    inPlay=False
    pitchList=[]

    while balls<4 and strikes<3 and inPlay==False:
        print(balls,strikes)
        pitchCount+=1
        P=Pitch(pitcher)
        pitchList.append(P.getLocation())
        S=Swing(pitcher,P,batter)
        if S.swingOrTake(balls,strikes)==False:
            if P.isStrike()==True:strikes+=1
            else:balls+=1
        else:
            if S.swingContact()==True:
                inPlay=True
##                plotPitches(pitcher,P,None,pitchCount)
                print('Ball in play')
            else:
                strikes+=1
                print('Swinging Strike')
    if balls==4:print('Base on Balls')
    elif strikes==3: print('Strike Out')
    print(pitchList)
    pitchW,pitchH,labels,pi=[],[],[],0
    for i in pitchList:
        pi+=1
        pitchW.append(i[0])
        pitchH.append(i[1])
        labels.append('Pitch '+str(pi))
    ax=pylab.subplot(111)
    ax.scatter(pitchW,pitchH)
    for label, xpt, ypt in zip(labels,pitchW,pitchH):
        pylab.text(xpt, ypt, label)
    pylab.plot([STRIKE_ZONE[0],STRIKE_ZONE[1],STRIKE_ZONE[1],STRIKE_ZONE[0],STRIKE_ZONE[0]],
               [STRIKE_ZONE[2],STRIKE_ZONE[2],STRIKE_ZONE[3],STRIKE_ZONE[3],STRIKE_ZONE[2]])
    pylab.xlim(-2.5,2.5)
    pylab.ylim(STRIKE_HEIGHT)
    pylab.show()
        
    


        
BobGibson=Pitcher('Bob','Gibson',20,'Right','Right',98)
StanMusial=Batter('Stan','Musical',20,'Right','Right',94)
BadBatter=Batter('Bad','Batter',40,'Left','Left',40)
atBat(BobGibson,StanMusial)
##PitchCount=0

Result=False
while Result==False:
    PitchCount+=1
    print('Pitch',PitchCount)
    P=Pitch(BobGibson)
    S=Swing(BobGibson,P,StanMusial)
    if S.swingOrTake()==True:
        if S.swingContact()==True:
            print('Batter Swings Contact Made')
            Result=True
        else:
            print('Batter Swings and Misses')
