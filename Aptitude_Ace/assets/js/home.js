
//on hovering over score container
$(".score-block-round").hover(function() {
	$(this).css("font-size", "2em");
}, function() {
	$(this).css("font-size", "1.8em");
});
//on hovering of filter-dropdown
$(".filter-hover").hover(function() {
  $(this).css("color", "#292929");
  $(this).children("#filter-angle").css("color", "#292929");
}, function() {
  $(this).css("color", "#5E5E5E");
  $(this).children("#filter-angle").css("color", "#D1D1D1");
});
//on hovering to get check
$(".filter-dropdown-content a").hover(function() {
  $(this).children("#filter-checkicon").css("color", "#D3D3D3");
},function() {
  $(this).children("#filter-checkicon").css("color", "white");
});

//for dropDown filter-buttons
/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
$(".f-d-1").click(function() {
  $(".filter-dropdown-content1").toggleClass("show");
});

// Close the dropdown if the user clicks outside of it
$('body').click(function(e) {
    if ($(e.target).closest('.f-d-1').length === 0) {
        $(".filter-dropdown-content1").removeClass("show");
    }
});

$(".f-d-2").click(function() {
  $(".filter-dropdown-content2").toggleClass("show");
});
$('body').click(function(e) {
    if ($(e.target).closest('.f-d-2').length === 0) {
        $(".filter-dropdown-content2").removeClass("show");
    }
});

$(".f-d-3").click(function() {
  $(".filter-dropdown-content3").toggleClass("show");
});
$('body').click(function(e) {
    if ($(e.target).closest('.f-d-3').length === 0) {
        $(".filter-dropdown-content3").removeClass("show");
    }
});
//when hovering on option of question

$(".option").hover(function() {
  $(this).children(".option-number").css("border-color", "#ADADAD");
}, function() {
  $(this).children(".option-number").css("border-color", "#EBEBEB");
});
//on hovering over bookmark
$(".bookmark-circle").hover(function() {
  $(".bookmark-hover").show();
  $(".bookmark-circle").css("border-color", "#33A1C9");
  $(".fa-star").css("color", "#33A1C9");
}, function() {
  $(".bookmark-hover").hide();
  $(".bookmark-circle").css("border-color", "#EBEBEB");
  $(".fa-star").css("color", "#EBEBEB");
});
