#Return: Pickup Filed

text_rpf = """\
    Hey {name},
    Hope you're doing great.

    This mail is in reference to your order ID {order_id}

    You can track your order https://www.delhivery.com/track/package/{tracking_details}.

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

            <p>This mail is in reference to your order <b>#{order_id}</b><br>

            <b>You can track your order <a href = "https://www.delhivery.com/track/package/{tracking_details}">here</a>.</p></b>
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

# Exchange order: Manifested
text_eom = """\
    Hey {name},

    This  is in reference to your order id #{order_id}

    Your Exchange Order has been Manifested.
    You can track your order at https://www.delhivery.com/track/package/{tracking_details}.

    Lots of love,
    Team Spirit Animal
    """

html_eom = """\
    <html>
        <body>
            Hey {name},<br>
            <br>
            This is in reference to your order <b>#{order_id}</b>
            <br><br>
            <p>Your Exchange Order has been Manifested.<br>
            <b>You can track your order <a href = "https://www.delhivery.com/track/package/{tracking_details}">here</a></b>.<br></p>

            Lots of love,<br>
            Team Spirit Animal<br>
        </body>
    </html>
    """
        

#Exchange Order: Pickup Filed
text_eopf= """\
    Hey {name},
    Hope you're doing great.

    This mail is in reference to your order ID #{order_id}
    As requested, we have initiated the exchange for your order. The return will be picked up from your doorsteps in the next 24-72 hours. Please ensure that the product(s) are in a resaleable condition and all the tags are intact.

    You can track your return shipment https://www.delhivery.com/track/package/{tracking_details}.

    Your exchange will be dispatched in 2-3 business days after the return has been picked up from your shipping address.

    Please feel free to reach out to us in case you have any questions or concerns.
    Lots of love,
    Team Spirit Animal
    """
html_eopf = """\
    <html>
        <body>
            Hey {name},<br>
            Hope you're doing great.<br>
            <p><br>
            This mail is in reference to your order ID <b>#{order_id}</b> <br><br>
            As requested, we have initiated the exchange for your order. The return will be picked up from your doorsteps in the next 24-72 hours. Please ensure that the product(s) are in a resaleable condition and all the tags are intact.
            </p>
            <p>
            <b>You can track your return shipment <a href = "https://www.delhivery.com/track/package/{tracking_details}">here</a>.</b>
            </p>
            <p>
            Your exchange will be dispatched in 2-3 business days after the return has been picked up from your shipping address.
            </p>
            <p>
            Please feel free to reach out to us in case you have any questions or concerns.<br><br>
            Lots of love,<br>
            Team Spirit Animal<br>
            </p>
        </body>
    </html>
    """


# Refund Completed COD
text_rcc = """\
    Hey {name},
    Hope you are doing great.

    Here is the coupon code as a refund for you: {ref_no_refund}
    It has life-time validity, can be used only once, and has no minimum order requirements. This coupon code will offer you Rs. {amount} off on your entire order.

    If you have any questions or concerns, please feel free to reach out to us.
    Lots of love,
    Team Spirit Animal
    """

html_rcc = """\
    <html>
        <body>
            Hey {name},<br>
            Hope you are doing great.<br><br>
            <p>
            Here is the coupon code as a refund for you: <b>{ref_no_refund}</b> <br>
            It has life-time validity, can be used only once, and has no minimum order requirements. This coupon code will offer you <b>Rs.{amount} off</b> on your entire order.
            </p>
            <br>
            If you have any questions or concerns, please feel free to reach out to us. <br>
            Lots of love,<br>
            Team Spirit Animal<br>
        </body>
    </html>
    """


#Refund Completed Prepaid
text_rcp = """\
    Hey {name},
    Hope you are doing great.

    The refund for the amount Rs.{amount} has been done. It might take 5-7 business days for it to be reflected in your account.
    Payment Reference Number: {ref_no_refund}

    If you have any questions or concerns, please feel free to reach out to us.
    Lots of love,
    Team Spirit Animal
    """

html_rcp = """\
    <html>
        <body>
            Hey {name},<br>
            Hope you are doing great.<br>
            <p>
            The refund for the amount <b> Rs. {amount}</b> has been done. It might take 5-7 business days for it to be reflected in your account.<br>
            Payment Reference Number: <b>{ref_no_refund}</b>
            </p>
            <p>
            If you have any questions or concerns, please feel free to reach out to us.<br>
            Lots of love,<br>
            Team Spirit Animal<br>
            </p>
        </body>
    </html>
    """



#Exchange Request Size 6 Confirmation
text_ersc = """\
    Hey {name},

    This is in reference to your order ID #{order_id} .

    We recently received an Exchange request from you, requesting Size 6 product(s).
    We want to inform you that since size 6 orders are custom orders, Rs. 249(for each size 6 product) would be charged to you before we dispatch your size 6 product(s). You can pay us through PayTM, or GPay. We will file the pickup as soon as we get the confirmation from your side that you are willing to pay Rs. 249 (for each size 6 product), after which we will file the pickup from your side ASAP.

    Please give us confirmation in reply to this email.

    You can also talk to our Size-Guide Expert if you want to know what size will be best for you. You can call her anytime from 1pm-6pm or message her on WhatsApp (Don't forget to mention your OrderNo)

    Kriti
    +91-98100-56172
    Size-Guide Expert

    Lots of love,
    Team Spirit Animal
    """

html_resc = """\
    <html>
        <body>
            Hey {name},
            <br><br>
            This is in reference to your order ID <b>#{order_id} </b>
            <br><br>
            We recently received an Exchange request from you, requesting Size 6 product(s).<br>
            We want to inform you that since size 6 orders are custom orders, Rs. 249(for each size 6 product) would be charged to you before we dispatch your size 6 product(s). You can pay us through PayTM, or GPay. <b>We will file the pickup as soon as we get the confirmation from your side</b> that you are willing to pay Rs. 249 (for each size 6 product), after which we will file the pickup from your side ASAP.
            <br><br>
            Please give us confirmation in reply to this email.
            <br><br>
            You can also talk to our Size-Guide Expert if you want to know what size will be best for you. You can call her anytime from 1pm-6pm or message her on WhatsApp (Don't forget to mention your OrderNo)
            <br><br>
            <b>Kriti</b><br>
            +91-98100-56172<br>
            <i>Size-Guide Expert</i>
            <br><br>    
            Lots of love,<br>
            Team Spirit Animal
        </body>
    </html>
    """
