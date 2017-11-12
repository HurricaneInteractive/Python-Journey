$ = jQuery.noConflict();

$(document).ready(function() { 
    $('body').bootstrapMaterialDesign();

    var api = {
        routes: {
            "home": "/",
            "login": "/login"
        },
        register_user: function(data) {
            $.ajax({
                url: '/postregistration',
                type: 'POST',
                data: data,
                success: function(res) {
                    console.log(res);
                    window.location.href = api.routes.login;
                }
            });
        },
        login_user: function(data) {
            $.ajax({
                url: '/check-login',
                type: 'POST',
                data: data,
                success: function(res) {
                    if (res == "error") {
                        alert("Could not login");
                    }
                    else {
                        window.location.href = api.routes.home;
                    }
                }
            });
        },
        logout: function() {
            $.ajax({
                url: '/logout',
                type: 'GET',
                success: function(res) {
                    if (res == 'success') {
                        window.location.href = api.routes.login
                    }
                    else {
                        alert("Something went wrong");
                    }
                }
            });
        },
        post: function(data) {
            $.ajax({
                url: '/post-activity',
                type: 'POST',
                data: data,
                success: function(res) {
                    console.log(res);
                    window.location.href = api.routes.home;
                }
            })
        },
        update_user_info: function(data) {
            $.ajax({
                url: '/update-settings',
                type: 'POST',
                data: data,
                success: function(res) {
                    if (res == "success") {
                        location.reload();
                    }
                    else {
                        alert(res)
                    }
                }
            });
        },
        comment: function(data) {
            $.ajax({
                url: "/submit-comment",
                type: "POST",
                data: data,
                success: function(res) {
                    window.location.reload(true);
                }
            })
        }
    };

    $(document).on("submit", "#register-form", function(e) {
        e.preventDefault();
        var form = $('#register-form').serialize();
        api.register_user(form);
    });

    $(document).on("submit", '#login-form', function(e) {
        e.preventDefault();
        var form = $(this).serialize();
        api.login_user(form);
    });

    $('#logout').on('click', function(e) {
        e.preventDefault();
        api.logout();
    });

    $(document).on("submit", '#post-activity', function(e) {
        e.preventDefault();
        var form = $(this).serialize();
        api.post(form);
    });

    $(document).on("submit", "#settings-form", function(e) {
        e.preventDefault();
        var form = $(this).serialize();
        api.update_user_info(form);
    });

    $(document).on('submit', '.comment-form', function(e) {
        e.preventDefault();
        var form = $(this).serialize();
        api.comment(form);
    });

    $('#profile-tabs a').click(function (e) {
        e.preventDefault();
        $(this).tab('show');
    });

});