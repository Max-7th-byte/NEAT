from Evolution import Evolution


def read_data(path):
    X = list()
    y = list()
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = [int(d.replace('\n', '')) for d in line.split(' ')]
            X.append(data[:-1])
            y.append(data[-1])
    return X, y


"""THIS FORM IS ALWAYS USED"""
def reward(predictions, _y_train):
    score = 0
    if len(predictions) != len(_y_train):
        raise ValueError('Lengths are not the same')

    for pred, correct in zip(predictions, _y_train):
        if pred[0] == correct:
            score += 10
    return score


"""THIS FORM IS ALWAYS USED"""
def solve(predict, _X_train):
    predictions = list()
    for sample in _X_train:
        predictions.append(predict(sample))
    return predictions

if __name__ == '__main__':
    X_train, y_train = read_data('../data/xor_train.txt')

    evolution = Evolution(reward, solve)
    evolution.start_simulation(X_train, y_train)

    X_test, y_test = read_data('../data/xor_test.txt')
