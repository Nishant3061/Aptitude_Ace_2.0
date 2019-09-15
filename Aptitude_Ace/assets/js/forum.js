//for dropDown filter-buttons 
/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
$(".f-d-1").click(function() {
  $(".filter-dropdown-content1").toggleClass("show");
});
$(".f-d-1").hover(function() {
	$(this).children("a").css("color", "black");
}, function() {
	$(this).children("a").css("color", "grey");
});

// Close the dropdown if the user clicks outside of it
$('body').click(function(e) {
    if ($(e.target).closest('.f-d-1').length === 0) {
        $(".filter-dropdown-content1").removeClass("show");
    }
});

//*********************************for popup of ask button***************************************
$(".ask-bgc").click(function() {
	$(".pop-outer, .pop-inner").fadeIn('fast');
	popUpCenterAlign();
});

function popUpCenterAlign() {
	var popInner = $(".pop-inner"),
    top = $(window).scrollTop() + 50;

	popInner.css({'top': top});
}

//on clicking of next button
$(".next-step").click(function() {
	$(".question-details, .choose-topic-dropbtn, .popup-btn").addClass("show");
	$(".ques-instr, .next-step").addClass("hide");
	$(".ques-textarea").css("height", "60px");
});
$(".cancel, .close").click(function() {
	$(".question-details, .choose-topic-dropbtn, .popup-btn").removeClass("show");
	$(".ques-instr, .next-step").removeClass("hide");
	$(".pop-outer, .pop-inner").fadeOut(0);
	$(".ques-textarea").css("height", "80px");
});
