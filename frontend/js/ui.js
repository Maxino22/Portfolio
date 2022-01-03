class UI {
	constructor() {
		this.profile_pic = document.getElementById('profile_pic');
		this.bio = document.getElementById('bio');
		this.cv = document.getElementById('cv');
	}
	showProfile(data) {
		this.profile_pic.setAttribute('src', `${data[0].profile_pic}`);
		this.bio.innerHTML = data[0].bio;
		this.cv.setAttribute('href', `${data[0].resume}`);
	}
	showBlogs(blogs) {
		let blogdata = '';
		blogs.results.forEach((results) => {
			blogdata += `
      <div>
      <div class="post">
        <img class="thumbnail" src="${results.thumbnail}" alt="" />
        <div class="post-preview">
          <h6 class="post-title">${results.title}</h6>
          <p class="post-intro">
           ${results.sub_title}
          </p>
          <a href="https://blog.maxino.xyz/blog/${results.slug}">Read More</a>
        </div>
      </div>
    </div>
      `;
		});
		document.querySelector('.post-wrapper').innerHTML = blogdata;
	}
}
