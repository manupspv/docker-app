document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.select-price').forEach(function(item){
        item.onchange = function(){
            let item_id = item.dataset.itemid;
            let item_type = item.dataset.itemtype;
            let item_name = item.dataset.itemname;
            let item_size = item.value;
            let page = item.dataset.page;
            var url = '/menu/item_price/'
            
            fetch(url, {
                method: 'POST',
                headers:{
                    'Content-Type':'application/json',
                    'X-CSRFToken': csrftoken,
                },
                body: JSON.stringify({'item_type':item_type, 'item_name':item_name, 'item_size': item_size})
            })
            .then((response)=> {
                return response.json()
            })
            .then((data) => {
                if (page == 'mainpage'){
                    document.querySelector(`#price-${item_id}`).innerHTML = `$ ${data.price}`
                    document.querySelector(`button[data-product="${item_id}"]`).dataset.product = `${data.id}`

                }
                else if(page == 'modal'){
                    document.querySelector(`#modalprice-${item_id}`).placeholder = `$ ${data.price}`;
                    document.querySelector(`#modaladd-${item_id}`).dataset.product = `${data.id}`
                    
                    if (document.querySelector(`button[data-checkid="${item_id}"]`) != null){
                        if(document.querySelector(`button[data-checkid="${item_id}"]`).innerHTML == "Remove Extra Cheese"){
                            let newprice = parseFloat(data.price)+ 0.50;
                            document.querySelector(`#modalprice-${item_id}`).placeholder = `$ ${newprice}`;
                        }
                    }

                }
            });
        }
    })
})

document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('button[data-cheese="checkbox"]').forEach(function(item){
        item.onclick = function(){
            let item_id = item.dataset.checkid
            let oldprice = document.querySelector(`#modalprice-${item_id}`);
            let price = oldprice.placeholder.replace(/\$/,'').trim()
            let b_text = item.innerHTML
            if( b_text == 'Extra Cheese: $ 0.50'){
                document.querySelector(`button[data-checkid="${item_id}"]`).innerHTML = "Remove Extra Cheese"
                let newprice = parseFloat(price) + 0.50
                document.querySelector(`#modalprice-${item_id}`).placeholder = `$ ${newprice.toFixed(2)}`
            }
            else{
                document.querySelector(`button[data-checkid="${item_id}"]`).innerHTML = "Extra Cheese: $ 0.50"
                let newprice = parseFloat(price) - 0.50
                document.querySelector(`#modalprice-${item_id}`).placeholder = `$ ${newprice.toFixed(2)}`
            }
        }
    })
})

