from pydantic import BaseModel

class Product(BaseModel):
    product_title: str = "1 x GDC Extraction Forceps Lower Molars – 86 Ergonomic (FX86E)"
    product_price: float = 850.00
    path_to_image: str = "https://dentalstall.com/wp-content/uploads/2021/11/GDC-Extraction-Forceps-Lower-Molars-86A-Standard-FX86AS.jpg"
