from django.db import models

# Create your models here.
class Product( models.Model ) :

    AMERICAN_DOLLAR = 'USD';
    LEBANESE_POUND  = 'LBP';

    CURRENCY_CHOICES = [

        ( AMERICAN_DOLLAR, 'USD' ),
        ( LEBANESE_POUND, 'LBP' ),

    ];

    sku         = models.CharField( max_length = 255, default = '' );
    title       = models.CharField( max_length = 255 );
    description = models.TextField();
    price       = models.PositiveIntegerField();
    currency    = models.CharField(

        max_length = 3,
        choices = CURRENCY_CHOICES,
        default = AMERICAN_DOLLAR,

    );
    created_at  = models.DateTimeField( 'date created', auto_now_add = True );

    def __str__(self):
        return self.title
