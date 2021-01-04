$(function () {

    /* Functions */
  
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-post").modal("show");
        },
        success: function (data) {
          $("#modal-post .modal-content").html(data.html_form);
        }
      });
    };
  
    var saveForm = function () {
        var form = $(this);
        var formData = new FormData(this);

        $.ajax({
            url: form.attr("action"),
            data: formData,
            type: form.attr("method"),
            dataType: 'json',
            cache: false,
            processData: false,
            contentType: false,
            success: function (data) {
                if (data.form_is_valid) {
                    $("#post-table").html(data.html_list);
                    $("#modal-post").modal("hide");
                }
                else {
                    $("#modal-post .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };
  
  
    /* Binding */
  
    // Create post
    $(".js-create-post").click(loadForm);
    $("#modal-post").on("submit", ".js-post-create-form", saveForm);
  
    // Update post
    $("#post-table").on("click", ".js-update-post", loadForm);
    $("#modal-post").on("submit", ".js-post-update-form", saveForm);
    
    // Delete post
    $("#post-table").on("click", ".js-delete-post", loadForm);
    $("#modal-post").on("submit", ".js-post-delete-form", saveForm);
    
});