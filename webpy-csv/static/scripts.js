$ = jQuery.noConflict();
$(document).ready(function() {
    $(document).on('submit', '#csv-upload', function(e) {
        e.preventDefault();
        // var data = $('#csv_upload')[0];
        var fd = new FormData();
        fd.append('csv_upload', $('#csv_upload')[0].files[0]);
        $.ajax({
            url: '/processCSV',
            data: fd,
            type: 'POST',
            contentType: false,
            processData: false,
            dataType: 'json',
            success: function(res) {
                code = JSON.stringify(res, null, 4);
                $('#result').parent().show();
                $('#result').empty().append('<pre>' + code + '</pre>');
            },
            error: function(err) {
                console.log(err);
            }
        });
    });
});