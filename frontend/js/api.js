class maxinoHttp {
	constructor() {
		this.profileUrl = 'http://127.0.0.1:8000/profile/';
		this.contactUrl = 'http://127.0.0.1:8000/contacts/';
		this.BlogsUrl = 'http://127.0.0.1:8000/blogs/';
	}
	async get() {
		const response = await fetch(this.profileUrl);

		const resData = await response.json();
		return resData;
	}

	async getBlog() {
		const response = await fetch(this.BlogsUrl);
		const resData = await response.json();
		return resData;
	}

	async post(data) {
		const response = await fetch(this.contactUrl, {
			method: 'POST',
			headers: {
				'content-type': 'application/json',
			},
			body: JSON.stringify(data),
		});

		const resData = await response.json();
		return resData;
	}
}
