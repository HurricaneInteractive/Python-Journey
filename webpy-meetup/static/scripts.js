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
        },
        autoComplete: function(callback) {
            $.ajax({
                url: '/autoComplete',
                type: 'GET',
                data: {},
                dataType: 'json',
                success: function(res) {
                    if (typeof callback !== 'undefined') {
                        callback(res)
                    }
                }
            })
        }
    };

    var topics = null;

    function find_pattern_in_topics(human) {
        var pattern = '';
        for (var i = 0; i < topics.length; i++) {
            if (topics[i].human == human) {
                pattern = topics[i].name;
                break;
            }
        }
        return pattern;
    }

    restAPI.autoComplete(function(res) {
        topics = res;
    });

    function autocomplete(val, list) {
        var footer = $('<div class="card-footer"></div>');
        if ($('.card.search .card-footer').length < 1) {
            $('.card.search').append(footer);
        }
        footer = $('.card.search .card-footer');
        val = val.toLowerCase();
        matches = [];
        for (var i = 0; i < list.length; i++) {
            var human = list[i].human.toLowerCase();
            if (list[i].name.indexOf(val) !== -1 || human.indexOf(val) !== -1) {
                matches.push(list[i].human);
            }
        }
        $(footer).empty();
        if (matches.length > 0) {
            var ul = $('<ul class="list-group list-group-flush"></ul>');
            $(footer).append(ul);
            ul = footer.find('ul');
            for (var x = 0; x < matches.length; x++) {
                $(ul).append('<li class="list-group-item auto-option">' + matches[x] + '</li>');
            }
        }
        else {
            $(footer).append('<ul class="list-group list-group-flush"><li class="list-group-item">No Results Found.</li></ul>');
        }
    }

    $(document).on('click', 'li.auto-option', function(e) {
        e.preventDefault();
        human = $(this).text();
        $('#topic').val(human);
        $('#meetup-search').submit();
    });

    $('#topic').on('input', function(e) {
        var value = $(this).val();
        if (value.trim() != '') {
            if (topics != null) {
                autocomplete(value, topics);
            }
            else {
                restAPI.autoComplete(function(res) {
                    topics = res;
                    if (res.length > 0) {
                        autocomplete(value, res);
                    }
                });
            }
        }
        else {
            $('.card.search .card-footer').remove();
        }
    });

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
        $('.card.search .card-footer').remove();
        var selection = $('#topic').val();
        selection = find_pattern_in_topics(selection);
        var data = {
            "topic": selection
        }
        if (data != '' && data != null) {
            $(this).find('button[type="submit"]').text('Searching');
            $('#generated-meetups .row').empty();
            if (masonryActive == true) {
                $('#generated-meetups .row').masonry('destroy');
            }
            $('#generated-meetups .row').append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid" class="lds-rolling"><circle cx="50" cy="50" fill="none" stroke="#3086f1" stroke-width="10" r="35" stroke-dasharray="164.93361431346415 56.97787143782138" transform="rotate(330 50 50)"><animateTransform attributeName="transform" type="rotate" calcMode="linear" values="0 50 50;360 50 50" keyTimes="0;1" dur="1s" begin="0s" repeatCount="indefinite"/></circle></svg>');
            restAPI.getResults(data, function(res) {
                $('#generated-meetups .row').empty();
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