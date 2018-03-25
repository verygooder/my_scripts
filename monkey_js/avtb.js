// ==UserScript==
// @name         avtb_exe
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        http://www.222avtb.com/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    function getUrl () {
        var frame = document.getElementById('player_html5_api');
        var url = frame.src;
        alert(url);
    }
    window.onload = getUrl;
    // Your code here...
})();