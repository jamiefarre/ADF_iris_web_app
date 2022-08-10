from calc import predict_species


def test_versicolor():
    # Arrange
    sepal_length = 6.1
    sepal_width = 2.9
    petal_length = 4.7
    petal_width = 1.4
    expected_output = 'versicolor'


# Act
    actual_output = predict_species(
        sepal_length, sepal_width, petal_length, petal_width)

# Assert
    assert actual_output == expected_output
