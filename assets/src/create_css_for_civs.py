from urllib.parse import quote

url_prefix = 'https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/'

mapping = {
    'aztecs': ['niliJaguar B', 'niliJaguar R'],
    'berbers': ['niliCamelArcher B', 'niliCamelArcher R'],
    'britons': ['nililongbow B', 'nililongbow R'],
    'bulgarians': ['niliKonnik B', 'niliKonnik R'],
    'burgundians': ['niliCoustie B', 'niliCoustie R'],
    'burmese': ['niliArambai B', 'niliArambai R'],
    'byzantines': ['niliCata v3 B', 'niliCata v3 R'],
    'celts': ['niliWoad B', 'niliWoad R'],
    'chinese': ['niliChuKoNu B', 'niliChuKoNu R'],
    'cumans': ['niliKipchak B', 'niliKipchak R'],
    'ethiopians': ['niliShotel B', 'niliShotel R'],
    'franks': ['niliAxeman B', 'niliAxeman R'],
    'goths': ['niliHuskarl2 B', 'niliHuskarl2 R'],
    'huns': ['niliTarkan B', 'niliTarkan R'],
    'incas': ['niliKamayuk B', 'niliKamayuk R'],
    'indians': ['niliEleArch B', 'niliEleArch R'],
    'italians': ['niliGenoese XBow B', 'niliGenoese XBow R'],
    'japanese': ['niliSamurai B', 'niliSamurai R'],
    'khmer': ['niliBallerEle B', 'niliBallerEle R'],
    'koreans': ['niliHippoShip B', 'niliHippoShip R'],
    'lithuanians': ['niliLeitis B', 'niliLeitis R'],
    'magyars': ['niliMH B', 'niliMH R'],
    'malay': ['niliKarambit B', 'niliKarambit R'],
    'malians': ['niliGbeto B', 'niliGbeto R'],
    'mayans': ['niliPlume B', 'niliPlume R'],
    'mongols': ['niliMangudai B', 'niliMangudai R'],
    'persians': ['niliWarEle B', 'niliWarEle R'],
    'portuguese': ['niliOrganGun B', 'niliOrganGun R'],
    'saracens': ['niliMameluke B', 'niliMameluke R'],
    'sicilians': ['niliserjeant Bv2', 'niliserjeant Rv2'],
    'slavs': ['niliBoyar B', 'niliBoyar R'],
    'spanish': ['niliConq B', 'niliConq R'],
    'tatars': ['niliFlamingCamel B', 'niliFlamingCamel R'],
    'teutons': ['niliTeuto2 B', 'niliTeuto2 R'],
    'turks': ['niliJanissary B', 'niliJanissary R'],
    'vietnamese': ['niliRattan B', 'niliRattan R'],
    'vikings': ['niliBerserk B v2', 'niliBerserk R v2'],
};


full_css = ""

prefix = "img"
guest_prefix = "#player-guest > .player"
host_prefix = "#player-host > .player"
grid_prefix = "#civgrid"

for key, value in mapping.items():
    blue = quote(value[0] + ".png")
    red = quote(value[1] + ".png")

    host = f"{host_prefix} {prefix}[alt~=\"{key.capitalize()}\"]"
    host += f"{{content: url(\"{url_prefix+blue}\")}}"
    
    guest = f"{guest_prefix} {prefix}[alt~=\"{key.capitalize()}\"]"
    guest += f"{{content: url(\"{url_prefix+red}\")}}"

    grid = f"{grid_prefix} {prefix}[alt~=\"{key.capitalize()}\"]"
    grid += f"{{content: url(\"{url_prefix+blue}\")}}"

    full_css += host + "\n" + guest + "\n" + grid

print(full_css)