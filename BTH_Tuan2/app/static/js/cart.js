function addToCart(id,name,price){
//Fetch API là một API đơn giản cho việc gửi và nhận request bằng js.
//Với fetch thì việc thực hiện các yêu cầu web và xử lý phản hồi dễ dàng hơn so với XMLHttpRequest cũ.
    fetch('/api/cart',{
    method:"post",
    body: JSON.stringify({ // Chuyển từ data sang SJON
           "id" : id,
           "name" : name,
           "price": price
    }),
    headers: {
        'Content-Type':"application/json"
    }
    }).then(function(res){
        return res.json();

    }).then(function(data){
        let c = document.getElementsByClassName('cart-counter');
        for( let d of c)
            d.innerText = data.total_quantity
    })
}

function updateCart(id, obj){
    obj.disabled=true;
    fetch(`/api/cart/${id}`,{
        method:'put',
        body:JSON.stringify({
            'quantity' : obj.value
        }),
        headers: {
            'Content-Type':"application/json"
//           xác định rằng dữ liệu đang được gửi đi ở định dạng JSON.
        }
    }).then(res=>res.json()).then(data=>{
    obj.disabled = false;
      let c = document.getElementsByClassName('cart-counter');
      for( let d of c)
        d.innerText = data.total_quantity

      let a = document.getElementsByClassName('cart-total');
      for( let d of a)
        d.innerText = data.total_amount
    })
}

function deleteCart(id, obj){
    if (confirm("Ban chac chan muon xoa khong") ===true){
        obj.disabled=true;
        fetch(`/api/cart/${id}`,{
            method:'delete',
        }).then(res=>res.json()).then(data=>{
        obj.disabled = false;
          let c = document.getElementsByClassName('cart-counter');
            for( let d of c)
                d.innerText = data.total_quantity

            let r = document.getElementById(`product${id}`);
            r.style.display = "none"
        })
    }
}