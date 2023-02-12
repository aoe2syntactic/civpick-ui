from urllib.parse import quote
from textwrap import dedent

url_prefix = 'https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/'

mapping = {
    'aztecs': ['niliJaguar B', 'niliJaguar R'],
    'berbers': ['niliCamelArcher B', 'niliCamelArcher R'],
    'bengalis': ['niliCamelRatha B', 'niliRatha R'],
    'britons': ['nililongbow B', 'nililongbow R'],
    'bohemians': ['niliBohemians B', 'niliBohemians R'],
    'bulgarians': ['niliKonnik B', 'niliKonnik R'],
    'burgundians': ['niliCoustie B', 'niliCoustie R'],
    'burmese': ['niliArambai B', 'niliArambai R'],
    'byzantines': ['niliCata v3 B', 'niliCata v3 R'],
    'celts': ['niliWoad B', 'niliWoad R'],
    'chinese': ['niliChuKoNu B', 'niliChuKoNu R'],
    'cumans': ['niliKipchak B', 'niliKipchak R'],
    'dravidians': ['niliUrumi B', 'niliUrumi R'],
    'ethiopians': ['niliShotel B', 'niliShotel R'],
    'franks': ['niliAxeman B', 'niliAxeman R'],
    'goths': ['niliHuskarl2 B', 'niliHuskarl2 R'],
    'gurjaras': ['niliChakram B', 'niliChakram R'],
    'hindustanis': ['niliGhulam B', 'niliGhulam R'],
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
    'poles': ['niliObuch B', 'niliObuch R'],
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


full_css = dedent("""\
            body {
                background-color: rgba(0, 0, 0, 0);
                margin: 0px auto;
                overflow: hidden;
            }

            .pick,
            .steal {
                height: 138px;
            }

            .ban {
                height: 138px;
                width: 112px;
            }

            .ban img,
            .pick img,
            .steal img {
                background: black;
            }

            div.stretchy-wrapper {
                padding-bottom: 127.5%;
            }

            div.stretchy-wrapper>div.stretchy-text {
                background: rgba(0, 0, 0, 0.5);
                font-size: 18px;
                font-weight: 500;
                line-height: 1.25;
            }

            div.stretchy-wrapper>div.stretchy-text {
                text-shadow: 1px 1px 0px black, -1px -1px 0px black, 1px -1px 0px black, -1px 1px 0px black;
            }

            .choice>div>div.stretchy-wrapper {
                padding-bottom: 126%;
            }

            .choice>div>div.stretchy-wrapper>div.stretchy-text {
                font-size: 12px;
                padding-top: 0;
            }
            """)

prefix = "img"
guest_prefix = "#player-guest > .player"
host_prefix = "#player-host > .player"
grid_prefix = "#civgrid"

for key, value in mapping.items():
    blue = quote(value[0] + ".png")
    red = quote(value[1] + ".png")

    full_css += dedent(f"""
                {host_prefix} {prefix}[alt~=\"{key.capitalize()}\"]
                {{
                    content: url(\"{url_prefix+blue}\")
                }}
                {guest_prefix} {prefix}[alt~=\"{key.capitalize()}\"]
                {{
                    content: url(\"{url_prefix+red}\")
                }}
                {grid_prefix} {prefix}[alt~=\"{key.capitalize()}\"]
                {{
                    content: url(\"{url_prefix+blue}\")
                }}""")

print(full_css)