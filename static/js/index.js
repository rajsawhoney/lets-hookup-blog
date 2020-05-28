// Toggle Fav Article Functionality
$(document).on("click", ".fav_btn", function (event) {
	event.preventDefault();
	var pk = $(this).attr("post-id");
	txtid = "fav-div" + pk;
	var id = get_correct_id(txtid);
	console.log("ID ", pk);
	var csrftoken = getCookie("csrftoken");
	console.log(csrftoken);
	console.log(id);



	$.ajax({
		type: "POST",
		url: $(this).attr('url'),
		data: {
			csrfmiddlewaretoken: csrftoken,
		},
		dataType: "json",
		success: function (response) {
			$(`#${id}`).html(response["fav_data"]);
			console.log("Fav article toggled!");
		},
		error: function (rs, e) {
			console.error(rs.responseText);
		},
	});
});


// $(document).on('click', '.fav_btn', (event) => {
// 	event.preventDefault();
// 	console.log("I am cliked to add or remove article to or from MyFav List... ");
// 	console.log("Target Url ", $('form.add-remove-fav').attr('action'));
// 	const post_id = $(this).attr('post-id')
// 	console.log("Post ID new", post_id);
// 	console.log("Url:", $('.fav_btn').attr('url'));


// 	$.ajax({
// 		type: "post",
// 		url: $(this).attr('url'),
// 		data: {
// 			'csrfmiddlewaretoken': getCookie('csrftoken'),
// 		},
// 		dataType: "json",
// 		success: function (response) {
// 			$('.fav-div1').html(response['fav_data']);
// 			// console.log(response['fav_data']);

// 			console.log("Fav article toggled!");

// 		},
// 		error: (err) => {
// 			console.log("Facing Problems:");

// 			console.log(err.responseText);
// 			$('#fav-error-div').html(err.responseText);

// 		}
// 	});
// });

// Confirmation PopUp
$(document).on('click', '.delete-post-btn', function (env) {
	$('#delete-post-confirm-modal').modal('show');

});

// Action of confirmation
$(document).on('submit', 'form.delete-post', function (env) {
	env.preventDefault();
	const id = $(this).attr('post-id');
	console.log("We are in for the delete post process!!!!!!");

	$.ajax({
		type: "post",
		url: '/testapp/delete-article/',
		data: {
			'id': id,
			'csrfmiddlewaretoken': getCookie('csrftoken'),
		},
		dataType: "json",
		success: function (response) {
			$('#delete-post-confirm-modal').modal('hide');
			location.assign('/testapp/your/articles/');
			console.log("Got successs");
			console.log(response);
		},
		error: function (err) {
			console.log(err.responseText);
		}
	});

});


// Follow User Functionality
$(document).on("submit", "form.follow-profile", function (e) {
	e.preventDefault();
	url = "/testapp/articles/follow/";
	const id = $(this).attr("userid");
	var postid = "empty";
	postid = $(this).attr("postid");
	console.log("postid is ", postid);

	var roughid = "";
	if (postid === undefined) {
		roughid = "follow-my-btn" + id;
		console.log("Its if territory");
	} else {
		roughid = "follow-my-btn" + postid;
		console.log("Its else territory");
	}

	const valid_id = get_correct_id(roughid);
	console.log(valid_id);

	$.ajax({
		type: "post",
		url: url,
		data: {
			id: id,
			csrfmiddlewaretoken: getCookie("csrftoken"),
		},
		dataType: "json",
		success: function (response) {
			if (response["success"] === "followed") {
				$(`#${valid_id}`).html(
					'<i class="fa fa-link" aria-hidden="true"> Following</i>'
				);
				console.log("Success in following user");
			} else {
				$(`#${valid_id}`).html(
					'<i class="fa fa-link" aria-hidden="true"> Follow</i>'
				);
				console.log("Success in unfollowing");
			}
		},
		error: function (err) {
			console.log("Error in following user");
			console.error(err.responseText);
		},
	});
});

// Reply btn toggle functionality
$(document).on("click", ".replybtn", function (event) {
	event.preventDefault();
	var form_id = $(this).attr("comment_id");
	txtid = "reply_div" + form_id;
	var id = get_correct_id(txtid);
	console.log(id);
	$(`#${id}`).fadeToggle('slow');

});

