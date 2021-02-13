text_rpf = """\
    Hey {name},
    Hope you're doing great.

    This mail is in reference to your order ID {order_id}

    You can track your order https://google.com/{tracking_details}.

    As requested, we have initiated the return for your order. The return will be picked up from your doorsteps in the next 24-72 hours. Please ensure that the product(s) are in a resaleable condition and all the tags are intact.

    The refund for the product will be initiated once the product is received by us at the warehouse and has passed the QC test.
    If you had paid via COD, then the amount will be refunded in the form of store credits(lifetime validity) which can be redeemed in your future orders.
    For online payments, the amount will be refunded to the payment method used during checkout.

    Please feel free to reach out to us in case you have any questions or concerns.
    Lots of love,
    Team Spirit Animal 

    """

html_rpf = """\
    <html>
        <body>
            Hey {name},<br>
            <p>Hope you're doing great.<br></p>

            <p>This mail is in reference to your order <a href = "https://google.com/{tracking_details}">here</a> <br>

            You can track your order here.</p>
            <p>
            As requested, we have initiated the return for your order. The return will be picked up from your doorsteps in the next 24-72 hours. Please ensure that the product(s) are in a resaleable condition and all the tags are intact.</p>
            <p>
            The refund for the product will be initiated once the product is received by us at the warehouse and has passed the QC test.
            If you had paid via COD, then the amount will be refunded in the form of store credits(lifetime validity) which can be redeemed in your future orders.</p>
            <p>
            For online payments, the amount will be refunded to the payment method used during checkout.</p>

            Please feel free to reach out to us in case you have any questions or concerns.<br>
            Lots of love,<br>
            Team Spirit Animal<br>
        </body>
    </html> 
    """