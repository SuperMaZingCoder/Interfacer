$(document).ready(function () {
    $(".delete").click((event) => {
        $(event.target).toggleClass("expand");
        $(event.target)
            .parent()
            .parent()
            .find(".message-body")
            .toggleClass("hidden");
    });
    $(".navbar-burger").click(function () {
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
    });
});
