// ==UserScript==
// @name         aoe2cm civ icon replacement
// @namespace    http://mbergen.de/
// @version      1.6.0
// @downloadURL  https://aoe2syntactic.github.io/civpick-ui/assets/src/aoe2cm_civ_replacement_TM.user.js
// @updateURL    https://aoe2syntactic.github.io/civpick-ui/assets/src/aoe2cm_civ_replacement_TM.user.js
// @description  Replaces Civ Icons in the AoE2 Captains Mode
// @author       mbergen (SyntacticSalt)
// @match        https://aoe2cm.net/*
// @match        https://*.aoe2cm.net/*
// @icon         https://www.google.com/s2/favicons?domain=aoe2cm.net
// @grant        GM_addStyle
// ==/UserScript==

/**
 * This is the mapping that defines which images get replaced by which other images.
 * The string to the left matches the original image used and is just the name + png.
 * On the right two strings can be specified, the first is going to be used for images
 * on the host side as well as in the grid to pick civs from, the second will be used
 * on the guest side of the pick.
 *
 * Any valid URL can be used for replacement images.
 */
let mapping = {
    'armenians.png': ['niliCompositeBowman B.png', 'niliCompositeBowman R.png'],
    'aztecs.png': ['niliJaguar B.png', 'niliJaguar R.png'],
    'berbers.png': ['niliCamelArcher B.png', 'niliCamelArcher R.png'],
    'bengalis.png': ['niliRatha B.png', 'niliRatha R.png'],
    'britons.png': ['nililongbow B.png', 'nililongbow R.png'],
    'bohemians.png': ['niliBohemians B.png', 'niliBohemians R.png'],
    'bulgarians.png': ['niliKonnik B.png', 'niliKonnik R.png'],
    'burgundians.png': ['niliCoustie B.png', 'niliCoustie R.png'],
    'burmese.png': ['niliArambai B.png', 'niliArambai R.png'],
    'byzantines.png': ['niliCata v3 B.png', 'niliCata v3 R.png'],
    'celts.png': ['niliWoad B.png', 'niliWoad R.png'],
    'chinese.png': ['niliChuKoNu B.png', 'niliChuKoNu R.png'],
    'cumans.png': ['niliKipchak B.png', 'niliKipchak R.png'],
    'dravidians.png': ['niliUrumi B.png', 'niliUrumi R.png'],
    'ethiopians.png': ['niliShotel B.png', 'niliShotel R.png'],
    'franks.png': ['niliAxeman B.png', 'niliAxeman R.png'],
    'georgians.png': ['niliMonaspa B.png', 'niliMonaspa R.png'],
    'goths.png': ['niliHuskarl2 B.png', 'niliHuskarl2 R.png'],
    'gurjaras.png': ['niliChakram B.png', 'niliChakram R.png'],
    'hindustanis.png': ['niliGhulam B.png', 'niliGhulam R.png'],
    'huns.png': ['niliTarkan B.png', 'niliTarkan R.png'],
    'incas.png': ['niliKamayuk B.png', 'niliKamayuk R.png'],
    'indians.png': ['niliEleArch B.png', 'niliEleArch R.png'],
    'italians.png': ['niliGenoese XBow B.png', 'niliGenoese XBow R.png'],
    'japanese.png': ['niliSamurai B.png', 'niliSamurai R.png'],
    'khmer.png': ['niliBallerEle B.png', 'niliBallerEle R.png'],
    'koreans.png': ['niliHippoShip B.png', 'niliHippoShip R.png'],
    'lithuanians.png': ['niliLeitis B.png', 'niliLeitis R.png'],
    'magyars.png': ['niliMH B.png', 'niliMH R.png'],
    'malay.png': ['niliKarambit B.png', 'niliKarambit R.png'],
    'malians.png': ['niliGbeto B.png', 'niliGbeto R.png'],
    'mayans.png': ['niliPlume B.png', 'niliPlume R.png'],
    'mongols.png': ['niliMangudai B.png', 'niliMangudai R.png'],
    'persians.png': ['niliWarEle B.png', 'niliWarEle R.png'],
    'poles.png': ['niliObuch B.png', 'niliObuch R.png'],
    'portuguese.png': ['niliOrganGun B.png', 'niliOrganGun R.png'],
    'romans.png': ['niliCenturion B.png', 'niliCenturion R.png'],
    'saracens.png': ['niliMameluke B.png', 'niliMameluke R.png'],
    'sicilians.png': ['niliserjeant Bv2.png', 'niliserjeant Rv2.png'],
    'slavs.png': ['niliBoyar B.png', 'niliBoyar R.png'],
    'spanish.png': ['niliConq B.png', 'niliConq R.png'],
    'tatars.png': ['niliFlamingCamel B.png', 'niliFlamingCamel R.png'],
    'teutons.png': ['niliTeuto2 B.png', 'niliTeuto2 R.png'],
    'turks.png': ['niliJanissary B.png', 'niliJanissary R.png'],
    'vietnamese.png': ['niliRattan B.png', 'niliRattan R.png'],
    'vikings.png': ['niliBerserk B v2.png', 'niliBerserk R v2.png'],
};

