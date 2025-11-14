import unittest

from hello import sayhello


class SayHelloTestCase(unittest.TestCase):  # 测试用例

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_sayhello(self):
        rv = sayhello()
        self.assertEqual(rv, 'Hello!')

    def test_sayhello_to_somebody(self):
        rv = sayhello(to='czp')
        self.assertEqual(rv, 'Hello, czp!')

if __name__ == '__main__':
    unittest.main()