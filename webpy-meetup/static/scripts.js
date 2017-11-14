$ = jQuery.noConflict();

$(document).ready(function() {
    var restAPI = {
        getResults: function(data, callback) {
            $.ajax({
                url: '/retrievePosts',
                type: 'POST',
                data: data,
                dataType: 'json',
                success: function(res) {
                    callback(res);
                },
                error: function(err) {
                    console.log(err);
                }
            });
        }
    };

    var masonryActive = false;

    function generate_structure(content) {
        element = `
            <div class="card">`;
            if (content.imageUrl != null || content.imageUrl != '') {
                element += `<div class="card-image" style="${content.imageUrl} height: 200px;"></div>`;
            }
        element += `
                <div class="card-body">
                    <h4 class="card-title">${content.title}</h4>
                    <a target="_blank" href="${content.link}">View</a>
                </div>
            </div>
        `;
        return $(element);
    }

    $(document).on('submit', '#meetup-search', function(e) {
        e.preventDefault();
        var data = $(this).serialize();
        console.log(data);
        if (data != '' && data != null) {
            $(this).find('button[type="submit"]').text('Searching');
            $('#generated-meetups .row').empty();
            if (masonryActive == true) {
                $('#generated-meetups .row').masonry('destroy');
            }
            restAPI.getResults(data, function(res) {
                $('#meetup-search').find('button[type="submit"]').text('Search');
                meetups = res;
                for (var i = 0; i < meetups.length; i++) {
                    var elem = generate_structure(meetups[i]);
                    $('#generated-meetups .row').append(elem);
                }
                $('#generated-meetups .row').masonry({
                    gutter: 10,
                    itemSelector: '.card'
                });
                masonryActive = true;
            });
        }
    });

});