PyThai
======

Some basic python functions for working with the Thai language. For example:

```python
import pythai

pythai.split(u"การที่ได้ต้องแสดงว่างานดี")
>>> u"การ ที่ ได้ ต้อง แสดง ว่า งาน ดี"

pythai.word_count(u"การที่ได้ต้องแสดงว่างานดี")
>>> 8

pythai.contains_thai(u"hello")
>>> False

pythai.contains_thai(u"helloการที่ไ")
>>> True
```

It's meant to be fast and efficient enough to handle large documents without breaking a sweat.

Includes
------------

Currently the library supports these functions:

- Word segmentation (`split`)
- Word count (`word_count`) (faster than counting the result of `split`)
- Whether a string contains Thai or not (`contains_thai`)


Installation
------------

PyThai equires `thailib` to work. You can install it quite easily:

    sudo apt-get install thailib

And then you can simply install `pythai` through **pip**:

    pip install pythai

More
------------

Special thanks to Vee Satayamas for the original python bindings of libthai from C.

This library was written for use in [Gengo](http://www.gengo.com). It's free and open-source under the GNU lesser public license. Any contributions are welcome!


