#Los test se deben aclarar, es decir, indicar en el nombre de es un test (test_proccessor.py)
from proccessor import clean_id #indicmaos que revice si hay un archivo proccessory si en ester archivo esta la función clean_id y que la importe
def test_clean_id():
    assert clean_id("cc-75.087.345")=="75087345"

from proccessor import clean_id, merge_name #Se pueden poner varias
def test_clean_id():
    assert clean_id("cc-75.087.345")=="75087345"
def test_merge_name():
    assert merge_name("Luis","Gallego")=="Luis Gallego"
