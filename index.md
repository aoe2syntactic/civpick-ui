<style>
 img { width: 100%; }
 pre.highlight > button {
     opacity: 0;
 }
 pre.highlight:hover > button {
  opacity: 1;
}

pre.highlight > button:active,
pre.highlight > button:focus {
  opacity: 1;
}
</style>

## Welcome to the Civpick-UI-Project
Created to enjoy an unique look of [civilization drafts](https://aoe2cm.net) on [Nili's](https://twitch.tv/nili_aoe) streams.

| ![The Draft](assets/images/draft.png) |
|:--:|
| How a draft could look like |

Drawings were made and owned by [AgniousPrime](https://twitch.tv/agniousprime).
Code was written by SyntacticSalt (or SyntacticSugar, who knows -- contact on discord SyntacticSugar#1829).

## Installation Instructions and Requirements

### In the browser
 Currently, only Chrome/Chromium is tested and supported.
Firefox might work as well.

1. Install [Tampermonkey](https://www.tampermonkey.net/), a browser addon to support userscripts.
2. [Click here to install the script](https://gist.github.com/mbergen/556b7b2618165fba69abc90f66540a4f/raw/aoe2cm_civ_replacement_TM.user.js).
3. Accept installation when asked by Tampermonkey.
4. You are done! Enjoy a hippo-themed civ draft.

### In OBS
1. Create a "Browser Source" in OBS with the link to the draft
2. Copy the following CSS into the *Custom CSS* section in the source settings.

```css
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

#player-host > .player img[alt~="Aztecs"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliJaguar%20B.png")
}
#player-guest > .player img[alt~="Aztecs"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliJaguar%20R.png")
}
#civgrid img[alt~="Aztecs"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliJaguar%20B.png")
}
#player-host > .player img[alt~="Berbers"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliCamelArcher%20B.png")
}
#player-guest > .player img[alt~="Berbers"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliCamelArcher%20R.png")
}
#civgrid img[alt~="Berbers"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliCamelArcher%20B.png")
}
#player-host > .player img[alt~="Britons"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/nililongbow%20B.png")
}
#player-guest > .player img[alt~="Britons"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/nililongbow%20R.png")
}
#civgrid img[alt~="Britons"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/nililongbow%20B.png")
}
#player-host > .player img[alt~="Bohemians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliBohemians%20B.png")
}
#player-guest > .player img[alt~="Bohemians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliBohemians%20R.png")
}
#civgrid img[alt~="Bohemians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliBohemians%20B.png")
}
#player-host > .player img[alt~="Bulgarians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliKonnik%20B.png")
}
#player-guest > .player img[alt~="Bulgarians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliKonnik%20R.png")
}
#civgrid img[alt~="Bulgarians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliKonnik%20B.png")
}
#player-host > .player img[alt~="Burgundians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliCoustie%20B.png")
}
#player-guest > .player img[alt~="Burgundians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliCoustie%20R.png")
}
#civgrid img[alt~="Burgundians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliCoustie%20B.png")
}
#player-host > .player img[alt~="Burmese"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliArambai%20B.png")
}
#player-guest > .player img[alt~="Burmese"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliArambai%20R.png")
}
#civgrid img[alt~="Burmese"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliArambai%20B.png")
}
#player-host > .player img[alt~="Byzantines"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliCata%20v3%20B.png")
}
#player-guest > .player img[alt~="Byzantines"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliCata%20v3%20R.png")
}
#civgrid img[alt~="Byzantines"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliCata%20v3%20B.png")
}
#player-host > .player img[alt~="Celts"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliWoad%20B.png")
}
#player-guest > .player img[alt~="Celts"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliWoad%20R.png")
}
#civgrid img[alt~="Celts"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliWoad%20B.png")
}
#player-host > .player img[alt~="Chinese"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliChuKoNu%20B.png")
}
#player-guest > .player img[alt~="Chinese"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliChuKoNu%20R.png")
}
#civgrid img[alt~="Chinese"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliChuKoNu%20B.png")
}
#player-host > .player img[alt~="Cumans"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliKipchak%20B.png")
}
#player-guest > .player img[alt~="Cumans"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliKipchak%20R.png")
}
#civgrid img[alt~="Cumans"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliKipchak%20B.png")
}
#player-host > .player img[alt~="Ethiopians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliShotel%20B.png")
}
#player-guest > .player img[alt~="Ethiopians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliShotel%20R.png")
}
#civgrid img[alt~="Ethiopians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliShotel%20B.png")
}
#player-host > .player img[alt~="Franks"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliAxeman%20B.png")
}
#player-guest > .player img[alt~="Franks"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliAxeman%20R.png")
}
#civgrid img[alt~="Franks"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliAxeman%20B.png")
}
#player-host > .player img[alt~="Goths"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliHuskarl2%20B.png")
}
#player-guest > .player img[alt~="Goths"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliHuskarl2%20R.png")
}
#civgrid img[alt~="Goths"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliHuskarl2%20B.png")
}
#player-host > .player img[alt~="Huns"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliTarkan%20B.png")
}
#player-guest > .player img[alt~="Huns"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliTarkan%20R.png")
}
#civgrid img[alt~="Huns"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliTarkan%20B.png")
}
#player-host > .player img[alt~="Incas"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliKamayuk%20B.png")
}
#player-guest > .player img[alt~="Incas"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliKamayuk%20R.png")
}
#civgrid img[alt~="Incas"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliKamayuk%20B.png")
}
#player-host > .player img[alt~="Indians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliEleArch%20B.png")
}
#player-guest > .player img[alt~="Indians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliEleArch%20R.png")
}
#civgrid img[alt~="Indians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliEleArch%20B.png")
}
#player-host > .player img[alt~="Italians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliGenoese%20XBow%20B.png")
}
#player-guest > .player img[alt~="Italians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliGenoese%20XBow%20R.png")
}
#civgrid img[alt~="Italians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliGenoese%20XBow%20B.png")
}
#player-host > .player img[alt~="Japanese"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliSamurai%20B.png")
}
#player-guest > .player img[alt~="Japanese"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliSamurai%20R.png")
}
#civgrid img[alt~="Japanese"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliSamurai%20B.png")
}
#player-host > .player img[alt~="Khmer"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliBallerEle%20B.png")
}
#player-guest > .player img[alt~="Khmer"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliBallerEle%20R.png")
}
#civgrid img[alt~="Khmer"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliBallerEle%20B.png")
}
#player-host > .player img[alt~="Koreans"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliHippoShip%20B.png")
}
#player-guest > .player img[alt~="Koreans"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliHippoShip%20R.png")
}
#civgrid img[alt~="Koreans"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliHippoShip%20B.png")
}
#player-host > .player img[alt~="Lithuanians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliLeitis%20B.png")
}
#player-guest > .player img[alt~="Lithuanians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliLeitis%20R.png")
}
#civgrid img[alt~="Lithuanians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliLeitis%20B.png")
}
#player-host > .player img[alt~="Magyars"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliMH%20B.png")
}
#player-guest > .player img[alt~="Magyars"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliMH%20R.png")
}
#civgrid img[alt~="Magyars"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliMH%20B.png")
}
#player-host > .player img[alt~="Malay"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliKarambit%20B.png")
}
#player-guest > .player img[alt~="Malay"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliKarambit%20R.png")
}
#civgrid img[alt~="Malay"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliKarambit%20B.png")
}
#player-host > .player img[alt~="Malians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliGbeto%20B.png")
}
#player-guest > .player img[alt~="Malians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliGbeto%20R.png")
}
#civgrid img[alt~="Malians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliGbeto%20B.png")
}
#player-host > .player img[alt~="Mayans"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliPlume%20B.png")
}
#player-guest > .player img[alt~="Mayans"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliPlume%20R.png")
}
#civgrid img[alt~="Mayans"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliPlume%20B.png")
}
#player-host > .player img[alt~="Mongols"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliMangudai%20B.png")
}
#player-guest > .player img[alt~="Mongols"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliMangudai%20R.png")
}
#civgrid img[alt~="Mongols"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliMangudai%20B.png")
}
#player-host > .player img[alt~="Persians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliWarEle%20B.png")
}
#player-guest > .player img[alt~="Persians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliWarEle%20R.png")
}
#civgrid img[alt~="Persians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliWarEle%20B.png")
}
#player-host > .player img[alt~="Poles"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliObuch%20B.png")
}
#player-guest > .player img[alt~="Poles"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliObuch%20R.png")
}
#civgrid img[alt~="Poles"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliObuch%20B.png")
}
#player-host > .player img[alt~="Portuguese"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliOrganGun%20B.png")
}
#player-guest > .player img[alt~="Portuguese"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliOrganGun%20R.png")
}
#civgrid img[alt~="Portuguese"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliOrganGun%20B.png")
}
#player-host > .player img[alt~="Saracens"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliMameluke%20B.png")
}
#player-guest > .player img[alt~="Saracens"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliMameluke%20R.png")
}
#civgrid img[alt~="Saracens"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliMameluke%20B.png")
}
#player-host > .player img[alt~="Sicilians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliserjeant%20Bv2.png")
}
#player-guest > .player img[alt~="Sicilians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliserjeant%20Rv2.png")
}
#civgrid img[alt~="Sicilians"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliserjeant%20Bv2.png")
}
#player-host > .player img[alt~="Slavs"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliBoyar%20B.png")
}
#player-guest > .player img[alt~="Slavs"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliBoyar%20R.png")
}
#civgrid img[alt~="Slavs"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliBoyar%20B.png")
}
#player-host > .player img[alt~="Spanish"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliConq%20B.png")
}
#player-guest > .player img[alt~="Spanish"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliConq%20R.png")
}
#civgrid img[alt~="Spanish"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliConq%20B.png")
}
#player-host > .player img[alt~="Tatars"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliFlamingCamel%20B.png")
}
#player-guest > .player img[alt~="Tatars"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliFlamingCamel%20R.png")
}
#civgrid img[alt~="Tatars"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliFlamingCamel%20B.png")
}
#player-host > .player img[alt~="Teutons"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliTeuto2%20B.png")
}
#player-guest > .player img[alt~="Teutons"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliTeuto2%20R.png")
}
#civgrid img[alt~="Teutons"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliTeuto2%20B.png")
}
#player-host > .player img[alt~="Turks"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliJanissary%20B.png")
}
#player-guest > .player img[alt~="Turks"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliJanissary%20R.png")
}
#civgrid img[alt~="Turks"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliJanissary%20B.png")
}
#player-host > .player img[alt~="Vietnamese"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliRattan%20B.png")
}
#player-guest > .player img[alt~="Vietnamese"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliRattan%20R.png")
}
#civgrid img[alt~="Vietnamese"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliRattan%20B.png")
}
#player-host > .player img[alt~="Vikings"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliBerserk%20B%20v2.png")
}
#player-guest > .player img[alt~="Vikings"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliBerserk%20R%20v2.png")
}
#civgrid img[alt~="Vikings"]
{
    content: url("https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/niliBerserk%20B%20v2.png")
}
```
