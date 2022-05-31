import converters
from converters import lbs_to_kg
#import ecommerce.shipping
#from ecommerce.shipping import calc_shipping,calc_discount
from ecommerce import shipping

shipping.calc_shipping()
shipping.calc_discount()
#ecommerce.shipping.calc_shipping()
print(lbs_to_kg(177))
print(converters.kg_to_lbs(80))