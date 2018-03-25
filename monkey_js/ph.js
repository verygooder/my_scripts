// ==UserScript==
// @name         pornhub extract
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://www.pornhub.com/view_video.php*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
function findUrl() {
	var div = document.getElementsByClassName('mhp1138_videoWrapper')[0];
	var video = div.children[0];
	var source = video.children[0];
	var result = source.src;
	alert(result);
}

findUrl();
    // Your code here...
})();