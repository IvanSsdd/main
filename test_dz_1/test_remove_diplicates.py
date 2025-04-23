import test_remove_duplicates


def remove_duplicates(s):
    return "".join(sorted(set(s), key=s.index))


class TestRemoveDuplicates(remove_duplicates.TestCase):

   

if __name__ == '__main__':
   remove_duplicates.main()

