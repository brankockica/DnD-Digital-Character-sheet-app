import PySimpleGUI as sg   #pip install pysimplegui
from pathlib import Path
import random
import os
#import json

#[sg.Spin(values=[i for i in range(1, 1000)], initial_value=20)]
POCETNO = 10
NAME_SIZE = 12
NAMEE_SIZE = 13
def name(name):                         ### PORAVNANJE 
    dots = NAME_SIZE-len(name)
    return sg.Text(name + ' ' + ' '*dots, size=(NAME_SIZE,1), justification='l',pad=(3,0), font='Helvetica 13')
def namee(name):
    dots = NAMEE_SIZE-len(name)
    return sg.Text(name + ' ' + ' '*dots, size=(NAMEE_SIZE,1), justification='l', font='Helvetica 9')


#print(f"{text}")       proba umesto name()
#print(f"{text:#<20}")
#print(f"{text:_>20}")
#print(f"{textL.^20}")

def popup(filename):

    layout = [
         
        [sg.Image(filename=filename, expand_x=True)],        
    ]

    window = sg.Window("Ok", layout, keep_on_top=True, modal=True)
    while True:
               event, values = window.read()
               if event == "Exit" or event == sg.WIN_CLOSED:
                    break

def open_journal():
     layout = [
          [sg.T("New Window", key="docName"), sg.Push(), sg.B("Open", key="jOPEN"),sg.B("Save", key="jSAVE")],
          [sg.Multiline(key="jTEXT", size=(55,30))]
          ]
     window = sg.Window("Journal", layout, modal=False)
     choice = None
     while True:
               event, values = window.read()
               if event == "Exit" or event == sg.WIN_CLOSED:
                    break
               if event == "jOPEN":
                    file_path = sg.popup_get_file("open", no_window=True)
                    if file_path:
                         file = Path(file_path)
                         window["jTEXT"](file.read_text())
                         window["docName"](file_path.split("/")[-1])
               if event == "jSAVE":
                    file_path = sg.popup_get_file("Save as", no_window=True, save_as=True) + ".txt"
                    file = Path(file_path)
                    file.write_text(values["jTEXT"])
                    window["docName"](file_path.split("/")[-1])

                    
     window.close()

def open_Roll():
     layout = [
          [    sg.B("Roll d20", key="r20",size=(7,3)),
               sg.Frame("", [[sg.B("Roll d12", key="r12")],[sg.Spin(values=[i for i in range(1, 15)], key="n12", size=(3,1), change_submits=True)]], element_justification='center'),
               sg.Frame("", [[sg.B("Roll d10", key="r10")],[sg.Spin(values=[i for i in range(1, 15)], key="n10", size=(3,1), change_submits=True)]], element_justification="center"),
               sg.Frame("", [[sg.B("Roll d8", key="r8")],[sg.Spin(values=[i for i in range(1, 30)], key="n8", size=(3,1), change_submits=True)]], element_justification="center"),
               sg.Frame("", [[sg.B("Roll d6", key="r6")],[sg.Spin(values=[i for i in range(1, 30)], key="n6", size=(3,1), change_submits=True)]], element_justification="center"),
               sg.Frame("", [[sg.B("Roll d4", key="r4")],[sg.Spin(values=[i for i in range(1, 30)], key="n4", size=(3,1), change_submits=True)]], element_justification="center"),
           ],
          [    sg.B("Roll d100", key="r100",size=(7,3)),
               sg.B("Toss a coin", key="rCoin",size=(9,3)),          
          ],
          [sg.VPush()],
          [sg.Multiline(key="rTEXT", size=(40,10), autoscroll = True), sg.B("Clear", key="Clear",size=(16,9))]
          ]
     window = sg.Window("ROLL!", layout, size=(480,300), modal=False)
     choice = None
     while True:
               event, values = window.read()
               if event == "Exit" or event == sg.WIN_CLOSED:
                    break
               
               roll20 = random.randint(1, 20)
               roll100 = random.randint(1,100)
               tossCoin = random.choice(["Heads", "Tails"])          
               roll12 = [random.randint(1, 12) for _ in range(values["n12"])]
               roll12_sum = sum(roll12)
               roll10 = [random.randint(1, 10) for _ in range(values["n10"])]
               roll10_sum = sum(roll10)
               roll8 = [random.randint(1, 8) for _ in range(values["n8"])]
               roll8_sum = sum(roll8)
               roll6 = [random.randint(1, 6) for _ in range(values["n6"])]
               roll6_sum = sum(roll6)
               roll4 = [random.randint(1, 4) for _ in range(values["n4"])]
               roll4_sum = sum(roll4)
               rTEXT = window["rTEXT"]
               
               if event == "Clear":
                    window["rTEXT"]("")
               if event == "rCoin":
                    window["rTEXT"](rTEXT.get()+"\n" + "- You got " + str(tossCoin) + " ! ")
               if event == "r20":
                    window["rTEXT"](rTEXT.get()+"\n" + "- You rolled a " + str(roll20) + " ! ")
               if event == "r100":
                    window["rTEXT"](rTEXT.get()+"\n" + "- You rolled a " + str(roll100) + " ! ")
               if event == "r12":
                    window["rTEXT"](rTEXT.get()+"\n" + "- You rolled these " + str(roll12) + "\n" + "- Total " + str(roll12_sum) + " ! ")
               if event == "r10":
                    window["rTEXT"](rTEXT.get()+"\n" + "- You rolled these " + str(roll10) + "\n" + "- Total " + str(roll10_sum) + " ! ")
               if event == "r8":
                    window["rTEXT"](rTEXT.get()+"\n" + "- You rolled these " + str(roll8) + "\n" + "- Total " + str(roll8_sum) + " ! ")
               if event == "r6":
                    window["rTEXT"](rTEXT.get()+"\n" + "- You rolled these " + str(roll6) + "\n" + "- Total " + str(roll6_sum) + " ! ")
               if event == "r4":
                    window["rTEXT"](rTEXT.get()+"\n" + "- You rolled these " + str(roll4) + "\n" + "- Total " + str(roll4_sum) + " ! ")
               
