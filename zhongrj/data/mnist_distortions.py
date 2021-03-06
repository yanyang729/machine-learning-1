import numpy as np
import math
from zhongrj.utils.path_util import *
import zhongrj.data.mnist as mnist_data

FILE_DIR = get_file_dir(__file__)
STORE_DIR = FILE_DIR + 'MNIST_data_distortions/'
make_dir(STORE_DIR)
FILE_NAME = 'mnist_distortions_40x40.npz'


def load_data():
    """读取数据"""
    try:
        return np.load(STORE_DIR + FILE_NAME)
    except:
        print('找不到', STORE_DIR + FILE_NAME, ' 生成数据中 慢慢等吧 ...')
        return __store_data()


def __store_data():
    """存储数据"""
    mnist = mnist_data.load_data()
    print('生成训练数据...')
    train_image_list, train_label_list = __create_distortions_data(mnist['train_x'], mnist['train_y'])
    print('生成测试数据...')
    test_image_list, test_label_list = __create_distortions_data(mnist['test_x'], mnist['test_y'])
    result = {
        'train_x': train_image_list,
        'train_y': train_label_list,
        'test_x': test_image_list,
        'test_y': test_label_list
    }
    np.savez(STORE_DIR + FILE_NAME, **result)
    return result


def __create_distortions_data(images, labels):
    """
    生成随机旋转图片
    :param num: 数量
    """
    num = len(images)
    image_list = []
    label_list = []

    for n in range(num):
        plain_image = images[n].reshape(28, 28)
        plain_label = labels[n]

        # 旋转
        a = math.pi / (np.random.randint(60, 90) / 10) * np.random.choice([-1, 1])  # (pi/5 ~ pi/3)
        rotate_matrix = np.array([[math.cos(a), math.sin(a)],
                                  [-math.sin(a), math.cos(a)],
                                  [(1 - math.cos(a)) * 13.5 + 13.5 * math.sin(a),
                                   (1 - math.cos(a)) * 13.5 - 13.5 * math.sin(a)]])
        # 缩放
        x_scale, y_scale = np.random.randint(8, 12) / 10, np.random.randint(8, 12) / 10
        scale_matrix = np.array([[x_scale, 0],
                                [0, y_scale],
                                [(1 - x_scale) * 13.5, (1 - y_scale) * 13.5]])
        # 平移
        shift_matrix = np.array([[1, 0],
                                     [0, 1],
                                     [np.random.randint(-13, 1), np.random.randint(-13, 1)]])

        trans_image = np.zeros([40, 40])
        shape = trans_image.shape
        for i in range(shape[0]):
            for j in range(shape[1]):
                x, y = np.matmul(
                    np.array([i, j, 1]),
                    rotate_matrix
                )
                x, y = np.matmul(
                    np.array([x, y, 1]),
                    scale_matrix
                )
                x, y = np.matmul(
                    np.array([x, y, 1]),
                    shift_matrix
                )
                value = 0
                try:
                    x_, y_ = int(x), int(y)
                    if x_ >= 0 and y_ >= 0:
                        value = (plain_image[x_][y_] * (x_ - x + 1) + plain_image[x_][y_ + 1] * (x - x_)) * (
                            y_ - y + 1) + (plain_image[x_ + 1][y_] * (x_ - x + 1) + plain_image[x_ + 1][y_ + 1] * (
                            x - x_)) * (y - y_)
                except BaseException:
                    # print("炸裂", x, ", ", y)
                    pass
                trans_image[i][j] = value

        trans_image = trans_image.astype(np.float32)
        image_list.append(trans_image)
        label_list.append(plain_label)

        if n % 50 == 0:
            print("\r{}% 完成~".format(n * 100 / num), end='')

    return np.array(image_list), np.array(label_list)


if __name__ == '__main__':
    # store_distortions_data()

    # import zhongrj.utils.view_util as view
    #
    # mnist_distortions = load_data()
    #
    # def data_gen():
    #     mask = np.random.choice(10000, 18)
    #     yield np.append(mnist_distortions['train_x'][mask], mnist_distortions['test_x'][mask], axis=0)
    #
    # view.show_dynamic_image(data_gen)

    import zhongrj.utils.view_util as view

    mnist_distortions = load_data()
    view.show_image(mnist_distortions['train_x'][:20], 10, text=['hw~'] * 10)
