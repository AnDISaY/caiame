$(document).ready(function() {
    $('.select-wrapper select').on('focus', function() {
        $(this).parent().addClass('active');
    }).on('blur', function() {
        $(this).parent().removeClass('active');
    });

    $('.select-wrapper select').on('change', function() {
        $(this).blur();
    });

    $('.select-wrapper select').on('click', 'option', function() {
        $(this).closest('.select-wrapper').removeClass('active');
    });

    $(document).click(function(e) {
        if (!$(e.target).closest('.select-wrapper').length) {
            $('.select-wrapper').removeClass('active');
        }
    });

    $('.select-wrapper select').click(function(e) {
        e.stopPropagation();
    });
});