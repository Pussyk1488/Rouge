







image Test_Overlay:
    "images/screenshot0021.png"
    alpha 0.1


image Mega_Mask:

    contains:
        Solid("#159457", xysize=(2350,2350))



        alpha .5
        pos (200,0)
































































































































































label Failsafe:
    if "Player" not in globals().keys():

        $ Player = PlayerClass()
    $ Player.Name =     Playername if "Playername" in globals().keys() else 2
    $ Player.Semen =    P_Semen if "P_Semen" in globals().keys() else 2
    $ Player.Semen_Max = P_Semen_Max if "P_Semen_Max" in globals().keys() else 3
    $ Player.Focus =    P_Focus if "P_Focus" in globals().keys() else 0
    $ Player.FocusX =   P_FocusX if "P_FocusX" in globals().keys() else 0
    $ Player.XP =       P_XP if "P_XP" in globals().keys() else 0
    $ Player.StatPoints =       P_Statpoints if "P_Statpoints" in globals().keys() else 0
    $ Player.XPgoal =    P_XPgoal if "P_XPgoal" in globals().keys() else 100
    $ Player.Lvl =      P_Lvl if "P_Lvl" in globals().keys() else 1
    $ Player.Rep =      P_Rep if "P_Rep" in globals().keys() else 600
    $ Player.RecentActions =    P_RecentActions[:] if "P_RecentActions" in globals().keys() else []
    $ Player.DailyActions =     P_DailyActions[:] if "P_DailyActions" in globals().keys() else []
    $ Player.Traits =   P_Traits[:] if "P_Traits" in globals().keys() else []
    $ Player.History =  P_History[:] if "P_History" in globals().keys() else []
    $ Player.Harem =    P_Harem[:] if "P_Harem" in globals().keys() else []
    $ Player.Male =      P_Male if "P_Male" in globals().keys() else 1

    $ Player.Income =   P_Income if "P_Income" in globals().keys() else 12
    $ Player.Cash =     P_Cash if "P_Cash" in globals().keys() else 20
    $ Player.Inventory =        P_Inventory[:] if "P_Inventory" in globals().keys() else []

    $ Player.Sprite =   P_Sprite if "P_Sprite" in globals().keys() else 0
    $ Player.Color =    P_Color if "P_Color" in globals().keys() else "green"
    $ Player.Cock =     P_Cock if "P_Cock" in globals().keys() else "out"
    $ Player.Spunk =    P_Spunk if "P_Spunk" in globals().keys() else 0
    $ Player.Wet =      P_Wet if "P_Wet" in globals().keys() else 0


    if "RogueX" not in globals().keys():
        $ RogueX = GirlClass("Rogue",500,0,0,10)
    $ RogueX.Name = RogueName if "RogueName" in globals().keys() else "Rogue"
    $ RogueX.Tag = "Rogue"
    $ RogueX.Names = ["Rogue"]
    $ RogueX.Love = R_Love if "R_Love" in globals().keys() else RogueX.Love
    $ RogueX.Obed = R_Obed if "R_Obed" in globals().keys() else RogueX.Obed
    $ RogueX.Inbt = R_Inbt if "R_Inbt" in globals().keys() else RogueX.Inbt
    $ RogueX.Lust = R_Lust if "R_Lust" in globals().keys() else RogueX.Lust
    $ RogueX.Thirst = R_Thirst if "R_Thirst" in globals().keys() else 0
    $ RogueX.Addict = R_Addict if "R_Addict" in globals().keys() else 0
    $ RogueX.Addictionrate = R_Addictionrate if "R_Addictionrate" in globals().keys() else 0
    $ RogueX.Resistance = R_Resistance if "R_Resistance" in globals().keys() else 0
    $ RogueX.Taboo = R_Taboo if "R_Taboo" in globals().keys() else 0
    $ RogueX.XP = R_XP if "R_XP" in globals().keys() else 0
    $ RogueX.StatPoints = R_StatPoints if "R_StatPoints" in globals().keys() else 0
    $ RogueX.XPgoal = R_XPgoal if "R_XPgoal" in globals().keys() else 100
    $ RogueX.Lvl = R_Lvl if "R_Lvl" in globals().keys() else 1
    $ RogueX.SpriteLoc = R_SpriteLoc if "R_SpriteLoc" in globals().keys() else StageCenter
    $ RogueX.Layer = R_Layer if "R_Layer" in globals().keys() else 50
    $ RogueX.Action = R_Action if "R_Action" in globals().keys() else 3
    $ RogueX.MaxAction = R_MaxAction if "R_MaxAction" in globals().keys() else 3
    $ RogueX.Rep = R_Rep if "R_Rep" in globals().keys() else 600
    $ RogueX.RecentActions = R_RecentActions[:] if "R_RecentActions" in globals().keys() else []
    $ RogueX.DailyActions = R_DailyActions[:] if "R_DailyActions" in globals().keys() else []
    $ RogueX.Traits = R_Traits[:] if "R_Traits" in globals().keys() else []
    $ RogueX.History = R_History[:] if "R_History" in globals().keys() else []
    $ RogueX.Date = R_Date if "R_Date" in globals().keys() else 0
    $ RogueX.Chat = R_Chat[:] if "R_Chat" in globals().keys() else [0,0,0,0,0,0]
    $ RogueX.Event = R_Event[:] if "R_Event" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ RogueX.Petname = R_Petname if "R_Petname" in globals().keys() else "Zero"
    $ RogueX.Petnames = R_Petnames[:] if "R_Petnames" in globals().keys() else ["Zero"]
    $ RogueX.Pet = R_Pet if "R_Pet" in globals().keys() else "Girl"
    $ RogueX.Pets = R_Pets[:] if "R_Pets" in globals().keys() else ["Girl"]
    $ RogueX.Break = R_Break[:] if "R_Break" in globals().keys() else [0,0]
    $ RogueX.Forced = R_Forced if "R_Forced" in globals().keys() else 0
    $ RogueX.ForcedCount = R_ForcedCount if "R_ForcedCount" in globals().keys() else 0
    $ RogueX.Loc = R_Loc if "R_Loc" in globals().keys() else "hold"

    $ RogueX.Outfit = R_Outfit if "R_Outfit" in globals().keys() else "casual1"
    $ RogueX.OutfitDay = R_OutfitDay if "R_OutfitDay" in globals().keys() else "casual1"
    $ RogueX.SeenPeen = R_SeenPeen if "R_SeenPeen" in globals().keys() else 0
    $ RogueX.SeenChest = R_SeenChest if "R_SeenChest" in globals().keys() else 0
    $ RogueX.SeenPussy = R_SeenPussy if "R_SeenPussy" in globals().keys() else 0
    $ RogueX.SeenPanties = R_SeenPanties if "R_SeenPanties" in globals().keys() else 0
    $ RogueX.Upskirt = R_Upskirt if "R_Upskirt" in globals().keys() else 0
    $ RogueX.Uptop = R_Uptop if "R_Uptop" in globals().keys() else 0
    $ RogueX.PantiesDown = R_PantiesDown if "R_PantiesDown" in globals().keys() else 0
    $ RogueX.Wet = R_Wet if "R_Wet" in globals().keys() else 0
    $ RogueX.Water = R_Water if "R_Water" in globals().keys() else 0
    $ RogueX.Spunk = R_Spunk if "R_Spunk" in globals().keys() else []
    $ RogueX.Pierce = R_Pierce if "R_Pierce" in globals().keys() else 0
    $ RogueX.Pubes = R_Pubes if "R_Pubes" in globals().keys() else 1
    $ RogueX.ArmPose = R_ArmPose if "R_ArmPose" in globals().keys() else 1
    $ RogueX.Blush = R_Blush if "R_Blush" in globals().keys() else 0
    $ RogueX.Eyes = R_Eyes if "R_Eyes" in globals().keys() else "normal"
    $ RogueX.Mouth = R_Mouth if "R_Mouth" in globals().keys() else "normal"
    $ RogueX.Brows = R_Brows if "R_Brows" in globals().keys() else "normal"
    $ RogueX.Emote = R_Emote if "R_Emote" in globals().keys() else "normal"
    $ RogueX.Held = R_Held if "R_Held" in globals().keys() else 0
    $ RogueX.Arms = R_Arms if "R_Arms" in globals().keys() else 0
    $ RogueX.Legs = R_Legs if "R_Legs" in globals().keys() else 0
    $ RogueX.Over = R_Over if "R_Over" in globals().keys() else 0
    $ RogueX.Neck = R_Neck if "R_Neck" in globals().keys() else 0
    $ RogueX.Chest = R_Chest if "R_Chest" in globals().keys() else 0
    $ RogueX.Panties = R_Panties if "R_Panties" in globals().keys() else 0
    $ RogueX.Acc = R_Acc if "R_Acc" in globals().keys() else 0
    $ RogueX.Hair = R_Hair if "R_Hair" in globals().keys() else 1
    $ RogueX.Hose = R_Hose if "R_Hose" in globals().keys() else 0
    $ RogueX.Shame = R_Shame if "R_Shame" in globals().keys() else 0
    $ RogueX.Inventory = R_Inventory[:] if "R_Inventory" in globals().keys() else []



    $ RogueX.Custom1 = R_Custom[:] if "R_Custom" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ RogueX.Custom2 = R_Custom2[:] if "R_Custom2" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ RogueX.Custom3 = R_Custom3[:] if "R_Custom3" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ RogueX.TempClothes = R_TempClothes[:] if "R_TempClothes" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ RogueX.Gym = R_Gym[:] if "R_Gym" in globals().keys() else [0,"gloved",0,"hoodie",0,"sports bra","shorts",0,0,0,10]
    $ RogueX.Sleepwear = R_Sleepwear[:] if "R_Sleepwear" in globals().keys() else [0,0,0,0,0,"tank","green panties",0,0,0,20]
    $ RogueX.Swim = R_Swim[:] if "R_Swim" in globals().keys() else [0,0,0,"hoodie",0,"bikini top","bikini bottoms",0,0,0,0]

    $ RogueX.Gag = R_Gag if "R_Gag" in globals().keys() else 0
    $ RogueX.Todo = R_Todo[:] if "R_Todo" in globals().keys() else []
    $ RogueX.PubeC = R_PubeC if "R_PubeC" in globals().keys() else 0
    $ RogueX.Clothing = R_Schedule if "R_Schedule" in globals().keys() else [0,0,0,0,0,0,0,0,0,0]

    $ RogueX.Org = R_Org if "R_Org" in globals().keys() else 0
    $ RogueX.OCount = R_OCount if "R_OCount" in globals().keys() else 0
    $ RogueX.Caught = R_Caught if "R_Caught" in globals().keys() else 0
    $ RogueX.Kissed = R_Kissed if "R_Kissed" in globals().keys() else 0
    $ RogueX.Sleep = R_Sleep if "R_Sleep" in globals().keys() else 0
    $ RogueX.Hand = R_Hand if "R_Hand" in globals().keys() else 0
    $ RogueX.Foot = R_Foot if "R_Foot" in globals().keys() else 0
    $ RogueX.Slap = R_Slap if "R_Slap" in globals().keys() else 0
    $ RogueX.Strip = R_Strip if "R_Strip" in globals().keys() else 0
    $ RogueX.Tit = R_Tit if "R_Tit" in globals().keys() else 0
    $ RogueX.Sex = R_Sex if "R_Sex" in globals().keys() else 0
    $ RogueX.Anal = R_Anal if "R_Anal" in globals().keys() else 0
    $ RogueX.Loose = R_Loose if "R_Loose" in globals().keys() else 0
    $ RogueX.Hotdog = R_Hotdog if "R_Hotdog" in globals().keys() else 0
    $ RogueX.Mast = R_Mast if "R_Mast" in globals().keys() else 0
    $ RogueX.FondleB = R_FondleB if "R_FondleB" in globals().keys() else 0
    $ RogueX.FondleT = R_FondleT if "R_FondleT" in globals().keys() else 0
    $ RogueX.FondleP = R_FondleP if "R_FondleP" in globals().keys() else 0
    $ RogueX.FondleA = R_FondleA if "R_FondleA" in globals().keys() else 0
    $ RogueX.DildoP = R_DildoP if "R_DildoP" in globals().keys() else 0
    $ RogueX.DildoA = R_DildoA if "R_DildoA" in globals().keys() else 0
    $ RogueX.Vib = R_Vib if "R_Vib" in globals().keys() else 0
    $ RogueX.Plug = R_Plug if "R_Plug" in globals().keys() else 0
    $ RogueX.SuckB = R_SuckB if "R_SuckB" in globals().keys() else 0
    $ RogueX.InsertP = R_InsertP if "R_InsertP" in globals().keys() else 0
    $ RogueX.InsertA = R_InsertA if "R_InsertA" in globals().keys() else 0
    $ RogueX.LickP = R_LickP if "R_LickP" in globals().keys() else 0
    $ RogueX.LickA = R_LickA if "R_LickA" in globals().keys() else 0
    $ RogueX.Blow = R_Blow if "R_Blow" in globals().keys() else 0
    $ RogueX.Swallow = R_Swallow if "R_Swallow" in globals().keys() else 0
    $ RogueX.CreamP = R_CreamP if "R_CreamP" in globals().keys() else 0
    $ RogueX.CreamA = R_CreamA if "R_CreamA" in globals().keys() else 0
    $ RogueX.Les = R_Les if "R_Les" in globals().keys() else 0
    $ RogueX.LesWatch = R_LesWatch if "R_LesWatch" in globals().keys() else 0
    $ RogueX.SEXP = R_SEXP if "R_SEXP" in globals().keys() else 0
    $ RogueX.PlayerFav = R_PlayerFav if "R_PlayerFav" in globals().keys() else 0
    $ RogueX.Favorite = R_Favorite if "R_Favorite" in globals().keys() else 0


    $ RogueX.Acc = R_Boots if "R_Boots" in globals().keys() else 0
    $ RogueX.Home = "bg rogue"

    $ RogueX.Outfit = "casual1" if RogueX.Outfit == "evo_green" else RogueX.Outfit
    $ RogueX.OutfitDay = "casual1" if RogueX.OutfitDay == "evo_green" else RogueX.OutfitDay
    $ RogueX.Outfit = "casual2" if RogueX.Outfit == "evo_pink" else RogueX.Outfit
    $ RogueX.OutfitDay = "casual2" if RogueX.OutfitDay == "evo_pink" else RogueX.OutfitDay

    $ RogueX.Casual1 = [2,"gloved","skirt","mesh top","spiked collar","tank","black panties",0,0,"tights",0]
    $ RogueX.Casual2 = [2,"gloved","pants","pink top",0,"buttoned tank","black panties",0,0,0,0]

    $ RogueX.Schedule = [["bg rogue","bg classroom","bg dangerroom","bg rogue"],
                                        ["bg classroom","bg dangerroom","bg rogue","bg rogue"],
                                        ["bg rogue","bg classroom","bg dangerroom","bg rogue"],
                                        ["bg classroom","bg dangerroom","bg rogue","bg rogue"],
                                        ["bg rogue","bg classroom","bg dangerroom","bg rogue"],
                                        ["bg dangerroom","bg pool","bg rogue","bg rogue"],
                                        ["bg dangerroom","bg pool","bg rogue","bg rogue"],
                                        ]
    $ RogueX.Hair = "evo"
    $ RogueX.LikeKitty = R_LikeKitty if "R_LikeKitty" in globals().keys() else 600
    $ RogueX.LikeEmma = R_LikeEmma if "R_LikeEmma" in globals().keys() else 500
    $ RogueX.LikeLaura = R_LikeLaura if "R_LikeLaura" in globals().keys() else 500
    $ RogueX.SexKitty = R_SexKitty if "R_SexKitty" in globals().keys() else 0
    $ RogueX.SexEmma = R_SexEmma if "R_SexEmma" in globals().keys() else 0
    $ RogueX.SexLaura = R_SexLaura if "R_SexLaura" in globals().keys() else 0

    $ RogueX.MassageChart = ["shoulders","arms","arms","hands","hands","back","hips","back","breasts","breasts"]
    $ RogueX.History.append("met") if "met" not in RogueX.History else RogueX.History
    while len(RogueX.Custom1) < 11:
        $ RogueX.Custom1.append(0)
    while len(RogueX.Custom2) < 11:
        $ RogueX.Custom2.append(0)
    while len(RogueX.Custom3) < 11:
        $ RogueX.Custom3.append(0)
    while len(RogueX.TempClothes) < 11:
        $ RogueX.TempClothes.append(0)
    while len(RogueX.Gym) < 11:
        $ RogueX.Gym.append(0)
    while len(RogueX.Sleepwear) < 11:
        $ RogueX.Sleepwear.append(0)
    while len(RogueX.Swim) < 11:
        $ RogueX.Swim.append(0)



    if "KittyX" not in globals().keys():
        $ KittyX = GirlClass("Kitty",500,0,0,10)
    $ KittyX.Name = KittyName if "KittyName" in globals().keys() else "Kitty"
    $ KittyX.Tag = "Kitty"
    $ KittyX.Names = ["Kitty"]
    $ KittyX.Love = K_Love if "K_Love" in globals().keys() else KittyX.Love
    $ KittyX.Obed = K_Obed if "K_Obed" in globals().keys() else KittyX.Obed
    $ KittyX.Inbt = K_Inbt if "K_Inbt" in globals().keys() else KittyX.Inbt
    $ KittyX.Lust = K_Lust if "K_Lust" in globals().keys() else KittyX.Lust
    $ KittyX.Thirst = K_Thirst if "K_Thirst" in globals().keys() else 0
    $ KittyX.Addict = K_Addict if "K_Addict" in globals().keys() else 0
    $ KittyX.Addictionrate = K_Addictionrate if "K_Addictionrate" in globals().keys() else 0
    $ KittyX.Resistance = K_Resistance if "K_Resistance" in globals().keys() else 0
    $ KittyX.Taboo = K_Taboo if "K_Taboo" in globals().keys() else 0
    $ KittyX.XP = K_XP if "K_XP" in globals().keys() else 0
    $ KittyX.StatPoints = K_StatPoints if "K_StatPoints" in globals().keys() else 0
    $ KittyX.XPgoal = K_XPgoal if "K_XPgoal" in globals().keys() else 100
    $ KittyX.Lvl = K_Lvl if "K_Lvl" in globals().keys() else 1
    $ KittyX.SpriteLoc = K_SpriteLoc if "K_SpriteLoc" in globals().keys() else StageCenter
    $ KittyX.Layer = K_Layer if "K_Layer" in globals().keys() else 50
    $ KittyX.Action = K_Action if "K_Action" in globals().keys() else 3
    $ KittyX.MaxAction = K_MaxAction if "K_MaxAction" in globals().keys() else 3
    $ KittyX.Rep = K_Rep if "K_Rep" in globals().keys() else 600
    $ KittyX.RecentActions = K_RecentActions[:] if "K_RecentActions" in globals().keys() else []
    $ KittyX.DailyActions = K_DailyActions[:] if "K_DailyActions" in globals().keys() else []
    $ KittyX.Traits = K_Traits[:] if "K_Traits" in globals().keys() else []
    $ KittyX.History = K_History[:] if "K_History" in globals().keys() else []
    $ KittyX.Date = K_Date if "K_Date" in globals().keys() else 0
    $ KittyX.Chat = K_Chat[:] if "K_Chat" in globals().keys() else [0,0,0,0,0,0]
    $ KittyX.Event = K_Event[:] if "K_Event" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ KittyX.Petname = K_Petname if "K_Petname" in globals().keys() else "Zero"
    $ KittyX.Petnames = K_Petnames[:] if "K_Petnames" in globals().keys() else ["Zero"]
    $ KittyX.Pet = K_Pet if "K_Pet" in globals().keys() else "Girl"
    $ KittyX.Pets = K_Pets[:] if "K_Pets" in globals().keys() else ["Girl"]
    $ KittyX.Break = K_Break[:] if "K_Break" in globals().keys() else [0,0]
    $ KittyX.Forced = K_Forced if "K_Forced" in globals().keys() else 0
    $ KittyX.ForcedCount = K_ForcedCount if "K_ForcedCount" in globals().keys() else 0
    $ KittyX.Loc = K_Loc if "K_Loc" in globals().keys() else "hold"

    $ KittyX.Outfit = K_Outfit if "K_Outfit" in globals().keys() else "casual1"
    $ KittyX.OutfitDay = K_OutfitDay if "K_OutfitDay" in globals().keys() else "casual1"
    $ KittyX.SeenPeen = K_SeenPeen if "K_SeenPeen" in globals().keys() else 0
    $ KittyX.SeenChest = K_SeenChest if "K_SeenChest" in globals().keys() else 0
    $ KittyX.SeenPussy = K_SeenPussy if "K_SeenPussy" in globals().keys() else 0
    $ KittyX.SeenPanties = K_SeenPanties if "K_SeenPanties" in globals().keys() else 0
    $ KittyX.Upskirt = K_Upskirt if "K_Upskirt" in globals().keys() else 0
    $ KittyX.Uptop = K_Uptop if "K_Uptop" in globals().keys() else 0
    $ KittyX.PantiesDown = K_PantiesDown if "K_PantiesDown" in globals().keys() else 0
    $ KittyX.Wet = K_Wet if "K_Wet" in globals().keys() else 0
    $ KittyX.Water = K_Water if "K_Water" in globals().keys() else 0
    $ KittyX.Spunk = K_Spunk if "K_Spunk" in globals().keys() else []
    $ KittyX.Pierce = K_Pierce if "K_Pierce" in globals().keys() else 0
    $ KittyX.Pubes = K_Pubes if "K_Pubes" in globals().keys() else 1
    $ KittyX.ArmPose = K_ArmPose if "K_ArmPose" in globals().keys() else 1
    $ KittyX.Blush = K_Blush if "K_Blush" in globals().keys() else 0
    $ KittyX.Eyes = K_Eyes if "K_Eyes" in globals().keys() else "normal"
    $ KittyX.Mouth = K_Mouth if "K_Mouth" in globals().keys() else "normal"
    $ KittyX.Brows = K_Brows if "K_Brows" in globals().keys() else "normal"
    $ KittyX.Emote = K_Emote if "K_Emote" in globals().keys() else "normal"
    $ KittyX.Held = K_Held if "K_Held" in globals().keys() else 0
    $ KittyX.Arms = K_Arms if "K_Arms" in globals().keys() else 0
    $ KittyX.Legs = K_Legs if "K_Legs" in globals().keys() else 0
    $ KittyX.Over = K_Over if "K_Over" in globals().keys() else 0
    $ KittyX.Neck = K_Neck if "K_Neck" in globals().keys() else 0
    $ KittyX.Chest = K_Chest if "K_Chest" in globals().keys() else 0
    $ KittyX.Panties = K_Panties if "K_Panties" in globals().keys() else 0
    $ KittyX.Acc = K_Acc if "K_Acc" in globals().keys() else 0
    $ KittyX.Hair = K_Hair if "K_Hair" in globals().keys() else 1
    $ KittyX.Hose = K_Hose if "K_Hose" in globals().keys() else 0
    $ KittyX.Shame = K_Shame if "K_Shame" in globals().keys() else 0
    $ KittyX.Inventory = K_Inventory[:] if "K_Inventory" in globals().keys() else []



    $ KittyX.Custom1 = K_Custom[:] if "K_Custom" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ KittyX.Custom2 = K_Custom2[:] if "K_Custom2" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ KittyX.Custom3 = K_Custom3[:] if "K_Custom3" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ KittyX.TempClothes = K_TempClothes[:] if "K_TempClothes" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ KittyX.Gym = K_Gym[:] if "K_Gym" in globals().keys() else [0,0,"shorts",0,0,"sports bra","green panties",0,0,0,10]
    $ KittyX.Sleepwear = K_Sleepwear[:] if "K_Sleepwear" in globals().keys() else [0,0,"shorts",0,0,"cami","green panties",0,0,0,20]
    $ KittyX.Swim = K_Swim[:] if "K_Swim" in globals().keys() else [0,0,"blue skirt",0,0,"bikini top","bikini bottoms",0,0,0,0]

    $ KittyX.Gag = K_Gag if "K_Gag" in globals().keys() else 0
    $ KittyX.Todo = K_Todo[:] if "K_Todo" in globals().keys() else []
    $ KittyX.PubeC = K_PubeC if "K_PubeC" in globals().keys() else 0
    $ KittyX.Clothing = K_Schedule if "K_Schedule" in globals().keys() else [0,0,0,0,0,0,0,0,0,0]

    $ KittyX.Org = K_Org if "K_Org" in globals().keys() else 0
    $ KittyX.OCount = K_OCount if "K_OCount" in globals().keys() else 0
    $ KittyX.Caught = K_Caught if "K_Caught" in globals().keys() else 0
    $ KittyX.Kissed = K_Kissed if "K_Kissed" in globals().keys() else 0
    $ KittyX.Sleep = K_Sleep if "K_Sleep" in globals().keys() else 0
    $ KittyX.Hand = K_Hand if "K_Hand" in globals().keys() else 0
    $ KittyX.Foot = K_Foot if "K_Foot" in globals().keys() else 0
    $ KittyX.Slap = K_Slap if "K_Slap" in globals().keys() else 0
    $ KittyX.Strip = K_Strip if "K_Strip" in globals().keys() else 0
    $ KittyX.Tit = K_Tit if "K_Tit" in globals().keys() else 0
    $ KittyX.Sex = K_Sex if "K_Sex" in globals().keys() else 0
    $ KittyX.Anal = K_Anal if "K_Anal" in globals().keys() else 0
    $ KittyX.Loose = K_Loose if "K_Loose" in globals().keys() else 0
    $ KittyX.Hotdog = K_Hotdog if "K_Hotdog" in globals().keys() else 0
    $ KittyX.Mast = K_Mast if "K_Mast" in globals().keys() else 0
    $ KittyX.FondleB = K_FondleB if "K_FondleB" in globals().keys() else 0
    $ KittyX.FondleT = K_FondleT if "K_FondleT" in globals().keys() else 0
    $ KittyX.FondleP = K_FondleP if "K_FondleP" in globals().keys() else 0
    $ KittyX.FondleA = K_FondleA if "K_FondleA" in globals().keys() else 0
    $ KittyX.DildoP = K_DildoP if "K_DildoP" in globals().keys() else 0
    $ KittyX.DildoA = K_DildoA if "K_DildoA" in globals().keys() else 0
    $ KittyX.Vib = K_Vib if "K_Vib" in globals().keys() else 0
    $ KittyX.Plug = K_Plug if "K_Plug" in globals().keys() else 0
    $ KittyX.SuckB = K_SuckB if "K_SuckB" in globals().keys() else 0
    $ KittyX.InsertP = K_InsertP if "K_InsertP" in globals().keys() else 0
    $ KittyX.InsertA = K_InsertA if "K_InsertA" in globals().keys() else 0
    $ KittyX.LickP = K_LickP if "K_LickP" in globals().keys() else 0
    $ KittyX.LickA = K_LickA if "K_LickA" in globals().keys() else 0
    $ KittyX.Blow = K_Blow if "K_Blow" in globals().keys() else 0
    $ KittyX.Swallow = K_Swallow if "K_Swallow" in globals().keys() else 0
    $ KittyX.CreamP = K_CreamP if "K_CreamP" in globals().keys() else 0
    $ KittyX.CreamA = K_CreamA if "K_CreamA" in globals().keys() else 0
    $ KittyX.Les = K_Les if "K_Les" in globals().keys() else 0
    $ KittyX.LesWatch = K_LesWatch if "K_LesWatch" in globals().keys() else 0
    $ KittyX.SEXP = K_SEXP if "K_SEXP" in globals().keys() else 0
    $ KittyX.PlayerFav = K_PlayerFav if "K_PlayerFav" in globals().keys() else 0
    $ KittyX.Favorite = K_Favorite if "K_Favorite" in globals().keys() else 0


    $ KittyX.Acc = K_Boots if "K_Boots" in globals().keys() else 0
    $ KittyX.Home = "bg kitty"

    $ KittyX.Outfit = "casual1" if KittyX.Outfit == "pink outfit" else KittyX.Outfit
    $ KittyX.OutfitDay = "casual1" if KittyX.OutfitDay == "pink outfit" else KittyX.OutfitDay
    $ KittyX.Outfit = "casual2" if KittyX.Outfit == "red outfit" else KittyX.Outfit
    $ KittyX.OutfitDay = "casual2" if KittyX.OutfitDay == "red outfit" else KittyX.OutfitDay

    $ KittyX.Casual1 = [2,0,"capris","pink top","gold necklace","cami","green panties",0,0,0,0]
    $ KittyX.Casual2 = [2,0,"black jeans","red shirt",0,"bra","green panties",0,0,0,0]

    $ KittyX.Schedule = [["bg classroom","bg dangerroom","bg kitty","bg kitty"],
                                        ["bg classroom","bg pool","bg kitty","bg kitty"],
                                        ["bg classroom","bg dangerroom","bg kitty","bg kitty"],
                                        ["bg classroom","bg pool","bg kitty","bg kitty"],
                                        ["bg classroom","bg dangerroom","bg kitty","bg kitty"],
                                        ["bg campus","bg dangerroom","bg kitty","bg kitty"],
                                        ["bg campus","bg dangerroom","bg kitty","bg kitty"],
                                        ]
    $ KittyX.Hair = "evo"
    $ KittyX.LikeRogue = K_LikeRogue if "K_LikeRogue" in globals().keys() else 600
    $ KittyX.LikeEmma = K_LikeEmma if "K_LikeEmma" in globals().keys() else 500
    $ KittyX.LikeLaura = K_LikeLaura if "K_LikeLaura" in globals().keys() else 500
    $ KittyX.SexRogue = K_SexRogue if "K_SexRogue" in globals().keys() else 0
    $ KittyX.SexEmma = K_SexEmma if "K_SexEmma" in globals().keys() else 0
    $ KittyX.SexLaura = K_SexLaura if "K_SexLaura" in globals().keys() else 0

    $ KittyX.like = K_like if "K_like" in globals().keys() else ", like, "
    $ KittyX.Like = K_Like if "K_Like" in globals().keys() else "Like, "

    $ KittyX.MassageChart = ["shoulders","back","hips","thighs","calves","feet","feet","hips","ass","pussy"]

    while len(KittyX.Custom1) < 11:
        $ KittyX.Custom1.append(0)
    while len(KittyX.Custom2) < 11:
        $ KittyX.Custom2.append(0)
    while len(KittyX.Custom3) < 11:
        $ KittyX.Custom3.append(0)
    while len(KittyX.TempClothes) < 11:
        $ KittyX.TempClothes.append(0)
    while len(KittyX.Gym) < 11:
        $ KittyX.Gym.append(0)
    while len(KittyX.Sleepwear) < 11:
        $ KittyX.Sleepwear.append(0)
    while len(KittyX.Swim) < 11:
        $ KittyX.Swim.append(0)



    if "EmmaX" not in globals().keys():
        $ EmmaX = GirlClass("Emma",500,0,0,10)
    $ EmmaX.Name = EmmaName if "EmmaName" in globals().keys() else "Emma"
    $ EmmaX.Tag = "Emma"
    $ EmmaX.Names = ["Emma"]
    $ EmmaX.Love = E_Love if "E_Love" in globals().keys() else EmmaX.Love
    $ EmmaX.Obed = E_Obed if "E_Obed" in globals().keys() else EmmaX.Obed
    $ EmmaX.Inbt = E_Inbt if "E_Inbt" in globals().keys() else EmmaX.Inbt
    $ EmmaX.Lust = E_Lust if "E_Lust" in globals().keys() else EmmaX.Lust
    $ EmmaX.Thirst = E_Thirst if "E_Thirst" in globals().keys() else 0
    $ EmmaX.Addict = E_Addict if "E_Addict" in globals().keys() else 0
    $ EmmaX.Addictionrate = E_Addictionrate if "E_Addictionrate" in globals().keys() else 0
    $ EmmaX.Resistance = E_Resistance if "E_Resistance" in globals().keys() else 0
    $ EmmaX.Taboo = E_Taboo if "E_Taboo" in globals().keys() else 0
    $ EmmaX.XP = E_XP if "E_XP" in globals().keys() else 0
    $ EmmaX.StatPoints = E_StatPoints if "E_StatPoints" in globals().keys() else 0
    $ EmmaX.XPgoal = E_XPgoal if "E_XPgoal" in globals().keys() else 100
    $ EmmaX.Lvl = E_Lvl if "E_Lvl" in globals().keys() else 1
    $ EmmaX.SpriteLoc = E_SpriteLoc if "E_SpriteLoc" in globals().keys() else StageCenter
    $ EmmaX.Layer = E_Layer if "E_Layer" in globals().keys() else 50
    $ EmmaX.Action = E_Action if "E_Action" in globals().keys() else 3
    $ EmmaX.MaxAction = E_MaxAction if "E_MaxAction" in globals().keys() else 3
    $ EmmaX.Rep = E_Rep if "E_Rep" in globals().keys() else 600
    $ EmmaX.RecentActions = E_RecentActions[:] if "E_RecentActions" in globals().keys() else []
    $ EmmaX.DailyActions = E_DailyActions[:] if "E_DailyActions" in globals().keys() else []
    $ EmmaX.Traits = E_Traits[:] if "E_Traits" in globals().keys() else []
    $ EmmaX.History = E_History[:] if "E_History" in globals().keys() else []
    $ EmmaX.Date = E_Date if "E_Date" in globals().keys() else 0
    $ EmmaX.Chat = E_Chat[:] if "E_Chat" in globals().keys() else [0,0,0,0,0,0]
    $ EmmaX.Event = E_Event[:] if "E_Event" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ EmmaX.Petname = E_Petname if "E_Petname" in globals().keys() else "Zero"
    $ EmmaX.Petnames = E_Petnames[:] if "E_Petnames" in globals().keys() else ["Zero"]
    $ EmmaX.Pet = E_Pet if "E_Pet" in globals().keys() else "Girl"
    $ EmmaX.Pets = E_Pets[:] if "E_Pets" in globals().keys() else ["Girl"]
    $ EmmaX.Break = E_Break[:] if "E_Break" in globals().keys() else [0,0]
    $ EmmaX.Forced = E_Forced if "E_Forced" in globals().keys() else 0
    $ EmmaX.ForcedCount = E_ForcedCount if "E_ForcedCount" in globals().keys() else 0
    $ EmmaX.Loc = E_Loc if "E_Loc" in globals().keys() else "hold"

    $ EmmaX.Outfit = E_Outfit if "E_Outfit" in globals().keys() else "casual1"
    $ EmmaX.OutfitDay = E_OutfitDay if "E_OutfitDay" in globals().keys() else "casual1"
    $ EmmaX.SeenPeen = E_SeenPeen if "E_SeenPeen" in globals().keys() else 0
    $ EmmaX.SeenChest = E_SeenChest if "E_SeenChest" in globals().keys() else 0
    $ EmmaX.SeenPussy = E_SeenPussy if "E_SeenPussy" in globals().keys() else 0
    $ EmmaX.SeenPanties = E_SeenPanties if "E_SeenPanties" in globals().keys() else 0
    $ EmmaX.Upskirt = E_Upskirt if "E_Upskirt" in globals().keys() else 0
    $ EmmaX.Uptop = E_Uptop if "E_Uptop" in globals().keys() else 0
    $ EmmaX.PantiesDown = E_PantiesDown if "E_PantiesDown" in globals().keys() else 0
    $ EmmaX.Wet = E_Wet if "E_Wet" in globals().keys() else 0
    $ EmmaX.Water = E_Water if "E_Water" in globals().keys() else 0
    $ EmmaX.Spunk = E_Spunk if "E_Spunk" in globals().keys() else []
    $ EmmaX.Pierce = E_Pierce if "E_Pierce" in globals().keys() else 0
    $ EmmaX.Pubes = E_Pubes if "E_Pubes" in globals().keys() else 0
    $ EmmaX.ArmPose = E_ArmPose if "E_ArmPose" in globals().keys() else 1
    $ EmmaX.Blush = E_Blush if "E_Blush" in globals().keys() else 0
    $ EmmaX.Eyes = E_Eyes if "E_Eyes" in globals().keys() else "normal"
    $ EmmaX.Mouth = E_Mouth if "E_Mouth" in globals().keys() else "normal"
    $ EmmaX.Brows = E_Brows if "E_Brows" in globals().keys() else "normal"
    $ EmmaX.Emote = E_Emote if "E_Emote" in globals().keys() else "normal"
    $ EmmaX.Held = E_Held if "E_Held" in globals().keys() else 0
    $ EmmaX.Arms = E_Arms if "E_Arms" in globals().keys() else 0
    $ EmmaX.Legs = E_Legs if "E_Legs" in globals().keys() else 0
    $ EmmaX.Over = E_Over if "E_Over" in globals().keys() else 0
    $ EmmaX.Neck = E_Neck if "E_Neck" in globals().keys() else 0
    $ EmmaX.Chest = E_Chest if "E_Chest" in globals().keys() else 0
    $ EmmaX.Panties = E_Panties if "E_Panties" in globals().keys() else 0
    $ EmmaX.Acc = E_Acc if "E_Acc" in globals().keys() else 0
    $ EmmaX.Hair = E_Hair if "E_Hair" in globals().keys() else 1
    $ EmmaX.Hose = E_Hose if "E_Hose" in globals().keys() else 0
    $ EmmaX.Shame = E_Shame if "E_Shame" in globals().keys() else 0
    $ EmmaX.Inventory = E_Inventory[:] if "E_Inventory" in globals().keys() else []



    $ EmmaX.Custom1 = E_Custom[:] if "E_Custom" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ EmmaX.Custom2 = E_Custom2[:] if "E_Custom2" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ EmmaX.Custom3 = E_Custom3[:] if "E_Custom3" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ EmmaX.TempClothes = E_TempClothes[:] if "E_TempClothes" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ EmmaX.Gym = E_Gym[:] if "E_Gym" in globals().keys() else [0,0,0,0,0,"sports bra","sports panties",0,0,0,10]
    $ EmmaX.Sleepwear = E_Sleepwear[:] if "E_Sleepwear" in globals().keys() else [0,0,0,0,0,"corset","white panties",0,0,0,25]
    $ EmmaX.Swim = E_Swim[:] if "E_Swim" in globals().keys() else [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0]

    $ EmmaX.Gag = E_Gag if "E_Gag" in globals().keys() else 0
    $ EmmaX.Todo = E_Todo[:] if "E_Todo" in globals().keys() else []
    $ EmmaX.PubeC = E_PubeC if "E_PubeC" in globals().keys() else 0
    $ EmmaX.Clothing = E_Schedule if "E_Schedule" in globals().keys() else [0,0,0,0,0,0,0,0,0,0]

    $ EmmaX.Org = E_Org if "E_Org" in globals().keys() else 0
    $ EmmaX.OCount = E_OCount if "E_OCount" in globals().keys() else 0
    $ EmmaX.Caught = E_Caught if "E_Caught" in globals().keys() else 0
    $ EmmaX.Kissed = E_Kissed if "E_Kissed" in globals().keys() else 0
    $ EmmaX.Sleep = E_Sleep if "E_Sleep" in globals().keys() else 0
    $ EmmaX.Hand = E_Hand if "E_Hand" in globals().keys() else 0
    $ EmmaX.Foot = E_Foot if "E_Foot" in globals().keys() else 0
    $ EmmaX.Slap = E_Slap if "E_Slap" in globals().keys() else 0
    $ EmmaX.Strip = E_Strip if "E_Strip" in globals().keys() else 0
    $ EmmaX.Tit = E_Tit if "E_Tit" in globals().keys() else 0
    $ EmmaX.Sex = E_Sex if "E_Sex" in globals().keys() else 0
    $ EmmaX.Anal = E_Anal if "E_Anal" in globals().keys() else 0
    $ EmmaX.Loose = E_Loose if "E_Loose" in globals().keys() else 2
    $ EmmaX.Hotdog = E_Hotdog if "E_Hotdog" in globals().keys() else 0
    $ EmmaX.Mast = E_Mast if "E_Mast" in globals().keys() else 0
    $ EmmaX.FondleB = E_FondleB if "E_FondleB" in globals().keys() else 0
    $ EmmaX.FondleT = E_FondleT if "E_FondleT" in globals().keys() else 0
    $ EmmaX.FondleP = E_FondleP if "E_FondleP" in globals().keys() else 0
    $ EmmaX.FondleA = E_FondleA if "E_FondleA" in globals().keys() else 0
    $ EmmaX.DildoP = E_DildoP if "E_DildoP" in globals().keys() else 0
    $ EmmaX.DildoA = E_DildoA if "E_DildoA" in globals().keys() else 0
    $ EmmaX.Vib = E_Vib if "E_Vib" in globals().keys() else 0
    $ EmmaX.Plug = E_Plug if "E_Plug" in globals().keys() else 0
    $ EmmaX.SuckB = E_SuckB if "E_SuckB" in globals().keys() else 0
    $ EmmaX.InsertP = E_InsertP if "E_InsertP" in globals().keys() else 0
    $ EmmaX.InsertA = E_InsertA if "E_InsertA" in globals().keys() else 0
    $ EmmaX.LickP = E_LickP if "E_LickP" in globals().keys() else 0
    $ EmmaX.LickA = E_LickA if "E_LickA" in globals().keys() else 0
    $ EmmaX.Blow = E_Blow if "E_Blow" in globals().keys() else 0
    $ EmmaX.Swallow = E_Swallow if "E_Swallow" in globals().keys() else 0
    $ EmmaX.CreamP = E_CreamP if "E_CreamP" in globals().keys() else 0
    $ EmmaX.CreamA = E_CreamA if "E_CreamA" in globals().keys() else 0
    $ EmmaX.Les = E_Les if "E_Les" in globals().keys() else 0
    $ EmmaX.LesWatch = E_LesWatch if "E_LesWatch" in globals().keys() else 0
    $ EmmaX.SEXP = E_SEXP if "E_SEXP" in globals().keys() else 0
    $ EmmaX.PlayerFav = E_PlayerFav if "E_PlayerFav" in globals().keys() else 0
    $ EmmaX.Favorite = E_Favorite if "E_Favorite" in globals().keys() else 0


    $ EmmaX.Acc = E_Boots if "E_Boots" in globals().keys() else 0
    $ EmmaX.Home = "bg emma"

    $ EmmaX.Outfit = "casual1" if EmmaX.Outfit == "teacher" else EmmaX.Outfit
    $ EmmaX.OutfitDay = "casual1" if EmmaX.OutfitDay == "teacher" else EmmaX.OutfitDay
    $ EmmaX.Outfit = "casual2" if EmmaX.Outfit == "costume" else EmmaX.Outfit
    $ EmmaX.OutfitDay = "casual2" if EmmaX.OutfitDay == "costume" else EmmaX.OutfitDay

    $ EmmaX.Casual1 = [2,0,"pants","jacket","choker","corset","white panties",0,0,0,0]
    $ EmmaX.Casual2 = [2,"gloves","pants",0,"choker","corset","white panties",0,0,0,5]

    $ EmmaX.Schedule = [["bg teacher","bg teacher","bg classroom","bg emma"],
                                        ["bg teacher","bg teacher","bg dangerroom","bg emma"],
                                        ["bg teacher","bg teacher","bg classroom","bg emma"],
                                        ["bg teacher","bg teacher","bg dangerroom","bg emma"],
                                        ["bg teacher","bg teacher","bg classroom","bg emma"],
                                        ["bg pool","bg pool","bg emma","bg emma"],
                                        ["bg pool","bg pool","bg emma","bg emma"],
                                        ]
    $ EmmaX.Hair = "wavy"
    $ EmmaX.LikeRogue = E_LikeRogue if "E_LikeRogue" in globals().keys() else 500
    $ EmmaX.LikeKitty = E_LikeKitty if "E_LikeKitty" in globals().keys() else 500
    $ EmmaX.LikeLaura = E_LikeLaura if "E_LikeLaura" in globals().keys() else 500
    $ EmmaX.SexRogue = E_SexRogue if "E_SexRogue" in globals().keys() else 0
    $ EmmaX.SexKitty = E_SexKitty if "E_SexKitty" in globals().keys() else 0
    $ EmmaX.SexLaura = E_SexLaura if "E_SexLaura" in globals().keys() else 0
    $ EmmaX.MassageChart = ["shoulders","neck","neck","back","hips","ass","ass","back","breasts","breasts"]
    $ EmmaX.History.append("met") if "met" not in EmmaX.History else EmmaX.History

    while len(EmmaX.Custom1) < 11:
        $ EmmaX.Custom1.append(0)
    while len(EmmaX.Custom2) < 11:
        $ EmmaX.Custom2.append(0)
    while len(EmmaX.Custom3) < 11:
        $ EmmaX.Custom3.append(0)
    while len(EmmaX.TempClothes) < 11:
        $ EmmaX.TempClothes.append(0)
    while len(EmmaX.Gym) < 11:
        $ EmmaX.Gym.append(0)
    while len(EmmaX.Sleepwear) < 11:
        $ EmmaX.Sleepwear.append(0)
    while len(EmmaX.Swim) < 11:
        $ EmmaX.Swim.append(0)




    if "LauraX" not in globals().keys():
        $ LauraX = GirlClass("Laura",500,0,0,10)
    $ LauraX.Name = LauraName if "LauraName" in globals().keys() else "Laura"
    $ LauraX.Tag = "Laura"
    $ LauraX.Names = ["Laura"]
    $ LauraX.Love = L_Love if "L_Love" in globals().keys() else LauraX.Love
    $ LauraX.Obed = L_Obed if "L_Obed" in globals().keys() else LauraX.Obed
    $ LauraX.Inbt = L_Inbt if "L_Inbt" in globals().keys() else LauraX.Inbt
    $ LauraX.Lust = L_Lust if "L_Lust" in globals().keys() else LauraX.Lust
    $ LauraX.Thirst = L_Thirst if "L_Thirst" in globals().keys() else 0
    $ LauraX.Addict = L_Addict if "L_Addict" in globals().keys() else 0
    $ LauraX.Addictionrate = L_Addictionrate if "L_Addictionrate" in globals().keys() else 0
    $ LauraX.Resistance = L_Resistance if "L_Resistance" in globals().keys() else 0
    $ LauraX.Taboo = L_Taboo if "L_Taboo" in globals().keys() else 0
    $ LauraX.XP = L_XP if "L_XP" in globals().keys() else 0
    $ LauraX.StatPoints = L_StatPoints if "L_StatPoints" in globals().keys() else 0
    $ LauraX.XPgoal = L_XPgoal if "L_XPgoal" in globals().keys() else 100
    $ LauraX.Lvl = L_Lvl if "L_Lvl" in globals().keys() else 1
    $ LauraX.SpriteLoc = L_SpriteLoc if "L_SpriteLoc" in globals().keys() else StageCenter
    $ LauraX.Layer = L_Layer if "L_Layer" in globals().keys() else 50
    $ LauraX.Action = L_Action if "L_Action" in globals().keys() else 3
    $ LauraX.MaxAction = L_MaxAction if "L_MaxAction" in globals().keys() else 3
    $ LauraX.Rep = L_Rep if "L_Rep" in globals().keys() else 600
    $ LauraX.RecentActions = L_RecentActions[:] if "L_RecentActions" in globals().keys() else []
    $ LauraX.DailyActions = L_DailyActions[:] if "L_DailyActions" in globals().keys() else []
    $ LauraX.Traits = L_Traits[:] if "L_Traits" in globals().keys() else []
    $ LauraX.History = L_History[:] if "L_History" in globals().keys() else []
    $ LauraX.Date = L_Date if "L_Date" in globals().keys() else 0
    $ LauraX.Chat = L_Chat[:] if "L_Chat" in globals().keys() else [0,0,0,0,0,0]
    $ LauraX.Event = L_Event[:] if "L_Event" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ LauraX.Petname = L_Petname if "L_Petname" in globals().keys() else "Zero"
    $ LauraX.Petnames = L_Petnames[:] if "L_Petnames" in globals().keys() else ["Zero"]
    $ LauraX.Pet = L_Pet if "L_Pet" in globals().keys() else "Girl"
    $ LauraX.Pets = L_Pets[:] if "L_Pets" in globals().keys() else ["Girl"]
    $ LauraX.Break = L_Break[:] if "L_Break" in globals().keys() else [0,0]
    $ LauraX.Forced = L_Forced if "L_Forced" in globals().keys() else 0
    $ LauraX.ForcedCount = L_ForcedCount if "L_ForcedCount" in globals().keys() else 0
    $ LauraX.Loc = L_Loc if "L_Loc" in globals().keys() else "hold"

    $ LauraX.Outfit = L_Outfit if "L_Outfit" in globals().keys() else "casual1"
    $ LauraX.OutfitDay = L_OutfitDay if "L_OutfitDay" in globals().keys() else "casual1"
    $ LauraX.SeenPeen = L_SeenPeen if "L_SeenPeen" in globals().keys() else 0
    $ LauraX.SeenChest = L_SeenChest if "L_SeenChest" in globals().keys() else 0
    $ LauraX.SeenPussy = L_SeenPussy if "L_SeenPussy" in globals().keys() else 0
    $ LauraX.SeenPanties = L_SeenPanties if "L_SeenPanties" in globals().keys() else 0
    $ LauraX.Upskirt = L_Upskirt if "L_Upskirt" in globals().keys() else 0
    $ LauraX.Uptop = L_Uptop if "L_Uptop" in globals().keys() else 0
    $ LauraX.PantiesDown = L_PantiesDown if "L_PantiesDown" in globals().keys() else 0
    $ LauraX.Wet = L_Wet if "L_Wet" in globals().keys() else 0
    $ LauraX.Water = L_Water if "L_Water" in globals().keys() else 0
    $ LauraX.Spunk = L_Spunk if "L_Spunk" in globals().keys() else []
    $ LauraX.Pierce = L_Pierce if "L_Pierce" in globals().keys() else 0
    $ LauraX.Pubes = L_Pubes if "L_Pubes" in globals().keys() else 1
    $ LauraX.ArmPose = L_ArmPose if "L_ArmPose" in globals().keys() else 1
    $ LauraX.Blush = L_Blush if "L_Blush" in globals().keys() else 0
    $ LauraX.Eyes = L_Eyes if "L_Eyes" in globals().keys() else "normal"
    $ LauraX.Mouth = L_Mouth if "L_Mouth" in globals().keys() else "normal"
    $ LauraX.Brows = L_Brows if "L_Brows" in globals().keys() else "normal"
    $ LauraX.Emote = L_Emote if "L_Emote" in globals().keys() else "normal"
    $ LauraX.Held = L_Held if "L_Held" in globals().keys() else 0
    $ LauraX.Arms = L_Arms if "L_Arms" in globals().keys() else 0
    $ LauraX.Legs = L_Legs if "L_Legs" in globals().keys() else 0
    $ LauraX.Over = L_Over if "L_Over" in globals().keys() else 0
    $ LauraX.Neck = L_Neck if "L_Neck" in globals().keys() else 0
    $ LauraX.Chest = L_Chest if "L_Chest" in globals().keys() else 0
    $ LauraX.Panties = L_Panties if "L_Panties" in globals().keys() else 0
    $ LauraX.Acc = L_Acc if "L_Acc" in globals().keys() else 0
    $ LauraX.Hair = L_Hair if "L_Hair" in globals().keys() else 1
    $ LauraX.Hose = L_Hose if "L_Hose" in globals().keys() else 0
    $ LauraX.Shame = L_Shame if "L_Shame" in globals().keys() else 0
    $ LauraX.Inventory = L_Inventory[:] if "L_Inventory" in globals().keys() else []



    $ LauraX.Custom1 = L_Custom[:] if "L_Custom" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ LauraX.Custom2 = L_Custom2[:] if "L_Custom2" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ LauraX.Custom3 = L_Custom3[:] if "L_Custom3" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ LauraX.TempClothes = L_TempClothes[:] if "L_TempClothes" in globals().keys() else [0,0,0,0,0,0,0,0,0,0,0]
    $ LauraX.Gym = L_Gym[:] if "L_Gym" in globals().keys() else [2,"wrists","leather pants",0,0,"leather bra","leather panties",0,0,0,0]
    $ LauraX.Sleepwear = L_Sleepwear[:] if "L_Sleepwear" in globals().keys() else [0,0,0,0,0,"leather bra","leather panties",0,0,0,20]
    $ LauraX.Swim = L_Swim[:] if "L_Swim" in globals().keys() else [0,0,0,0,0,"bikini top","bikini bottoms",0,0,0,0]

    $ LauraX.Gag = L_Gag if "L_Gag" in globals().keys() else 0
    $ LauraX.Todo = L_Todo[:] if "L_Todo" in globals().keys() else []
    $ LauraX.PubeC = L_PubeC if "L_PubeC" in globals().keys() else 0
    $ LauraX.Clothing = L_Schedule if "L_Schedule" in globals().keys() else [0,0,0,0,0,0,0,0,0,0]

    $ LauraX.Org = L_Org if "L_Org" in globals().keys() else 0
    $ LauraX.OCount = L_OCount if "L_OCount" in globals().keys() else 0
    $ LauraX.Caught = L_Caught if "L_Caught" in globals().keys() else 0
    $ LauraX.Kissed = L_Kissed if "L_Kissed" in globals().keys() else 0
    $ LauraX.Sleep = L_Sleep if "L_Sleep" in globals().keys() else 0
    $ LauraX.Hand = L_Hand if "L_Hand" in globals().keys() else 0
    $ LauraX.Foot = L_Foot if "L_Foot" in globals().keys() else 0
    $ LauraX.Slap = L_Slap if "L_Slap" in globals().keys() else 0
    $ LauraX.Strip = L_Strip if "L_Strip" in globals().keys() else 0
    $ LauraX.Tit = L_Tit if "L_Tit" in globals().keys() else 0
    $ LauraX.Sex = L_Sex if "L_Sex" in globals().keys() else 0
    $ LauraX.Anal = L_Anal if "L_Anal" in globals().keys() else 0
    $ LauraX.Loose = L_Loose if "L_Loose" in globals().keys() else 2
    $ LauraX.Hotdog = L_Hotdog if "L_Hotdog" in globals().keys() else 0
    $ LauraX.Mast = L_Mast if "L_Mast" in globals().keys() else 0
    $ LauraX.FondleB = L_FondleB if "L_FondleB" in globals().keys() else 0
    $ LauraX.FondleT = L_FondleT if "L_FondleT" in globals().keys() else 0
    $ LauraX.FondleP = L_FondleP if "L_FondleP" in globals().keys() else 0
    $ LauraX.FondleA = L_FondleA if "L_FondleA" in globals().keys() else 0
    $ LauraX.DildoP = L_DildoP if "L_DildoP" in globals().keys() else 0
    $ LauraX.DildoA = L_DildoA if "L_DildoA" in globals().keys() else 0
    $ LauraX.Vib = L_Vib if "L_Vib" in globals().keys() else 0
    $ LauraX.Plug = L_Plug if "L_Plug" in globals().keys() else 0
    $ LauraX.SuckB = L_SuckB if "L_SuckB" in globals().keys() else 0
    $ LauraX.InsertP = L_InsertP if "L_InsertP" in globals().keys() else 0
    $ LauraX.InsertA = L_InsertA if "L_InsertA" in globals().keys() else 0
    $ LauraX.LickP = L_LickP if "L_LickP" in globals().keys() else 0
    $ LauraX.LickA = L_LickA if "L_LickA" in globals().keys() else 0
    $ LauraX.Blow = L_Blow if "L_Blow" in globals().keys() else 0
    $ LauraX.Swallow = L_Swallow if "L_Swallow" in globals().keys() else 0
    $ LauraX.CreamP = L_CreamP if "L_CreamP" in globals().keys() else 0
    $ LauraX.CreamA = L_CreamA if "L_CreamA" in globals().keys() else 0
    $ LauraX.Les = L_Les if "L_Les" in globals().keys() else 0
    $ LauraX.LesWatch = L_LesWatch if "L_LesWatch" in globals().keys() else 0
    $ LauraX.SEXP = L_SEXP if "L_SEXP" in globals().keys() else 0
    $ LauraX.PlayerFav = L_PlayerFav if "L_PlayerFav" in globals().keys() else 0
    $ LauraX.Favorite = L_Favorite if "L_Favorite" in globals().keys() else 0


    $ LauraX.Acc = L_Boots if "L_Boots" in globals().keys() else 0
    $ LauraX.Home = "bg laura"

    $ LauraX.Outfit = "casual1" if LauraX.Outfit == "mission" else LauraX.Outfit
    $ LauraX.OutfitDay = "casual1" if LauraX.OutfitDay == "mission" else LauraX.OutfitDay
    $ LauraX.Outfit = "casual2" if LauraX.Outfit == "street" else LauraX.Outfit
    $ LauraX.OutfitDay = "casual2" if LauraX.OutfitDay == "street" else LauraX.OutfitDay

    $ LauraX.Casual1 = [2,"wrists","leather pants",0,0,"leather bra","leather panties",0,0,0,0]
    $ LauraX.Casual2 = [2,0,"skirt",0,"jacket","leather bra","leather panties",0,0,0,0]

    $ LauraX.Schedule = [["bg pool","bg classroom","bg dangerroom","bg laura"],
                                        ["bg dangerroom","bg classroom","bg campus","bg laura"],
                                        ["bg pool","bg classroom","bg dangerroom","bg laura"],
                                        ["bg dangerroom","bg classroom","bg campus","bg laura"],
                                        ["bg pool","bg classroom","bg dangerroom","bg laura"],
                                        ["bg pool","bg laura","bg dangerroom","bg laura"],
                                        ["bg pool","bg laura","bg dangerroom","bg laura"],
                                        ]
    $ LauraX.Hair = "long"
    $ LauraX.LikeRogue = L_LikeRogue if "L_LikeRogue" in globals().keys() else 500
    $ LauraX.LikeKitty = L_LikeKitty if "L_LikeKitty" in globals().keys() else 500
    $ LauraX.LikeEmma = L_LikeEmma if "L_LikeEmma" in globals().keys() else 500
    $ LauraX.SexRogue = L_SexRogue if "L_SexRogue" in globals().keys() else 0
    $ LauraX.SexKitty = L_SexKitty if "L_SexKitty" in globals().keys() else 0
    $ LauraX.SexEmma = L_SexEmma if "L_SexEmma" in globals().keys() else 0
    $ LauraX.MassageChart = ["shoulders","back","arms","hips","thighs","calves","ass","ass","pussy","pussy"]
    $ LauraX.History.append("met") if "met" not in LauraX.History else LauraX.History

    $ LauraX.ScentTimer = 0
    $ LauraX.Claws = 0

    while len(LauraX.Custom1) < 11:
        $ LauraX.Custom1.append(0)
    while len(LauraX.Custom2) < 11:
        $ LauraX.Custom2.append(0)
    while len(LauraX.Custom3) < 11:
        $ LauraX.Custom3.append(0)
    while len(LauraX.TempClothes) < 11:
        $ LauraX.TempClothes.append(0)
    while len(LauraX.Gym) < 11:
        $ LauraX.Gym.append(0)
    while len(LauraX.Sleepwear) < 11:
        $ LauraX.Sleepwear.append(0)
    while len(LauraX.Swim) < 11:
        $ LauraX.Swim.append(0)


    $ RogueX.Names = ["Rogue"]
    $ RogueX.Petname = R_Petname if "R_Petname" in globals().keys() else "Sugar"
    $ RogueX.Petnames = R_Petnames[:] if "R_Petnames" in globals().keys() else ["Sugar",Player.Name]
    $ RogueX.Pet = R_Pet if "R_Pet" in globals().keys() else "Rogue"
    $ RogueX.Pets = R_Pets[:] if "R_Pets" in globals().keys() else ["Rogue"]
    $ RogueX.History.append("met")

    $ KittyX.Names = ["Kitty"]
    $ KittyX.Petname = K_Petname if "K_Petname" in globals().keys() else Player.Name[:1]
    $ KittyX.Petnames = K_Petnames[:] if "K_Petnames" in globals().keys() else ["sweetie",Player.Name[:1],Player.Name]
    $ KittyX.Pet = K_Pet if "K_Pet" in globals().keys() else "Kitty"
    $ KittyX.Pets = K_Pets[:] if "K_Pets" in globals().keys() else ["Kitty"]

    $ EmmaX.Names = ["Ms. Frost","Emma"]
    $ EmmaX.Petname = E_Petname if "E_Petname" in globals().keys() else "young man"
    $ EmmaX.Petnames = E_Petnames[:] if "E_Petnames" in globals().keys() else ["young man",Player.Name]
    $ EmmaX.Pet = E_Pet if "E_Pet" in globals().keys() else EmmaX.Name
    $ EmmaX.Pets = E_Pets[:] if "E_Pets" in globals().keys() else ["Emma","Ms. Frost"]

    $ LauraX.Names = ["X-23","Laura"]
    $ LauraX.Petname = L_Petname if "L_Petname" in globals().keys() else "guy"
    $ LauraX.Petnames = L_Petnames[:] if "L_Petnames" in globals().keys() else ["guy",Player.Name]
    $ LauraX.Pet = L_Pet if "L_Pet" in globals().keys() else LauraX.Name
    $ LauraX.Pets = L_Pets[:] if "L_Pets" in globals().keys() else ["Laura","X-23"]




    if Ch_Focus == "Rogue":
        $ Ch_Focus = RogueX
    elif Ch_Focus == "Kitty":
        $ Ch_Focus = KittyX
    elif Ch_Focus == "Emma":
        $ Ch_Focus = EmmaX
    elif Ch_Focus == "Laura":
        $ Ch_Focus = LauraX

    if "Rogue" in Player.Harem:
        $ Player.Harem.remove("Rogue")
        $ Player.Harem.append(RogueX)
    elif "Kitty" in Player.Harem:
        $ Player.Harem.remove("Kitty")
        $ Player.Harem.append(KittyX)
    elif "Emma" in Player.Harem:
        $ Player.Harem.remove("Emma")
        $ Player.Harem.append(EmmaX)
    elif "Laura" in Player.Harem:
        $ Player.Harem.remove("Laura")
        $ Player.Harem.append(LauraX)

    if "Rogue" in Digits:
        $ Digits.remove("Rogue")
        $ Digits.append(RogueX)
    elif "Kitty" in Digits:
        $ Digits.remove("Kitty")
        $ Digits.append(KittyX)
    elif "Emma" in Digits:
        $ Digits.remove("Emma")
        $ Digits.append(EmmaX)
    elif "Laura" in Digits:
        $ Digits.remove("Laura")
        $ Digits.append(LauraX)

    if "Rogue" in Keys:
        $ Keys.remove("Rogue")
        $ Keys.append(RogueX)
    elif "Kitty" in Keys:
        $ Keys.remove("Kitty")
        $ Keys.append(KittyX)
    elif "Emma" in Keys:
        $ Keys.remove("Emma")
        $ Keys.append(EmmaX)
    elif "Laura" in Keys:
        $ Keys.remove("Laura")
        $ Keys.append(LauraX)

    if "Rogue" in Rules:
        $ Rules.remove("Rogue")
        $ Rules.append(RogueX)
    elif "Kitty" in Rules:
        $ Rules.remove("Kitty")
        $ Rules.append(KittyX)
    elif "Emma" in Rules:
        $ Rules.remove("Emma")
        $ Rules.append(EmmaX)
    elif "Laura" in Rules:
        $ Rules.remove("Laura")
        $ Rules.append(LauraX)

    $ Party = []
    $ del Adjacent
    $ Present = []
    $ Partner = 0
    $ RogueX.OutfitChange(Changed=1)
    $ KittyX.OutfitChange(Changed=1)
    $ EmmaX.OutfitChange(Changed=1)
    $ LauraX.OutfitChange(Changed=1)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
