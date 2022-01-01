const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

let theme = localStorage.getItem('theme');

if (theme == null) {
	setTheme('light');
} else {
	setTheme(theme);
}

let themeDots = document.getElementsByClassName('theme-dot');

for (var i = 0; themeDots.length > i; i++) {
	themeDots[i].addEventListener('click', function () {
		let mode = this.dataset.mode;
		console.log('Option clicked:', mode);
		setTheme(mode);
	});
}

function setTheme(mode) {
	if (mode == 'light') {
		document.getElementById('theme-style').href = 'css/style.css';
	}

	if (mode == 'dark') {
		document.getElementById('theme-style').href = 'css/dark.css';
	}

	if (mode == 'bot') {
		document.getElementById('theme-style').href = 'css/bot.css';
	}

	localStorage.setItem('theme', mode);
}

// TabPanels
// save all the tabs in avariable
const tabs = document.querySelectorAll('.tab');

// go over each one of the tabs
tabs.forEach((tab) => {
	// for each tab, listen for the event 'click'
	tab.addEventListener('click', function () {
		// make the tabs change class .active on click
		let activeTab = document.querySelector('.active');
		activeTab.classList.remove('active'); //remove the class ative from the tab is active now
		tab.classList.add('active'); // add the class active to the tab that I clicked

		// make the content-tabs change the class visible on click
		let dataTab = tab.getAttribute('data-tab'); //save the attribute data-tab of the tab I have just clicked
		let contentTab = document.getElementById(dataTab); //find the content-tab with id the same as the attribute data-tab that I just clicked
		let visibleContentTab = document.querySelector('.visible'); // find the contant-tab that is visible

		visibleContentTab.classList.remove('visible'); // remove the class visible from the content-tab that is visible now
		contentTab.classList.add('visible'); //add class visible to the contant-tab with the same id as the attribute data-tab that I clicked
	});
});

// form handing

const form = document.getElementById('contact-form');
const senderName = document.getElementById('name');
const senderSubject = document.getElementById('subject');
const senderEmail = document.getElementById('email');
const senderMessage = document.getElementById('message');
const alertBox = document.getElementById('alert');

form.addEventListener('submit', handleMessage);

function handleMessage(e) {
	console.log(senderEmail.value, senderName.value);

	const data = {
		name: senderName.value,
		subject: senderSubject.value,
		email: senderEmail.value,
		message: senderMessage.value,
	};

	const http = new maxinoHttp();

	http
		.post(data)
		.then((data) => console.log(data))
		.catch((err) => console.log(err));

	// clear values
	senderName.value = '';
	senderSubject.value = '';
	senderEmail.value = '';
	senderMessage.value = '';

	alertBox.innerHTML = `<div class="alert"> 
   <span class="msg">Message Recieved</span> 
   <span class="fas fa-check"></span>
 </div>`;

	//timeout after 3 seconds
	setTimeout(() => {
		alertBox.innerHTML = '';
	}, 3000);

	e.preventDefault();
}

const http = new maxinoHttp();
const ui = new UI();
//  The api part
document.addEventListener('DOMContentLoaded', addProfile);

function addProfile() {
	http
		.get()
		.then((data) => {
			ui.showProfile(data);
		})
		.catch((err) => console.log(err));
	http
		.getBlog()
		.then((blogs) => {
			ui.showBlogs(blogs);
			console.log(blogs);
		})
		.catch((err) => console.log(err));
}
