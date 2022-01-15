$(document).ready(function () {
    var base_url = window.location.origin;
    var id = window.location.href;
    var arr = id.split('/');
    console.log(arr[arr.length - 2]);

    $.ajax({
        url: base_url + '/api/gethotelimages/' + arr[arr.length - 2] + '/',
        context: document.body
    }).done(function (response) {
        for (const image in response['images']) {
            $('#add_image').before('<div class="col-3">\n' +
                '            <img class="img-thumbnail img-item"\n' +
                '                 src="' + response['images'][image] + '"' +
                '                 srcset="">\n' +
                '            <a href="" class="btn btn-danger btn-block">حذف</a>\n' +
                '        </div>')
        }
        console.log(response['images']);
    });
    $('#but_upload').click(function () {
        console.log('response')
    });
    $('#add_image').click(function () {
        $('#add_image').before(
            '<div class="col-3">\n' +
            '    <form method="post" action="' + base_url + '/api/uploadimageitem/" enctype="multipart/form-data" id="myform">\n' +
            '         <img  class="img-responsive img-item" id="img" width="100" height="100">\n' +
            '         <input type="file" id="file" name="file" />\n' +
            '         <a href="#but_upload" class="but-upload btn btn-success"  id="but_upload">آپلود</a>\n' +
            '    </form>\n' +
            '</div>')
    });


})

