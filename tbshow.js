function run () {
	var anchor = document.getElementsByClassName('tb-tab-anchor')[1];
	anchor.click();
	clickPic();
}

function clickPic () {
	var point = document.getElementById('reviews-t-val3');
	if (point === null) {
		setTimeout(clickPic, 500);
	}
	else {
		point.click();
		exePics();
	}
}

function exePics () {
	var all = document.getElementsByClassName('photo-item');
	var result = [];
	if (all.length !== 0) {
		for (var i of all) {
		var url = i.children[0].src;
		result.push(url);
        }
    var short_urls = exeUrls(result);
    builtDom(short_urls);
    }
	else {
		setTimeout(exePics, 500);
	}

}

function exeUrls (array) {
	var reg = /https:.*?jpg/;
	var result = [];
	for (var url of array) {
		var big_pic_url = reg.exec(url)[0];
		result.push(big_pic_url);
	}
	return result;
}

function builtDom (urls) {
	var insert = document.getElementById('J_TabBarWrap');
	var insert_upper_dom = insert.parentElement;
	var new_dom = document.createElement('div');
	for (var url of urls) {
		var img = document.createElement('img');
		img.src = url;
		img.height = '400';
		new_dom.appendChild(img);
	}
	insert_upper_dom.insertBefore(new_dom, insert);
}

window.onload = run;