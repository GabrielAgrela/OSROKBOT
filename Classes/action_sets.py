from Actions.find_and_click_image_action import FindAndClickImageAction
from Actions.soft_find_and_click_image_action import SoftFindAndClickImageAction
from Actions.press_key_action import PressKeyAction
from Actions.find_image_action import FindImageAction
from Actions.manual_click_action import ManualClickAction
from Actions.manual_scroll_action import ManualScrollAction
from Actions.conditional_action import ConditionalAction
from Actions.manual_sleep_action import ManualSleepAction
from Actions.email_action import EmailAction
from Actions.extract_text_action import ExtractTextAction
from Actions.screenshot_action import ScreenshotAction
from Actions.chatgpt_action import ChatGPTAction
from manual_click import ManualClick
from email_handler import EmailHandler
from state_machine import StateMachine

class ActionSets:
    def __init__(self):
        self.manual_click = ManualClick()
        self.email_handler = EmailHandler("fdsfsdfsrfwefes@proton.me", "fdsfsADDA1235+")
        self.machine = StateMachine()
    
    def scout_explore(self):
        
        
        self.machine.add_state("state1", FindAndClickImageAction('Media/explorenight.png', offset_y=25, check=False), "state2", "failure_state")
        self.machine.add_state("state2", FindAndClickImageAction('Media/explore.png', offset_y=25), "state3", "failure_state")
        self.machine.add_state("state3", FindAndClickImageAction('Media/exploreicon.png',delay=.2,check=False), "state4", "failure_state")
        self.machine.add_state("state4", FindAndClickImageAction('Media/exploreaction.png',delay=.1,check=False), "state5", "failure_state")
        self.machine.add_state("state5", FindAndClickImageAction('Media/exploreaction.png',delay=1.5,check=False), "state6", "failure_state")
        self.machine.add_state("state6", FindAndClickImageAction('Media/sendaction.png',delay=.5, retard=1), "state7", "failure_state")
        self.machine.add_state("state7", PressKeyAction('space'), None, "failure_state")
        self.machine.set_initial_state("state1")

        return self.machine
    
    def farm_barb (self):

        self.machine.add_state("cityview", PressKeyAction('space'), "birdview","cityview")
        self.machine.add_state("birdview", PressKeyAction('f'), "barbland","cityview")
        self.machine.add_state("barbland", FindAndClickImageAction('Media/barbland.png'), "searchaction","birdview")
        self.machine.add_state("searchaction", FindAndClickImageAction('Media/searchaction.png'), "arrow","barbland")
        self.machine.add_state("arrow", FindAndClickImageAction('Media/arrow.png', offset_y=80), "attackaction","searchaction")
        self.machine.add_state("attackaction", FindAndClickImageAction('Media/attackaction.png'), "lohar","attackaction")
        self.machine.add_state("lohar", FindAndClickImageAction('Media/lohar.png'), "smallmarchaction","newtroopaction")
        self.machine.add_state("newtroopaction", FindAndClickImageAction('Media/newtroopaction.png'), "marchaction","newtroopaction")
        self.machine.add_state("marchaction", FindAndClickImageAction('Media/marchaction.png'), "victory","marchaction")
        self.machine.add_state("smallmarchaction", FindAndClickImageAction('Media/smallmarchaction.png'), "victory","smallmarchaction")
        self.machine.add_state("victory", FindImageAction('Media/victory.png'), "birdview","victory")
        self.machine.set_initial_state("cityview")
        return self.machine

    def pick_rss():
        return [
            FindAndClickImageAction('Media/wood.png'),
            FindAndClickImageAction('Media/corn.png'),
            FindAndClickImageAction('Media/rock.png'),
        ]
    
    def help_alliance(): 
        return [
        FindAndClickImageAction('Media/alliancehelp.png', offset_y=10),
    ]

    def cure_troops ():
        return [
        FindAndClickImageAction('Media/curetroops.png'),
        FindAndClickImageAction('Media/healaction.png'),
    ]

    def pickup_cured_troops ():
        return [
        FindAndClickImageAction('Media/pickuptroopscured.png'),
    ]

    def farm_crop ():
        return [
        FindImageAction('Media/isgathering.png',check=False, dont_find=True),
        FindImageAction('Media/isreturning.png',check=False, dont_find=True),
        FindImageAction('Media/isgoing.png',check=False, dont_find=True),
        PressKeyAction('space'),
        PressKeyAction('f'),
        FindAndClickImageAction('Media/cropland.png'),
        FindAndClickImageAction('Media/searchaction.png'),
        ManualClickAction(),
        FindAndClickImageAction('Media/gatheraction.png'),
        FindAndClickImageAction('Media/newtroopaction.png'),
        FindAndClickImageAction('Media/marchaction.png'),
        PressKeyAction('space'), 
    ] 

    def farm_wood ():
        return [
        FindImageAction('Media/isgathering.png', dont_find=True),
        FindImageAction('Media/isreturning.png', dont_find=True),
        FindImageAction('Media/isgoing.png', dont_find=True),
        PressKeyAction('space'),
        PressKeyAction('f'),
        FindAndClickImageAction('Media/woodland.png'),
        FindAndClickImageAction('Media/searchaction.png'),
        ManualClickAction(),
        FindAndClickImageAction('Media/gatheraction.png'),
        FindAndClickImageAction('Media/newtroopaction.png'),
        FindAndClickImageAction('Media/marchaction.png'),
        PressKeyAction('space'), 
    ] 

   

    def train_inf ():
        return [
        FindAndClickImageAction('Media/infantryhouse.png'),
        FindAndClickImageAction('Media/traininfantry.png'),
        FindAndClickImageAction('Media/t1.png'),
        FindAndClickImageAction('Media/upgrade.png'),
        FindAndClickImageAction('Media/upgradeaction.png'),
        FindAndClickImageAction('Media/infantryhouse.png'),
        FindAndClickImageAction('Media/traininfantry.png'),
        FindAndClickImageAction('Media/speedupaction.png'),
        FindAndClickImageAction('Media/useaction.png'),
        FindAndClickImageAction('Media/spam.png'),
        FindAndClickImageAction('Media/useaction.png'),
        FindAndClickImageAction('Media/infantryhouse.png'),
    ]


    def reconnect ():
        return [
        FindAndClickImageAction('Media/confirm.png'),
    ]

    def explore_villages():
        return[
        PressKeyAction('z'),
        FindAndClickImageAction('Media/reportactive.png', check=False,delay=.2),
        FindAndClickImageAction('Media/report.png', check=False, offset_y=-10),
        ConditionalAction(
            primary_actions=
            [
                FindAndClickImageAction('Media/explorationreport.png', check=True,delay=.2),
                FindAndClickImageAction('Media/explorationreportactive.png', check=True),
            ],
                primary_subsequent_actions=
                [
                    ConditionalAction
                    (
                        primary_actions=
                        [
                            FindAndClickImageAction('Media/villagereport.png', offset_x=370,delay=.1),
                            FindAndClickImageAction('Media/barbreport.png', offset_x=370,retard=3),
                            FindAndClickImageAction('Media/barbreport2.png', offset_x=370,retard=3),
                            FindAndClickImageAction('Media/passreport.png', offset_x=370,retard=3),
                            FindAndClickImageAction('Media/holyreport.png', offset_x=370,retard=3),
                            
                        ],
                            primary_subsequent_actions=
                            [
                                ManualClickAction(50,54,delay=2),
                            ],
                            alternative_subsequent_actions=
                            [
                                FindAndClickImageAction('Media/reportbanner.png', check=False),
                                ManualScrollAction(15)
                            ],
                        retry_times=15  # retry up to 5 times
                    ),
                ],
                alternative_subsequent_actions=
                [
                    FindAndClickImageAction('Media/reportside.png'),
                    ManualScrollAction(y_scroll=15)
                ],
                retry_times=15  # retry up to 5 times
        ),
        PressKeyAction('space',delay=.1,retard=2),
    ]

    def captcha ():
        return [
        FindImageAction('Media/captcha.png'),
        EmailAction(email_handler, "100cabessa@gmail.com", "Rise of Kingdoms Captcha", " ")
    ]

    def lyceumS ():
        return [
        ScreenshotAction(33.5,75,38,50),
        ExtractTextAction(description= "Question: In rise of kingdoms, "),
        ScreenshotAction(33,52,45,51),
        ExtractTextAction(description= " A: ", aggregate=True),
        ScreenshotAction(57,74,45,51),
        ExtractTextAction(description= " B: ", aggregate=True),
        ScreenshotAction(33,52,54,60),
        ExtractTextAction(description= " C: ", aggregate=True),
        ScreenshotAction(57,74,54,60),
        ExtractTextAction(description= " D: ", aggregate=True),
        ChatGPTAction(),
    ]

    def lyceum (self):
        self.machine.add_state("sstittle",  ScreenshotAction(33.5,85,35,43), "ettitle")
        self.machine.add_state("ettitle", ExtractTextAction(description= " Question: In rise of kingdoms, "), "ssq1")
        self.machine.add_state("ssq1", ScreenshotAction(33,52,45,51,), "eq1")
        self.machine.add_state("eq1",ExtractTextAction(description= " A: ", aggregate=True), "ssq2")
        self.machine.add_state("ssq2", ScreenshotAction(57,74,45,51), "eq2")
        self.machine.add_state("eq2", ExtractTextAction(description= " B: ", aggregate=True), "ssq3")
        self.machine.add_state("ssq3",  ScreenshotAction(33,52,54,60), "eq3")
        self.machine.add_state("eq3", ExtractTextAction(description= " C: ", aggregate=True), "ssq4")
        self.machine.add_state("ssq4", ScreenshotAction(57,74,54,60), "eq4")
        self.machine.add_state("eq4", ExtractTextAction(description= " D: ", aggregate=True), "cgpt")
        self.machine.add_state("cgpt", ChatGPTAction(),"sstittle")
        self.machine.set_initial_state("sstittle")
        return self.machine

    def explore_caves():
        return[
    PressKeyAction('z'),
    ManualClickAction(26,5,delay=1),
    ConditionalAction
    (
        primary_actions=
        [
            FindAndClickImageAction('Media/explorationreport.png', check=True,delay=.1),
            FindAndClickImageAction('Media/explorationreportactive.png', check=True),
        ],
            primary_subsequent_actions=
            [
                ConditionalAction
                (
                    primary_actions=
                    [
                        FindAndClickImageAction('Media/caveexploring.png',delay=1, max_matches=3), 
                    ],
                        primary_subsequent_actions=
                        [
                            FindAndClickImageAction('Media/cavereport.png', offset_x=300, offset_y=20, delay=.2),
                            ManualClickAction(50,54,delay=2),
                            FindAndClickImageAction('Media/investigateaction.png',delay=1),
                            FindAndClickImageAction('Media/sendaction.png',delay=1),
                        ],
                        alternative_subsequent_actions=
                        [
                            PressKeyAction('esc'),
                        ],
                    retry_times=0  # retry up to 5 times
                ),
            ],
            alternative_subsequent_actions=
            [
                ManualClickAction(26,25,delay=1),
                ManualScrollAction(y_scroll=15)
            ],
            retry_times=15  # retry up to 5 times
    ),
    ]

    def pick_village():
        return[
        ManualScrollAction(y_scroll=150),
        FindAndClickImageAction('Media/house.png',delay=.5),
        FindAndClickImageAction('Media/village.png',delay=2),
    ]