let prefix = 'https://aoe2syntactic.github.io/civpick-ui/assets/images/civs/'


function replace_source(el) {
    var key = el.src.split("/").last();

    if (mapping[key]) {
        var userName = document.querySelector('.usernameSelector').textContent;
        var guestName = document.querySelector("#player-guest>.player>.player-head>.player-name").textContent;

        var isGuestSection = el.closest('#player-guest') != null;
        var isHostSection = el.closest('#player-host') != null;
        var userIsGuest = userName === guestName;

        if (isGuestSection || (!isHostSection && !isGuestSection && userIsGuest)) {
            // Guest picks
            if (el.src != prefix + mapping[key][1]) el.src = prefix + mapping[key][1];
        } else {
            // Host picks
            if (el.src != prefix + mapping[key][0]) el.src = prefix + mapping[key][0];
        }
    }

    el.onchange = () => {replace_source(el)};
}

function replace_sources(els) {
    Array.prototype.forEach.call(els, replace_source);
}


(function() {
    'use strict';

    GM_addStyle(".pick, .steal {height: 138px;}");
    GM_addStyle(".ban {height: 138px; width: 112px;");
    GM_addStyle(".ban img, .pick img, .steal img {background: black;}");

    GM_addStyle("div.stretchy-wrapper {padding-bottom: 127.5%;}");

    GM_addStyle("div.stretchy-wrapper>div.stretchy-text {background: rgba(0,0,0,0.5); font-size:18px; font-weight:500; padding 0 0; line-height:1.25;");
    GM_addStyle("div.stretchy-wrapper>div.stretchy-text {text-shadow: 1px 1px 0px black, -1px -1px 0px black, 1px -1px 0px black, -1px 1px 0px black;");

    GM_addStyle(".choice>div>div.stretchy-wrapper {padding-bottom: 126%;}");
    GM_addStyle(".choice>div>div.stretchy-wrapper>div.stretchy-text {font-size: 12px; padding-top:0;}");

    if (!Array.prototype.last){
        Array.prototype.last = function(){
            return this[this.length - 1];
        };
    };

    const checkElements = async selector => {
        while ( document.querySelectorAll(selector).length <= 1) {
            await new Promise( resolve => requestAnimationFrame(resolve) )
        }
        return document.querySelectorAll(selector);
    };

    checkElements(".civ-indicator").then((els) => {
        var imgs = Array.from(els).map(el => el.childNodes[0]).filter(el => {return el;});
        replace_sources(imgs);

        var observers = [];
        els.forEach(el => {
            var callback = function ( mutations, observer ) {
                mutations.forEach((mutation) => {
                    if (mutation.type.includes('childList')) {
                        if (mutation.target.childNodes.length == 0) return;
                        replace_source(mutation.target.childNodes[0]);
                    } else if (mutation.attributeName.includes('src')) {
                        replace_source(mutation.target);
                    }
                });
            };
            var observer = new MutationObserver(callback);
            observer.observe(el, {characterData: true, childList: true, subtree: true, attributes: true});
            observers.push(observer);
        });
    });

})();