character = [sg.TabGroup([
                [sg.Tab('General',[
                    [sg.Frame("Character", [
                              [namee("Character name"),sg.I(size=(28,1))],
                              [namee("Background"),sg.I(size=(20,1))],
                              [namee("Race"),sg.I(size=(20,1))],
                              [namee("Alignment"),sg.OptionMenu(["Lawful good","Neutral good","Chaotic good","Lawful neutral","True neutral","Chaotic neutral","Lawfull evil","Neutral evil","Chaotic evil"],s=(20,1))],                            
                              [namee("Player name"),sg.I(size=(28,1))],
                              ],size=(343,165)),
                         ],
                         [sg.Col([
                              [sg.Frame("Class & level", [
                                   [sg.OptionMenu(["Artificer","Barbarian", "Bard","Blood Hunter", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"]),sg.Spin(values=[i for i in range(1, 21)], key="LVL", size=(3,1), change_submits=True)],
                                   [sg.T("        Class              "),sg.T("LVL")],
                                   ],pad=(0,0))
                              ],
                         ]),
                         sg.Col([
                              [sg.Frame("Money", [
                                   [sg.I(size=(3,1)),sg.I(size=(3,1)),sg.I(size=(3,1)),sg.I(size=(3,1)),],
                                   [sg.T(" Pp    Gp     Sp     Cp  "),],
                                   ],pad=(0,0))
                              ],
                         ]),
                         ],
                         [#sg.Button("Journal", key="journalB",size=(24,2)),
                          #sg.Button("Spells", key="spellsB",size=(15,2)),
                          sg.Button("Roll!", key="attackB",size=(49,2))
                         ],
                         [sg.Frame("", [
                              [sg.T("Items")],
                              [sg.Multiline(size=(24,6),)]
                              ]),
                         sg.Frame("", [
                              [sg.T("Equiped")],
                              [sg.Multiline(size=(24,6), )]
                              ])
                         ],
                         [sg.Frame("", [
                              [sg.T("Other proficiencies")],
                              [sg.Multiline(size=(24,6), )]
                              ]),
                         sg.Frame("", [
                              [sg.T("Languages")],
                              [sg.Multiline(size=(24,6), )]
                              ])
                         ],
                         [sg.Frame("", [
                              [sg.T("Features&Traits")],
                              [sg.Multiline(size=(24,6), )]
                              ]),
                         sg.Frame("", [
                              [sg.T("Status effects")],
                              [sg.Multiline(size=(24,6), )]
                              ])
                         ],
                    ]), 

                sg.Tab('Character', [
                    [sg.Frame("Character", [
                              [sg.Push(),sg.T("Age "),sg.I(size=(10,1)),
                               sg.T("Height"),sg.I(size=(10,1)),
                               sg.T("Weight"),sg.I(size=(10,1)),sg.Push(),],
                              [sg.Push(),sg.T("Eyes"),sg.I(size=(10,1)),                            
                               sg.T("Skin  "),sg.I(size=(10,1)),
                               sg.T("Hair     "),sg.I(size=(10,1)),sg.Push(),],
                              ],size=(400,80)),
                         ],
                    [sg.Frame("", [
                              [sg.T("Personality Traits")],
                              [sg.Multiline(size=(23,8),)]
                              ]),
                    sg.Frame("", [
                              [sg.T("Ideals")],
                              [sg.Multiline(size=(23,8),)]
                              ])
                         ],
                    [sg.Frame("", [
                              [sg.T("Bonds")],
                              [sg.Multiline(size=(23,8),)]
                              ]),
                    sg.Frame("", [
                              [sg.T("Flaws")],
                              [sg.Multiline(size=(23,8),)]
                              ])
                         ],
                    [sg.Frame("", [
                              [sg.T("Character Backstory")],
                              [sg.Multiline(size=(52,8),)]
                              ]),
                         ],
                    [sg.Frame("", [
                              [sg.T("Notes")],
                              [sg.Multiline(size=(52,8),)]
                              ]),
                         ],
                    
                    ]),
                sg.Tab('Spell Book', [
                    [sg.Frame("Character", [
                              [sg.T("Spellcastign Class"),sg.I(size=(12,1)),
                               sg.T("Spellcasting ability "),sg.I(size=(3,1)),
                               ],
                              [sg.T("Spell Save DC"),sg.I(size=(3,1), p=(0,0)),                            
                               sg.T("Spell Att. mod."),sg.I(size=(3,1), p=(0,0)),
                               sg.T("Prepared spells"),sg.I(size=(3,1), p=(0,0))],
                              ],size=(400,80)),
                         ],
                    [sg.Frame("", [
                              [sg.T("0. Cantrips")],
                              [sg.Multiline(size=(23,6),)]
                              ]),
                    sg.Frame("", [
                              [sg.T("1. Total / Expended"),sg.I("    / ",size=(6,1), p=(0,0))],
                              [sg.Multiline(size=(23,6),)]
                              ])
                         ],
                    [sg.Frame("", [
                              [sg.T("2. Total / Expended"), sg.I("    / ",size=(6,1), p=(0,0))],
                              [sg.Multiline(size=(23,6),)]
                              ]),
                    sg.Frame("", [
                              [sg.T("3. Total / Expended"),sg.I("    / ",size=(6,1), p=(0,0))],
                              [sg.Multiline(size=(23,6),)]
                              ])
                         ],
                    [sg.Frame("", [
                              [sg.T("4. Total / Expended"), sg.I("    / ",size=(6,1), p=(0,0))],
                              [sg.Multiline(size=(23,6),)]
                              ]),
                    sg.Frame("", [
                              [sg.T("5. Total / Expended"),sg.I("    / ",size=(6,1), p=(0,0))],
                              [sg.Multiline(size=(23,6),)]
                              ])
                         ],
                    [sg.Frame("", [
                              [sg.T("6. Total / Expended"), sg.I("    / ",size=(6,1), p=(0,0))],
                              [sg.Multiline(size=(23,5),)]
                              ]),
                    sg.Frame("", [
                              [sg.T("7. Total / Expended"),sg.I("    / ",size=(6,1), p=(0,0))],
                              [sg.Multiline(size=(23,5),)]
                              ])
                         ],
                    [sg.Frame("", [
                              [sg.T("8. Total / Expended"), sg.I("    / ",size=(6,1), p=(0,0))],
                              [sg.Multiline(size=(23,4),)]
                              ]),
                    sg.Frame("", [
                              [sg.T("9. Total / Expended"),sg.I("    / ",size=(6,1), p=(0,0))],
                              [sg.Multiline(size=(23,4),)]
                              ])
                         ],
                    ]),
                sg.Tab('Journal', [
                         
                              [sg.T("New Window", key="docName"), sg.Push(), sg.B("Open", key="jOPEN"),sg.B("Save", key="jSAVE")],
                              [sg.Multiline(key="jTEXT", size=(55,25))],
                              [sg.Frame("", [
                                   [sg.Image(key="getPicture")],
                                        ], size=(400,280), element_justification="center"),
                              ],
                              [sg.Button("Upload Picture", key="Picture",size=(20,1))],
                              
                    
                    ])         
                ]
            ]),  
        ],           
            
layout_top = [sg.Frame("", [
               [sg.Col([[sg.Frame('PROFICIENCY \n BONUS', [
                    [sg.T("+"), sg.I(2, key=("ProfB"), size=(3,1), change_submits=True)],              
                    ], element_justification="center")],]),
              sg.Col([[sg.Frame('ARMOR \n CLASS', [
                    [sg.I("", font='Helvetica 10', size=(5,2))],                           
                    ], element_justification="center")],]), 
              sg.Col([[sg.Frame('  HITPOINTS', [
                    [sg.I("", font='Helvetica 10', size=(5,2))],            
                    [sg.T("Max"),sg.I("", font='Helvetica 10', size=(5,2))],
                    [sg.T("Temp"),sg.I("", font='Helvetica 10', size=(5,2))],               
                    ], element_justification="right")],]), 
              sg.Col([[sg.Frame('   DEATH SAVES', [
                    [sg.Checkbox("",p=0),sg.Checkbox("",p=0),sg.Checkbox("Success", p=0)],
                    [sg.Checkbox("",p=0),sg.Checkbox("",p=0),sg.Checkbox("Failure   ", p=0)],                
                    ], element_justification="right")],]), 
              sg.Col([[sg.Frame('INITIATIVE', [
                    [sg.T("+"), sg.T("", key=("INI"))],             
                    ], element_justification="center")],]),
               sg.Col([[sg.Frame('SPEED', [
                    [sg.I(size=(3,2)),sg.T("ft.")],             
                    ], element_justification="center")],]),
               sg.Col([[sg.Frame('HIT DICE', [
                    [sg.I(size=(3,2)),sg.T("/"),sg.I(size=(3,2))],
                    [sg.T("d"),sg.I(size=(3,2))],             
                    ], element_justification="center")],]),
                    ],
               ],size=(800,120))]
               
layout_l = [
          [sg.Frame('Strength', [
               [name("Strength")],
               [sg.Spin(values=[i for i in range(1, 31)], key="STR", size=(3,1), initial_value=POCETNO, change_submits=True)],
               [sg.T("Modifier ", font='Helvetica 10'), sg.T(key="mSTR")],                 
               ])],
          [sg.Frame("Dexterity", [
               [name("Dexterity")],
               [sg.Spin(values=[i for i in range(1, 31)], key="DEX", size=(3,1), initial_value=POCETNO, change_submits=True)],
               [sg.T("Modifier ", font='Helvetica 10'), sg.T(key="mDEX")],                 
               ])],
          
          [sg.Frame("Constitution", [
               [name("Constitution")],
               [sg.Spin(values=[i for i in range(1, 31)], key="CON", size=(3,1), initial_value=POCETNO, change_submits=True)],
               [sg.T("Modifier ", font='Helvetica 10'), sg.T(key="mCON")],                 
               ])],
          [sg.Frame("Intelligence", [
               [name("Intelligence")],
               [sg.Spin(values=[i for i in range(1, 31)], key="INT", size=(3,1), initial_value=POCETNO, change_submits=True)],
               [sg.T("Modifier ", font='Helvetica 10'), sg.T(key="mINT")],                 
               ])],
          [sg.Frame("Wisdom", [
               [name("Wisdom")],
               [sg.Spin(values=[i for i in range(1, 31)], key="WIS", size=(3,1), initial_value=POCETNO, change_submits=True)],
               [sg.T("Modifier ", font='Helvetica 10'), sg.T(key="mWIS")],                 
               ])],
          [sg.Frame("Charisma", [
               [name("Charisma")],
               [sg.Spin(values=[i for i in range(1, 31)], key="CHA", size=(3,1), initial_value=POCETNO, change_submits=True)],
               [sg.T("Modifier ", font='Helvetica 10'), sg.T(key="mCHA")],                 
               ])],
          
          
          [sg.OK(key="Ok", size=(14,8))],
          
          [sg.T("Made by Bane")]
          ]

layout_r = [
               [sg.Frame('Strength',  [
                    [namee("STR save"), sg.Checkbox("●", key="pcStr", enable_events=True, p=0), sg.T(key="sSTR",p=0)],
                    [namee("Athletics "), sg.Checkbox("●", key="pcAth",enable_events=True, p=0), sg.Checkbox("♦", key="ecAth",enable_events=True, p=0),sg.T(key="sAth",p=0)],                        
                    ], size=(200,70))],
               [sg.Frame('Dexterity', [
                    [namee("DEX save"),sg.Checkbox("●", key="pcDex", enable_events=True, p=0), sg.T(key="sDEX",p=0)],
                    [namee("Acrobatics"),sg.Checkbox("●", key="pcAcr",enable_events=True, p=0), sg.Checkbox("♦", key="ecAcr",enable_events=True, p=0),sg.T(key="sAcr",p=0)],
                    [namee("Sleight of Hand"),sg.Checkbox("●", key="pcSoh",enable_events=True, p=0), sg.Checkbox("♦", key="ecSoh",enable_events=True, p=0),sg.T(key="sSoh",p=0)],
                    [namee("Stealth"),sg.Checkbox("●", key="pcSte",enable_events=True, p=0), sg.Checkbox("♦", key="ecSte",enable_events=True, p=0),sg.T(key="sSte",p=0)],     
                    ], size=(200,120))],
               [sg.Frame("Constitution", [
                    [namee("CON save"),sg.Checkbox("●", key="pcCon", enable_events=True, p=0), sg.T(key="sCON",p=0)],
                    ], size=(200,47))],
               [sg.Frame('Intelligence', [
                    [namee("INT save"),sg.Checkbox("●", key="pcInt", enable_events=True, p=0), sg.T(key="sINT",p=0)],
                    [namee("Arcana"),sg.Checkbox("●", key="pcArc",enable_events=True, p=0), sg.Checkbox("♦", key="ecArc",enable_events=True, p=0),sg.T(key="sArc",p=0)],
                    [namee("History"),sg.Checkbox("●", key="pcHis",enable_events=True, p=0), sg.Checkbox("♦", key="ecHis",enable_events=True, p=0),sg.T(key="sHis",p=0)],
                    [namee("Investigation"),sg.Checkbox("●", key="pcInv",enable_events=True, p=0), sg.Checkbox("♦", key="ecInv",enable_events=True, p=0),sg.T(key="sInv",p=0)],     
                    [namee("Nature"),sg.Checkbox("●", key="pcNat",enable_events=True, p=0), sg.Checkbox("♦", key="ecNat",enable_events=True, p=0),sg.T(key="sNat",p=0)],
                    [namee("Religion"),sg.Checkbox("●", key="pcRel",enable_events=True, p=0), sg.Checkbox("♦", key="ecRel",enable_events=True, p=0),sg.T(key="sRel",p=0)],
                    ], size=(200,170))],
               [sg.Frame('Wisdom', [
                    [namee("WIS save"),sg.Checkbox("●", key="pcWis", enable_events=True, p=0), sg.T(key="sWIS",p=0)],
                    [namee("Animal Handling"),sg.Checkbox("●", key="pcAni",enable_events=True, p=0), sg.Checkbox("♦", key="ecAni",enable_events=True, p=0),sg.T(key="sAni",p=0)],
                    [namee("Insight"),sg.Checkbox("●", key="pcIns",enable_events=True, p=0), sg.Checkbox("♦", key="ecIns",enable_events=True, p=0),sg.T(key="sIns",p=0)],
                    [namee("Medicine"),sg.Checkbox("●", key="pcMed",enable_events=True, p=0), sg.Checkbox("♦", key="ecMed",enable_events=True, p=0),sg.T(key="sMed",p=0)],     
                    [namee("Perception"),sg.Checkbox("●", key="pcPer",enable_events=True, p=0), sg.Checkbox("♦", key="ecPer",enable_events=True, p=0),sg.T(key="sPer",p=0)],
                    [namee("Survival"),sg.Checkbox("●", key="pcSur",enable_events=True, p=0), sg.Checkbox("♦", key="ecSur",enable_events=True, p=0),sg.T(key="sSur",p=0)],
                    ], size=(200,170))],
               [sg.Frame('Charisma', [
                    [namee("CHR save"),sg.Checkbox("●", key="pcCha", enable_events=True, p=0), sg.T(key="sCHA",p=0)],
                    [namee("Deception"),sg.Checkbox("●", key="pcDec",enable_events=True, p=0), sg.Checkbox("♦", key="ecDec",enable_events=True, p=0),sg.T(key="sDec",p=0)],
                    [namee("Intimidation"),sg.Checkbox("●", key="pcIti",enable_events=True, p=0), sg.Checkbox("♦", key="ecIti",enable_events=True, p=0),sg.T(key="sIti",p=0)],
                    [namee("Performance"),sg.Checkbox("●", key="pcPrf",enable_events=True, p=0), sg.Checkbox("♦", key="ecPrf",enable_events=True, p=0),sg.T(key="sPrf",p=0)],     
                    [namee("Persuasion"),sg.Checkbox("●", key="pcPrs",enable_events=True, p=0), sg.Checkbox("♦", key="ecPrs",enable_events=True, p=0),sg.T(key="sPrs",p=0)],
                    ], size=(200,150))],
          
          
          

          ]
menu_layout =[["File",["Open","Save","---","Exit"]]]

layout = [[sg.Menu(menu_layout, key="menu")],[layout_top], [sg.HSep()],
          [sg.Col(layout_l, p=0, vertical_alignment="top"), sg.VSep(), sg.Col(layout_r, p=0), sg.VSep(), sg.Col(character, vertical_alignment="top")]
          ]

sz = POCETNO
window = sg.Window("DnD", layout, finalize=True, size = (820,950))

while True:
    
     event, values = window.read()
     if event == sg.WIN_CLOSED or event == "Exit":        
          break
     
     lvl = int(values["LVL"])
          
     checkpSTR = [
                    (values["pcStr"]),
                    ((values["pcAth"]),(values["ecAth"])),                             
                    ]
     checkpDEX = [
                    (values["pcDex"]),
                    ((values["pcAcr"]),(values["ecAcr"])),
                    ((values["pcSoh"]),(values["ecSoh"])),
                    ((values["pcSte"]),(values["ecSte"])),                
                    ]
     checkpCON = [(values["pcCon"])]
     checkpINT = [
                    (values["pcInt"]),
                    ((values["pcArc"]),(values["ecArc"])),
                    ((values["pcHis"]),(values["ecHis"])),
                    ((values["pcInv"]),(values["ecInv"])),
                    ((values["pcNat"]),(values["ecNat"])),
                    ((values["pcRel"]),(values["ecRel"])),
                    ]
     checkpWIS = [
                    (values["pcWis"]),
                    ((values["pcAni"]),(values["ecAni"])),
                    ((values["pcIns"]),(values["ecIns"])),
                    ((values["pcMed"]),(values["ecMed"])),
                    ((values["pcPer"]),(values["ecPer"])),
                    ((values["pcSur"]),(values["ecSur"])),
                    ]
     checkpCHA = [
                    (values["pcCha"]),
                    ((values["pcDec"]),(values["ecDec"])),
                    ((values["pcIti"]),(values["ecIti"])),
                    ((values["pcPrf"]),(values["ecPrf"])),
                    ((values["pcPrs"]),(values["ecPrs"])),                
                    ]
     atr = [
               (int(values["STR"])),
               (int(values["DEX"])),
               (int(values["CON"])),
               (int(values["INT"])),
               (int(values["WIS"])),
               (int(values["CHA"])),                
               ]
     mod = [
               ((int(values["STR"]) - 10) // 2),
               ((int(values["DEX"]) - 10) // 2),
               ((int(values["CON"]) - 10) // 2),
               ((int(values["INT"]) - 10) // 2),
               ((int(values["WIS"]) - 10) // 2),
               ((int(values["CHA"]) - 10) // 2),
               ]
     STRcks = ["sSTR","sAth",]
     DEXcks = ["sDEX","sAcr","sSoh","sSte",]
     CONcks = ["sCON",]
     INTcks = ["sINT","sArc","sHis","sInv","sNat","sRel"]
     WIScks = ["sWIS","sAni","sIns","sMed","sPer","sSur"]
     CHAcks = ["sCHA","sDec","sIti","sPrf","sPrs"]
     
     pb = int(values["ProfB"]) #+ mod[0]                
          
     sz = atr if atr != POCETNO else mod        #INSTANT UPDATE na klik ? black magick
     if sz != POCETNO:
               POCETNO = sz                
               #window['STR'].update(sz)           #MODIFIER UPDATE
               window["mSTR"].update(mod[0])
               window["mDEX"].update(mod[1])
               window["mCON"].update(mod[2])
               window["mINT"].update(mod[3])
               window["mWIS"].update(mod[4])
               window["mCHA"].update(mod[5])
               window["INI"].update(mod[1])           
     if event == "Open":
                    file_path = sg.popup_get_file("open", no_window=True)
                    if file_path:
                         file = Path(file_path)
                         loaded = file.read_text()     #Treba podeliti keys and values unutar Loaded
                         loaded_dict = eval(loaded)    #eval sluzi da prebaci str u dict !!!!
                         del loaded_dict["menu"]
                         for key in loaded_dict:  
                         #print(type(loaded_dict))
                              window[key](loaded_dict[key]) ## Kako uploadovati sve windowse sa svojim values
                         
     if event == "Save":
                    file_path = sg.popup_get_file("Save as", no_window=True, save_as=True) + ".txt"
                    file = Path(file_path)
                    file.write_text(str(values))
                         
     if event == "Picture":                      ## Slika u Journalu
          file_path = sg.popup_get_file("open", no_window=True)
          if file_path:
               file = Path(file_path)
               window["getPicture"](filename=file)
               
     
     if lvl >= 17:                           #PROF BONUS po LVLu
          window["ProfB"].update(6)
     elif lvl >= 13:
          window["ProfB"].update(5)
     elif lvl >= 9:
          window["ProfB"].update(4)
     elif lvl >= 5:
          window["ProfB"].update(3)
     else :
          window["ProfB"].update(2)      #Mozemo da se otarasimo .update i da ostane samo ( )
     

     if event == "attackB":
          open_Roll()
          
     if event == "Ok":                                 # POPUP OK SAITAMA!
          popup(os.path.dirname(__file__)+"/OK.gif")
     
     
     if event == "jOPEN":                      ## event for JOURNAL
          file_path = sg.popup_get_file("open", no_window=True)
          if file_path:
               file = Path(file_path)
               window["jTEXT"](file.read_text())
               window["docName"](file_path.split("/")[-1])
          if event == "jSAVE":
               file_path = sg.popup_get_file("Save as", no_window=True, save_as=True) + ".txt"
               file = Path(file_path)
               file.write_text(values["jTEXT"])
               window["docName"](file_path.split("/")[-1])
     
     if checkpSTR[0] == True:                # STRENGTH
          window[STRcks[0]](pb + mod[0])
     else: window[STRcks[0]](mod[0])
     if checkpSTR[1] == (True,True):
          window[STRcks[1]](pb*2 + mod[0])
     elif checkpSTR[1] == (True,False):
          window[STRcks[1]](pb + mod[0])
     else: window[STRcks[1]](mod[0])

     if checkpDEX[0] == True:                #DEXTERITY
          window[DEXcks[0]](pb + mod[1])
     else: window[DEXcks[0]](mod[1])
     if checkpDEX[1] == (True,True):
          window[DEXcks[1]](pb*2 + mod[1])
     elif checkpDEX[1] == (True,False):
          window[DEXcks[1]](pb + mod[1])
     else: window[DEXcks[1]](mod[1])
     if checkpDEX[2] == (True,True):
          window[DEXcks[2]](pb*2 + mod[1])
     elif checkpDEX[2] == (True,False):
          window[DEXcks[2]](pb + mod[1])
     else: window[DEXcks[2]](mod[1])
     if checkpDEX[3] == (True,True):
          window[DEXcks[3]](pb*2 + mod[1])
     elif checkpDEX[3] == (True,False):
          window[DEXcks[3]](pb + mod[1])
     else: window[DEXcks[3]](mod[1])

     if checkpCON[0] == True:                # CONSTITUTION
          window[CONcks[0]](pb + mod[2])
     else: window[CONcks[0]](mod[2])

     if checkpINT[0] == True:                #INTELLIGENCE
          window[INTcks[0]](pb + mod[3])
     else: window[INTcks[0]](mod[3])
     if checkpINT[1] == (True,True):
          window[INTcks[1]](pb*2 + mod[3])
     elif checkpINT[1] == (True,False):
          window[INTcks[1]](pb + mod[3])
     else: window[INTcks[1]](mod[3])
     if checkpINT[2] == (True,True):
          window[INTcks[2]](pb*2 + mod[3])
     elif checkpINT[2] == (True,False):
          window[INTcks[2]](pb + mod[3])
     else: window[INTcks[2]](mod[3])
     if checkpINT[3] == (True,True):
          window[INTcks[3]](pb*2 + mod[3])
     elif checkpINT[3] == (True,False):
          window[INTcks[3]](pb + mod[3])
     else: window[INTcks[3]](mod[3])
     if checkpINT[4] == (True,True):
          window[INTcks[4]](pb*2 + mod[3])
     elif checkpINT[4] == (True,False):
          window[INTcks[4]](pb + mod[3])
     else: window[INTcks[4]](mod[3])
     if checkpINT[5] == (True,True):
          window[INTcks[5]](pb*2 + mod[3])
     elif checkpINT[5] == (True,False):
          window[INTcks[5]](pb + mod[3])
     else: window[INTcks[5]](mod[3])

     if checkpWIS[0] == True:                #WISDOM
          window[WIScks[0]](pb + mod[4])
     else: window[WIScks[0]](mod[4])
     if checkpWIS[1] == (True,True):
          window[WIScks[1]](pb*2 + mod[4])
     elif checkpWIS[1] == (True,False):
          window[WIScks[1]](pb + mod[4])
     else: window[WIScks[1]](mod[4])
     if checkpWIS[2] == (True,True):
          window[WIScks[2]](pb*2 + mod[4])
     elif checkpWIS[2] == (True,False):
          window[WIScks[2]](pb + mod[4])
     else: window[WIScks[2]](mod[4])
     if checkpWIS[3] == (True,True):
          window[WIScks[3]](pb*2 + mod[4])
     elif checkpWIS[3] == (True,False):
          window[WIScks[3]](pb + mod[4])
     else: window[WIScks[3]](mod[4])
     if checkpWIS[4] == (True,True):
          window[WIScks[4]](pb*2 + mod[4])
     elif checkpWIS[4] == (True,False):
          window[WIScks[4]](pb + mod[4])
     else: window[WIScks[4]](mod[4])
     if checkpWIS[5] == (True,True):
          window[WIScks[5]](pb*2 + mod[4])
     elif checkpWIS[5] == (True,False):
          window[WIScks[5]](pb + mod[4])
     else: window[WIScks[5]](mod[4])

     if checkpCHA[0] == True:                #CHARISMA
          window[CHAcks[0]](pb + mod[5])
     else: window[CHAcks[0]](mod[5])
     if checkpCHA[1] == (True,True):
          window[CHAcks[1]](pb*2 + mod[5])
     elif checkpCHA[1] == (True,False):
          window[CHAcks[1]](pb + mod[5])
     else: window[CHAcks[1]](mod[5])
     if checkpCHA[2] == (True,True):
          window[CHAcks[2]](pb*2 + mod[5])
     elif checkpCHA[2] == (True,False):
          window[CHAcks[2]](pb + mod[5])
     else: window[CHAcks[2]](mod[5])
     if checkpCHA[3] == (True,True):
          window[CHAcks[3]](pb*2 + mod[5])
     elif checkpCHA[3] == (True,False):
          window[CHAcks[3]](pb + mod[5])
     else: window[CHAcks[3]](mod[5])
     if checkpCHA[4] == (True,True):
          window[CHAcks[4]](pb*2 + mod[5])
     elif checkpCHA[4] == (True,False):
          window[CHAcks[4]](pb + mod[5])
     else: window[CHAcks[4]](mod[5])
      
window.close()


