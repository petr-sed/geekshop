/**
 * Created by 482 on 24.06.2019.
 */
window.onload = function () {
    $(".basket_list").on('click', 'input[type="number"]', function () {
        var t_href = event.target;

        $.ajax({
            url: "/basket/edit/" + t_href.name + "/?quantity=" + t_href.value,
        });

        event.preventDefault();
    });
}