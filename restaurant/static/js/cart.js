document.addEventListener('DOMContentLoaded', function(){
	document.querySelectorAll('.update-cart').forEach(function(item){
		item.onclick = function(){
			let product_id = item.dataset.product
			let action = item.dataset.action
			console.log(product_id,action)

			if (user == 'AnonymousUser'){
				alert("Log In before Ordering");
				window.location.href = "/login/"
			}
			else{
				updateUserOrder(product_id, action);
			}
		
		}
	})
})


function updateUserOrder(product_id, action){

		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'product_id':product_id, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}

