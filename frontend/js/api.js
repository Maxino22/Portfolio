class maxinoHttp {
	constructor() {
		this.profileUrl = 'https://blog.maxino.xyz/profile/';
		this.contactUrl = 'https://blog.maxino.xyz/contacts/';
		this.BlogsUrl = 'http://blogs.maxino.xyz/blogs/';
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

		const resData = response;
		return resData;
	}
}
