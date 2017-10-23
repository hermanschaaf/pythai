#-*- coding: UTF-8 -*-
import six
import unittest
import pythai


class TestSentence:
    def __init__(self, sentence, split, word_count, contains_thai=True):
        self.sentence = sentence
        self.split = split
        self.word_count = word_count
        self.contains_thai = contains_thai


class PyThaiCase(unittest.TestCase):

    def setUp(self):
        self.test_sentences = [
            TestSentence(u"hello", "hello", 1, contains_thai=False),
            TestSentence(u"การที่ได้ต้องแสดงว่างานดี", 
                         u"การ ที่ ได้ ต้อง แสดง ว่า งาน ดี", 8),
            TestSentence(u"บริษัทชื่อ XY&Z - คุยกับ xyz@demo.com", 
                         u"บริษัท ชื่อ XY&Z - คุย กับ xyz@demo.com", 7),
            TestSentence(u"ประโยคว่า The quick brown fox jumped over the lazy dogs", 
                         u"ประโยค ว่า The quick brown fox jumped over the lazy dogs", 11),
            TestSentence(u"การ", u"การ", 1),
            TestSentence(u"helloที่ได้ต้อsomehidden", u"hello ที่ ได้ ต้อ somehidden", 5)
        ]


    def test_contains_thai(self):
        for sentence in self.test_sentences:
            self.assertEqual(pythai.contains_thai(sentence.sentence), sentence.contains_thai)


    def test_word_count(self):
        for sentence in self.test_sentences:
            self.assertEqual(pythai.word_count(sentence.sentence), sentence.word_count)


    def test_split(self):
        for sentence in self.test_sentences:
            six.print_(sentence.split, ' '.join(pythai.split(sentence.sentence)))
            self.assertEqual(' '.join(pythai.split(sentence.sentence)), sentence.split)
