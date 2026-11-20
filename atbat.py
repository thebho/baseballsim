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
    def __init__(self, firstName, lastName, throwingHand, battingHand, age, height, weight, position, team, jersey_number, experience_years):
        """
        battingHand='Left','Right','Switch'
        throwingHand='Left','Right'
        age: int (18-40)
        height: str (e.g. "6'2\"")
        weight: int (lbs, 150-260)
        position: str (e.g. "SP", "1B", "CF")
        team: str (e.g. "River Cats")
        jersey_number: int (1-99)
        experience_years: int (0-20)
        """
        self.firstName = str(firstName)
        self.lastName = str(lastName)
        self.name = self.firstName + " " + self.lastName
        self.throwingHand = throwingHand
        self.battingHand = battingHand
        self.age = age
        self.height = height
        self.weight = weight
        self.position = position
        self.team = team
        self.jersey_number = jersey_number
        self.experience_years = experience_years
    
    def __str__(self):
        """Returns a human-readable summary"""
        return f"#{self.jersey_number} {self.name} | {self.position} | {self.team} | Age: {self.age}"
    
    def __repr__(self):
        """Returns a developer-friendly representation"""
        return f"Player(name='{self.name}', position='{self.position}', team='{self.team}')"
    
    def get_info(self):
        """Returns a multi-line profile card with all base attributes"""
        info = f"""
========== PLAYER PROFILE ==========
Name:              {self.name}
Jersey Number:     #{self.jersey_number}
Position:          {self.position}
Team:              {self.team}
Age:               {self.age}
Height:            {self.height}
Weight:            {self.weight} lbs
Throwing Hand:     {self.throwingHand}
Batting Hand:      {self.battingHand}
Experience:        {self.experience_years} years
====================================
"""
        return info
    
class Pitcher(Player):
    """
    A MLB pitcher. Subclass of Player
    """
    def __init__(self, firstName, lastName, throwingHand, battingHand, age, height, weight, position, team, jersey_number, experience_years, stamina, accuracy, velocity, pitch_variety, wins=0, losses=0, era=0.0):
        """
        Creates a Pitcher Instance.
        stamina: int (30-99)
        accuracy: int (30-99)
        velocity: int (30-99, represents mph rating)
        pitch_variety: int (30-99)
        wins: int (default 0)
        losses: int (default 0)
        era: float (e.g. 1.50-6.50)
        """
        Player.__init__(self, firstName, lastName, throwingHand, battingHand, age, height, weight, position, team, jersey_number, experience_years)
        self.pitchDict = PITCH_DICT.copy()
        self.energy = 100
        self.stamina = stamina
        self.accuracy = accuracy
        self.velocity = velocity
        self.pitch_variety = pitch_variety
        self.wins = wins
        self.losses = losses
        self.era = era

    def getRating(self):
        """Returns pitcher's overall rating (average of key stats)"""
        return int((self.stamina + self.accuracy + self.velocity + self.pitch_variety) / 4)
    
    def get_stats(self):
        """Returns a formatted string showing all pitching stats"""
        stats = f"""
========== PITCHER STATS ==========
Name:              {self.name}
Position:          {self.position}
Stamina:           {self.stamina}
Accuracy:          {self.accuracy}
Velocity:          {self.velocity} mph
Pitch Variety:     {self.pitch_variety}
Wins:              {self.wins}
Losses:            {self.losses}
ERA:               {self.era:.2f}
Overall Rating:    {self.getRating()}
===================================
"""
        return stats
    
    def reduce_energy(self, amount):
        """Subtracts amount from stamina, flooring at 0"""
        self.stamina = max(0, self.stamina - amount)

class Batter(Player):
    """
    A MLB batter. Subclass of Player
    """
    def __init__(self, firstName, lastName, throwingHand, battingHand, age, height, weight, position, team, jersey_number, experience_years, power, speed, plate_discipline, home_runs=0, hits=0, strikeouts=0, batting_average=0.0):
        """
        Creates a Batter Instance.
        power: int (30-99)
        speed: int (30-99)
        plate_discipline: int (30-99)
        home_runs: int (default 0)
        hits: int (default 0)
        strikeouts: int (default 0)
        batting_average: float (e.g. 0.180-0.350)
        """
        Player.__init__(self, firstName, lastName, throwingHand, battingHand, age, height, weight, position, team, jersey_number, experience_years)
        self.power = power
        self.speed = speed
        self.plate_discipline = plate_discipline
        self.home_runs = home_runs
        self.hits = hits
        self.strikeouts = strikeouts
        self.batting_average = batting_average

    def getRating(self):
        """Returns batter's overall rating (average of key stats)"""
        return int((self.power + self.speed + self.plate_discipline) / 3)
    
    def get_stats(self):
        """Returns a formatted string showing all batting stats"""
        stats = f"""
========== BATTER STATS ==========
Name:              {self.name}
Position:          {self.position}
Power:             {self.power}
Speed:             {self.speed}
Plate Discipline:  {self.plate_discipline}
Home Runs:         {self.home_runs}
Hits:              {self.hits}
Strikeouts:        {self.strikeouts}
Batting Average:   {self.batting_average:.3f}
Overall Rating:    {self.getRating()}
==================================
"""
        return stats
    
    def update_stats(self, hit=False, home_run=False, strikeout=False):
        """Increments appropriate counters and recalculates batting_average"""
        if home_run:
            self.home_runs += 1
            self.hits += 1
        elif hit:
            self.hits += 1
        
        if strikeout:
            self.strikeouts += 1
        
        # Recalculate batting average
        denominator = self.hits + self.strikeouts
        if denominator > 0:
            self.batting_average = self.hits / denominator
        else:
            self.batting_average = 0.0

   ### Temporary classes ###

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
        
    


        
BobGibson=Pitcher('Bob','Gibson','Right','Right',42,"6'1\"",195,'SP','River Cats',42,15,92,88,94,87,251,174,2.91)
StanMusial=Batter('Stan','Musial','Right','Right',42,"6'0\"",200,'RF','River Cats',6,22,89,72,91,475,3630,1311,0.330)
BadBatter=Batter('Bad','Batter','Left','Left',40,"5'8\"",160,'DH','River Cats',99,5,35,25,30,5,45,120,0.273)
# atBat(BobGibson,StanMusial)
##PitchCount=0

# Result=False
# while Result==False:
#     PitchCount+=1
#     print('Pitch',PitchCount)
#     P=Pitch(BobGibson)
#     S=Swing(BobGibson,P,StanMusial)
#     if S.swingOrTake()==True:
#         if S.swingContact()==True:
#             print('Batter Swings Contact Made')
#             Result=True
#         else:
#             print('Batter Swings and Misses')
