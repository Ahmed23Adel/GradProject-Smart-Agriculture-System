<template>
<!-- Copied from https://codepen.io/rjmr/pen/zmRrxm -->
<div class="logocontainer">
        <div class="yellowpencil">
            <div class="yellowstrip"></div>
            <div class="yellowrubbertip"></div>
            <div class="yellowrubberend"></div>
            <div class="yellowtip">
                <div class="lead"></div>
            </div>
        </div>
        <div class="bluepencil">
            <div class="bluepencilstrip"></div>
            <div class="bluepencilend"></div>
            <div class="bluepenciltop"></div>
            <div class="bluepenciltext"></div>
            <div class="bluepenciltip">
                <div class="lead"></div>
            </div>
        </div>
        <div class="ruler">
            <div class="rulerlines"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines2"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines2"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines2"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines2"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines2"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines"></div>
            <div class="rulerlines"></div>
        </div>
        <div class="biro">
            <div class="birotip"></div>
            <div class="biroclip"></div>
            <div class="birostrip"></div>
            <div class="birotop"></div>
        </div>
        <div class="highlighter">
            <div class="highlighterstrip"></div>
            <div class="highlighternib"></div>
            <div class="highlightertop"></div>
            <div class="highlightertip"></div>
            <div class="highlighterclip"></div>
        </div>
    </div>
</template>

<style scoped>
.logocontainer {
    position: absolute;
    margin: auto;
    top: 0px;
    bottom: 0;
    left: 0;
    right: 0;
    width: 200px;
    height: 220px;
    border-style: solid;
    border-width: 0 0 2px 0;
    transform: scale(1.5, 1.5);
}

.logocontainer .bottomline {
    position: absolute;
    letter-spacing: 2px;
    font-family: "verdana";
    font-size: 10px;
    text-align: center;
    top: 230px;
    width: 200px;
    height: 40px;
    color: grey;
}

a {
    position: relative;
    letter-spacing: 2px;
    font-family: "verdana";
    font-size: 10px;
    text-align: center;
    color: black;
    text-decoration: none;
}

.logocontainer .yellowpencil {
    position: absolute;
    top: 86px;
    left: 5px;
    width: 12px;
    height: 120px;
    border-radius: 10px 10px 0px 0px;
    background-color: #f4d03f;
    animation: bounce 0.5s linear 0s infinite;
    animation-play-state: paused;
}

.logocontainer .bluepencil {
    position: absolute;
    top: 57px;
    left: 42px;
    width: 12px;
    height: 150px;
    background-color: #004462;
    border-radius: 10px 10px 0px 0px;
    animation: bounce 0.5s linear 0.1s infinite;
    animation-play-state: paused;
}

.logocontainer .ruler {
    position: absolute;
    top: 19px;
    left: 80px;
    width: 18px;
    height: 200px;
    background-color: #edf4f9;
    animation: bounce 0.5s linear 0.2s infinite;
    animation-play-state: paused;
}

.logocontainer .biro {
    position: absolute;
    top: 46px;
    left: 124px;
    width: 12px;
    height: 160px;
    border-radius: 10px 10px 0px 0px;
    background-color: #bdbdbd;
    /* overflow: hidden;*/
    animation: bounce 0.5s linear 0.3s infinite;
    animation-play-state: paused;
}

.logocontainer .highlighter {
    position: absolute;
    top: 100px;
    left: 166px;
    width: 24px;
    height: 90px;
    border-radius: 10px 10px 0px 0px;
    background-color: #c0ca33;
    /* overflow: hidden;*/
    animation: bounce 0.5s linear 0.4s infinite;
    animation-play-state: paused;
}

/* Animation control start */

.logocontainer:hover .bluepencil,
.logocontainer:hover .yellowpencil,
.logocontainer:hover .ruler,
.logocontainer:hover .biro,
.logocontainer:hover .highlighter {
    animation-play-state: running;
}

/* Animation control end */
.logocontainer .lead {
    position: absolute;
    margin-left: -4px;
    margin-top: -9px;
    border-top: solid 8px #646464;
    border-left: solid 4px transparent;
    border-right: solid 4px transparent;
}

