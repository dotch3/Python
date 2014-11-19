import unittest 


from matrix import MatrixGenerator

class MatrixGeneratorTest(unittest.TestCase):

    # def test_matrix_generator_generates_an_empty_matrix_if_n_is_zero(self):
    #     generator = MatrixGenerator(n=0)
    #     self.assertEqual(0, len(generator.generate_matrix()))

    # def test_matrix_generator_should_generate_the_numbers_to_fill_in_the_matrix_according_to_n(self):
    #     generator = MatrixGenerator(n=0)

    #     self.assertEqual([], generator.numbers)

    #     self.assertEqual([1, 2, 3, 4], MatrixGenerator(n=2).numbers)

    # def test_can_fill_top_right_cell_returns_false_if_col_and_row_are_zero(self):
    #     generator = MatrixGenerator(n=2)

    #     self.assertFalse(generator.can_fill_top_right_cell(0, 0))

    # def test_can_fill_top_right_cell_returns_true_if_there_is_a_cell_one_position_at_the_right_and_one_position_at_the_top_of_the_given_cell(self):
    #     generator = MatrixGenerator(n=3)

    #     self.assertTrue(generator.can_fill_top_right_cell(1, 0))
    #     self.assertTrue(generator.can_fill_top_right_cell(1, 1))
    #     self.assertTrue(generator.can_fill_top_right_cell(2, 0))
    #     self.assertTrue(generator.can_fill_top_right_cell(2, 1))

    # def test_can_fill_top_right_cell_should_return_false_if_the_cell_is_in_the_top_or_right_limit_of_the_matrix(self):
    #     generator = MatrixGenerator(n=3)

    #     self.assertFalse(generator.can_fill_top_right_cell(0, 0))
    #     self.assertFalse(generator.can_fill_top_right_cell(0, 1))
    #     self.assertFalse(generator.can_fill_top_right_cell(0, 2))
    #     self.assertFalse(generator.can_fill_top_right_cell(1, 2))
    #     self.assertFalse(generator.can_fill_top_right_cell(2, 2))

    # def test_can_fill_bottom_left_cell_should_return_false_if_the_cell_is_in_the_bottom_or_left_limit_of_the_matrix(self):
    #     generator = MatrixGenerator(n=3)

    #     self.assertFalse(generator.can_fill_bottom_left_cell(0, 0))
    #     self.assertFalse(generator.can_fill_bottom_left_cell(1, 0))
    #     self.assertFalse(generator.can_fill_bottom_left_cell(2, 0))
    #     self.assertFalse(generator.can_fill_bottom_left_cell(2, 1))
    #     self.assertFalse(generator.can_fill_bottom_left_cell(2, 2))

    def test_can_fill_bottom_left_cell_should_return_true_if_cell_is_not_in_the_bottom_or_left_limit_of_the_matrix(self):
        generator = MatrixGenerator(n=3)

        self.assertTrue(generator.can_fill_bottom_left_cell(0, 1))
        self.assertTrue(generator.can_fill_bottom_left_cell(1, 1))

    def test_next_position_should_return_below_cell_if_row_and_column_are_zero(self):
        generator = MatrixGenerator(n=3)

        row, col = generator.next_position(0, 0)

        self.assertEqual(1, row)
        self.assertEqual(0, col)

    def test_next_position_should_return_top_right_cell_position_if_it_exists(self):
        generator = MatrixGenerator(n=3)

        self.assertEqual((0, 1), generator.next_position(1, 0))
        self.assertEqual((0, 2), generator.next_position(1, 1))
        self.assertEqual((1, 2), generator.next_position(2, 1))

    def test_next_position_should_return_bottom_and_left_position_if_no_top_right_cell_exists(self):
        generator = MatrixGenerator(n=3)

        self.assertEqual((1, 0), generator.next_position(0, 0))
        self.assertEqual((2, 1), generator.next_position(0, 2))



    def test_generate_matrix_should_return_the_expected_matrix_if_n_is_2(self):
        generator = MatrixGenerator(n=2)

        expected = [
                    [1, 2], 
                    [4, 3]
                   ]

        self.assertEqual(expected, generator.generate_matrix())    


    def test_generate_matrix_should_return_the_expected_value_if_there_is_a_cell_available_in_the_right_side(self)  :
        generator = MatrixGenerator(n = 3)

        self.assertTrue((0 , 1), generator.can_fill_right_cell(0 , 0))
        self.assertTrue((1, 2),generator.can_fill_right_cell(1 , 1))


    def test_can_fill_bottom_cell_return_the_expected(self):

        generator = MatrixGenerator(n=3)
        self.assertTrue((1, 0), generator.can_fill_bottom_cell(0 , 0))
        self.assertTrue((1, 2), generator.can_fill_bottom_cell(0 , 2))



    def test_generate_matrix_should_return_the_expected_matrix_if_n_is_2(self):
        generator = MatrixGenerator(n=3)

        expected = [
                    [1, 2 , 3], 
                    [8, 9 , 4],
                    [7, 6 , 5]
                   ]
       # generator.next_position()

        self.assertEqual(expected, generator.generate_matrix())  


if __name__ == '__main__':
    unittest.main()