$(".go_up_1").on("mouseover", function () {
    $(".go_up_1").stop().animate({
        height: "220px"});
});
$(".go_up_1").on("mouseout", function() {
    $(".go_up_1").stop().animate({
        height: "150px"
    });
});
$(".go_up_2").on("mouseover", function () {
    $(".go_up_2").stop().animate({
        height: "220px"});
});
$(".go_up_2").on("mouseout", function() {
    $(".go_up_2").stop().animate({
        height: "150px"
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const link = document.querySelector('.link-hover-animation');

    link.addEventListener('mouseover', () => {
        link.classList.add('bounce-animation');
    });

    link.addEventListener('animationend', () => {
        link.classList.remove('bounce-animation');
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const body = document.querySelector('body');
    body.classList.add('visible');
});

document.addEventListener('DOMContentLoaded', () => {
    const link = document.querySelector('.link-shake');

    link.addEventListener('click', (event) => {
        event.preventDefault();
        link.classList.add('shake-animation');
        link.addEventListener('animationend', () => {
            link.classList.remove('shake-animation');
            window.location.href = link.href; // Redirect after the animation
        }, { once: true });
    });
});