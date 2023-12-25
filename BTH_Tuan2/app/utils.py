def count_cart(cart):
    # Khởi tạo hai biến total_quantity và total_amount với giá trị ban đầu là 0
    total_quantity, total_amount= 0, 0

    # Kiểm tra xem giỏ hàng (cart) có tồn tại hay không
    if cart:
        # Duyệt qua từng sản phẩm trong giỏ hàng và cập nhật total_quantity và total_amount
        for c in cart.values():
            total_quantity += c['quantity']
            total_amount += c['quantity'] * c['price']

    # Trả về một dictionary chứa thông tin tổng số lượng và tổng số tiền của giỏ hàng
    return {
        'total_quantity': total_quantity,
        'total_amount': total_amount
    }