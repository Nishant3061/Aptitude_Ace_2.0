//for changing color of logo and home on hovering
$(".logohover").hover(function() {
	$(".logo").attr('src', '../static/img/ace-of-spades-onhover.svg');
	$("#home-btn").css("color", "white");
}, function() {
	$(".logo").attr('src', '../static/img/ace-of-spades.svg');
	$("#home-btn").css("color", "#C1C1C1");
});
//on clicking on navbar menu button
function openNav() {
    document.getElementById("myNav").style.width = "100%";
    $("html").css("overflow", "hidden");
}

function closeNav() {
    document.getElementById("myNav").style.width = "0%";
    $("html").css("overflow", "scroll");
}
//for changing color of notifications button on hovering
$(".notification-image").hover(function() {
	$(this).attr('src', '../static/img/notifications-button-onhover.svg');
}, function() {
	$(this).attr('src', '../static/img/notifications-button.svg');
});
//for changing color of profile icon on hovering
$(".profilehover").hover(function() {
	$("#currentScore").css("color", "white");
	$(".arrow-image").attr('src', '../static/img/angle-arrow-down-onhover.svg');
}, function() {
	$("#currentScore").css("color", "#C1C1C1");
	$(".arrow-image").attr('src', '../static/img/angle-arrow-down.svg');
});
//for the dropdown of navbar

$(".profilehover").click(function() {
  $(".navbar-dropdown-content, .arrow_box").toggleClass("show");
});
window.onclick = function(event) {
  if (!event.target.matches('.profilehover, #currentScore')) {
    $(".arrow_box").removeClass("show");
    var dropdowns = document.getElementsByClassName("navbar-dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
