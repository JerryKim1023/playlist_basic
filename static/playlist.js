$(document).ready(function () {
    listing();
});

function listing() {

    $.ajax({
        type: 'GET',
        url: '/playlist',
        data: {},
        success: function (response) {
            let rows = response['lists']
            for (let i = 0; i < rows.length; i++) {
                
                let title = rows[i]['title']
                let image = rows[i]['image']                   
                let url = rows[i]['url']
                let job = rows[i]['job']
                let comment = rows[i]['comment']

                let temp_html = `<div class="col">
                                    <div class="card h-100">
                                        <a href="${url}" target="_blank"><img src="${image}"
                                            class="card-img-top"></a>
                                        <div class="card-body">
                                            <h5 class="card-title">${comment}</h5>
                                            <p>업종 : ${job}</p>
                                            <p class="mycomment">${title}</p>
                                        </div>
                                    </div>
                                </div>`

                $('#cards-box').append(temp_html)
            }
            console.log(response['lists'])
        }
    })
}



function posting() {
    let url = $('#url').val()
    let job = $('#job').val()
    let comment = $('#comment').val()

    $.ajax({
        type: 'POST',
        url: '/playlist',
        data: { url_give: url, job_give: job, comment_give: comment },
        success: function (response) {
            alert(response['msg'])
            window.location.reload()
        }
    });
}

function open_box() {
    $('#post-box').show()
}
function close_box() {
    $('#post-box').hide()
}