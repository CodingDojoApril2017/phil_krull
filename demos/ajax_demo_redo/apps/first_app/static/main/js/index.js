$(document).ready(function(){
  // alert('working jQuery!')
  $.get({
    url:"http://pokeapi.co/api/v2/pokemon/1",
    success:function(response){
      console.log(response);
    }
  })
  $('form').submit(function(event){
    console.log(event);
    console.log('event');
    event.preventDefault();
    $.ajax({
      url:'/create',
      method:'post',
      data:$(this).serialize(),
      success:function(response){
        console.log(response);
        $('.courses').append(`<p>Name: ${response.name}, Description: ${response.description}</p>`)
        $('form')[0].reset();
      }
    })
  })
})