.logocontainer .yellowtip {
    position: absolute;
    margin-top: 120px;
    border-top: solid 14px #f6ddcc;
    border-left: solid 6px transparent;
    border-right: solid 6px transparent;
}

.logocontainer .yellowrubberend {
    position: absolute;
    width: 12px;
    height: 12px;
    border-radius: 10px 10px 0px 0px;
    background-color: pink;
}

.logocontainer .yellowrubbertip {
    position: absolute;
    margin-top: 12px;
    width: 12px;
    height: 8px;
    background-color: #b4c0c6;
}

.logocontainer .yellowstrip {
    position: absolute;
    margin-left: 4px;
    width: 5px;
    height: 120px;
    background-color: #f9dc6b;
}

.logocontainer .bluepenciltop {
    position: absolute;
    width: 12px;
    height: 25px;
    background-color: black;
    border-radius: 10px 10px 0px 0px;
}

.logocontainer .bluepencilstrip {
    position: absolute;
    margin-top: 10px;
    margin-left: 4px;
    width: 4px;
    height: 150px;
    background-color: #026692;
}

.logocontainer .bluepencilend {
    position: absolute;
    margin-top: 10px;
    width: 12px;
    height: 24px;
    background-color: #cfd8dc;
}

.logocontainer .bluepenciltext {
    position: absolute;
    top: 8px;
    left: -1px;
    color: #a9a9a9;
    transform: rotate(-90deg);
    font-family: "verdana";
    font-size: 10px;
}

.logocontainer .bluepenciltip {
    position: absolute;
    margin-top: 150px;
    border-top: solid 14px #f6ddcc;
    border-left: solid 6px transparent;
    border-right: solid 6px transparent;
}

.logocontainer .rulerlines {
    position: relative;
    margin-top: 5px;
    width: 7px;
    height: 2px;
    background-color: #a9a9a9;
}

.logocontainer .rulerlines2 {
    position: relative;
    margin-top: 5px;
    width: 10px;
    height: 2px;
    background-color: #a9a9a9;
}

.logocontainer .birotop {
    position: absolute;
    left: 0px;
    width: 12px;
    height: 45px;
    border-radius: 10px 10px 0px 0px;
    background-color: #484848;
}

.logocontainer .birostrip {
    position: absolute;
    left: 4px;
    width: 4px;
    height: 160px;
    background-color: #d9d9d9;
}

.logocontainer .birotip {
    position: absolute;
    margin-top: 160px;
    border-top: solid 14px #484848;
    border-left: solid 6px transparent;
    border-right: solid 6px transparent;
}

.logocontainer .biroclip {
    position: absolute;
    top: 15px;
    left: 13px;
    width: 4px;
    height: 55px;
    background-color: #484848;
}

.logocontainer .highlighterstrip {
    position: absolute;
    top: 20px;
    left: 4px;
    width: 15px;
    height: 80px;
    background-color: #cddc39;
}

.logocontainer .highlightertop {
    position: absolute;
    top: 0px;
    left: 0px;
    width: 24px;
    height: 40px;
    border-radius: 10px 10px 0 0;
    background-color: #393939;
}

.logocontainer .highlighterclip {
    position: absolute;
    top: 46px;
    left: 10px;
    width: 4px;
    height: 38px;
    border-radius: 5px;
    background-color: #e6ee9c;
}

.logocontainer .highlightertip {
    position: absolute;
    top: 90px;
    width: 24px;
    height: 18px;
    background-color: #393939;
}

.logocontainer .highlightertip:before {
    content: "";
    position: absolute;
    top: 0px;
    left: 19px;
    width: 6px;
    height: 18px;
    border-top-left-radius: 80% 100%;
    background-color: white;
}

.logocontainer .highlightertip:after {
    content: "";
    position: absolute;
    top: 0px;
    left: -1px;
    width: 6px;
    height: 18px;
    border-top-right-radius: 80% 100%;
    background-color: white;
}

.logocontainer .highlighternib {
    position: absolute;
    top: 100px;
    left: 7px;
    width: 10px;
    height: 18px;
    background-color: #cddc39;
    transform: skewy(20deg);
}

@keyframes bounce {

    0%,
    100% {
        transform: translatey(0px);
    }

    25%,
    75% {
        transform: translateY(-16px);
    }

    50% {
        transform: translatey(-20px);
    }
}
</style>