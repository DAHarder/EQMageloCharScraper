class CharacterInventory:
    def __init__(self, name=0, level=0, charClass=0,earsL=0, earsR=0, head=0, face=0, chest=0, neck=0, arms=0, back=0, waist=0, shoulders=0, wristsL=0, wristsR=0, legs=0, hands=0, charm=0, feet=0, fingerL=0, fingerR=0, rangeAmmo=0, primary=0, secondary=0, range=0, powersource=0, patterns=[]):
        self.name = name
        self.level = level
        self.charClass = charClass        
        self.earsL = earsL
        self.earsR = earsR
        self.head = head
        self.face = face
        self.chest = chest
        self.neck = neck
        self.arms = arms
        self.back = back
        self.waist = waist
        self.shoulders = shoulders
        self.wristsL = wristsL
        self.wristsR = wristsR
        self.legs = legs
        self.hands = hands
        self.charm = charm
        self.feet = feet
        self.fingerL = fingerL
        self.fingerR = fingerR
        self.rangeAmmo = rangeAmmo
        self.primary = primary
        self.secondary = secondary
        self.range = range
        self.powersource = powersource
        self.patterns=[] # Mold and pattern

    def printInventory(self):
        # print(vars(self))
        printTemp = vars(self)
        for item in printTemp:
            print(item, ':', printTemp[item])
        