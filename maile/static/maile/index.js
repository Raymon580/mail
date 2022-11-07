$(document).ready(() => {
    $("div#compose-view").hide();

    $("a.nav-link").click((e) => { 
        switchTabs(e);
    });

    $("button#compose").click(() => {
        compose();
    })
});

function switchTabs(event) {
    if (event.target.className === "nav-link active") {
        return;
    } else {
        $(".nav-link.active").toggleClass("active");
        event.target.className = "nav-link active";
    }
}

function compose() {
    $("div.container").hide();
    $("div#compose-view").show();
}