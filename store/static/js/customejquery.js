$(document).ready(function() {

    $(window).scroll(function() {

        var height = $('.first-container').height();
        var scrollTop = $(window).scrollTop();

        if (scrollTop >= height - 40) {
            $('.navbar').addClass('top-nav-collapse');
        } else {
            $('.navbar').removeClass('top-nav-collapse');
        }

    });
});