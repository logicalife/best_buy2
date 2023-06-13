import pytest
import products


def test_normal_product():
    normal_product = products.Product("New Item name", price=450, quantity=100)
    assert isinstance(normal_product, products.Product)


def test_invalid_product():
    with pytest.raises(ValueError):
        assert products.Product("", price="xyz", quantity=25.50)


def test_prod_status_inactive():
    normal_active_product = products.Product("New Item name", price=450, quantity=100)
    assert normal_active_product.is_active() == True
    normal_active_product.set_quantity(0)
    assert normal_active_product.is_active() == False


def test_prdct_purchase_modify_qty_and_output():
    normal_active_product = products.Product("New Item name", price=450, quantity=100)
    assert normal_active_product.buy(10) == 4500
    assert normal_active_product.get_quantity() == 90


def test_buying_too_much():
    normal_active_product = products.Product("New Item name", price=450, quantity=100)
    with pytest.raises(Exception):
        assert normal_active_product.buy(200)
