{
    'name': 'fiskaltrust',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            ('after', 'point_of_sale/static/src/js/Screens/PaymentScreen/PaymentScreen.js',
             'fiskaltrust/static/src/js/Screens/PaymentScreen/PaymentScreen.js'),
        ]
    }
}
