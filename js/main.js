var CARD_JSON_FILES = {
	'codechef': {
		'file': 'codechef.json', 'block-identifier': 'codechef', 'sections': [
			'rating:rating',
			'best_rating:bestrating',
			'global_rank:grank',
			'country_rank:crank'
		]
	},
	'codeforces': {
		'file': 'codeforces.json', 'block-identifier': 'codeforces', 'sections': [
			'last_activity:last-seen',
			'rank:textrank',
			'best_rating:bestrating',
			'rating:rating'
		]
	},
	'leetcode': {
		'file': 'leetcode.json', 'block-identifier': 'leetcode', 'sections': [
			'last_activity:last-seen',
			'global_rank:grank',
			'total_solved:solved',
			'rating:rating',
			'contests_participated:contests'
		]
	},
	'atcoder': {
		'file': 'atcoder.json', 'block-identifier': 'atcoder', 'sections': [
			'rating:rating',
			'last_activity:last-seen',
			'rank:grank',
			'best_rating:bestrating',
			'contests_participated:contests'
		]
	},
	'uva': {
		'file': 'uva.json', 'block-identifier': 'uva', 'sections': [
			'global_rank:grank',
			'last_activity:last-seen',
			'past7d_solved:last7d',
			'past31d_solved:last31d',
			'past3m_solved:last3m',
			'past1y_solved:last1y',
			'total_solved:solved'
		]
	}
}

$(document).ready(function () {
	'use strict';

	//********* page loader js

	setTimeout(function () {
		$('.loader_bg').fadeToggle();
	}, 1500);

	//********** menu background color change while scroll

	$(window).on('scroll', function () {
		var menu_area = $('.nav-area');
		if ($(window).scrollTop() > 200) {
			menu_area.addClass('sticky_navigation');
		} else {
			menu_area.removeClass('sticky_navigation');
		}
	});


	//********** menu hides after click (mobile menu)

	$(document).on('click', '.navbar-collapse.in', function (e) {
		if ($(e.target).is('a') && $(e.target).attr('class') != 'dropdown-toggle') {
			$(this).collapse('hide');
		}
	});


	//*********** scrollspy js

	$('body').scrollspy({
		target: '.navbar-collapse',
		offset: 195
	});


	//************ smooth scroll js

	$('a.smooth-menu,a.dadada,a.skill-btn').on("click", function (e) {
		e.preventDefault();
		var anchor = $(this);
		$('html, body').stop().animate({
			scrollTop: $(anchor.attr('href')).offset().top - 50
		}, 1000);
	});

	//*********** Animated headline js

	$('.animate-scale').animatedHeadline({
		animationType: 'clip'
	});

	/**
	 * Reading JSON files and update cards
	 */
	$("#last-updated").text(formatDate(Date.now()))
	updateCards();


});

function updateCards() {
	Object.keys(CARD_JSON_FILES).forEach(key => {
		var payload = CARD_JSON_FILES[key];
		readJSONFFile(payload['file'], (data) => {
			let block = $(`#${payload['block-identifier']}`)
			let sections = payload['sections']
			sections && sections.forEach(item => {
				let splitArr = item.split(":");
				let htmlFieldName = splitArr[1];
				let jsonFieldName = splitArr[0];
				let foundItems = $(block).find(`.${htmlFieldName}`);
				foundItems.each((index, item) => {
					if (jsonFieldName === 'last_activity' && typeof data[jsonFieldName] != undefined) {
						if (key === 'codeforces') {
							data[jsonFieldName] = data[jsonFieldName] * 1000;
						}
						if (data[jsonFieldName] == 0) {
							$(item).text("N/A");
						} else if (isNaN(data[jsonFieldName])) {
							$(item).text((data[jsonFieldName]));
						} else {
							$(item).text(formatDate(data[jsonFieldName]));
						}
					} else {
						$(item).text(data[jsonFieldName]);
					}
				});
			})
		});
	});
}

function readJSONFFile(file, callback) {
	$.getJSON(file, function (data) {
		callback(data[0])
	});
}

function formatDate(timestamp) {
	const monthNames = ["January", "February", "March", "April", "May", "June",
		"July", "August", "September", "October", "November", "December"];
	let dateObj = new Date(Number.parseInt(timestamp));
	let month = monthNames[dateObj.getMonth()];
	let day = String(dateObj.getDate()).padStart(2, '0');
	let year = dateObj.getFullYear();
	let output = `${day}, ${month} ${year}`;
	return output;
}