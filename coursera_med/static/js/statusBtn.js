$('#my-form').on('submit', function(event) {
    event.preventDefault();
    $.ajax({
      url: window.location.pathname,
      type: 'POST',
      data: $(this).serialize(),
      success: function() {
        const statusBtn = document.querySelector('.lecture__status-btn'),
        statusBtn2 = document.querySelector('.lecture__status-btn2'),
        form = document.getElementById('my-form');
        
        form.remove()
        statusBtn.style.display = 'none';
        statusBtn2.style.display = 'flex';
        }
    });
  });