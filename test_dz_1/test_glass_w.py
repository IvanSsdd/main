import  test_glass_w2


def glass_w(s):
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    return ''.join([char for char in s if char in vowels])

class Testglass_w(test_glass_w2.TestCase):


if __name__ == '__main__':
    glass_w.main()
