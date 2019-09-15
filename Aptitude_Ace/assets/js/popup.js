$(".forget").click(function() {
	$(".pop-outer, .pop-inner").fadeIn('fast');
	popUpCenterAlign();
});

function popUpCenterAlign() {
	var popInner = $(".pop-inner"),
    //top = $(window).scrollTop();
    top = 60;
	popInner.css({'top': top});
}

$(".close").click(function() {
	$(".pop-outer, .pop-inner").fadeOut(0);
});
