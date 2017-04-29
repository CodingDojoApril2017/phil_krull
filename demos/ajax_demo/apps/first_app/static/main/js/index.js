$(document).ready(function(){
  alert('working jQuery!')
  $('form').submit(function(event){
    event.preventDefault();
    $.ajax({
      url:'/create',
      method:'post',
      data: $(this).serialize(),
      success:function(response){
        console.log(response);
        $('form')[0].reset();
        $('.courses').append(`<p>${response.course.name}</p>`)
      }
    })
  })
})
