import barcode
from barcode.writer import ImageWriter

def make_barcode():
    UPC = barcode.get_barcode_class('upc')
    upc = UPC(pk, writer=ImageWriter())
    code = upc.save('upc_code')
    return code

make_barcode()
   


