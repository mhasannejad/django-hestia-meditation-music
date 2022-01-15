$(document).ready(function () {
    var base_url = window.location.origin;
    var arr = window.location.href.split('/');

    $('.js-example-basic-single').select2();
    $('.js-example-basic-single').on('change', function (e) {
        //var data = e.params.data;
        console.log($('.js-example-basic-single').val());
    });
    $('#submit').click(function () {
        if ($('.js-example-basic-single').val().length > 0) {
            $.ajax({
                url: base_url + '/api/chotels/submit/',
                type: 'POST',
                data: {
                    json_data: JSON.stringify({
                        'chotels': $('.js-example-basic-single').val().join(','),
                        'hotel_id': arr[arr.length - 2]
                    })
                },
                beforeSend: function (xhr, settings) {
                    xhr.setRequestHeader("X-CSRFToken", $("[name='csrfmiddlewaretoken']").val());
                },
                success: function (arg) {
                    $('.js-example-basic-single').val([]).trigger('change');
                    //location.reload()
                }
            }).then(function () {
                $('.js-example-basic-single').val([]).trigger('change');
            });
            alert('انجام شد');
        } else {
            alert("هیچ موردی انتخاب نشده");
        }
    });
});