import unittest
import homework3

class hw3UnitTestCases(unittest.TestCase):

    def test_column_names(self):
        """
        check if only the expected column names are present
        """
        db_path = "/Users/whamsy/Desktop/class.db"
        df_to_test = homework3.create_dataframe(db_path)
        cols_to_have = ['category_id','language','video_id']
        self.assertEqual(sorted(df_to_test.columns), cols_to_have)

    def test_num_rows(self):
        """
        check if number of records is as expected (taking value of rows from
        result obtained in sqlite outside python)
        """
        db_path = "/Users/whamsy/Desktop/class.db"
        df_to_test = homework3.create_dataframe(db_path)
        rows_to_have = 35950
        self.assertEqual(df_to_test.shape[0],rows_to_have)

    def test_column_not_key(self):
        """
        Testing that no combination of columns that isnt ['category_id', 'video_id', 'language']
        constitutes a key
        """
        db_path = "/Users/whamsy/Desktop/class.db"
        df_to_test = homework3.create_dataframe(db_path)

        test_not_key_sets = [['video_id'],['category_id'],['language'],['video_id', 'language'],['category_id', 'video_id'],['category_id','language']]

        for cat_group in test_not_key_sets:
            grp = df_to_test.groupby(cat_group)
            self.assertNotEqual(df_to_test.shape[0], len(grp))

    def test_column_key(self):
        """
        Testing that ['category_id', 'video_id', 'language'] constitutes a key
        """
        db_path = "/Users/whamsy/Desktop/class.db"
        df_to_test = homework3.create_dataframe(db_path)

        test_key_set = ['category_id', 'video_id', 'language']

        grp = df_to_test.groupby(test_key_set)
        self.assertEqual(df_to_test.shape[0], len(grp))

    def test_path(self):
        """
        check if correct error raised on wrong path input
        """
        self.assertRaises(ValueError, homework3.create_dataframe,'random/path/null.db')


if __name__ == '__main__':
    unittest.main()
