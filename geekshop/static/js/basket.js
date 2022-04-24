window.onload = function () {
    $('.basket-list').on('click', 'input[type="number"]', function () {
        let t_href = event.target;
        console.log(t_href.name, t_href.value);

        $.ajax(
            {
                url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",
                success: function (data) {
                    $('.basket-list').html(data.result)
                }
            }
        )
    })


    $('.card-add-basket').on('click', 'button[type="button"]', function () {
        let t_href = event.target.value;
        console.log(t_href);

        $.ajax(
            {
                url: "/basket/add/" + t_href + "/",
                success: function (data) {
                    $('.card-add-basket').html(data.result)
                }
            }
        )
    })
}