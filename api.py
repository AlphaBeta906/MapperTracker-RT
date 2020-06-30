import requests
import re
followlist = {}
index = "1"
names = ["AlphaBeta906", "Rem889", "FREEMoneys", "IgorGamingPL", "ScratchMapping", "Notforc2", "DeltaBlue0", "MapperTracker", "moomoowillie", "Belastan", "geogranerd", "Malayan_mapping", "Ontario_Mapping", "OasisMapping", "DugongMapping", "cyphercat", "Germanczy", "BFDIASpongyFTW", "Dominica_", "Anglo11471215", "Scanat", "MinepieMapping", "MaritimeMapping", "EnjMaps", "madfedad", "Exotos_Mapping", "SquillionthUser", "AFasterSlowpoke", "-catscanmap-", "TheSoccerDude16", "renland_republic", "skyminer1593", "Seany10", "estoniaball-", "TheBoyThatsGood", "Hiuyju", "Finland_ball", "ArizonaMapping", "NJfinalproject", "deet0109", "WisestMiner888", "BetarNicoaMapping", "Countryballs_10", "ChineseChickenKing", "CrashMapping", "aaale", "Marslandare", "flamzer098", "stingy22", "StrayaBall_mapping", "scapanduy", "VisionMapping", "7mapper7", "Luca2464-H", "Argentine_Mapping", "Axel_The_Beagle", "JustYourAverage", "erysenga", "Cambodiaaaaa", "AG1978", "Ethan8games", "OrangeDeather", "EestiBall", "SwagMeisterKing-YT", "ysenthil-sf", "An-n-drew", "BoisZ123", "Malt10", "Polska_Ball", "MuteTheNeko", "sonicalgi", "SubChannelMapping", "tsant2009", "randomguyboi", "vojvodina_mapper", "renland_republic", "Septillion_", "Bryce090309", "Lil_YoshOfficial", "Neptunium-Mapping", "CanadaBalI", "CountryBallFan", "imsonicnoob", "Jesper220", "Ervenion", "-ECCE-", "Bowling-Ball", "NrCookie", "luigi888", "CalifornianMapper", "GeographyStuff", "American_Mapper", "maplife383", "AngeryFAce", "hi-six-100", "FrozenMapping", "SodaMapping1", "Gaumontia22", "FNAFfunny", "France_Mapper", "OttomanMapping", "OasisMapping2", "BlueStarPort", "PigDoge"]
print ("MapperTracker Realtime")
print ("WARNING: This project is slow cause it gets data from the internet, needs internet connection to work")
print ("Writes leaderboard in leaderboard.txt")
print ("If you see bugs or want something to be added please contact AlphaBeta906#5002 in Discord")

for x in names:
        followers = int(re.search(r'Followers \(([0-9]+)\)', requests.get(f'https://scratch.mit.edu/users/' + x + '/followers').text, re.I).group(1))
        followlist[x] = followers

print ("\n")
followlistfinal = sorted(followlist.items(), key=lambda x: x[1], reverse=True)
file = open("leaderboard.txt", "w")
for i in followlistfinal:
        file.write("{}. {} - {}\n".format(index, i[0], i[1]))
        index = int(index)
        index = index + 1
        index = str(index)
file.close()