// Comment btn toggle functionality
$(document).on("click", ".commenthandler", function (event) {
	event.preventDefault();
	console.log("I am really called now!!!");
	var form_id = $(this).attr("article_id");
	txtid = "comment_div" + form_id;
	var id = get_correct_id(txtid);
	console.log(id);
	$(`#${id}`).fadeToggle('slow');

});

// Ajax update article Functionality
$(document).on("submit", ".updateform", function (event) {
	event.preventDefault();
	console.log("Udpate form submitted!");
	var url = $(this).attr("action");
	$('#update-spinner').html = '<span class="spinner-border spinner-border-md" role="status"></span> <span class="sr-only">Updating...</span>'
	$.ajax({
		type: "POST",
		url: url,
		data: $("form.updateform").serialize(),
		dataType: "json",
		success: function (response) {
			console.log("Update OK!!!");
			$("#alert-area").html(response["form"]);
			$('#update-spinner').html='Updated'
			$("#updatestatus-modal").modal("show");
			setTimeout(() => {
				$("#updatestatus-modal").modal("hide");
			}, 4000);
		},
		error: function (e) {
			console.log(e.responseText);
		},
	});
});

// $(document).on('mouseover', '.commentbutton', function () {
// 	var is_authenticated = $(this).attr('auth-status')
// 	console.log("I am In with ", is_authenticated);

// 	if (!is_authenticated) {
// 		console.log("Not an authenticated user...!!!");
// 		var alert = document.getElementById('login-alert')
// 		alert.style.display = "block";
// 		$('#login-alert').css("display", "block");

// 	} else {
// 		console.log("An Authenticated User!");
// 	}
// });


// Edit comment form toggle
$(document).on('click', '.editbtn', function (e) {
	e.preventDefault();
	var roughid = 'edit-comment-sec' + $(this).attr('comment_id');

	console.log("Rough ID:", roughid);
	var id = get_correct_id(roughid);
	$(`#${id}`).fadeToggle('slow');

	console.log('correctId', id);
	var comment_id = $(this).attr('comment_id');

	var edit_area_id = 'edit-area' + comment_id;
	edit_area_id = get_correct_id(edit_area_id);
	$.ajax({
		type: "post",
		url: "/testapp/edit-comment/form/",
		data: {
			'comment_id': comment_id,
			'csrfmiddlewaretoken': getCookie('csrftoken'),
		},
		dataType: "json",
		success: function (response) {
			console.log("Edit comment form put successfully!");
			$(`#${edit_area_id}`).val(response['comment_txt']);

		},
		error: function (err) {
			console.log("Failed to put comment form!!!");
			console.log(err.responseText);
		}
	});

});


// Edit Comment Request Functionality

$(document).on('submit', 'form.edit-comment-form', function (e) {
	e.preventDefault();
	console.log("Data submitted!!!!!!!");

	var comment_id = $(this).attr('comment_id')

	var btnid = 'edit-comment-sec' + comment_id;

	var comment_display_sec_id = 'reply_comment_div' + $(this).attr('article_id');

	console.log('article_id is ', $(this).attr('article_id'));


	comment_display_sec_id = get_correct_id(comment_display_sec_id);


	console.log('comment_display_sec_id', comment_display_sec_id);

	btnid = get_correct_id(btnid);

	var edit_area_id = 'edit-area' + comment_id;
	edit_area_id = get_correct_id(edit_area_id);

	const comment_txt = $(`#${edit_area_id}`).val()
	console.log('comment Data: ', comment_txt);

	$.ajax({
		type: "post",
		url: "/testapp/edit-comment/",
		data: {
			'id': comment_id,
			'comment_txt': comment_txt,
			'csrfmiddlewaretoken': getCookie('csrftoken'),
		},
		dataType: "json",
		success: function (response) {
			console.log("Comment edited successfully!");
			$(`#${btnid}`).css('display', 'none');
			$('.comment_div').html(response["form"]);
		},

		error: function (err) {
			console.log("Failed to edit comment!!!");
			console.log(err.responseText);
		}
	});
});



