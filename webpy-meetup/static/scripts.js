$ = jQuery.noConflict();

$(document).ready(function() {
    var restAPI = {
        getResults: function(data, callback) {
            $.ajax({
                url: '/retrievePosts',
                type: 'POST',
                data: data,
                success: function(res) {
                    callback(res);
                }
            });
        }
    };

    $(document).on('submit', '#meetup-search', function(e) {
        e.preventDefault();
        var data = $(this).serialize();
        console.log(data);
        if (data != '' && data != null) {
            restAPI.getResults(data, function(res) {
                console.log(res)
            });
        }
    });

});