// Ajax Reply & Comment Functionality
$(document).on("submit", "form.reply_comment_form", function (event) {
	event.preventDefault();
	var is_authenticated = $(this).attr("auth-status");
	console.log("Hi I am working!");
	console.log("Auth status ", is_authenticated);
	if (is_authenticated === "True") {
		var url = $(this).attr("url");
		var roughid = "";
		var form_id = $(this).attr("article_id");
		roughid = "reply_comment_div" + form_id;

		var id = get_correct_id(roughid);
		console.log(id);

		$.ajax({
			type: "POST",
			url: url,
			data: $(this).serialize(),
			dataType: "json",
			success: function (response) {
				$(`#${id}`).html(response["form"]);
				$("textarea").val("");
			},
			error: function (es, e) {
				console.log(es.responseText);
				$("#error-div").html(es.responseText);
			},
		});
	} else {
		console.log("Not an authenticated User!!!");
		var alert = document.getElementById("login-alert");
		alert.style.display = "block";
		setTimeout(() => {
			alert.style.display = "none";
		}, 7000);
	}
});

//Ajax Reply Functionality
// $(document).on("submit", "form.replyform", function (event) {
//   event.preventDefault();
//   console.log("Hi I am working!");
//   var url = $(this).attr("url");
//   console.log(url);
//   var comment_id = $(this).attr("comment_id");
//   txtid = "reply_div" + comment_id;
//   var id = get_correct_id(txtid);
//   console.log(id);
//   $.ajax({
//     type: "POST",
//     url: url,
//     data: $(this).serialize(),
//     dataType: "json",
//     success: function (response) {
//       $(`#${id}`).html(response["form"]);
//       $("textarea").val("");
//     },
//     error: function (es, e) {
//       console.log(es.responseText);
//       $("textarea").val("");
//       $("#error-div").html(es.responseText);
//     },
//   });
// });

// Share Article Functionality
function shareArticle(url) {
	location.assign(url);
}

// Clapping Functionality
$(document).on("submit", "form.clap", function (event) {
	event.preventDefault();
	console.log("Clapping iniated...");
	const pk = $(this).attr("comment_id");
	console.log("Id is ", pk);
	var roughId = "clap-div" + pk;
	var claproughid = 'clapping-music' + pk;
	var id = get_correct_id(roughId);
	const clapid = get_correct_id(claproughid);
	console.log("ClapId", clapid);

	var clap_alert = document.getElementById(clapid);

	$.ajax({
		type: "post",
		url: $(this).attr("action"),
		data: {
			pk: pk,
			csrfmiddlewaretoken: getCookie("csrftoken"),
		},
		dataType: "json",
		success: function (response) {
			$(`#${id}`).html(response["form"]);
			clap_alert.load();
			clap_alert.play();
			setTimeout(() => {
				clap_alert.pause();
			}, 5000);

			console.log("Clapped!");
		},
		error: function (e) {
			console.error(e.responseText);
		},
	});
});

// Like Button Toggle Ajax Functionality
$(document).on("click", ".likebutton", function (event) {
	event.preventDefault();
	var pk = $(this).attr("data-catid");
	txtid = "like-section" + pk;
	var id = get_correct_id(txtid);
	console.log(pk);
	var csrftoken = getCookie("csrftoken");
	console.log(csrftoken);
	console.log(id);



	$.ajax({
		type: "POST",
		url: "/testapp/likepost/",
		data: {
			id: pk,
			csrfmiddlewaretoken: csrftoken,
		},
		dataType: "json",
		success: function (response) {
			$(`#${id}`).html(response["form"]);
		},
		error: function (rs, e) {
			console.error(rs.responseText);
		},
	});
});

function scroll_to_comment() {
	var handler = document.getElementById("scrolled_to");
	handler.scrollIntoView();
}

// $(document).on('mouseover', '.likebutton', function (event) {
// 	event.preventDefault();
// 	$("#myModal").modal("show");

// });

// $(document).on('mouseout', '.likebutton', function (event) {
// 	event.preventDefault();
// 	$("#myModal").modal("hide");

// });

//correct id calculator
function get_correct_id(roughid) {
	var correct_id = "";
	for (let i = 0; i < roughid.length; i++) {
		if (roughid[i] == " " || roughid[i] == "\n") {
			continue;
		} else {
			correct_id += roughid[i];
		}
	}
	return correct_id;
}

// csrf token generator
function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== "") {
		var cookies = document.cookie.split(";");
		for (var i = 0; i < cookies.length; i++) {
			var cookie = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === name + "=") {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}